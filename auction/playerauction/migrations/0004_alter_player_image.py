# Generated by Django 5.0.3 on 2024-03-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playerauction', '0003_alter_player_image_alter_player_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.TextField(default=None, null=True),
        ),
    ]
