"""Models for the ``image_gallery`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from filer.fields.folder import FilerFolderField


class Gallery(models.Model):
    """
    Model to display a filer folder's contents and provide extra information.

    :title: Gallery title.
    :date: Date/Time of the gallery event.
    :location: Location of the gallery items.
    :description: Description of the gallery.
    :folder: Linked folder of the filer app.

    """
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


class GalleryPlugin(CMSPlugin):
    """Plugin model to link to a specific gallery instance."""
    gallery = models.ForeignKey(
        Gallery,
        verbose_name=_('Gallery'),
    )
