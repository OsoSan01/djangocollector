from django.shortcuts import render


# Add knifes cats list below the imports
knives = [
  {'name': 'Okeya Ginsan Ai-Deba', 'type': 'Deba-fish. Single bebel', 'description': '	Okeya knives are crafted by a Father and Son team in Miki City, Hyogo. The Ginsan (Silver 3, GIN3) Stainless Steel series of knives are incredible value for money, perhaps the best we offer. All stainless, with a unique Tsuchime (hammered) finish, they are hardened to HRC61 and hold a great edge without being brittle, whilst being very light and nimble. The grinds are thin behind the edge but come to have a 2mm thick spine. ', 'size': 135},
  {'name': 'HADO Blue 1 Damascus Bunka', 'type': 'Bunka. General purpose', 'description': "HADO Sakai are, in our opinion, among Japan's premier knife makers. Everything about their ranges is exquisite. The packaging has been custom designed in collaboration with French artist Phillipe Weisbecker, of which this packaging houses one of the finest blades we have ever seen.", 'size': 167},
]


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def knives_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'knives/index.html', {
    'knives': knives
  })
