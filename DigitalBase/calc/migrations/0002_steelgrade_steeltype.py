# Generated by Django 3.2.9 on 2022-10-20 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SteelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SteelGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('F_y', models.IntegerField()),
                ('F_u', models.IntegerField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.steeltype')),
            ],
        ),
    ]