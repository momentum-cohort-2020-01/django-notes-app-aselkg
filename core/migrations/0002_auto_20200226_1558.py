# Generated by Django 3.0.3 on 2020-02-26 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='description',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='item',
            new_name='title',
        ),
    ]
