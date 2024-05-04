# Generated by Django 3.2 on 2024-05-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.CharField(max_length=256)),
                ('image_url', models.CharField(max_length=128)),
                ('discount', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
    ]
