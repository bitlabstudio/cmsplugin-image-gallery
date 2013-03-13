"""Tests for the tags of the ``image_gallery`` app."""
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.template.context import RequestContext
from django.test import TestCase
from django.test.client import RequestFactory

from ..templatetags.image_gallery_tags import render_pictures
from ..tests.factories import GalleryFactory, ImageFactory


class RenderPicturesTestCase(TestCase):
    """Tests for the ``render_pictures`` tag."""
    longMessage = True

    def setUp(self):
        # create context mock
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        SessionMiddleware().process_request(request)
        request.session.save()
        self.context = RequestContext(request)
        self.gallery = GalleryFactory()

    def test_tag(self):
        # Returns None, because of an invalid selection name
        self.assertFalse(render_pictures(self.context, selection='fail'))

        # Returns empty queryset
        self.assertFalse(render_pictures(self.context).get('pictures'))

        # Returns two pictures
        ImageFactory(folder=self.gallery.folder)
        ImageFactory(folder=self.gallery.folder)
        self.assertEqual(
            render_pictures(self.context).get('pictures').count(), 2)

        # Returns one picture, because amount was set to `1`
        ImageFactory(folder=self.gallery.folder)
        ImageFactory(folder=self.gallery.folder)
        self.assertEqual(render_pictures(self.context, 'recent', 1).get(
            'pictures').count(), 1)

        # Returns three random pictures
        self.assertEqual(
            render_pictures(self.context, 'random').get('pictures').count(), 3)
