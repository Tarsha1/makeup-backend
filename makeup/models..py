from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100, default='', blank=False)
    photo_url = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.product_name

class Comment(models.Model):
    user = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.user
