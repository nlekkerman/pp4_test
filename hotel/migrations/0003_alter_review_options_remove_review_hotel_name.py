# Generated by Django 4.2.11 on 2024-05-09 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_review_updated_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='review',
            name='hotel_name',
        ),
    ]
