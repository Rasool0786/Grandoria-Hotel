from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("terms_of_service/", views.terms_of_service, name="terms_of_service"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),   
]