from django.urls import path
from .views import books

urlpatterns = [
		path('', books, name = 'books'),
]
