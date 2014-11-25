from app.models import *


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
                self.filter_complementary(m_filter)
            elif filter_type == 'R':
                pass
            else:
                raise Exception('no filter type provided')
        return self.match_list.all().values()

    def filter_same(self, m_filter):
        print("START SAME FILTER")
        user_values = self.user.m_filters.filter(m_filter__pk=m_filter.pk).values_list('user_value', flat=True)
        value_options = m_filter.options.all().values_list('match_value', flat=True)
        print("SAME: user values: "+str(user_values))
        print("SAME: value options: "+str(value_options))
        for option in value_options:
            print("SAME: LOOP: ")
            print("SAME: LOOP: option: " + str(option))
            m_filter_option = option not in user_values
            print("SAME: LOOP: filter?: " + str(m_filter_option))
            if m_filter_option:
                print("SAME: LOOP: IF: not in user match values")
                self.match_list = self.match_list.exclude(
                    m_filters__m_filter=m_filter.pk,
                    m_filters__user_value=option
                )

    def filter_complementary(self, m_filter):
        print("START SAME FILTER")
        user_values = self.user.m_filters.filter(m_filter__pk=m_filter.pk).values_list('user_value', flat=True)
        value_options = m_filter.options.all().values_list('match_value', flat=True)
        match_values = []
        for user_value in user_values:
            filter_option = m_filter.options.get(user_value=user_value)
            match_values.append(filter_option.match_value)
        print("COMP: user values: "+str(user_values))
        print("COMP: match values: " + str(match_values))
        print("COMP: value options: "+str(value_options))
        for option in value_options:
            print("COMP: LOOP: ")
            print("COMP: LOOP: option: " + str(option))
            m_filter_option = option not in user_values
            print("SAME: LOOP: filter?: " + str(m_filter_option))
            if m_filter_option:
                print("SAME: LOOP: IF: not in match values")
                #self.match_list = self.match_list.exclude(
                #    user_filters__filter=m_filter.pk,
                #    user_filters__user_value=option
                #)
