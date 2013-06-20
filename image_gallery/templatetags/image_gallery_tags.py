"""Template tags for the ``image_gallery`` app."""
from django import template

from filer.models import Image

from image_gallery.models import Gallery

register = template.Library()


@register.inclusion_tag('image_gallery/pictures.html', takes_context=True)
def render_pictures(context, selection='recent', amount=3):
    """Template tag to render a list of pictures."""
    folder_pks = [gallery.folder.pk for gallery in Gallery.objects.filter(
        is_published=True)]
    pictures = Image.objects.filter(folder__id__in=folder_pks)
    if selection == 'recent':
        context.update({
            'pictures': pictures.order_by('-uploaded_at')[:amount]
        })
    elif selection == 'random':
        context.update({
            'pictures': pictures.order_by('?')[:amount]
        })
    else:
        return None
    return context
