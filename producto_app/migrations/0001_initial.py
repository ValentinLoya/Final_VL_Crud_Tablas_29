# Generated by Django 5.1.1 on 2024-12-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('id_sucursal', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('stock', models.PositiveIntegerField()),
                ('id_provedor', models.PositiveIntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('marca', models.CharField(max_length=100)),
            ],
        ),
    ]
