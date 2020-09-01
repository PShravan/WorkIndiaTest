from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    """
    user serializer with just the email field
    """
    class Meta:
        model = Note
        fields = (
            'note',
        )
        read_only_fields = ('user',)