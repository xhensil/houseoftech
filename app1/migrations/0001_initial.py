# Generated by Django 3.2.6 on 2021-08-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emri', models.CharField(blank=True, max_length=30, null=True)),
                ('mbiemri', models.CharField(blank=True, max_length=30, null=True)),
                ('mosha', models.DecimalField(blank=True, decimal_places='3', max_digits='3', null=True)),
                ('pershkrimi', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
