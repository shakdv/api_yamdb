from django.db.models import Avg
from rest_framework import filters, mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from reviews.models import Category, Genre, Title
from .filters import TitlesFilter
from .permissions import (IsAdminOrReadOnly)
from .serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    TitleReadOnlySerializer
)


class CategoryViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    # queryset = Title.objects.all()
    queryset = Title.objects.all().annotate(rating=Avg('reviews__score'),)
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        if self.action in ("retrieve", "list"):
            return TitleReadOnlySerializer
        return TitleSerializer
