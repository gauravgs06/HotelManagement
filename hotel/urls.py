from django.urls import path

from . import views

urlpatterns = [
    path('listing/<int:page>/', views.listing, name='listing')
]