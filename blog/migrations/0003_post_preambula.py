# Generated by Django 2.1.4 on 2018-12-21 20:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_auto_20181209_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preambula',
            field=ckeditor.fields.RichTextField(default='', verbose_name='преамбула'),
            preserve_default=False,
        ),
    ]