CMSplugin Image Gallery
====================

A Django application adding filer-based galleries to Django-CMS.


Installation
------------

You need to install the following prerequisites in order to use this app::

    pip install Django
    pip install django-cms
    pip install django-filer
    pip install Pillow

If you want to install the latest stable release from PyPi::

    $ pip install cmsplugin-image-gallery

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/cmsplugin-image-gallery.git#egg=image_gallery

Add ``image_gallery`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'image_gallery',
    )


Usage
-----

First create a gallery object with a filer folder and set ``is_published`` to
``True`` once you want to publish the gallery.

Using the apphook
+++++++++++++++++

Simply create a django-cms page and select it in the ``Application`` field of
the ``Advanced Settings``.

Using the cmsplugin
+++++++++++++++++++

Create a CMS page with a placeholder and simply insert the plugin
``Filer Gallery``.

Using the template tags
+++++++++++++++++++++++

You can also use our template tag to display a list of pictures::

    {% render_pictures %}

...for the last 3 uploaded pictures. You can use the selection parameters
``recent`` (default) and ``random`` and set an amount of pictures to display::

    {% render_pictures 'random' 10 %}


Settings
--------

GALLERY_PAGINATION_AMOUNT
+++++++++++++++++++++++++

Default: 10

Amount of galleries to display in the list view.


GALLERY_DISPLAY_TYPE_CHOICES
++++++++++++++++++++++++++++

Default::

    (
        ('default', _('Default')),
        ('teaser', _('Teaser')),
    )

When you use the ``Filer Gallery`` plugin, you can select the gallery that
should be rendered and a display type. This is useful if one and the same
gallery should be rendrerd in different ways at different places on your
site. The selected value will be added to the plugin template's context with
the variable name ``{{ display_type }}``.


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 cmsplugin-image-gallery
    $ pip install -r requirements.txt
    $ ./logger/tests/runtests.sh
    # You should get no failing tests

    $ git co -b feature_branch master
    # Implement your feature and tests
    # Describe your change in the CHANGELOG.txt
    $ git add . && git commit
    $ git push origin feature_branch
    # Send us a pull request for your feature branch

Whenever you run the tests a coverage output will be generated in
``tests/coverage/index.html``. When adding new features, please make sure that
you keep the coverage at 100%.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
