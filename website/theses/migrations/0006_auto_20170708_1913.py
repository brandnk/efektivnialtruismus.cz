# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-08 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('theses', '0005_remove_thesispage_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThesisSimple',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('rawHtml', wagtail.core.blocks.RawHTMLBlock())))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='thesisindexpage',
            name='intro',
            field=wagtail.core.fields.StreamField((('rawHtml', wagtail.core.blocks.RawHTMLBlock()), ('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()))),
        ),
    ]
