# Generated by Django 2.1.2 on 2018-11-17 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsletters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('document_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='newsletters.Newsletter')),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newsletterCommentModifier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Newsletter Comment',
                'verbose_name_plural': 'Newsletter Comments',
                'ordering': ('-last_modified',),
            },
        ),
    ]