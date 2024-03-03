# Generated by Django 5.0.2 on 2024-03-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_1_ids', models.CharField(max_length=255)),
                ('team_2_ids', models.CharField(max_length=255)),
                ('match_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
