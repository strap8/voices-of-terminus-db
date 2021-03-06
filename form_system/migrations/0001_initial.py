# Generated by Django 2.1.7 on 2019-05-08 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FormAuthorName', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Form',
                'verbose_name_plural': 'Forms',
                'ordering': ('-last_modified',),
            },
        ),
        migrations.CreateModel(
            name='FormChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=280, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('position', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FormChoiceAuthorName', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Choice',
                'verbose_name_plural': 'Choices',
                'ordering': ('question_id', 'position'),
            },
        ),
        migrations.CreateModel(
            name='FormQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, max_length=280, null=True)),
                ('question_type', models.CharField(default='Multiple', max_length=28)),
                ('image', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('position', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FormQuestionAuthorName', to=settings.AUTH_USER_MODEL)),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FormQuestion', to='form_system.Form')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='FormRecipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FormRecipient', to=settings.AUTH_USER_MODEL)),
                ('recipient_Form_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FormGroup', to='form_system.Form')),
            ],
            options={
                'verbose_name': 'Recipient',
                'verbose_name_plural': 'Recipients',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='FormResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FormResponseAuthorName', to=settings.AUTH_USER_MODEL)),
                ('choice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FormResponse', to='form_system.FormChoice')),
            ],
            options={
                'verbose_name': 'Response',
                'verbose_name_plural': 'Responses',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='formchoice',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FormChoice', to='form_system.FormQuestion'),
        ),
        migrations.AlterUniqueTogether(
            name='formresponse',
            unique_together={('author', 'choice_id')},
        ),
    ]
