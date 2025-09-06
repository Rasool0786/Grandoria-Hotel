from django.urls import path
from django.shortcuts import render

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home_page_view, name="home"),
    path("about/", views.about_page_view, name="about"),
    path("contact/", views.contact_page_view, name="contact"),
    path("terms_of_service/", views.terms_of_service_page_view, name="terms_of_service"),
    path("privacy_policy/", views.privacy_policy_page_view, name="privacy_policy"),
    path('location/', views.location_page_view, name="location"),
]