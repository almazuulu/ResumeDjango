# Generated by Django 4.0.3 on 2022-04-08 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skills'),
        ('projects', '0007_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile', verbose_name='Автор'),
        ),
    ]