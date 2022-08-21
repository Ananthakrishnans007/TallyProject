from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request,'index.html')


# Cash in Hand    


def cash_bank_summary(request):
    return render(request,'cash_bank_summary.html')

def group_summary(request):
    return render(request,'group_summary.html')    
    
    