from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('knives/', views.knives_index, name='index'),
  path('knives/<int:knife_id>/', views.knives_detail, name="detail"),
  path('knives/create/', views.KnifeCreate.as_view(), name='knives_create'),
  path('knives/<int:pk>/update', views.KnifeUpdate.as_view(), name='knife_update'),
  path('knives/<int:pk>/delete', views.KnifeDelete.as_view(), name='knife_delete'),
  path('knives/<int:knife_id>/add_sharpening/', views.add_sharpening, name='add_sharpening'),
]