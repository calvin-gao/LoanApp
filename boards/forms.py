from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from django import forms
from .models import Business, Owner

class BusinessForm(forms.ModelForm):
  
  def __init__(self, *args, **kwargs):
    super(BusinessForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper(self)
    self.helper.form_method = 'post'
    self.helper.layout = Layout(
      "Name",
      "Phone",
      "Address1",
      "Address2",
      "City",
      "State",
      "Zip",
      "AnnualRevenue",
      "MonthlyAverageBankBalance",
      "MonthlyAverageCreditCardVolume",
      "TaxID",
      "NAICS",
      "HasBeenProfitable",
      "HasBankruptedInLast7Years",
      "InceptionDate",
       Submit('submit', 'Submit', css_class='btn-success')
    )
    
  class Meta:
    model = Business
    fields = ("Name", "Phone", "Address1" , "Address2", "City", "State", "Zip", "AnnualRevenue" , "MonthlyAverageBankBalance",                  "MonthlyAverageCreditCardVolume", "TaxID", "NAICS", "HasBeenProfitable", "HasBankruptedInLast7Years", "InceptionDate")
    
  
class OwnerForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(OwnerForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper(self)
    self.helper.form_method = 'post'
    self.helper.layout = Layout(
      'Name',
      'FirstName',
      'LastName',
      'Email',
      'DateOfBirth',
      'HomePhone',
      'SSN',
      'PercentageOfOwnership',
      Submit('submit', 'Submit', css_class='btn-success')
    )
  class Meta:
    model = Owner
    fields = ('Name', 'FirstName', 'LastName', 'Email', 'DateOfBirth', 'HomePhone', 'SSN', 'PercentageOfOwnership')