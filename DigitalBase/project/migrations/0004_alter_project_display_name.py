# Generated by Django 3.2.9 on 2021-12-18 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='display_name',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
