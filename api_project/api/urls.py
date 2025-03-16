from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]



router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', include(router.urls)),  # Includes all routes registered with the router
]
