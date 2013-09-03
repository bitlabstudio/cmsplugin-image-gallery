"""Simple admin registration for ``image_gallery`` models."""
from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdmin
from filer.admin.imageadmin import ImageAdmin

from . import models


class GalleryAdmin(PlaceholderAdmin):
    """Custom admin for the ``Gallery`` model."""
    list_display = ('title', 'date', 'location', 'folder', 'category')
    list_filter = ['category', ]


class GalleryCategoryAdmin(admin.ModelAdmin):
    """Custom admin for the ``GalleryCategory`` model."""
    list_display = ('name', 'slug')


class GalleryImageInline(admin.TabularInline):
    model = models.GalleryImageExtension


admin.site.register(models.GalleryCategory, GalleryCategoryAdmin)
admin.site.register(models.Gallery, GalleryAdmin)
ImageAdmin.inlines = ImageAdmin.inlines[:] + [GalleryImageInline]
