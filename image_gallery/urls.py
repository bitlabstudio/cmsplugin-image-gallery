"""URLs for the ``image_gallery`` app."""
from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView

from .app_settings import PAGINATION_AMOUNT
from .models import Gallery


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(model=Gallery),
        name='image_gallery_detail'),

    url(r'^$',
        ListView.as_view(model=Gallery, paginate_by=PAGINATION_AMOUNT),
        name='image_gallery_list'),
)
