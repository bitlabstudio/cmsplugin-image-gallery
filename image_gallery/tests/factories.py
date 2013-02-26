"""Factories for the models of the ``image_gallery`` app."""
from factory import Factory, SubFactory

from image_gallery.models import Gallery, GalleryPlugin


class GalleryFactory(Factory):
    FACTORY_FOR = Gallery

    title = 'Test Gallery'


class GalleryPluginFactory(Factory):
    FACTORY_FOR = GalleryPlugin

    gallery = SubFactory(GalleryFactory)
