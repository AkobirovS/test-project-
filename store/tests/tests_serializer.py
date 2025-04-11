from store.serializers import BookSerializer
from django.test import TestCase
from store.models import Book

class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='hello_1',price=25.00)
        book_2 = Book.objects.create(name='hello_2',price=255.00)

        serializer = BookSerializer([book_1,book_2], many=True).data
        print(serializer)
        expadet_data = [
            {
                'id': 11,
                'name': 'hello_1',
                'price': '25.00'
            },
            {
                'id': 12,
                'name': 'hello_2',
                'price': '255.00'
            }
        ]
        self.assertEqual(serializer, expadet_data)
