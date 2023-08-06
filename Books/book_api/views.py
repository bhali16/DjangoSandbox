# from rest_framework.response import Response
# from book_api.models import Book
# from book_api.serializer import BookSerializer
# from rest_framework.decorators import api_view
# from rest_framework import status

# @api_view(['GET', 'POST'])
# def books(request):
#     if request.method == "GET":
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def book(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == "DELETE":
#         book.delete()
#         return Response({
#             'success': True
#         }, status=status.HTTP_200_OK)
        
from rest_framework.views import APIView
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from book_api.models import Book
from rest_framework import status
from django.shortcuts import get_object_or_404


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Books(APIView):

    def get_book_by_pk(self, pk):
        return get_object_or_404(Book, pk=pk)
    
    def get(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response({
            'success': True
        }, status=status.HTTP_200_OK)