# Generated by Django 4.0.6 on 2022-12-13 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0005_program_subtit_alter_program_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Program',
            new_name='C_Program',
        ),
        migrations.RenameModel(
            old_name='KnowledgePost',
            new_name='Knowledge',
        ),
        migrations.RenameModel(
            old_name='QuestionPost',
            new_name='Question',
        ),
    ]