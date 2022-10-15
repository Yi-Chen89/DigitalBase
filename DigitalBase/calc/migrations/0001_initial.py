# Generated by Django 3.2.9 on 2022-10-15 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SteelSectionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='SteelSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('W', models.DecimalField(decimal_places=2, max_digits=5)),
                ('A', models.DecimalField(decimal_places=3, max_digits=6)),
                ('d', models.DecimalField(decimal_places=2, max_digits=4)),
                ('b_f', models.DecimalField(decimal_places=2, max_digits=4)),
                ('t_w', models.DecimalField(decimal_places=3, max_digits=4)),
                ('t_f', models.DecimalField(decimal_places=3, max_digits=4)),
                ('k_des', models.DecimalField(decimal_places=3, max_digits=4)),
                ('I_x', models.DecimalField(decimal_places=1, max_digits=6)),
                ('Z_x', models.DecimalField(decimal_places=2, max_digits=6)),
                ('S_x', models.DecimalField(decimal_places=2, max_digits=6)),
                ('r_x', models.DecimalField(decimal_places=2, max_digits=4)),
                ('I_y', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Z_y', models.DecimalField(decimal_places=2, max_digits=5)),
                ('S_y', models.DecimalField(decimal_places=2, max_digits=5)),
                ('r_y', models.DecimalField(decimal_places=3, max_digits=4)),
                ('J', models.DecimalField(decimal_places=4, max_digits=8)),
                ('C_w', models.DecimalField(decimal_places=1, max_digits=8)),
                ('W_no', models.DecimalField(decimal_places=2, max_digits=5)),
                ('S_w1', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Q_f', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Q_w', models.DecimalField(decimal_places=2, max_digits=6)),
                ('r_ts', models.DecimalField(decimal_places=3, max_digits=4)),
                ('h_o', models.DecimalField(decimal_places=2, max_digits=4)),
                ('P_A', models.DecimalField(decimal_places=1, max_digits=4)),
                ('P_B', models.DecimalField(decimal_places=1, max_digits=4)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.steelsectiontype')),
            ],
        ),
    ]
