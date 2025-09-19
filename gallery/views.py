from django.views.generic import ListView
from .models import GalleryImage


class GalleryListView(ListView):
    model = GalleryImage
    template_name = "gallery/gallery_list.html"
    context_object_name = "images"
    paginate_by = 12

    def get_queryset(self):
        queryset = GalleryImage.objects.filter(active=True).order_by("-datetime_created")

        filter_param = self.request.GET.get("filter", "*")
        if filter_param != "*":
            # از فیلد title برای فیلتر استفاده می‌کنیم
            reverse_mapping = {
                "rooms": "rm",
                "amenities": "as",
                "dining": "dr",
                "exterior": "ex",
            }
            title_value = reverse_mapping.get(filter_param)
            if title_value:
                queryset = queryset.filter(title=title_value)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # از همان queryset فیلتر شده استفاده می‌کنیم
        context["all_images"] = context["images"]
        context["active_filter"] = self.request.GET.get("filter", "*")
        return context
