from django.urls import path
from notes.views import NoteListView, NoteDetailView, add_note

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('add-note/', add_note, name='add-note'),
]
