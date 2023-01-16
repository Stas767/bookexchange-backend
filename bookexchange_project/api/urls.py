from django.urls import include, path
from rest_framework import routers
from .views import BookViewSet, GenreViewSet
from djoser.views import UserViewSet


v1_router = routers.DefaultRouter()
v1_router.register(r'books', BookViewSet, basename='books')
v1_router.register(r'genres', GenreViewSet, basename='genres')
# v1_router.register(
#     r'books\/(?P<book_id>\d+)\/comments',
#     CommentViewSet,
#     basename='comments'
# )
v1_router.register(r'signup', UserViewSet, basename='signup')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    # path('v1/', include('djoser.urls')),  # Работа с пользователями
    path('v1/auth/', include('djoser.urls.jwt')),  # Работа с токенами
]
