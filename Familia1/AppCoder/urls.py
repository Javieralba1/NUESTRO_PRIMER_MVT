from django.urls import URLPattern, path
from AppCoder import views


urlpatterns = [

     path('',views.Incio),
     path('Mama', views.Mama),
     path('Hermana',views.Hermana),
     path('Hermano',views.Hermano),
     path('Mascota',views.Novia),
     path('Novia',views.Mascota),

]