# flake8: noqa
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.folder
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('filer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('date', models.DateTimeField(null=True, verbose_name='Date', blank=True)),
                ('location', models.CharField(max_length=100, null=True, verbose_name='Location', blank=True)),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GalleryCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('slug', models.SlugField(max_length=32, verbose_name='Slug')),
            ],
            options={
                'ordering': ('slug',),
                'verbose_name': 'Gallery Category',
                'verbose_name_plural': 'Gallery Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GalleryImageExtension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_featured_image', models.BooleanField(default=False, verbose_name='Is featured image')),
                ('image', models.OneToOneField(verbose_name='Image', to='filer.Image')),
            ],
            options={
                'verbose_name': 'Gallery Image Extension',
                'verbose_name_plural': 'Gallery Image Extensions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GalleryPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('display_type', models.CharField(blank=True, max_length=256, choices=[(b'default', 'Default'), (b'teaser', 'Teaser')])),
                ('gallery', models.ForeignKey(verbose_name='Gallery', to='image_gallery.Gallery')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(verbose_name='Category', blank=True, to='image_gallery.GalleryCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=cms.models.fields.PlaceholderField(slotname='description', editable=False, to='cms.Placeholder', null=True, verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='folder',
            field=filer.fields.folder.FilerFolderField(verbose_name='Folder', to='filer.Folder'),
            preserve_default=True,
        ),
    ]
