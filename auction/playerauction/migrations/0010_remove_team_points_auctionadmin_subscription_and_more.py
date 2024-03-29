# Generated by Django 5.0.3 on 2024-03-22 03:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playerauction', '0009_alter_player_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='points',
        ),
        migrations.AddField(
            model_name='auctionadmin',
            name='subscription',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='initialPoint',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='auction',
            name='maxBid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='auction',
            name='status',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='auctionplayer',
            name='status',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='captainId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='playerauction.player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.TextField(default=None, null=True),
        ),
    ]
