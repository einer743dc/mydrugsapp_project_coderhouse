from django.db import models

# Create your models here.

# Country model
class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        # app_label = 'drug'
        ordering = ['name']
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

# Company model
class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=100)
    mail = models.EmailField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

# DrugType model
class DrugType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Drug Type'
        verbose_name_plural = 'Drug Types'

    def __str__(self):
        return self.name

# Drug model
class Drug(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    composition = models.CharField(max_length=255)
    package_qty = models.IntegerField()
    drugtype = models.ForeignKey(DrugType, on_delete=models.SET_NULL, null=True)
    restricted = models.BooleanField(default=False)
    stock = models.IntegerField()
    price = models.IntegerField()
    drug_picture = models.ImageField(null=True, blank=True, upload_to='media/')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Drug'
        verbose_name_plural = 'Drugs'

    def __str__(self):
        return self.name
    