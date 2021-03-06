from app.models import *
from django.db.models import Q


class Match:
    def __init__(self, user_pk):
        self.user = User.objects.get(pk=user_pk)
        self.m_filters = MFilter.objects.all()
        self.m_filter_options = MFilterOptions.objects.all()

        self.match_list = User.objects.all().exclude(pk=user_pk)

    def match(self):
        self.filter()

    def filter(self):
        for m_filter in self.m_filters:
            filter_type = m_filter.type
            print("BEGIN. Type is " + filter_type)
            if filter_type == 'S':
                self.filter_same(m_filter)
                #pass
            elif filter_type == 'C':
                self.filter_complementary(m_filter)
                #pass
            elif filter_type == 'R':
                self.filter_range(m_filter)
                #pass
            else:
                raise Exception('no filter type provided')
        return self.match_list.all().values()

    def filter_same(self, m_filter):
        user_match_meta = self.user.meta.filter(m_filter_id=m_filter.pk).values_list('user_value', flat=True)
        user_self_meta = self.user.self.filter(m_filter_id=m_filter.pk).values_list('user_value', flat=True)

        # check for "don't care", don't filter if so
        if 0 in user_match_meta:
            return

        # filter set for other potential match's self data based on user's match meta
        q = Q()
        for match_meta in user_match_meta:
            q.add(Q(self__user_value=match_meta, self__m_filter__pk=m_filter.pk), Q.OR)

        # filter set for other user's self data based on potential match's match meta
        q_prime = Q()
        for self_meta in user_self_meta:
            q_prime.add(Q(meta__user_value=self_meta, meta__m_filter__pk=m_filter.pk), Q.OR)

        # filter list
        self.match_list = self.match_list.filter(q).filter(q_prime)

    def filter_range(self, m_filter):
        # find the relevant min and max options for this filter (should only be one each)
        # @@ should reduce the number of DB calls here
        min_option_pk = m_filter.options.get(type='m').pk
        max_option_pk = m_filter.options.get(type='M').pk
        print("min pk: " + str(min_option_pk))
        print("max pk: " + str(max_option_pk))
        # obtain the user's minimum and maximum range
        min_user_value = self.user.meta.get(m_filter_id=m_filter.pk, option__pk=min_option_pk).user_value
        # need to add a don't care setting
        max_user_value = self.user.meta.get(m_filter_id=m_filter.pk, option__pk=max_option_pk).user_value

        # finally, get the user's own value for converse matching
        self_user_value = self.user.self.get(m_filter_id=m_filter.pk, option__pk=min_option_pk).user_value


        print("min value: " + str(min_user_value))
        print("max value: " + str(max_user_value))
        print("self value: " + str(self_user_value))
        # @@ change to Q filters.
        # @@ Functions should eventually just return Q filters that are combined all at once
        self.match_list = self.match_list.filter(self__user_value__gte=min_user_value, self__option__pk=min_option_pk)
        print(self.match_list)
        self.match_list = self.match_list.filter(self__user_value__lte=max_user_value, self__option__pk=min_option_pk)
        print(self.match_list)

        self.match_list = self.match_list.filter(meta__user_value__lte=self_user_value, meta__option__pk=min_option_pk)
        self.match_list = self.match_list.filter(meta__user_value__gte=self_user_value, meta__option__pk=max_option_pk)

    def filter_complementary(self, m_filter):
        user_match_meta = self.user.meta.get(m_filter_id=m_filter.pk).option.pk
        user_self_meta = self.user.self.get(m_filter_id=m_filter.pk).option.pk
        self.match_list = self.match_list.filter(self__option__pk=user_match_meta)
        self.match_list = self.match_list.filter(meta__option__pk=user_self_meta)
