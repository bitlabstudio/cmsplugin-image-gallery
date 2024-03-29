# Generated by Django 3.0.6 on 2020-05-05 06:21

import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.folder


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('filer', '0011_auto_20190418_0137'),
        # ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Date')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Location')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='GalleryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('slug', models.SlugField(max_length=32, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Gallery Category',
                'verbose_name_plural': 'Gallery Categories',
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='GalleryPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='image_gallery_galleryplugin', serialize=False, to='cms.CMSPlugin')),
                ('display_type', models.CharField(blank=True, choices=[('default', 'Default'), ('teaser', 'Teaser')], max_length=256)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_gallery.Gallery', verbose_name='Gallery')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GalleryImageExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_featured_image', models.BooleanField(default=False, verbose_name='Is featured image')),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Gallery Image Extension',
                'verbose_name_plural': 'Gallery Image Extensions',
            },
        ),
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='image_gallery.GalleryCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='description', to='cms.Placeholder', verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='folder',
            field=filer.fields.folder.FilerFolderField(on_delete=django.db.models.deletion.CASCADE, to='filer.Folder', verbose_name='Folder'),
        ),
    ]
