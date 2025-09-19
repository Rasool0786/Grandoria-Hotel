from django import template
from gallery.models import GalleryImage

register = template.Library()


@register.filter
def filter_by_title(images, choice):
    valid_choices = [code for code, name in GalleryImage.TITLE_CHOICES]
    if choice not in valid_choices:
        return images.none()

    return images.filter(title=choice, active=True)
