"""Simple admin registration for ``image_gallery`` models."""
from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdmin

from image_gallery.models import Gallery


class GalleryAdmin(PlaceholderAdmin):
    """Custom admin for the ``Gallery`` model."""
    list_display = ('title', 'date', 'location', 'folder')


admin.site.register(Gallery, GalleryAdmin)
