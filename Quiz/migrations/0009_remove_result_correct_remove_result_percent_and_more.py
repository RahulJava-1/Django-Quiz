# Generated by Django 4.0.1 on 2022-10-12 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0008_rename_marks_result_correct_result_percent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='correct',
        ),
        migrations.RemoveField(
            model_name='result',
            name='percent',
        ),
        migrations.RemoveField(
            model_name='result',
            name='total',
        ),
        migrations.RemoveField(
            model_name='result',
            name='wrong',
        ),
    ]