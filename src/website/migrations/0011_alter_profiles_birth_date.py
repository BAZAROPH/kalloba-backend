# Generated by Django 4.0.4 on 2022-05-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_profiles_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='birth_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date de naissance'),
        ),
    ]
