from My_Books import views
from django.urls import path


app_name = 'My_Books'

urlpatterns = [
         path('form/',views.Forms, name = 'Form'),
         path('search/',views.Search, name = 'Search'),
         path('show/',views.Show, name= 'Show'),
]
