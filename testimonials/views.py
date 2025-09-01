from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Testimonial

class TestimonialListView(ListView):
    model = Testimonial
    template_name = 'testimonials/testimonial_list.html'
    context_object_name = 'testimonials'
    paginate_by = 10  # Optional: paginate if there are many testimonials
    
    def get_queryset(self):
        return Testimonial.objects.filter(active=True).order_by('-datetime_created')
        
class TestimonialUpdateView(UpdateView):
    model = Testimonial
    fields = ['role', 'photo', 'message', 'rating', 'active']
    template_name = 'testimonials/testimonial_form.html'
    success_url = reverse_lazy('testimonials:list')  # Redirect to testimonials list after update
    
class TestimonialDeleteView(DeleteView):
    model = Testimonial
    template_name = 'testimonials/testimonial_confirm_delete.html'
    success_url = reverse_lazy('testimonials:list')  # Redirect to testimonials list after deletion
