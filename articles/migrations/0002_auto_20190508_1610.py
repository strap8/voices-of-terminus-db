# Generated by Django 2.1.7 on 2019-05-08 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(default='Article', max_length=512),
        ),
    ]
