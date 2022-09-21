from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),

    path('cash_bank_books_cash_bank_summary',views.cash_bank_books_cash_bank_summary,name='cash_bank_books_cash_bank_summary'),

    path('cash_bank_books_group_summary/<int:id>',views.cash_bank_books_group_summary,name='cash_bank_books_group_summary'),

   path('cash_bank_books_ledger_monthly_summary/<int:id>',views.cash_bank_books_ledger_monthly_summary,name='cash_bank_books_ledger_monthly_summary'),

    path('cash_bank_books_ledger_show/<int:id>/<int:pk>',views.cash_bank_books_ledger_show,name='cash_bank_books_ledger_show'),

    
    #ledger

    path('account_books_ledger',views.account_books_ledger,name='account_books_ledger'),

    path('account_books_create_ledger',views.account_books_create_ledger,name='account_books_create_ledger'),

    path('create_ledger',views.create_ledger,name='create_ledger'),


    path('account_books_ledger_show2/<int:id>',views.account_books_ledger_show2,name='account_books_ledger_show2'),







    path('group_alt',views.group_alt,name='group_alt'),
    path('ledger_chequed',views.ledger_chequed,name='ledger_chequed'),
    path('ledger_chequebk',views.ledger_chequebk,name='ledger_chequebk'),
    path('ledger_bd',views.ledger_bd,name='ledger_bd'),
    path('ledger_gst',views.ledger_gst,name='ledger_gst'),
    path('ledger_taxgst ',views.ledger_taxgst ,name='ledger_taxgst'),
       

    

    

   

    
    

    

    



    
]
