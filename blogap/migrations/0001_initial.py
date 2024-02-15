# Generated by Django 3.2.3 on 2023-04-20 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=450)),
                ('imagen', models.URLField()),
                ('autor', models.CharField(max_length=50)),
            ],
        ),
    ]
