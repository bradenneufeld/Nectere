from app.models import *
from django.db.models import Q


class Match:
    def __init__(self, user_pk):
        self.user = User.objects.get(pk=user_pk)
        self.m_filters = MFilter.objects.all()
        self.m_filter_options = MFilterOptions.objects.all()

        self.match_list = User.objects.all().exclude(pk=user_pk)

    def match(self):
        pass

    def filter(self):
        for m_filter in self.m_filters:
            filter_type = m_filter.type
            print("BEGIN. Type is " + filter_type)
            if filter_type == 'S':
                self.filter_same(m_filter)
            elif filter_type == 'C':
                #self.filter_complementary(m_filter)
                pass
            elif filter_type == 'R':
                pass
            else:
                raise Exception('no filter type provided')
        return self.match_list.all().values()


    def filter_same(self, m_filter):
        print("START SAME FILTER")
        # user_self_meta = self.user.self_meta.filter(option__matching_function__pk=m_filter.pk).values_list('user_value', flat=True)
        #print(self.user.self_meta.all().values_list('user_value', flat=True))
        print(self.user.meta.filter(m_filter_id=m_filter.pk).values())
        user_match_meta = self.user.meta.filter(m_filter_id=m_filter.pk).values_list('user_value', flat=True)
        print(user_match_meta)
        #value_options = m_filter.options.all().values_list('match_value', flat=True)

        #print("SAME: user match meta: "+str(user_match_meta))
        #print("SAME: value options: "+str(value_options))
        q = Q()
        for meta in user_match_meta:
            q.add(Q(meta__user_value=meta, meta__m_filter__pk=m_filter.pk), Q.OR)
        self.match_list = self.match_list.filter(q)
