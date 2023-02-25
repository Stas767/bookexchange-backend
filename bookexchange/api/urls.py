from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import get_doc_shema_view
from api.views import BookCardViewSet, FavoritesViewSet

router = DefaultRouter()
router.register(r'book_card', BookCardViewSet)
router.register(r'favorites', FavoritesViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),

    path(
        'v1/docs/dynamic/', get_doc_shema_view().with_ui('redoc', cache_timeout=0)
    ),

    path('v1/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.authtoken')),
]
