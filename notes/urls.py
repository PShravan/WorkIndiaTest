from django.urls import path, include
from .views import *

urlpatterns = [
    path("app/sites/list/", NoteListAPIView.as_view()),
    path("app/sites/", NoteCreateAPIView.as_view()),
]
