"""Template tags for the ``image_gallery`` app."""
from django import template

from filer.models import Image

register = template.Library()


@register.inclusion_tag('image_gallery/pictures.html', takes_context=True)
def render_pictures(context, amount=3, selection='recent'):
    """Template tag to render a list of pictures."""
    if selection == 'recent':
        pictures = Image.objects.all().order_by('-uploaded_at')[:amount]
    elif selection == 'random':
        pictures = Image.objects.all().order_by('?')[:amount]
    else:
        return None
    return {'pictures': pictures}
