"""Models for the ``image_gallery`` app."""
from itertools import chain

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from filer.fields.folder import FilerFolderField
from filer.models.imagemodels import Image

from . import app_settings


class Gallery(models.Model):
    """
    Model to display a filer folder's contents and provide extra information.

    :title: Gallery title.
    :date: Date/Time of the gallery event.
    :location: Location of the gallery items.
    :description: Description of the gallery.
    :folder: Linked folder of the filer app.
    :is_published: True if the Gallery is published or not.

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

    is_published = models.BooleanField(
        verbose_name=_('Is published'),
        default=False,
    )

    class Meta:
        ordering = ('title', )
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')

    def __unicode__(self):
        return '{0}'.format(self.title)

    def get_absolute_url(self):
        return reverse('image_gallery_detail', kwargs={'pk': self.pk, })

    def get_featured_images(self):
        """
        Returns those images of a given Gallery that are featured images.

        TODO: Find a way to test this

        """
        result = []
        for image in self.get_folder_images():
            try:
                if image.galleryimageextension.is_featured_image:
                    result.append(image)
            except GalleryImageExtension.DoesNotExist:
                pass
        return result

    def get_folder_images(self):
        """
        Returns a set of images, which have been placed in this folder.

        TODO: Find a way to test this

        """
        qs_files = self.folder.files.instance_of(Image)
        return qs_files.filter(is_public=True)

    def get_folder_image_list(self):
        """
        Returns a list of images, which have been placed in this folder.

        They are first sorted by name, followed by those without name, sorted
        by file name.

        """
        qs_files = self.folder.files.instance_of(Image)
        qs_files = qs_files.filter(is_public=True)
        return list(chain(
            qs_files.exclude(name='').order_by('name'),
            qs_files.filter(name='').order_by('file')))


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

    class Meta:
        ordering = ('sug', )
        verbose_name = _('Gallery Category')
        verbose_name_plural = _('Gallery Categories')


class GalleryImageExtension(models.Model):
    """
    Adds extra fields to the FilerImage admin.

    :image: The Image instance this object is extending.
    :is_featured_image: A boolean field that can be used for example to render
      a teaser of a gallery and only show a few featured images.
    """
    image = models.OneToOneField(
        Image,
        verbose_name=_('Image'),
    )

    is_featured_image = models.BooleanField(
        default=False,
        verbose_name=_('Is featured image'),
    )

    class Meta:
        verbose_name = _('Gallery Image Extension')
        verbose_name_plural = _('Gallery Image Extensions')


class GalleryPlugin(CMSPlugin):
    """
    Plugin model to link to a specific gallery instance.

    :gallery: The gallery instance that this plugin should render
    :display_type: A string that will be passed to the plugin templates. This
      allows you to render the gallery differently at different places on your
      page.

    """
    gallery = models.ForeignKey(
        Gallery,
        verbose_name=_('Gallery'),
    )

    display_type = models.CharField(
        max_length=256,
        choices=app_settings.DISPLAY_TYPE_CHOICES,
        blank=True,
    )
