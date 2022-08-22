from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request,'index.html')


# Cash in Hand    


def cash_bank_summary(request):
    return render(request,'cash_bank_summary.html')

def group_summary(request):
    return render(request,'group_summary.html')    
    

def ledger_cash(request):
    return render(request,'ledger_cash.html')    
       

# Bank Accounts

def bank_accounts(request):
    return render(request,'bank_accounts.html')    

def ledger_bank(request):
    return render(request,'ledger_bank.html')    



#leadger 

def ledger(request):
    return render(request,'ledger.html') 

def ledger_show(request):
    return render(request,'ledger_show.html') 


  
    