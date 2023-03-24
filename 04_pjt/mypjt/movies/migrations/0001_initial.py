# Generated by Django 3.2.18 on 2023-03-24 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('audience', models.IntegerField()),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=30)),
                ('score', models.FloatField()),
                ('poster_url', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('actor_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
