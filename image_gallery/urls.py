"""URLs for the ``image_gallery`` app."""
from django.conf.urls import url
from django.views.generic import DetailView

from .models import Gallery
from .views import GalleryListView


urlpatterns = [
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(model=Gallery),
        name='image_gallery_detail'),
    url(r'^$', GalleryListView.as_view(), name='image_gallery_list'),
]
