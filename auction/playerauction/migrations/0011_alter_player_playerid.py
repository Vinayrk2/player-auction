# Generated by Django 5.0.3 on 2024-03-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playerauction', '0010_remove_team_points_auctionadmin_subscription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='playerId',
            field=models.CharField(max_length=30),
        ),
    ]