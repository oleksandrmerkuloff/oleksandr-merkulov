# Generated by Django 5.1.3 on 2024-12-02 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postimage',
            options={'verbose_name': 'Post Image', 'verbose_name_plural': 'Post images'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
    ]
