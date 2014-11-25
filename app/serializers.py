from rest_framework import serializers
from app.models import User, UserMFilter, MFilter, MFilterOptions


class UserMFiltersSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMFilter
        fields = ('id', 'user', 'm_filter', 'user_value')


class MFilterOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MFilterOptions
        fields = ('id', 'matching_function', 'name', 'user_value', 'match_value')


class UserSerializer(serializers.ModelSerializer):

    m_filters = serializers.RelatedField(many=True)
    m_filter_options = serializers.RelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'm_filters', 'm_filter_options')


class MFilterSerializer(serializers.ModelSerializer):
    options = serializers.RelatedField(many=True)

    class Meta:
        model = MFilter
        fields = ('id', 'name', 'type', 'options')