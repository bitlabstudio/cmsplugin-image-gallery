"""CMS Plugins for the ``image_gallery`` app."""
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from image_gallery.models import GalleryPlugin


class CMSGalleryPlugin(CMSPluginBase):
    model = GalleryPlugin
    name = _('Filer Gallery')
    render_template = 'image_gallery/partials/gallery.html'

    def render(self, context, instance, placeholder):
        context.update({
            'gallery': instance.gallery,
            'images': instance.gallery.get_folder_images(),
            'placeholder': placeholder,
            'display_type': instance.display_type,
        })
        return context

plugin_pool.register_plugin(CMSGalleryPlugin)
