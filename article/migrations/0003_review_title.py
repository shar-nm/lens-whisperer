# Generated by Django 4.2.11 on 2024-03-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default=2, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
