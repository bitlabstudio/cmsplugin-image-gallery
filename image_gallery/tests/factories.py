"""Factories for the models of the ``image_gallery`` app."""
from factory import Factory, SubFactory
from filer.models import Folder, Image

from image_gallery.models import Gallery, GalleryPlugin


class FolderFactory(Factory):
    FACTORY_FOR = Folder

    name = 'Test Folder'


class ImageFactory(Factory):
    FACTORY_FOR = Image


class GalleryFactory(Factory):
    FACTORY_FOR = Gallery

    title = 'Test Gallery'
    folder = SubFactory(FolderFactory)


class GalleryPluginFactory(Factory):
    FACTORY_FOR = GalleryPlugin

    gallery = SubFactory(GalleryFactory)
