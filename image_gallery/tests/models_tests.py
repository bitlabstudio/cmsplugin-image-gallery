"""Tests for the models of the ``image_gallery`` app."""
from django.test import TestCase

from ..models import Gallery
from .factories import (
    GalleryFactory,
    GalleryCategoryFactory,
    GalleryImageExtensionFactory,
    GalleryPluginFactory,
)


class GalleryTestCase(TestCase):
    """Tests for the ``Gallery`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test if the ``Gallery`` model instantiates."""
        gallery = Gallery()
        self.assertTrue(gallery, msg='Should be correctly instantiated.')

    def test_get_folder_images(self):
        """Tests for the model's ``get_folder_images`` function."""
        gallery = GalleryFactory()
        self.assertEqual(gallery.get_folder_images().count(), 0, msg=(
            'Should return an empty image list.'))


class GalleryImageExtensionTestCase(TestCase):
    """Tests for the ``GalleryImageExtension`` model class."""
    longMessage = True

    def test_instantiation(self):
        obj = GalleryImageExtensionFactory()
        self.assertTrue(obj, msg=(
            'Should be able to instantiate and save the object.'))


class GalleryCategoryTestCase(TestCase):
    """Tests for the ``GalleryCategory`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``GalleryCategory`` model."""
        gallerycategory = GalleryCategoryFactory()
        self.assertTrue(gallerycategory.pk)


class GalleryPluginTestCase(TestCase):
    """Tests for the ``GalleryPlugin`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``GalleryPlugin`` model."""
        galleryplugin = GalleryPluginFactory()
        self.assertTrue(galleryplugin.pk)
