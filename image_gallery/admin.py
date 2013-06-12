"""Simple admin registration for ``image_gallery`` models."""
from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdmin

from image_gallery.models import Gallery, GalleryCategory


class GalleryAdmin(PlaceholderAdmin):
    """Custom admin for the ``Gallery`` model."""
    list_display = ('title', 'date', 'location', 'folder', 'category')
    list_filter = ['category', ]


class GalleryCategoryAdmin(admin.ModelAdmin):
    """Custom admin for the ``GalleryCategory`` model."""
    list_display = ('name', 'slug')


admin.site.register(GalleryCategory, GalleryCategoryAdmin)
admin.site.register(Gallery, GalleryAdmin)
