# Generated by Django 3.2 on 2021-07-10 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_history_done_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listenlater',
            old_name='watch_id',
            new_name='listen_id',
        ),
    ]
