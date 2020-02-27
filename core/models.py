
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"Note item: {self.title} description: {self.body}"




    