from django.views.generic import ListView

from .models import GalleryImage


class GalleryListView(ListView):
    model = GalleryImage
    template_name = "gallery/gallery_list.html"
    context_object_name = "images"
    paginate_by = 12

    def get_queryset(self):
        queryset = GalleryImage.objects.filter(active=True).order_by(
            "-datetime_created"
        )

        filter_param = self.request.GET.get("filter", "*")
        if filter_param != "*":
            filter_mapping = {
                "rm": "rooms",
                "as": "amenities",
                "dr": "dining",
                "ex": "exterior",
            }
            title_value = filter_mapping.get(filter_param)
            if title_value:
                queryset = queryset.filter(title=title_value)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_images"] = GalleryImage.objects.filter(active=True)
        context["active_filter"] = self.request.GET.get("filter", "*")
        return context
