"""Simple admin registration for ``filer_gallery`` models."""
from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdmin

from filer_gallery.models import Gallery


admin.site.register(Gallery, PlaceholderAdmin)
