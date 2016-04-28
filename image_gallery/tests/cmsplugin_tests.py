"""Tests for models of the ``image_gallery``` application."""
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.template.context import RequestContext
from django.test import TestCase
from django.test.client import RequestFactory

from mixer.backend.django import mixer

from ..cms_plugins import CMSGalleryPlugin


class CMSGalleryPluginTestCase(TestCase):
    """Tests for the ``CMSGalleryPlugin`` cmsplugin."""
    longMessage = True

    def setUp(self):
        # create context mock
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        SessionMiddleware().process_request(request)
        request.session.save()
        self.context = RequestContext(request)
        self.plugin = mixer.blend('image_gallery.GalleryPlugin')
        self.cmsplugin = CMSGalleryPlugin()

    def test_render(self):
        self.assertEqual(
            self.cmsplugin.render(context=self.context, instance=self.plugin,
                                  placeholder=None).get('gallery'),
            self.plugin.gallery)
