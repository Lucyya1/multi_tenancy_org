from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


# Create your models here.
class Client(TenantMixin):
    name = models.CharField(max_length = 255)
    created_on = models.DateField(auto_now_add = True)

class Domain(DomainMixin):
    pass



# class Tenant(models.Model):
#     name = models.CharField(max_length=255)
#     domain = models.CharField(max_length=255, unique=True)

#     def __str__(self):
#         return self.name