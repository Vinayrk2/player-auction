# Generated by Django 5.0.3 on 2024-04-05 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdata', '0020_alter_auction_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurruntPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.IntegerField()),
            ],
        ),
    ]
