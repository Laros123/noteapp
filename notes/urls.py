from django.urls import path
from notes.views import NoteListView, NoteDetailView

urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
]
