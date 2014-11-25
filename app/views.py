from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from app.models import *
from app.serializers import *
from app.match import Match


class UserViewSet(NestedViewSetMixin, ModelViewSet):
    model = User
    serializer_class = UserSerializer


class UserSelfMetaViewSet(NestedViewSetMixin, ModelViewSet):
    model = UserSelfMeta
    serializer_class = UserSelfMetaSerializer


class UserMatchMetaViewSet(NestedViewSetMixin, ModelViewSet):
    model = UserMatchMeta
    serializer_class = UserMatchMetaSerializer


class MFilterViewSet(NestedViewSetMixin, ModelViewSet):
    model = MFilter
    serializer_class = MFilterSerializer


class MFilterOptionsViewSet(NestedViewSetMixin, ModelViewSet):
    model = MFilterOptions
    serializer_class = MFilterOptionsSerializer


def index(request):
    test_match = Match(1)
    return HttpResponse(test_match.filter())