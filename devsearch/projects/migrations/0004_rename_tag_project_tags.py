# Generated by Django 3.2.4 on 2022-06-25 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20220625_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tag',
            new_name='tags',
        ),
    ]
