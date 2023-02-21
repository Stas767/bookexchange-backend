from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from django.conf.urls import url

# schema_view = get_schema_view(
#    openapi.Info(
#       title="BookExchange API",
#       default_version='v1',
#       description="Документация для приложения books проекта BooksExchange",
#       # terms_of_service="URL страницы с пользовательским соглашением",
#       contact=openapi.Contact(email="admin@bookexchange.ru"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # url(r'^swagger(?P<format>\.json|\.yaml)$',
    #     schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
    #     name='schema-swagger-ui'),
    # url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
    #     name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
