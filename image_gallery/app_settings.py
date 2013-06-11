"""Settings of the ``image_gallery``` application."""
from django.conf import settings

PAGINATION_AMOUNT = getattr(settings, 'GALLERY_PAGINATION_AMOUNT', 10)
