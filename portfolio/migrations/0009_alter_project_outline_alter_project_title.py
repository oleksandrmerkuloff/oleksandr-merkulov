# Generated by Django 5.1.3 on 2025-01-07 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_project_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='outline',
            field=models.CharField(max_length=450),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]