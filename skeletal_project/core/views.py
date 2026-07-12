from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer

# API view: Automatically handles GET and POST
class NoteListCreateAPI(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# HTML view: Fetches data from db and injects to HTML
def board_view(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'core/board.html', {'notes':notes})