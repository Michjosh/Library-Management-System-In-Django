import uuid
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    # date_of_death = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Firstname: {self.first_name}, Lastname: {self.last_name}"


class Book(models.Model):
    LANGUAGE_CHOICES = [

        ('Y', "YORUBA"),
        ('H', "HAUSA"),
        ('I', 'IGBO'),
        ('E', "ENGLISH")
    ]

    GENRE_CHOICES = [
        ('FIC', 'FICTION'),
        ('POL', 'POLITICS'),
        ('ROM', 'ROMANCE')

    ]

    title = models.CharField(max_length=255, blank=False, null=False)
    isbn = models.CharField(max_length=13, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    date_added = models.DateTimeField(blank=True, null=True)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES)
    language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title} "


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B')
    ]

    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"Book: {self.book}, Status: {self.status}, Due: {self.due_back}"
