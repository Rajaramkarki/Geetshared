# Generated by Django 3.2 on 2021-07-13 03:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_rename_video_id_listenlater_later_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='listenlater',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
