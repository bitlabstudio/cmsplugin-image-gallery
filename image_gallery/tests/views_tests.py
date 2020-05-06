"""Tests for the views of the ``image_gallery`` app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewRequestFactoryTestMixin
from model_bakery import baker

from .utils import generate_filer_folder
from .. import views

baker.generators.add('filer.fields.folder.FilerFolderField',
                     generate_filer_folder)


class GalleryListViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    """Tests for the ``GalleryListView`` view class."""
    view_class = views.GalleryListView

    def setUp(self):
        self.gallery = baker.make(
            'image_gallery.Gallery',
            category=baker.make('image_gallery.GalleryCategory'))

    def test_view(self):
        self.is_callable()
        self.is_callable(data={'category': self.gallery.category.slug})
