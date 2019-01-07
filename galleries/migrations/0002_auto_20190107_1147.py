# Generated by Django 2.1.4 on 2019-01-07 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimages',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='galleryimages',
            name='last_modified_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='galleryImageModifier', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]