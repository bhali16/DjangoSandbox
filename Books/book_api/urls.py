# from django.contrib import admin
# from django.urls import path
# from book_api.views import books, book

# urlpatterns = [
#     path('', books),
#     path('<int:pk>', book),
# ]

from django.contrib import admin
from django.urls import path
from book_api.views import BookList, Books

urlpatterns = [
    path('', BookList.as_view()),
    path('<int:pk>/', Books.as_view()),
]