from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('knives/', views.knives_index, name='index'),
  path('knives/<int:knife_id>/', views.knives_detail, name="detail"),
]