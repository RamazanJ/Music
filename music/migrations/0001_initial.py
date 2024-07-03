# Generated by Django 5.0.6 on 2024-06-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='musics/')),
                ('description', models.TextField(blank=True, max_length=360, null=True)),
                ('file', models.FileField(upload_to='music/')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('songs', models.ManyToManyField(to='music.song')),
            ],
        ),
    ]
