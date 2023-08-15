from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Knife, Accessory
from .forms import SharpeningForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def knives_index(request):
  knives = Knife.objects.all()
  return render(request, 'knives/index.html', {
    'knives': knives
  })


def knives_detail(request, knife_id):
  knife = Knife.objects.get(id=knife_id)
  id_list = knife.accessories.all().values_list('id')
  accessories_knife_doesnt_have = Accessory.objects.exclude(id__in=id_list)
  sharpening_form = SharpeningForm()
  return render(request, 'knives/detail.html', {
    'knife':knife, 'sharpening_form': sharpening_form,
    "accessories": accessories_knife_doesnt_have
  })


class KnifeCreate(CreateView):
  model = Knife
  fields = ['name', 'type', 'description', 'size']

class KnifeUpdate(UpdateView):
  model = Knife
  fields = ['type', 'description', 'size']

class KnifeDelete(DeleteView):
  model = Knife
  succes_url = '/knives'

def add_sharpening(request, knife_id):
  form = SharpeningForm(request.POST)
  if form.is_valid():
    new_sharpening = form.save(commit=False)
    new_sharpening.knife_id = knife_id
    new_sharpening.save()
    return redirect('detail', knife_id=knife_id)
  

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'purpose']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories'

def assoc_accessory(request, knife_id, accessory_id):
  Knife.objects.get(id=knife_id).accessories.add(accessory_id)
  return redirect('detail', knife_id=knife_id)

def unassoc_accessory(request, knife_id, accessory_id):
  Knife.objects.get(id=knife_id).accessories.remove(accessory_id)
  return redirect('detail', knife_id=knife_id)