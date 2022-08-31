from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),

    path('cash_bank_summary',views.cash_bank_summary,name='cash_bank_summary'),

    path('group_summary',views.group_summary,name='group_summary'),

    path('ledger_cash',views.ledger_cash,name='ledger_cash'),

    #bank account

    path('cash_bank_summary2/<int:id>',views.cash_bank_summary2,name='cash_bank_summary2'),

    # path('ledger_bank/<int:id>',views.ledger_bank,name='ledger_bank'),


    
    #ledger

    path('ledger',views.ledger,name='ledger'),

    path('create_ledger',views.create_ledger,name='create_ledger'),

    path('save_ledger',views.save_ledger,name='save_ledger'),



    

    path('ledger_show/<int:id>/<int:pk>',views.ledger_show,name='ledger_show'),

    path('ledger_show2/<int:id>',views.ledger_show2,name='ledger_show2'),

    

    path('ledger_monthly_summary/<int:id>',views.ledger_monthly_summary,name='ledger_monthly_summary'),

    

    



    
]
