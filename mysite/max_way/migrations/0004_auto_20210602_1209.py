# Generated by Django 3.2.3 on 2021-06-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('max_way', '0003_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
