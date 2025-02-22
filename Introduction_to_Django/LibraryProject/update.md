book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

updated_book = Book.objects.get(id=book.id)
print(f"Updated Title: {updated_book.title}")
# Output: Updated Title: Nineteen Eighty-Four

