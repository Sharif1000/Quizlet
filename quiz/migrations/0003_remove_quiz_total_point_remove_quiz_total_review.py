# Generated by Django 5.0.2 on 2024-04-11 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quiz_average_rating_quiz_total_point_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='total_point',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='total_review',
        ),
    ]