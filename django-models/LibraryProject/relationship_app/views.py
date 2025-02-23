from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Library, Book  # ✅ Ensure this is present

# Function-Based View (FBV) to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-Based View (CBV) for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# Class-Based View (CBV) to list books
class BookListView(ListView):
    model = Book
    template_name = "relationship_app/list_books.html"
    context_object_name = "books"

