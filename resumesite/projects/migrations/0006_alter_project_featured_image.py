# Generated by Django 4.0.3 on 2022-04-01 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='images/default.jpeg', null=True, upload_to=''),
        ),
    ]
