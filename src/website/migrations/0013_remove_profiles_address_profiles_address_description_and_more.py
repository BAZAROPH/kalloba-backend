# Generated by Django 4.0.4 on 2022-06-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_profiles_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='address',
        ),
        migrations.AddField(
            model_name='profiles',
            name='address_description',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name="Description de l'adresse"),
        ),
        migrations.AddField(
            model_name='profiles',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Ville'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='country',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Pays'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='district',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Quartier'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='municipality',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Commune'),
        ),
    ]
