# Generated by Django 3.1.7 on 2021-07-05 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_alter_postmodel_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
