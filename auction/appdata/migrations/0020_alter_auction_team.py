# Generated by Django 5.0.3 on 2024-04-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdata', '0019_alter_auctionplayer_teamid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='team',
            field=models.ManyToManyField(through='appdata.Auction_teams', to='appdata.team'),
        ),
    ]