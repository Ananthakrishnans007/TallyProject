from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),

    path('cash_bank_summary',views.cash_bank_summary,name='cash_bank_summary'),

    path('group_summary',views.group_summary,name='group_summary'),
    

    
]
