"""Tests for models of the ``image_gallery``` application."""
from django.test import TestCase

from image_gallery.cms_plugins import CMSGalleryPlugin
from image_gallery.tests.factories import GalleryPluginFactory


class CMSGalleryPluginTestCase(TestCase):
    """Tests for the ``CMSGalleryPlugin`` cmsplugin."""
    longMessage = True

    def setUp(self):
        self.plugin = GalleryPluginFactory()
        self.cmsplugin = CMSGalleryPlugin()

    def test_render(self):
        self.assertEqual(
            self.cmsplugin.render(context={}, instance=self.plugin,
                                  placeholder=None),
            {'gallery': self.plugin.gallery, 'placeholder': None})
