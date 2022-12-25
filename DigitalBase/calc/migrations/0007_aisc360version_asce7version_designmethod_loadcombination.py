# Generated by Django 3.2.9 on 2022-12-24 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_steelgrade_e'),
    ]

    operations = [
        migrations.CreateModel(
            name='AISC360Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='ASCE7Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='DesignMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='LoadCombination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.DecimalField(decimal_places=1, max_digits=2)),
                ('D', models.DecimalField(decimal_places=3, max_digits=4)),
                ('L', models.DecimalField(decimal_places=3, max_digits=4)),
                ('T', models.DecimalField(decimal_places=3, max_digits=4)),
                ('L_r', models.DecimalField(decimal_places=3, max_digits=4)),
                ('S', models.DecimalField(decimal_places=3, max_digits=4)),
                ('R', models.DecimalField(decimal_places=3, max_digits=4)),
                ('W', models.DecimalField(decimal_places=3, max_digits=4)),
                ('E', models.DecimalField(decimal_places=3, max_digits=4)),
                ('E_v', models.DecimalField(decimal_places=3, max_digits=4)),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.designmethod')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.asce7version')),
            ],
        ),
    ]
