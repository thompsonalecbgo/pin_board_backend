from rest_framework import viewsets

from .models import Note, Link
from .serializers import NoteSerializer, LinkSerializer

class NoteViewSet(viewsets.ModelViewSet):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class LinkViewSet(viewsets.ModelViewSet):

    queryset = Link.objects.all()
    serializer_class = LinkSerializer