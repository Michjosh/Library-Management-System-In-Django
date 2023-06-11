# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from templated_mail.mail import BaseEmailMessage

from .filters import AuthorFilter
from .pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Author
from .permissions import IsAdminOrReadOnly
from .serializers import AuthorSerializer
from .serializers import BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AuthorFilter
    search_fields = ['first_name', 'last_name']
    permission_classes = [IsAdminOrReadOnly]


class BookViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = BookSerializer


# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class AuthorDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get_serializer_context(self):
#         return {"request": self.request}


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def sendMailFunction(request):
    try:
        message = BaseEmailMessage(template_name='email.html', context={"name": "Michael"})

        message.send(['tinuade@gmail.com'])
    except BadHeaderError:
        pass
    return HttpResponse('Sent')
