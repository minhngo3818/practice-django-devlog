from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),        # token -> simple token
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),       # give a token -> a new token

    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('projects/<str:pk>', views.getProject),
    path('projects/<str:pk>/vote/', views.projectVote),
]