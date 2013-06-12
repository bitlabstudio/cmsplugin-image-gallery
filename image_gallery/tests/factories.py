"""Factories for the models of the ``image_gallery`` app."""
from factory import Factory, LazyAttribute, SubFactory, Sequence
from filer.models import Folder, Image

from image_gallery.models import Gallery, GalleryCategory, GalleryPlugin


class FolderFactory(Factory):
    FACTORY_FOR = Folder

    name = 'Test Folder'


class ImageFactory(Factory):
    FACTORY_FOR = Image


class GalleryCategoryFactory(Factory):
    FACTORY_FOR = GalleryCategory

    name = Sequence(lambda i: 'name {}'.format(i))
    slug = LazyAttribute(lambda a: a.name.replace(' ', '-'))


class GalleryFactory(Factory):
    FACTORY_FOR = Gallery

    title = 'Test Gallery'
    folder = SubFactory(FolderFactory)
    category = SubFactory(GalleryCategoryFactory)


class GalleryPluginFactory(Factory):
    FACTORY_FOR = GalleryPlugin

    gallery = SubFactory(GalleryFactory)
