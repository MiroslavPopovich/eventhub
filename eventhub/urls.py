from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('eventhub.main.urls')),
    path('user/', include('eventhub.user_auth.urls')),
    path('profile/', include('eventhub.user_profile.urls')),
    path('categories/', include('eventhub.categories.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'eventhub.main.views.handler404'
