from django.urls import URLPattern, path
from . import views


urlpatterns= [
    path('', views.getRouts),
    path('rooms/', views.getRooms),
     path('rooms/<str:pk>/', views.getRoom),
]