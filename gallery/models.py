from django.db import models


def get_upload_path(instance, filename):
    return f"media/gallery/{instance.title}/{filename}"


class GalleryImage(models.Model):
    TITLE_CHOICES = (
        ("rm", "Room"),
        ("as", "Amenities"),
        ("dr", "Dining"),
        ("ex", "Exterior"),
    )
    SIZE_CHOICES = (
        ("small", "Small (col-4)"),
        ("medium", "Medium (col-8)"),
        ("large", "Large (col-12)"),
    )

    title = models.CharField(max_length=9, choices=TITLE_CHOICES, blank=True)
    image = models.ImageField(upload_to=get_upload_path)
    description = models.TextField(blank=True, null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    size = models.CharField(max_length=6, choices=SIZE_CHOICES, default="small")

    def __str__(self):
        return self.title if self.title else f"Image {self.pk}"

    @property
    def css_filter(self):
        mapping = {
            "rm": "rooms",
            "as": "amenities",
            "dr": "dining",
            "ex": "exterior",
        }
        return mapping.get(self.title, "")
