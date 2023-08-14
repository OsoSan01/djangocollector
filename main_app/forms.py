from django.forms import ModelForm
from .models import Sharpening

class SharpeningForm(ModelForm):
  class Meta:
    model = Sharpening
    fields = ['date', 'condition']

