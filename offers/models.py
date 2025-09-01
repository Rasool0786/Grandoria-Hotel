from django.db import models
from django.utils import timezone

from rooms.models import Room

class Offer(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='offers',
        verbose_name='Room',
    )
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    offer_price = models.BigIntegerField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='offers/', null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.title:
            return f"{self.title} - {self.room.title}"
        return f"Offer for {self.room.title}"
    
    def is_current(self):
        today = timezone.now().date()
        return self.acive and self.start_date <= today <= self.end_date