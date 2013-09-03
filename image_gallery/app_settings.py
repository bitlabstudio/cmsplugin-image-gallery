"""Settings of the ``image_gallery``` application."""
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

GALLERY_DISPLAY_TYPE_CHOICES_DEFAULT = (
    ('default', _('Default')),
    ('teaser', _('Teaser')),
)

PAGINATION_AMOUNT = getattr(settings, 'GALLERY_PAGINATION_AMOUNT', 10)
DISPLAY_TYPE_CHOICES = getattr(
    settings,
    'GALLERY_DISPLAY_TYPE_CHOICES',
    GALLERY_DISPLAY_TYPE_CHOICES_DEFAULT
)
