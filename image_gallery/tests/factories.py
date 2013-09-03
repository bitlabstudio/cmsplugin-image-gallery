"""Factories for the models of the ``image_gallery`` app."""
from factory import DjangoModelFactory, LazyAttribute, SubFactory, Sequence
from filer.models import Folder, Image

from .. import models


class FolderFactory(DjangoModelFactory):
    FACTORY_FOR = Folder

    name = 'Test Folder'


class ImageFactory(DjangoModelFactory):
    FACTORY_FOR = Image


class GalleryCategoryFactory(DjangoModelFactory):
    FACTORY_FOR = models.GalleryCategory

    name = Sequence(lambda i: 'name {}'.format(i))
    slug = LazyAttribute(lambda a: a.name.replace(' ', '-'))


class GalleryImageExtensionFactory(DjangoModelFactory):
    FACTORY_FOR = models.GalleryImageExtension

    image = SubFactory(ImageFactory)


class GalleryFactory(DjangoModelFactory):
    FACTORY_FOR = models.Gallery

    title = 'Test Gallery'
    folder = SubFactory(FolderFactory)
    category = SubFactory(GalleryCategoryFactory)
    is_published = True


class GalleryPluginFactory(DjangoModelFactory):
    FACTORY_FOR = models.GalleryPlugin

    gallery = SubFactory(GalleryFactory)
