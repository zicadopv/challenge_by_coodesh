# Generated by Django 4.0 on 2021-12-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voos', '0013_delete_launch_remove_voo_events_delete_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='voo',
            name='events',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
