# Generated by Django 4.0.6 on 2022-12-13 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0006_rename_program_c_program_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Java_Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5, verbose_name='タイトル')),
                ('subtit', models.CharField(max_length=30, verbose_name='サブタイトル')),
                ('content', models.TextField(verbose_name='問題文')),
                ('code', models.TextField(verbose_name='プログラム')),
            ],
        ),
        migrations.CreateModel(
            name='Python_Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5, verbose_name='タイトル')),
                ('subtit', models.CharField(max_length=30, verbose_name='サブタイトル')),
                ('content', models.TextField(verbose_name='問題文')),
                ('code', models.TextField(verbose_name='プログラム')),
            ],
        ),
    ]
