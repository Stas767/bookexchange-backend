from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_versions.views import (BookViewSetV2, BookCardViewSetV1,
                                BookCardViewSetV2, FavoritesViewSetV1)

router_v1 = DefaultRouter()
router_v1.register(r'book_card', BookCardViewSetV1)
router_v1.register(r'favorites', FavoritesViewSetV1)

router_v2 = DefaultRouter()
router_v2.register(r'book', BookViewSetV2)
router_v2.register(r'book_card', BookCardViewSetV2)
router_v2.register(r'favorites', FavoritesViewSetV1)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v2/', include(router_v2.urls)),
    path('', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
]

schema = get_schema_view(
    info=openapi.Info(
        title='Bookexchange API documentation',
        default_version='1',
        description='The first version of dynamic documentation',
        terms_of_service="https://localhost:8000/",
        contact=openapi.Contact(email="test@admin.ru"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    patterns=urlpatterns,
)

urlpatterns += [
    path(
        'docs/', schema.with_ui('redoc', cache_timeout=0)
    ),
]
