"""Tests for the views of the ``image_gallery`` app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewRequestFactoryTestMixin
from mixer.backend.django import mixer

from .. import views


class GalleryListViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    """Tests for the ``GalleryListView`` view class."""
    view_class = views.GalleryListView

    def setUp(self):
        self.gallery = mixer.blend(
            'image_gallery.Gallery',
            category=mixer.blend('image_gallery.GalleryCategory'))

    def test_view(self):
        self.is_callable()
        self.is_callable(data={'category': self.gallery.category.slug})
