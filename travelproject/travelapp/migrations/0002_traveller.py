# Generated by Django 4.1.3 on 2022-11-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='traveller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('imag', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
