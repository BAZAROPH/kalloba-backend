# Generated by Django 4.0.4 on 2022-05-15 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0007_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default=None, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date de modification')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Date de suppression')),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Requests_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Destinataire')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Requests_sender', to=settings.AUTH_USER_MODEL, verbose_name='Émetteur')),
            ],
        ),
    ]