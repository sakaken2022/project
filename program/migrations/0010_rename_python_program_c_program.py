# Generated by Django 4.0.6 on 2022-12-14 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0009_rename_c_program_python2_program'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Python_Program',
            new_name='C_Program',
        ),
    ]
