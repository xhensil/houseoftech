# Generated by Django 3.2.7 on 2021-09-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='second',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulli', models.CharField(blank=True, max_length=30, null=True)),
                ('pershkrimi', models.TextField(blank=True, max_length=1000, null=True)),
                ('imazh', models.ImageField(blank=True, null=True, upload_to='static/images')),
            ],
        ),
    ]