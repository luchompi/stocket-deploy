# Generated by Django 4.2.2 on 2023-08-07 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0002_alter_elemento_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='elemento',
            name='delete_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
