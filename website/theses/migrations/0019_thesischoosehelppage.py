# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-28 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('theses', '0018_auto_20171228_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThesisChooseHelpPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('impact', wagtail.wagtailcore.fields.StreamField((('rawHtml', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())), blank=True, null=True)),
                ('career', wagtail.wagtailcore.fields.StreamField((('rawHtml', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())), blank=True, null=True)),
                ('research', wagtail.wagtailcore.fields.StreamField((('rawHtml', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())), blank=True, null=True)),
                ('body', wagtail.wagtailcore.fields.StreamField((('rawHtml', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())), blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]