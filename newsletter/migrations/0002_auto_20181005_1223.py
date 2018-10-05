# Generated by Django 2.1.1 on 2018-10-05 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='body',
            new_name='html',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='tags',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='design',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
