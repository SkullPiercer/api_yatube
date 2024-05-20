from django.urls import path
from rest_framework.authtoken import views

from api.views import get_groups, get_posts

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('posts/', get_posts),
    path('groups/', get_groups),
]
