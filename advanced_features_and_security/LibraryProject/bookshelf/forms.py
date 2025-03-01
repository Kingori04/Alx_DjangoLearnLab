from django import forms
from .models import Article 
from .models import Book
from django.utils.html import escape

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Article 
        fields = ["title", "content"] 

# bookshelf/forms.py

class BookForm(forms.ModelForm):
    """Secure Django form to prevent SQL injection and XSS attacks."""
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]

    def clean_title(self):
        """Sanitize input to prevent XSS attacks."""
        title = self.cleaned_data["title"]
        return escape(title)  # Escape HTML characters

    def clean_author(self):
        """Sanitize input for the author field."""
        author = self.cleaned_data["author"]
        return escape(author)

