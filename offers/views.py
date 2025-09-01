from django.views.generic import ListView
from django.utils import timezone

from .models import Offer


class OfferListView(ListView):
    model = Offer
    template_name = 'offers/offer_list.html'
    context_object_name = 'offers'
    paginate_by = 10

    def get_queryset(self):
        today = timezone.now().date()
        return Offer.objects.filter(
            acive=True,
            start_date__lte=today,
            end_date__gte=today
        ).order_by('-start_date')
