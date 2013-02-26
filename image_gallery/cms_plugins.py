"""CMS Plugins for the ``image_gallery`` app."""
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from filer.models.imagemodels import Image

from image_gallery.models import GalleryPlugin


class CMSGalleryPlugin(CMSPluginBase):
    model = GalleryPlugin
    name = _('Filer Gallery')
    render_template = 'image_gallery/gallery.html'

    def get_folder_images(self, folder, user):
        qs_files = folder.files.instance_of(Image)
        if user.is_staff:
            return qs_files
        else:
            return qs_files.filter(is_public=True)

    def render(self, context, instance, placeholder):
        context.update({
            'gallery': instance.gallery,
            'images': self.get_folder_images(instance.gallery.folder,
                                             context['request'].user),
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(CMSGalleryPlugin)
