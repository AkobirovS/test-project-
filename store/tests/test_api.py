from rest_framework.test import APITestCase
from rest_framework import status  # Добавлен импорт
from django.urls import reverse
from store.serializers import BookSerializer
from store.models import Book

class BookApiTest(APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(name='books', price=10.00)
        book_2 = Book.objects.create(name='books_2', price=111.00)
        url = reverse('book-list')
        print(url)
        response = self.client.get(url)
        the_date = BookSerializer([book_1, book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(the_date, response.data)
        print(response.data)
