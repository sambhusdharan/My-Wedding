# Generated by Django 3.2.12 on 2023-01-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventpgm', '0002_rename_date_wedding_wedding_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='friends')),
                ('Wishes', models.TextField()),
            ],
        ),
    ]
