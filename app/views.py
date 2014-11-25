from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from app.models import User, UserMFilter, MFilter, MFilterOptions
from app.serializers import UserSerializer, UserMFiltersSerializer, MFilterSerializer, MFilterOptionsSerializer
from app.match import Match


class UserViewSet(NestedViewSetMixin, ModelViewSet):
    model = User
    serializer_class = UserSerializer


class UserFilterDataViewSet(NestedViewSetMixin, ModelViewSet):
    model = UserMFilter
    serializer_class = UserMFiltersSerializer


class MFilterViewSet(NestedViewSetMixin, ModelViewSet):
    model = MFilter
    serializer_class = MFilterSerializer


class MFilterOptionsViewSet(NestedViewSetMixin, ModelViewSet):
    model = MFilterOptions
    serializer_class = MFilterOptionsSerializer


def index(request):
    test_match = Match(1)
    return HttpResponse(test_match.filter())