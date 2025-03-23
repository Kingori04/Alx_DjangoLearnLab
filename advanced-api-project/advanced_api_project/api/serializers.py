from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Ensures all fields are serialized and validates publication_year.
    """
    def validate_publication_year(self, value):
        """
        Custom validation to ensure publication_year is not in the future.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes a nested BookSerializer to serialize related books dynamically.
    Allows books to be created/updated within the AuthorSerializer.
    """
    id = serializers.IntegerField(read_only=True)  # Include ID for easier reference
    books = BookSerializer(many=True, required=False)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    def create(self, validated_data):
        """
        Custom create method to handle nested book creation.
        """
        books_data = validated_data.pop('books', [])
        author = Author.objects.create(**validated_data)
        
        for book_data in books_data:
            Book.objects.create(author=author, **book_data)

        return author

    def update(self, instance, validated_data):
        """
        Custom update method to handle nested book updates.
        """
        books_data = validated_data.pop('books', [])
        
        # Update author fields
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        # Clear existing books and add new ones (simplified approach)
        instance.books.all().delete()
        for book_data in books_data:
            Book.objects.create(author=instance, **book_data)

        return instance
