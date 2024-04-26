from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    Category_Name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True,)
    description = models.TextField(max_length=255, blank=True)
    Category_Image = models.ImageField(upload_to='images/categories', blank=True)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self) -> str:
        return self.Category_Name 