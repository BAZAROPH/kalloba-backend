# Generated by Django 4.0.4 on 2022-05-15 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0002_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Produit')),
                ('slug', models.SlugField(blank=True, default=None, max_length=300, null=True, verbose_name='Slug')),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=12, null=True, verbose_name='Prix')),
                ('stock', models.IntegerField(default=None, null=True, verbose_name='Quantité en stock')),
                ('image_one', models.ImageField(default=None, null=True, upload_to='image/', verbose_name='Image 1')),
                ('image_two', models.ImageField(default=None, null=True, upload_to='image/', verbose_name='Image 2')),
                ('image_three', models.ImageField(default=None, null=True, upload_to='image/', verbose_name='Image 3')),
                ('image_four', models.ImageField(default=None, null=True, upload_to='image/', verbose_name='Image 4')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date de modification')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Date de suppression')),
                ('category', models.ManyToManyField(related_name='Products_Categories', to='website.categories', verbose_name='Catégorie')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Vendeur')),
            ],
        ),
    ]
