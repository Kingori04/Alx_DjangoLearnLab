from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns in the list view
    search_fields = ('title', 'author')  # Enables searching by title and author
    list_filter = ('publication_year',)  # Filters by publication year

