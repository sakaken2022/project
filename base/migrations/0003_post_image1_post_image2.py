# Generated by Django 4.0.6 on 2022-12-14 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_delete_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(default=1, upload_to='photos', verbose_name='イメージ1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='イメージ2'),
        ),
    ]