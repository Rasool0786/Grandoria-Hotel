from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.BigIntegerField()
    amenities = models.ManyToManyField('Amenity', related_name='rooms')
    capacity = models.IntegerField()
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='rooms/', null=True, blank=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='rooms')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("room_detail", kwargs={"pk": self.pk})
    


class Amenity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100)  # e.g., FontAwesome icon class
    
    def __str__(self):
        return self.title 


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]
    
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    