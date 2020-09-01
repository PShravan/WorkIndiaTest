from django.db import models

# Create your models here.
from django.db import models
from django_cryptography.fields import encrypt
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='notes')
    note = encrypt(models.TextField(null=True, blank=True))
    
    def __str__(self):
        return "note"