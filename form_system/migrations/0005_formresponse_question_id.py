# Generated by Django 2.1.7 on 2019-05-15 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_system', '0004_auto_20190508_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='formresponse',
            name='question_id',
            field=models.ForeignKey(default=14, on_delete=django.db.models.deletion.CASCADE, related_name='FormQuestion', to='form_system.FormQuestion'),
            preserve_default=False,
        ),
    ]
