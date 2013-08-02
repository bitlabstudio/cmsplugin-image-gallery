"""Factories for the models of the ``image_gallery`` app."""
from factory import DjangoModelFactory, LazyAttribute, SubFactory, Sequence
from filer.models import Folder, Image

from image_gallery.models import Gallery, GalleryCategory, GalleryPlugin


class FolderFactory(DjangoModelFactory):
    FACTORY_FOR = Folder

    name = 'Test Folder'


class ImageFactory(DjangoModelFactory):
    FACTORY_FOR = Image


class GalleryCategoryFactory(DjangoModelFactory):
    FACTORY_FOR = GalleryCategory

    name = Sequence(lambda i: 'name {}'.format(i))
    slug = LazyAttribute(lambda a: a.name.replace(' ', '-'))


class GalleryFactory(DjangoModelFactory):
    FACTORY_FOR = Gallery

    title = 'Test Gallery'
    folder = SubFactory(FolderFactory)
    category = SubFactory(GalleryCategoryFactory)
    is_published = True


class GalleryPluginFactory(DjangoModelFactory):
    FACTORY_FOR = GalleryPlugin

    gallery = SubFactory(GalleryFactory)
