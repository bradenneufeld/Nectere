from rest_framework import serializers
from app.models import User, MFilter, MFilterOptions, UserMatchMeta, UserSelfMeta


class MFilterOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MFilterOptions
        fields = ('id', 'matching_function', 'name', 'value', 'type')


class MFilterSerializer(serializers.ModelSerializer):

    options = serializers.RelatedField(many=True)

    class Meta:
        model = MFilter
        fields = ('id', 'name', 'type', 'options')


class UserSerializer(serializers.ModelSerializer):

    self_meta = serializers.RelatedField(many=True)
    match_meta = serializers.RelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'self_meta', 'match_meta')


class UserSelfMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSelfMeta
        fields = ('id', 'm_filter', 'option', 'user_value')


class UserMatchMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMatchMeta
        fields = ('id', 'm_filter', 'option', 'user_value')