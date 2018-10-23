# Generated by Django 2.1.1 on 2018-10-11 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20181011_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='discord_url',
            field=models.CharField(blank=True, default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='primary_class',
            field=models.CharField(blank=True, default='null', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='primary_role',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='profession',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='secondary_class',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='secondary_role',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='twitch_url',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='youtube_url',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]