# Generated by Django 4.2.4 on 2024-05-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_teachers_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abouts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
