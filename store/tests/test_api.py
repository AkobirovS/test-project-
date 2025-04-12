from rest_framework.test import APITestCase
from rest_framework import status  # Добавлен импорт
from django.urls import reverse
from store.serializers import BookSerializer
from store.models import Book

class BookApiTest(APITestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(name='Book 1 Sardor',price=10.00,author_user='Author')
        self.book_2 = Book.objects.create(name='books_2', price=111.00,author_user='Sardor')

    def test_get(self):
        url = reverse('book-list')
        print(url)
        response = self.client.get(url)
        the_date = BookSerializer([self.book_1, self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(the_date, response.data)
        print(response.data)

    def test_get_filter(self):
        url = reverse('book-list')
        print(url)
        response = self.client.get(url,data={'search':'Sardor'})
        the_date = BookSerializer([self.book_1, self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(the_date, response.data)
        print(response.data)


    def test_get_order(self):
        url = reverse('book-list')
        print(url)
        response = self.client.get(url,data={'ordering':'price'})
        the_date = BookSerializer([self.book_1, self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(the_date, response.data)
        print(response.data)
