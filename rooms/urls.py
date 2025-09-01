from django.urls import path

from . import views

app_name = "rooms"

urlpatterns = [
    path('', views.RoomListView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
    path('rooms/<int:pk>/reserve/', views.ReservationCreateView.as_view(), name='room_reserve'),
]
