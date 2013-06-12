"""Views for the ``image_gallery`` app."""
from django.views.generic import ListView

from .app_settings import PAGINATION_AMOUNT
from .models import Gallery


class GalleryListView(ListView):
    """View to display a list of ``Gallery`` instances."""
    paginate_by = PAGINATION_AMOUNT

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Gallery.objects.filter(category__slug=category).order_by(
                'date')
        return Gallery.objects.all().order_by('date')
