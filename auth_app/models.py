from django.db import models

# Create your models here.

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-fiction'),
        ('romance', 'Romance'),
        ('mystery', 'Mystery'),
        ('science', 'Science'),
        ('fantasy', 'Fantasy'),
    ]

    name = models.CharField(max_length=255)
    author = models.CharField(max_length=100, default='Unknown Author')
    description = models.TextField()
    image = models.ImageField(upload_to='book_images/')
    rent_price = models.DecimalField(max_digits=6, decimal_places=2)
    buy_price = models.DecimalField(max_digits=6, decimal_places=2, default=199.99)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='fiction')

    def __str__(self):
        return self.name
   