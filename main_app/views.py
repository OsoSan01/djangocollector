from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Knife


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
  return render(request, 'knives/detail.html', {'knife':knife})


class KnifeCreate(CreateView):
  model = Knife
  fields = '__all__'

class KnifeUpdate(UpdateView):
  model = Knife
  fields = ['type', 'description', 'size']

class KnifeDelete(DeleteView):
  model = Knife
  succes_url = '/knives'