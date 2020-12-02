from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .views import NoteViewSet

@api_view(['GET'])
def api_root(request):
    response = {
        'message': 'hello world'
    }
    return Response(response)

urlpatterns = [
    path('', api_root),
    path('auth/', include('rest_framework.urls')),
]

router = routers.SimpleRouter()
router.register('notes', NoteViewSet)

urlpatterns += router.urls
