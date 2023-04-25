from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from api.views import (
    ApplicationsViewSet,
    AuthorViewSet,
    BookCardViewSet,
    BookViewSet,
    FavoritesViewSet,
    GenreViewSet,
)

openapi_schema_view = get_schema_view(
    info=openapi.Info(
        title="Bookexchange API",
        default_version="1",
        description="API документация сервиса Книгообмен.",
        contact=openapi.Contact(url="https://t.me/jschupss"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

router = DefaultRouter()
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)
router.register(r"applications", ApplicationsViewSet)
router.register(r"book_cards", BookCardViewSet)
router.register(r"favorites", FavoritesViewSet)
router.register(r"genres", GenreViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("docs/", openapi_schema_view().with_ui(renderer="redoc")),
]
