# Generated by Django 4.2.4 on 2023-08-14 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_accessory_knife_accessories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='knife',
            old_name='accessories',
            new_name='accessory',
        ),
    ]
