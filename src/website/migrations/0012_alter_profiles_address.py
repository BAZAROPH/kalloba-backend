# Generated by Django 4.0.4 on 2022-05-31 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_profiles_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='address',
            field=models.JSONField(default=None, null=True, verbose_name='addresse'),
        ),
    ]