
from django.shortcuts import render, get_object_or_404
from .models import Song
from rest_framework import generics
from .serializers import MusicFileSerializer
from django.db.models import Q
from django.views.generic import ListView

class MusicFileListCreate(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = MusicFileSerializer
class MusicFileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = MusicFileSerializer


def index(request):
    music_files = Song.objects.all()
    return render(request, 'music/index.html', {'music_files': music_files})


def music_list(request):
    music_files = Song.objects.all()
    return render(request, 'music/music_list.html', {'music_files': music_files})

def music_detail(request, pk):
    music = get_object_or_404(Song, pk=pk)
    return render(request, 'music/music_detail.html', {'music': music})



class SearchResultsView(ListView):

    model = Song
    template_name = 'music/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = Song.objects.filter(
            Q(name__icontains=query)
        )
        return object_list
