from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Knife
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
  sharpening_form = SharpeningForm()
  return render(request, 'knives/detail.html', {
    'knife':knife, 'sharpening_form': sharpening_form
  })


class KnifeCreate(CreateView):
  model = Knife
  fields = '__all__'

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