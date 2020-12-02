from django.db import models

class Note(models.Model):
    text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.text[:100]}"