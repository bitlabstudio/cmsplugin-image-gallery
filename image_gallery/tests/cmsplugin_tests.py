"""Tests for models of the ``image_gallery``` application."""
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.template.context import RequestContext
from django.test import TestCase
from django.test.client import RequestFactory

# from filer.models import Folder
# from model_bakery import baker

# from ..cms_plugins import CMSGalleryPlugin


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
        # folder = Folder()
        # folder.save()
        # gallery = baker.make('image_gallery.Gallery', folder=folder)
        # self.plugin = baker.make('image_gallery.GalleryPlugin',
        #                          gallery=gallery)
        # self.cmsplugin = CMSGalleryPlugin()

    def _test_render(self):
        pass
        # self.assertEqual(
        #     self.cmsplugin.render(context=self.context, instance=self.plugin,
        #                           placeholder=None).get('gallery'),
        #     self.plugin.gallery)
