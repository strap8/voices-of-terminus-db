# Generated by Django 2.1.7 on 2019-03-18 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket_system', '0003_auto_20190222_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noteAuthorName', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='StatusChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statusChangeAuthorName', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'StatusChange',
                'verbose_name_plural': 'StatusChanges',
                'ordering': ('-date_created',),
            },
        ),
        migrations.AlterField(
            model_name='ticket',
            name='others_involved',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='statuschange',
            name='ticket_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statusChanges', to='ticket_system.Ticket'),
        ),
        migrations.AddField(
            model_name='note',
            name='ticket_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticketNotes', to='ticket_system.Ticket'),
        ),
    ]
