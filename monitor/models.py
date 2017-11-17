from django.db import models

# Create your models here.


class CertInfo(models.Model):
    sn = models.CharField(max_length=20)
    organization = models.CharField(max_length=20)
    addr = models.CharField(max_length=30)
    system_name = models.CharField(max_length=20)
    start_date = models.CharField(max_length=30)
    end_date = models.CharField(max_length=30)
    isCompatible = models.BooleanField(default=True)


class MonitorInfo(models.Model):
    # current_date = models.CharField(max_length=30)
    # freq = models.IntegerField(default=5)
    # state = models.CharField(max_length=10)
    cert = models.ForeignKey('CertInfo')
    email = models.EmailField()
    phone = models.CharField(max_length=12)

