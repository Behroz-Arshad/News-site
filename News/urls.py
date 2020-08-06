from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='Index' ),
    path('bbc',views.bbc,name='BBC' )
]