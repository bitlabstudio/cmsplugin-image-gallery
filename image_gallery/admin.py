"""Simple admin registration for ``image_gallery`` models."""
from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdmin

from image_gallery.models import Gallery


admin.site.register(Gallery, PlaceholderAdmin)
