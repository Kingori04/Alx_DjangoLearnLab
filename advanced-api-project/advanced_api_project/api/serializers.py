from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book model with validation for publication year."""
    
    def validate_publication_year(self, value):
        """Ensure publication year is not in the future."""
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author model with nested BookSerializer."""
    books = BookSerializer(many=True, read_only=True)  # Nested representation of books

    class Meta:
        model = Author
        fields = ['name', 'books']
