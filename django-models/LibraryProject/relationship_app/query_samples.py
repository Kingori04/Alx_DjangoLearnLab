import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)  # Explicit filter
    except Author.DoesNotExist:
        return []

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)  # Explicit get() query
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example Usage
if __name__ == "__main__":
    print(get_books_by_author("J.K. Rowling"))
    print(get_books_in_library("Central Library"))
    print(get_librarian_for_library("Central Library"))
