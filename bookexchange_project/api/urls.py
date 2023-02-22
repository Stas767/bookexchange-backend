from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import BookCardViewSet, FavoritesViewSet

# from djoser.views import UserViewSet


v1_router = DefaultRouter()
v1_router.register(r'books', BookCardViewSet)
v1_router.register(r'favorites', FavoritesViewSet)
# v1_router.register(r'signup', UserViewSet, basename='signup')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),  # Работа с пользователями/
    path('v1/auth/', include('djoser.urls.jwt')),  # Работа с токенами
]
