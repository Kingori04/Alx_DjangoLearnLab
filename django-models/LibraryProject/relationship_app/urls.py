from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import BookListView
from .views import user_login
from .views import user_logout
from .views import  register
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView 


urlpatterns = [
    path("books/", list_books, name="list_books"),  # FBV for listing books
    path("books_cbv/", BookListView.as_view(), name="book_list_cbv"),  # CBV for books
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # CBV for library
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),  # ✅ Fix
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),  # ✅ Fix
    path("register/", register, name="register"),
    path("", BookListView.as_view(), name="home"),  # ✅ Ensure a "home" URL exists
]

