"""Tests for the models of the ``image_gallery`` app."""
from django.test import TestCase

from image_gallery.models import Gallery


class GalleryTestCase(TestCase):
    """Tests for the ``Gallery`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test if the ``Gallery`` model instantiates."""
        gallery = Gallery()
        self.assertTrue(gallery, msg='Should be correctly instantiated.')
