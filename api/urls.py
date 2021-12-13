from django.urls import path, include
from django.http import JsonResponse

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.health_views import DatabaseHealth
from api import views

urlpatterns = [
    path('', DatabaseHealth.as_view()),
    path('articles/', views.articles),
    path('article_details/<int:id>/', views.article_id),
    path('article/', views.article_new),
    path('article/<int:id>/', views.article_update),
    path('article_delete/<int:id>/', views.article_delete),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("health/", lambda r: JsonResponse({"status": "ok"})),
]
