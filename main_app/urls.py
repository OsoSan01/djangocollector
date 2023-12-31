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
  path('knives/<int:knife_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
  path('knives/<int:knife_id>/unassoc_accessory/<int:accessory_id>/', views.unassoc_accessory, name='unassoc_accessory'),
  path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
  path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
  path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
  path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
  path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),
]

