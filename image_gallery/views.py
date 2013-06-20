"""Views for the ``image_gallery`` app."""
from django.views.generic import ListView

from .app_settings import PAGINATION_AMOUNT
from .models import Gallery, GalleryCategory


class GalleryListView(ListView):
    """View to display a list of ``Gallery`` instances."""
    paginate_by = PAGINATION_AMOUNT

    def get_queryset(self):
        self.category = self.request.GET.get('category')
        if self.category:
            return Gallery.objects.filter(
                is_published=True, category__slug=self.category).order_by(
                    '-date')
        return Gallery.objects.filter(is_published=True).order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(GalleryListView, self).get_context_data(**kwargs)
        ctx.update({'categories': GalleryCategory.objects.all()})
        if self.category:
            ctx.update({'active_category': self.category})
        return ctx
