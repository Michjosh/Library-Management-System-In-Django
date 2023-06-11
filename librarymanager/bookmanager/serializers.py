from decimal import Decimal
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as CurrentUser
from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(read_only=True)  # Set read_only=True for the nested serializer field

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'description', 'date_added', 'genre', 'author', 'language', 'price', 'discount_price']

    discount_price = serializers.SerializerMethodField(method_name='calculate')

    def calculate(self, book_instance: Book):
        disc = book_instance.price * Decimal(0.1)
        return str(disc)


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']


class UserSerializer(CurrentUser):
    class Meta(CurrentUser.Meta):
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

