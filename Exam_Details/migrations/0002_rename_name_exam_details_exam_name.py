# Generated by Django 5.0.1 on 2024-01-29 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_Details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam_details',
            old_name='name',
            new_name='exam_name',
        ),
    ]
