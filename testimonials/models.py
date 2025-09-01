from django.db import models
from django.contrib.auth import get_user_model


class Testimonial(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='testimonials',
        verbose_name='Author'
    )
    role = models.CharField(max_length=100, verbose_name='Role')
    photo = models.ImageField(upload_to='testimonials/photos/', verbose_name='Photo')
    message = models.TextField(verbose_name='Message')
    rating = models.PositiveSmallIntegerField(verbose_name='Rating')
    active = models.BooleanField(default=True, verbose_name='Active')
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    datetime_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
    
    def __str__(self):
        return self.author.username