from django.shortcuts import render
from django.views.generic.detail import DetailView  # ✅ Missing import added!
from django.views.generic import ListView
from .models import Library, Book  
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect

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



def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to a homepage or books list
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redirect after successful registration
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


