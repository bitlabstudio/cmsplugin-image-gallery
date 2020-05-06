"""Tests for the models of the ``image_gallery`` app."""
from django.test import TestCase
from model_bakery import baker

from .utils import generate_filer_folder

baker.generators.add('filer.fields.folder.FilerFolderField',
                     generate_filer_folder)


class GalleryTestCase(TestCase):
    """Tests for the ``Gallery`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test if the ``Gallery`` model instantiates."""
        gallery = baker.make('image_gallery.Gallery')
        self.assertTrue(str(gallery), msg='Should be correctly instantiated.')

    def test_get_folder_images(self):
        """Tests for the model's ``get_folder_images`` function."""
        gallery = baker.make('image_gallery.Gallery')
        self.assertEqual(gallery.get_folder_images().count(), 0, msg=(
            'Should return an empty image list.'))


class GalleryImageExtensionTestCase(TestCase):
    """Tests for the ``GalleryImageExtension`` model class."""
    longMessage = True

    def test_instantiation(self):
        obj = baker.make('image_gallery.GalleryImageExtension')
        self.assertTrue(str(obj), msg=(
            'Should be able to instantiate and save the object.'))


class GalleryCategoryTestCase(TestCase):
    """Tests for the ``GalleryCategory`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``GalleryCategory`` model."""
        gallerycategory = baker.make('image_gallery.GalleryCategory')
        self.assertTrue(str(gallerycategory))


class GalleryPluginTestCase(TestCase):
    """Tests for the ``GalleryPlugin`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``GalleryPlugin`` model."""
        galleryplugin = baker.make('image_gallery.GalleryPlugin')
        self.assertTrue(str(galleryplugin))
