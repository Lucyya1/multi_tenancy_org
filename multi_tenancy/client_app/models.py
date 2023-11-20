from django.db import models

# Create your models here.
class Organization(models.Model):
    ID = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50, unique=True)
    Address = models.CharField(max_length=200, blank=True)
    Email = models.EmailField(blank=True)
    EIN = models.CharField(max_length=10, blank=True)


class Othertable(models.Model):
    # Your other model fields here
    Name = models.CharField(max_length=50, unique=True)
    Org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)