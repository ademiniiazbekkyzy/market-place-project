from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Category(models.Model):
    title = models.TextField(max_length=30)
    slug = models.SlugField(max_length=30, primary_key=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        if not self.parent:
            return self.slug
        else:
            return f'{self.parent} --> {self.slug}'

    def save(self, *args, **kwargs):
        self.slug = self.title.lower()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug


class Post(models.Model):
    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')