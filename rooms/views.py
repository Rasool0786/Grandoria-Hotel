from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Room, Reservation
from .forms import ReservationForm

class RoomListView(ListView):
    model = Room
    template_name = 'rooms/room_list.html'
    context_object_name = 'rooms'
    paginate_by = 10
    

class RoomDetailView(DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'
    context_object_name = 'room'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['amenities'] = self.object.amenities.all()
        return context
    
    
class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'rooms/reservation_form.html'
    success_url = reverse_lazy('rooms:room_list')
    
    def dispatch(self, request, *args, **kwargs):
        self.room = get_object_or_404(Room, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.room = self.room
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('rooms:room_detail', kwargs={'pk': self.room.pk})