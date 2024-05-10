# Generated by Django 5.0.6 on 2024-05-10 14:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.course')),
                ('student', models.ForeignKey(limit_choices_to={'groups__name': 'Student'}, on_delete=django.db.models.deletion.CASCADE, related_name='student_registration', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]