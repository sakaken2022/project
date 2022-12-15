# Generated by Django 4.0.6 on 2022-12-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0004_remove_program_category_remove_program_posted_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='subtit',
            field=models.CharField(default=1, max_length=30, verbose_name='サブタイトル'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='title',
            field=models.CharField(max_length=5, verbose_name='タイトル'),
        ),
    ]