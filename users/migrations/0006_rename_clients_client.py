# Generated by Django 3.2.9 on 2021-11-29 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_project_category'),
        ('users', '0005_experience_is_current'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
    ]