# Generated by Django 4.2.3 on 2023-07-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_quizuser_groups_quizuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
