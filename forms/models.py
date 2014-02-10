from django.db import models
from django.forms import ModelForm


class Address(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    home_number = models.IntegerField()
    apartment_number = models.IntegerField(blank=True, null=True)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    def __unicode__(self):
        return self.last_name


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['first_name', 'last_name', 'street', 'home_number',
                  'apartment_number', 'postal_code', 'city', 'country']









