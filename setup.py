import os
from setuptools import setup, find_packages
import image_gallery


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="cmsplugin-image-gallery",
    version=image_gallery.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, filer, gallery, django-filer, image',
    author='Tobias Lorenz',
    author_email='tobias.lorenz@bitmazk.com',
    url="https://github.com/bitmazk/cmsplugin-image-gallery",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
        'django-cms',
        'django-filer',
        'Pillow',
    ],
)
