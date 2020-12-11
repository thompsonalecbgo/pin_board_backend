from rest_framework import serializers

from .models import Note, Link

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['id', 'text', 'top', 'left']

class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ['id', 'note1', 'note2']