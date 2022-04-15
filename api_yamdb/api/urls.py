
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet,
                    GenreViewSet, ReviewViewSet,
                    TitleViewSet, UserViewSet)

router = DefaultRouter()
router.register(
    'categories',
    CategoryViewSet,
    basename='сategories'
)
router.register(
    'titles',
    TitleViewSet,
    basename='titles'
)
router.register(
    'genres',
    GenreViewSet,
    basename='genres'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(
    'users',
    UserViewSet,
    basename='users'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]