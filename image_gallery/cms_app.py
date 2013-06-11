"""CMS apphook for the ``image_gallery`` app."""
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class ImageGalleryApphook(CMSApp):
    name = _("Image Gallery Apphook")
    urls = ["image_gallery.urls"]


apphook_pool.register(ImageGalleryApphook)
