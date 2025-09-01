from django.urls import path

from . import views

app_name = "testimonials"

urlpatterns = [
    path('', views.TestimonialListView.as_view(), name='list'),
    path('edit/<int:pk>/', views.TestimonialUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.TestimonialDeleteView.as_view(), name='delete'),
]