# Generated by Django 5.0.1 on 2024-01-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_Details', '0014_examindex_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examindex',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]