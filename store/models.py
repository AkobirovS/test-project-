from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author_user = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.id}: {self.name}"