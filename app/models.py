from django.db import models


class MatchingFunction(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        abstract = True


class MFilter(MatchingFunction):
    TYPES = (
        ('S', 'Same'),
        ('C', 'Complementary'),
        ('R', 'Range')
    )
    type = models.CharField(max_length=1, choices=TYPES)


class Options(models.Model):
    name = models.CharField(max_length=30)
    user_value = models.IntegerField()
    match_value = models.IntegerField(default=0)
    match_id = models.IntegerField(default=0)

    class Meta:
        abstract = True


class MFilterOptions(Options):
    matching_function = models.ForeignKey(MFilter, related_name='options')

    class Meta:
        ordering = ('matching_function',)

    def __unicode__(self):
        return '%s - %s: %s' % (self.matching_function, self.name, self.name)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    m_filter_options = models.ManyToManyField(MFilterOptions)


class UserMFilter(models.Model):
    user_value = models.IntegerField()
    m_filter = models.ForeignKey(MFilter)
    user = models.ForeignKey(User, related_name='m_filters')

    class Meta:
        ordering = ('m_filter',)

    def __unicode__(self):
        return '%s - %s: %s' % (self.m_filter, self.user, self.user_value)