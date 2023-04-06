from api.views import (
    AdvertViewSet,
    AuthorViewSet,
    BookCardViewSet,
    BookViewSet,
    FavoritesViewSet,
    GenreViewSet,
    get_doc_shema_view,
)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'adverts', AdvertViewSet)
# router.register(r'authors', AuthorViewSet)
# router.register(r'books', BookViewSet)
# удалить в следующей версии api
router.register(r"book_card", BookCardViewSet)
router.register(r"favorites", FavoritesViewSet)
# router.register(r'genres', GenreViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "docs/dynamic/", get_doc_shema_view().with_ui("redoc", cache_timeout=0)
    ),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
