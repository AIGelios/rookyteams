# Generated by Django 5.0.2 on 2024-02-25 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkillLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='defence_skill', to='skills.skilllevel')),
                ('goalkeeping', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='goalkeeping_skill', to='skills.skilllevel')),
                ('offence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='offence_skill', to='skills.skilllevel')),
            ],
        ),
    ]