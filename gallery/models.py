from django.db import models


class GalleryImage(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True, null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title if self.title else f"Image {self.pk}"
