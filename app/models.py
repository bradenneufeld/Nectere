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
    value = models.IntegerField()
    type = models.IntegerField(default=0)

    class Meta:
        abstract = True


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


