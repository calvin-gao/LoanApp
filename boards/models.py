from django.db import models
from pytz import unicode
from django.db.models import EmailField
from datetime import datetime

class Business(models.Model):
  Name = models.CharField(max_length=255)
  Address1 = models.CharField(max_length= 100, default = '')
  Address2 = models.CharField(max_length= 100, blank = True, default = '')
  City = models.CharField(max_length=200, default = '')
  State = models.CharField(max_length=20, default = '')
  Zip = models.CharField(max_length= 10, default = '')
  AnnualRevenue = models.DecimalField(max_digits=19, decimal_places=4) 
  MonthlyAverageBankBalance = models.DecimalField(max_digits=12, decimal_places=4) 
  MonthlyAverageCreditCardVolume = models.DecimalField(max_digits=12, decimal_places=4) 
  TaxID = models.BigIntegerField()
  Phone = models.BigIntegerField()
  NAICS = models.BigIntegerField()
  HasBeenProfitable = models.BooleanField()
  HasBankruptedInLast7Years = models.BooleanField()
  InceptionDate = models.DateField(default=datetime.now)
  
  def __str__(self):
      return self.Name

  
class Owner(models.Model): 
  business = models.ForeignKey(Business, on_delete=models.CASCADE, null = True)
  Name = models.CharField(max_length=255)
  FirstName = models.CharField(max_length=255)
  LastName = models.CharField(max_length=255)
  Email = EmailField(max_length=254)
  DateOfBirth = models.DateField(default=datetime.now)
  HomePhone = models.BigIntegerField()
  SSN = models.BigIntegerField()
  PercentageOfOwnership = models.DecimalField(max_digits=12, decimal_places=2) 
  def __str__(self):
      return self.Name

class RequestHeader(models.Model):
  CFRequestId = models.CharField(max_length=255)
  RequestDate = models.DateField(max_length=40)
  CFApiUserId = models.CharField(max_length=255)
  CFApiPassword = models.CharField(max_length=20)
  IsTestLead = models.BooleanField()

class CFApplicationData(models.Model):
  RequestedLoanAmount = models.CharField(max_length=255, unique=True)
  StatedCreditHistory = models.CharField(max_length=255, unique=True)
  LegalEntityType = models.CharField(max_length=255)
  FilterID = models.CharField(max_length=255)
  
  
