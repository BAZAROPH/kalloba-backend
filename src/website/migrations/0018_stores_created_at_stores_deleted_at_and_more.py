# Generated by Django 4.0.4 on 2022-06-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_rename_store_stores'),
    ]

    operations = [
        migrations.AddField(
            model_name='stores',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date de création'),
        ),
        migrations.AddField(
            model_name='stores',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='Date de suppression'),
        ),
        migrations.AddField(
            model_name='stores',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Date de modification'),
        ),
    ]