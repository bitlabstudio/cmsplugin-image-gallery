"""Factories for the models of the ``filer_gallery`` app."""
from factory import Factory, SubFactory

from filer_gallery.models import Gallery, GalleryPlugin


class GalleryFactory(Factory):
    FACTORY_FOR = Gallery

    title = 'Test Gallery'


class GalleryPluginFactory(Factory):
    FACTORY_FOR = GalleryPlugin

    gallery = SubFactory(GalleryFactory)
