"""Models for the ``image_gallery`` app."""
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from filer.fields.folder import FilerFolderField
from filer.models.imagemodels import Image


class Gallery(models.Model):
    """
    Model to display a filer folder's contents and provide extra information.

    :title: Gallery title.
    :date: Date/Time of the gallery event.
    :location: Location of the gallery items.
    :description: Description of the gallery.
    :folder: Linked folder of the filer app.

    """
    category = models.ForeignKey(
        'image_gallery.GalleryCategory',
        verbose_name=_('Category'),
        blank=True, null=True,
    )

    title = models.CharField(
        max_length=100,
        verbose_name=_('Title'),
    )

    date = models.DateTimeField(
        verbose_name=_('Date'),
        blank=True, null=True,
    )

    location = models.CharField(
        max_length=100,
        verbose_name=_('Location'),
        blank=True, null=True,
    )

    description = PlaceholderField(
        'description',
        verbose_name=_('Description'),
    )

    folder = FilerFolderField(
        verbose_name=_('Folder'),
    )

    def __unicode__(self):
        return '{0}'.format(self.title)

    def get_absolute_url(self):
        return reverse('image_gallery_detail', kwargs={'pk': self.pk, })

    def get_folder_images(self):
        """Returns a set of images, which have been placed in this folder."""
        qs_files = self.folder.files.instance_of(Image)
        return qs_files.filter(is_public=True)


class GalleryCategory(models.Model):
    """
    Is used to categorize galleries.

    :name: Then human readable name of the category.
    :slug: The slug of the category

    """
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    slug = models.SlugField(
        max_length=32,
        verbose_name=_('Slug'),
    )

    def __unicode__(self):
        return self.name


class GalleryPlugin(CMSPlugin):
    """Plugin model to link to a specific gallery instance."""
    gallery = models.ForeignKey(
        Gallery,
        verbose_name=_('Gallery'),
    )
