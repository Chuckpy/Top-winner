from django.urls import path, include
from .api import RegisterView, SignInView, sign_out


app_name = 'project_auth'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('logout/', sign_out, name='logout')
]   