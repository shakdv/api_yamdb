
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet,
                    GenreViewSet, ReviewViewSet,
                    TitleViewSet, UserViewSet,
                    GetTokenView, UserRegisterView)

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
    path('v1/auth/signup/', UserRegisterView.as_view(), name='signup'),
    path('v1/auth/token/', GetTokenView.as_view(), name='token')
]
