# Generated by Django 5.0.6 on 2024-05-10 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_rename_average_mark_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='enable',
            field=models.BooleanField(default=True, verbose_name='Regular'),
        ),
    ]
