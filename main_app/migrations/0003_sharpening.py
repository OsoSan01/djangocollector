# Generated by Django 4.2.4 on 2023-08-14 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_knife_description_alter_knife_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sharpening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Sharpen Date')),
                ('status', models.CharField(choices=[('B', 'Blunt'), ('C', 'Correction Needed'), ('H', 'Honing/Maintenance')], default='B', max_length=1)),
                ('knife', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.knife')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]