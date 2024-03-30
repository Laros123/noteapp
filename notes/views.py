from django.shortcuts import render
from django.views.generic import ListView, DetailView
from notes.models import Note

# Create your views here.

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
