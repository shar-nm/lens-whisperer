# Generated by Django 4.2.11 on 2024-03-19 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_review_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
    ]
