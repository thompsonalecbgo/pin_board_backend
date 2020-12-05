from django.db import models

class Note(models.Model):
    text = models.TextField(blank=True)
    top = models.PositiveIntegerField(default=0)
    left = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.text[:100]}"