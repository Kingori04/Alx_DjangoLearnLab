from django.urls import path
from .views import list_books, LibraryDetailView  # Ensure this matches views.py

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
