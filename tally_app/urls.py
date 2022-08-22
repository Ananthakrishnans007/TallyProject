from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),

    path('cash_bank_summary',views.cash_bank_summary,name='cash_bank_summary'),

    path('group_summary',views.group_summary,name='group_summary'),

    path('ledger_cash',views.ledger_cash,name='ledger_cash'),

    #bank account

    path('bank_accounts',views.bank_accounts,name='bank_accounts'),

    path('ledger_bank',views.ledger_bank,name='ledger_bank'),


    
    #ledger

    path('ledger',views.ledger,name='ledger'),

    path('ledger_show',views.ledger_show,name='ledger_show'),

    



    
]
