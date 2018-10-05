# Generated by Django 2.1.1 on 2018-10-05 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='document',
            name='last_modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_modifiers', to=settings.AUTH_USER_MODEL),
        ),
    ]