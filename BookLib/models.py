from django.db import models

# Create your models here.
class BookEntry(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    Published = models.DateField(null=True, blank=True)
    PagesNum = models.IntegerField(null=True, blank=True)
    BookType = models.CharField(max_length=100)