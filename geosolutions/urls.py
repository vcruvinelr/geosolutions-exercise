from django.contrib import admin
from django.urls import path, include
from apps.points import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.points.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
