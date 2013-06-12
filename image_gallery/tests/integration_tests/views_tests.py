"""Tests for the views of the ``image_gallery`` app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewTestMixin

from image_gallery.tests.factories import GalleryFactory


class GalleryListViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``GalleryListView`` view class."""
    longMessage = True

    def get_view_name(self):
        return 'image_gallery_list'

    def setUp(self):
        self.gallery = GalleryFactory()

    def test_view(self):
        self.is_callable()
        self.is_callable(data={'category': self.gallery.category.slug})
