from django.urls import path 
from . import views 

urlpatterns = [ 
    path('save-license', views.saveLicense.as_view(), name='Save License'),
    
]