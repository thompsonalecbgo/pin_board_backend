from django.db import models

class Note(models.Model):
    text = models.TextField(blank=True)
    top = models.IntegerField(default=0)
    left = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.text[:100]}"

class Link(models.Model):
    note1 = models.IntegerField(default=0)
    note2 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.note1}-{self.note2}"