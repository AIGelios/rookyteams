# Generated by Django 5.0.2 on 2024-02-25 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='gk_skill',
            new_name='skill',
        ),
        migrations.RemoveField(
            model_name='player',
            name='def_skill',
        ),
        migrations.RemoveField(
            model_name='player',
            name='off_skill',
        ),
    ]