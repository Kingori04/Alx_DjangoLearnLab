from django.urls import path
from .views import list_books, LibraryDetailView, BookListView

urlpatterns = [
    path("books/", list_books, name="list_books"),  # FBV for listing books
    path("books_cbv/", BookListView.as_view(), name="book_list_cbv"),  # CBV for books
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # CBV for library
]
