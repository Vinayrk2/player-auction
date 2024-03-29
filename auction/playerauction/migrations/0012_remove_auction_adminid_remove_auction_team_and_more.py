# Generated by Django 5.0.3 on 2024-03-24 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playerauction', '0011_alter_player_playerid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='adminId',
        ),
        migrations.RemoveField(
            model_name='auction',
            name='team',
        ),
        migrations.RemoveField(
            model_name='auctionplayer',
            name='auctionId',
        ),
        migrations.RemoveField(
            model_name='auction_teams',
            name='auctionId',
        ),
        migrations.RemoveField(
            model_name='auction_teams',
            name='teamId',
        ),
        migrations.RemoveField(
            model_name='auctionplayer',
            name='playerId',
        ),
        migrations.RemoveField(
            model_name='auctionplayer',
            name='teamId',
        ),
        migrations.DeleteModel(
            name='login',
        ),
        migrations.RemoveField(
            model_name='team',
            name='captainId',
        ),
        migrations.DeleteModel(
            name='AuctionAdmin',
        ),
        migrations.DeleteModel(
            name='Auction',
        ),
        migrations.DeleteModel(
            name='Auction_teams',
        ),
        migrations.DeleteModel(
            name='AuctionPlayer',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
