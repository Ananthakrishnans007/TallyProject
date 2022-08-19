from django .urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('profit',views.profit,name='profit'),
    # path('stockcate',views.stockcate,name='stockcate'),

    path('cash_bank_books',views.cash_bank_books,name='cash_bank_books'),
    
]