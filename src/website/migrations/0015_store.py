# Generated by Django 4.0.4 on 2022-06-10 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_remove_profiles_address_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Nom de la boutique')),
                ('store_email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email de la boutique')),
                ('store_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='Statut de la boutique')),
                ('manager_contact', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Contact du gérant')),
                ('other_contact', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Autre contact')),
                ('store_address', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Adresse de la boutique')),
            ],
        ),
    ]