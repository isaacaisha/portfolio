from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

from django.contrib import admin
from django.urls import path,  include
from portfolio_app import views as app_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('superadmin/', app_views.admin_proxy, name='admin_proxy'),
    path('', include('portfolio_app.urls')),
]

urlpatterns += i18n_patterns(
    # Translated URLs
    path('set_language/', set_language, name='set_language'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

