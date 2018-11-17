# Generated by Django 2.1.2 on 2018-11-17 02:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Document',
            new_name='Article',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-last_modified'], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
    ]
