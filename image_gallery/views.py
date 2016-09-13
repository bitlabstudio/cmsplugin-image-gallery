"""Views for the ``image_gallery`` app."""

from django.views.generic import ListView
from filer.models import File

from .app_settings import PAGINATION_AMOUNT
from .models import GalleryCategory


class GalleryListView(ListView):
    """View to display a list of ``Gallery`` instances."""
    paginate_by = PAGINATION_AMOUNT
    template_name = 'image_gallery/gallery_list.html'

    def get_pagination_options(self):
        options = {
            'pages_start': 10,
            'pages_visible': 4,
        }
        pages_visible_negative = -options['pages_visible']
        options['pages_visible_negative'] = pages_visible_negative
        options['pages_visible_total'] = options['pages_visible'] + 1
        options['pages_visible_total_negative'] = pages_visible_negative - 1
        return options

    def get_queryset(self):
        return File.objects.filter(
            folder__gallery__isnull=False).prefetch_related(
            'folder__gallery_set').order_by('-modified_at')

    def get_context_data(self, **kwargs):
        ctx = super(GalleryListView, self).get_context_data(**kwargs)
        ctx.update({'categories': GalleryCategory.objects.all()})
        ctx.update({'pagination': self.get_pagination_options()})
        return ctx
