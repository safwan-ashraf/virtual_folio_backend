# Generated by Django 3.2.9 on 2021-11-29 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('apps', 'Apps'), ('template', 'Template'), ('ios', 'IOS'), ('ui/ux', 'UI/UX'), ('graphic', 'Graphic'), ('wireframes', 'Wireframes')], default='a', max_length=255),
            preserve_default=False,
        ),
    ]