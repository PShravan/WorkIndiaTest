from django.shortcuts import render
from .models import Note
from .serializers import NoteSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class NoteListAPIView(generics.ListAPIView):
    """Provide the answers queryset of a specific question instance."""
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Note.objects.filter(user = self.request.user)
        return queryset

class NoteCreateAPIView(generics.CreateAPIView):
    """Allow users to answer a question instance if they haven't already."""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        serializer.save(user=request_user)