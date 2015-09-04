from django.db import models


class MatchingFunction(models.Model):
    """Meta  class for MFilter, MPreference, and MSimilarity classes.

    Establishes common attributes between all matching functions.

    Attributes:
        name: a descriptive name for the function
    """
    name = models.CharField(max_length=30)

    class Meta:
        abstract = True


class MFilter(MatchingFunction):
    """Model for filters.

    Attributes:
        type: defines the match type
    """

    FILTER_TYPES = (
        ('S', 'Same'),
        ('C', 'Complementary'),
        ('R', 'Range')
    )
    type = models.CharField(max_length=1, choices=FILTER_TYPES)

    def __str__(self):
        return '%s: %s' % (self.name, self.type)


class Options(models.Model):
    """Meta class for match options.

    Attributes:
        name: defines the match type
        value: this option's value
        type: minimum, maximum, same, or comp
    """
    name = models.CharField(max_length=30)
    value = models.IntegerField()

    OPTION_TYPES = (
        ('m', 'Min'),
        ('M', 'Max'),
        ('A', 'Complementary A of A-B'),
        ('B', 'Complementary B of B-A'),
        ('N', 'normal')
    )
    type = models.CharField(max_length=1, choices=OPTION_TYPES, default='N')

    class Meta:
        abstract = True

    def __str__(self):
        return '%s: %s' % (self.name, self.value)


class MFilterOptions(Options):
    matching_function = models.ForeignKey(MFilter, related_name='options')

    class Meta:
        ordering = ('matching_function',)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    self_meta = models.ManyToManyField(MFilterOptions, through='UserSelfMeta', related_name='self')
    match_meta = models.ManyToManyField(MFilterOptions, through='UserMatchMeta', related_name='meta')


class UserSelfMeta(models.Model):
    user = models.ForeignKey(User, related_name='self')
    option = models.ForeignKey(MFilterOptions, related_name='self_option')
    m_filter = models.ForeignKey(MFilter, related_name='user_self_meta')
    user_value = models.IntegerField()


class UserMatchMeta(models.Model):
    user = models.ForeignKey(User, related_name='meta')
    option = models.ForeignKey(MFilterOptions, related_name='meta_option')
    m_filter = models.ForeignKey(MFilter, related_name='user_match_meta')
    user_value = models.IntegerField()


