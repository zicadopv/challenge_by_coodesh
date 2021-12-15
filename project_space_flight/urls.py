from django.contrib import admin
from django.urls import path, include

from api import views

urlpatterns = [
    path('', include('api.urls')),
    path('articles/', views.articles, name="articles"),
    path('article_details/<int:key>/', views.article_key, name="article_details"),
    path('article/', views.article_new, name="article_new"),
    path('article/<int:key>/', views.article_update, name="article_update"),
    path('article_delete/<int:key>/', views.article_delete, name="article_delete"),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
