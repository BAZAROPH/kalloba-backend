from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils.text import slugify


# Create your models here.
class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, default=None, verbose_name='Adresse')
    # address = models.JSONField(null=True, default=None, verbose_name='addresse')
    contact = models.CharField(max_length=255, null=True, default=None, verbose_name='Contact')
    birth_date = models.DateField(null=True, default=None, blank=True, verbose_name='Date de naissance')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    deleted_at = models.DateTimeField(null=True, default=None, verbose_name='Date de suppression')
    picture = models.ImageField(upload_to='image/', null=True, default=None, verbose_name='Photo')

    class Meta:
        verbose_name = 'Profile'


class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True, blank=True, default=None, verbose_name='Nom')
    slug = models.SlugField(max_length=500, null=True, blank=True, default=None, verbose_name='Slug')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    deleted_at = models.DateTimeField(default=None, null=True, blank=True, verbose_name='Date de suppression')

    class Meta:
        verbose_name = 'Catégorie'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)


class SubCategories(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True, blank=True, default=None, verbose_name='Nom')
    slug = models.SlugField(max_length=500, null=True, blank=True, default=None, verbose_name='Slug')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    deleted_at = models.DateTimeField(default=None, null=True, blank=True, verbose_name='Date de suppression')
    parent = models.ForeignKey(Categories, on_delete=models.SET_NULL, blank=False, null=True,
                               verbose_name='Catégorie parent')

    class Meta:
        verbose_name = 'Sous catégorie'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategories, self).save(*args, **kwargs)


class Products(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, default=None, verbose_name='Produit')
    slug = models.SlugField(max_length=300, null=True, blank=True, default=None, verbose_name='Slug')
    price = models.DecimalField(decimal_places=2, max_digits=12, default=None, null=True, verbose_name='Prix')
    stock = models.IntegerField(null=True, default=None, verbose_name='Quantité en stock')
    image_one = models.ImageField(upload_to='image/', verbose_name='Image 1', default=None, null=True)
    image_two = models.ImageField(upload_to='image/', verbose_name='Image 2', default=None, null=True)
    image_three = models.ImageField(upload_to='image/', verbose_name='Image 3', default=None, null=True)
    image_four = models.ImageField(upload_to='image/', verbose_name='Image 4', default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date de création')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Date de modification')
    deleted_at = models.DateTimeField(default=None, null=True, verbose_name='Date de suppression')

    seller = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Vendeur')
    category = models.ManyToManyField(Categories, verbose_name='Catégorie', related_name='Products_Categories')
    subcategory = models.ManyToManyField(SubCategories, verbose_name='Sous Catégorie',
                                         related_name='Products_sub_Categories', null=True, blank=True)

    class Meta:
        verbose_name = 'Produit'
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Products, self).save()


UNIT = (
    ('percent', '%'),
    ('integer', 'nombre'),
)


class DiscountCodes(models.Model):
    code = models.TextField(default=None, null=True, verbose_name='code')
    min_purchase = models.IntegerField(null=True, default=None, verbose_name='Achat minimum')
    max_purchase = models.IntegerField(null=True, default=None, verbose_name='Achat maximal')
    deadline = models.DateTimeField(null=True, default=None, verbose_name='Date d\'expiration')
    unit = models.CharField(max_length=255, choices=UNIT, null=True, default=None, verbose_name='Unité d\'expression')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date de création')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Date de modification')
    deleted_at = models.DateTimeField(default=None, null=True, verbose_name='Date de suppression')

    client = models.ManyToManyField(User, verbose_name='Client', related_name='DiscountCode_clients')
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Vendeur')

    class Meta:
        verbose_name = 'Code Promo'


class Payments(models.Model):
    reference = models.CharField(max_length=255, null=True, default=None, verbose_name='Référence')
    motif = models.TextField(null=True, default=None, verbose_name='Motif')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date de création')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Date de modification')
    deleted_at = models.DateTimeField(default=None, null=True, verbose_name='Date de suppression')

    payer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Payeur',
                              related_name='payments_payer')
    beneficiary = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='beneficiary',
                                    related_name='payments_beneficiary')

    class Meta:
        verbose_name = 'Paiement'


class Messages(models.Model):
    content = models.TextField(null=True, default=None, verbose_name='Contenu')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date de création')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Date de modification')
    deleted_at = models.DateTimeField(default=None, null=True, verbose_name='Date de suppression')

    sender = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Envoyeur',
                               related_name='Messages_sender')
    recipient = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Destinataire',
                                  related_name='Messages_recipient')

    class Meta:
        verbose_name = 'Message'


class Orders(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date de création')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Date de modification')
    deleted_at = models.DateTimeField(default=None, null=True, verbose_name='Date de suppression')

    product = models.ManyToManyField(Products, verbose_name='Produit', related_name='Orders_products')
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Vendeur',
                               related_name='Orders_seller')
    client = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Client',
                               related_name='Orders_client')

    class Meta:
        verbose_name = 'Commande'


class Requests(models.Model):
    description = models.TextField(default=None, null=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date de création')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Date de modification')
    deleted_at = models.DateTimeField(default=None, null=True, verbose_name='Date de suppression')

    sender = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Émetteur',
                               related_name='Requests_sender')
    recipient = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Destinataire',
                                  related_name='Requests_recipient')

    class Meta:
        verbose_name = 'Requête'


class Stores(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, blank=True, default=None, verbose_name='Nom de la boutique')
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name='Email de la boutique')
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name='Statut de la boutique')
    manager_contact = models.CharField(max_length=255, null=True, blank=True, default=None,
                                       verbose_name='Contact du gérant')
    other_contact = models.CharField(max_length=255, null=True, blank=True, default=None,
                                     verbose_name='Autre contact')
    address = models.CharField(max_length=255, null=True, blank=True, default=None,
                               verbose_name='Adresse de la boutique')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date de création')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Date de modification')
    deleted_at = models.DateTimeField(default=None, null=True, verbose_name='Date de suppression')

    seller = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Propriétaire',
                               related_name='Store_User')

    class Meta:
        verbose_name = "Store"
