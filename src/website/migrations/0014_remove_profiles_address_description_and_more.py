# Generated by Django 4.0.4 on 2022-06-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_remove_profiles_address_profiles_address_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='address_description',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='country',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='district',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='municipality',
        ),
        migrations.AddField(
            model_name='profiles',
            name='address',
            field=models.TextField(default=None, null=True, verbose_name='Adresse'),
        ),
    ]