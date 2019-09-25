from rest_framework import generics

from books.models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):

    queryset = Book.objects.all() # all
    #queryset = Book.objects.all().order_by('id') # order by
    #queryset = Book.objects.all().order_by('id')[0:10] # order by , 0-10 rec
    #queryset = Book.objects.filter(id__iexact=2) # filter
    #queryset = Book.objects.all().order_by('id')[0:10]
    serializer_class = BookSerializer