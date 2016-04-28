"""Settings that need to be set in order to run the tests."""
import os


DEBUG = True
SITE_ID = 1

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = 'image_gallery.tests.urls'

PROJECT_ROOT = os.path.realpath(
    os.path.join(os.path.dirname(__file__), "../"))

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../media/')
STATIC_ROOT = os.path.join(PROJECT_ROOT, '../static/')

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'tests/test_static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
    'DIRS': [os.path.join(os.path.dirname(__file__), '../templates')],
    'OPTIONS': {
        'context_processors': (
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.contrib.messages.context_processors.messages',
            'sekizai.context_processors.sekizai',
            'cms.context_processors.cms_settings',
        )
    }
}]

EXTERNAL_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'filer',
    'easy_thumbnails',
]

INTERNAL_APPS = [
    'image_gallery',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

# django-cms settings
CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
)

# easy_thumbnails settings
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

SECRET_KEY = 'foo'
