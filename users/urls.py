from django.urls import path, include
from .views import CreateUser, login

urlpatterns = [
    path('app/user', CreateUser.as_view()),
    path('app/user/auth', login),
]