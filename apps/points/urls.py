from django.contrib import admin
from django.urls import path, include
from apps.points.views import (
    HomePage,
    search
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('search/', search, name='search_results'),
]
