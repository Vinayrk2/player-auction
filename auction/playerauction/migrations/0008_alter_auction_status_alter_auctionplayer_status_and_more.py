# Generated by Django 5.0.3 on 2024-03-22 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playerauction', '0007_auction_teams_auction_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='status',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='auctionplayer',
            name='status',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='login',
            name='role',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='gender',
            field=models.SmallIntegerField(),
        ),
    ]