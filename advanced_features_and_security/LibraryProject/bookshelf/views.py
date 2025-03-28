from .forms import ExampleForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from .models import Article
from .models import Book
from .forms import ExampleForm


def example_view(request):
    form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form})


@login_required
@permission_required("bookshelf.view_book", raise_exception=True)
def book_list(request):
    """Displays a list of all books."""
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, "bookshelf/article_list.html", {"articles": articles})

@login_required
@permission_required("bookshelf.can_create", raise_exception=True)
def create_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article.objects.create(title=title, content=content, author=request.user)
        return redirect("article_list")
    return render(request, "bookshelf/create_article.html")

@login_required
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect("article_list")
    return render(request, "bookshelf/edit_article.html", {"article": article})

@login_required
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect("article_list")
