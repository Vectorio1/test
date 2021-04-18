import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('cms/', admin.site.urls),
    path('', views.home),
]

if settings.DEBUG: 
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns