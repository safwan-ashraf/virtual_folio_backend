# Generated by Django 3.2.9 on 2021-11-30 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0006_rename_category_project_categori'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='categori',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(default='App', max_length=128),
            preserve_default=False,
        ),
    ]