from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'base.html')

# def profit(request):
#     return render(request,'profit.html') 


# def stockcate(request:)
#     return render(request,'stockcategory.html')        

def cash_bank_books(request):
    return render(request,'cash_bank_books.html')
