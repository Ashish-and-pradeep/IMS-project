# Generated by Django 4.1.3 on 2022-12-08 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.FileField(default=None, null=True, upload_to='newimages/'),
        ),
    ]