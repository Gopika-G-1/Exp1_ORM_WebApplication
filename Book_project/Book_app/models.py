from django.db import models
from django.contrib import admin

class Book(models.Model):
    Book_name = models.CharField(max_length=20,help_text="enter book name")
    Author =models.CharField(max_length=50,help_text="enter author name")
    price = models.FloatField(help_text="enter book price")

class BookAdmin(admin.ModelAdmin):
    list_display=['Book_name','Author','price']
# Create your models here.
