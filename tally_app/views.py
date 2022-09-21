from multiprocessing import context
from tokenize import group
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def Index(request):
    return render(request,'index.html')



def cash_bank_books_cash_bank_summary(request):

   
    group = Account_Books_Group_under.objects.all()


    balance = cash_bank_books_Group_Under_closing_balance.objects.all()
    total_debit=0
    total_credit=0

    for i in balance:
        if i.total_closing_balance_debit:
            total_debit += i.total_closing_balance_debit
        if  i.total_closing_balance_credit:  
            total_credit += i.total_closing_balance_credit

    
    
    context = {
        
        'group':group,
        'total_debit':total_debit,
        'total_credit':total_credit,
        


        

    }

  
    
    return render(request,'cash_bank_books_cash_bank_summary.html',context)

def cash_bank_books_group_summary(request,id):
    ledger = Account_Books_Ledger.objects.filter(group_under=id)
    
    total_debit=0
    total_credit=0

    for i in ledger:
        if i.ledger_opening_bal_type == 'Dr':
            clo =cash_bank_books_TotalClosing_balance.objects.filter(ledger= i.id)
            for j in clo:
                if j.type =="Dr":
                    if j.Total_Closing_balance :
                        total_debit += j.Total_Closing_balance
                else:
                    if j.Total_Closing_balance :
                        total_credit += j.Total_Closing_balance


                
        else:
            clo =cash_bank_books_TotalClosing_balance.objects.filter(ledger= i.id)
            for j in clo:
                if j.type =="Cr":
                    if j.Total_Closing_balance :
                        total_credit += j.Total_Closing_balance
                else:
                    if j.Total_Closing_balance :
                        total_debit += j.Total_Closing_balance    


         

    if cash_bank_books_Group_Under_closing_balance.objects.filter(group_under=id):

        gp = cash_bank_books_Group_Under_closing_balance.objects.get(group_under=id)
        group = Account_Books_Group_under.objects.get(id=id)
        gp.group_under= group
        gp.total_closing_balance_debit = total_debit
        gp.total_closing_balance_credit =  total_credit
        gp.save()

       
        
    else:
        gp = cash_bank_books_Group_Under_closing_balance()
        group = Account_Books_Group_under.objects.get(id=id)
        gp.group_under= group
        gp.total_closing_balance_debit = total_debit
        gp.total_closing_balance_credit =  total_credit
        gp.save()


        

    

    context ={
        'ledger' :ledger,
        'total_debit':total_debit,
        'total_credit':total_credit,
        


    }



    return render(request,'cash_bank_books_cash_bank_summary2.html',context)   
    



def cash_bank_books_ledger_show(request,id,pk):
    
    le = Account_Books_Ledger.objects.get(id=id)
    voucher = Account_books_Ledger_Voucher.objects.filter(ledger=le,month=pk)
    ledger = Account_Books_Ledger.objects.filter(id=le.id)
    
    ledger_n = le.ledger_name

    total_debit=0 
    total_credit=0 
    total_balance1 =0
    total_balance2 =0
    current_total1 = 0
    current_total2 =0
    for i in voucher:
        if i.Debit :

            total_debit +=  i.Debit
        if i.Credit :
            total_credit = total_credit + i.Credit


    total_balance1 = le.ledger_opening_bal+total_debit

    total_balance2 = le.ledger_opening_bal+total_credit

    
    if total_debit or total_credit!=0:
        if le.ledger_opening_bal_type =="Dr":
            current_total1 = total_balance1 - total_credit
            if (current_total1 < 0):
                current_total1 = -1*current_total1
                if cash_bank_books_Leger_Month_closing.objects.filter(Ledger=le,month=pk):
                    cl = cash_bank_books_Leger_Month_closing.objects.get(Ledger=le,month=pk)
                    cl.Ledger = le
                    mon = Months.objects.get(id=pk)
                    cl.month = mon 
                    cl.Closing_balance = current_total1
                    if total_balance1 >total_credit:
                        cl.type = 'Dr'
                    else:
                        cl.type = 'Cr'

                    cl.debit = total_debit
                    cl.credit =total_credit
                    cl.save()
                else:
                    cl = cash_bank_books_Leger_Month_closing()
                    cl.Ledger = le
                    mon = Months.objects.get(id=pk)
                    cl.month = mon 
                    cl.Closing_balance = current_total1
                    if total_balance1 >total_credit:
                        cl.type = 'Dr'
                    else:
                        cl.type = 'Cr'
                    cl.debit = total_debit
                    cl.credit =total_credit
                    cl.save()
            else:
                if cash_bank_books_Leger_Month_closing.objects.filter(Ledger=le,month=pk):
                    cl = cash_bank_books_Leger_Month_closing.objects.get(Ledger=le,month=pk)
                    cl.Ledger = le
                    mon = Months.objects.get(id=pk)
                    cl.month = mon 
                    cl.Closing_balance = current_total1
                    if total_balance1 >total_credit:
                        cl.type = 'Dr'
                    else:
                        cl.type = 'Cr'
                    cl.debit = total_debit
                    cl.credit =total_credit
                    cl.save()
                else:
                    cl = cash_bank_books_Leger_Month_closing()
                    cl.Ledger = le
                    mon = Months.objects.get(id=pk)
                    cl.month = mon 
                    cl.Closing_balance = current_total1
                    if total_balance1 >total_credit:
                        cl.type = 'Dr'
                    else:
                        cl.type = 'Cr'
                    cl.debit = total_debit
                    cl.credit =total_credit
                    cl.save() 
        else:
            if le.ledger_opening_bal_type =="Cr":
                current_total2 = total_balance2 - total_debit
                if (current_total2 < 0):
                    current_total2 = -1*current_total2
                    if cash_bank_books_Leger_Month_closing.objects.filter(Ledger=le,month=pk):
                        cl = cash_bank_books_Leger_Month_closing.objects.get(Ledger=le,month=pk)
                        cl.Ledger = le
                        mon = Months.objects.get(id=pk)
                        cl.month = mon 
                        cl.Closing_balance = current_total2
                        if total_balance2 >total_debit:
                            cl.type = 'Cr'
                        else:
                            cl.type = 'Dr'
                        cl.debit = total_debit
                        cl.credit =total_credit
                        cl.save()
                    else:
                        cl = cash_bank_books_Leger_Month_closing()
                        cl.Ledger = le
                        mon = Months.objects.get(id=pk)
                        cl.month = mon 
                        cl.Closing_balance = current_total2
                        if total_balance2 >total_debit:
                            cl.type = 'Cr'
                        else:
                            cl.type = 'Dr'
                        cl.debit = total_debit
                        cl.credit =total_credit
                        cl.save()
                else:
                    if cash_bank_books_Leger_Month_closing.objects.filter(Ledger=le,month=pk):
                        cl = cash_bank_books_Leger_Month_closing.objects.get(Ledger=le,month=pk)
                        cl.Ledger = le
                        mon = Months.objects.get(id=pk)
                        cl.month = mon 
                        cl.Closing_balance = current_total2
                        if total_balance2 >total_debit:
                            cl.type = 'Cr'
                        else:
                            cl.type = 'Dr'
                        cl.debit = total_debit
                        cl.credit =total_credit
                        cl.save()
                    else:
                        cl = cash_bank_books_Leger_Month_closing()
                        cl.Ledger = le
                        mon = Months.objects.get(id=pk)
                        cl.month = mon 
                        cl.Closing_balance = current_total2
                        if total_balance2 >total_debit:
                            cl.type = 'Cr'
                        else:
                            cl.type = 'Dr'
                        cl.debit = total_debit
                        cl.credit =total_credit
                        cl.save()





                
    type =""
    closing_balance =0
    if cash_bank_books_Leger_Month_closing.objects.filter(Ledger=le,month=pk):
        tcl1 = cash_bank_books_Leger_Month_closing.objects.get(Ledger=le,month=pk)
        type = tcl1.type
        closing_balance = tcl1.Closing_balance 


    context={
        'voucher' : voucher,
        'ledger' :ledger,
        'ledger_name':ledger_n,
        'total_debit':total_debit,
        'total_credit':total_credit,
        'current_total1':current_total1,
        'current_total2' :current_total2,
        "type1":type,
        'closing_balance':closing_balance,
        


    }
    

    return render(request,'cash_bank_books_ledger_show.html',context)  

     

def account_books_ledger_show2(request,id):
    voucher = Account_books_Ledger_Voucher.objects.filter(ledger=id)
    ledger = Account_Books_Ledger.objects.filter(id=id)
    le = Account_Books_Ledger.objects.get(id=id)


    total_debit=0
    total_credit=0
    total_balance1=0
    total_balance2 =0
    closing_balance =0


    for i in voucher:
        if i.Debit :

            total_debit +=  i.Debit
        if i.Credit :
            total_credit = total_credit + i.Credit

    total_balance1 = le.ledger_opening_bal+total_debit

    total_balance2 = le.ledger_opening_bal+total_credit

    if le.ledger_opening_bal_type =="Dr":
            closing_balance = total_balance1 - total_credit
            if (closing_balance < 0):
                closing_balance = -1*closing_balance
            type2="Dr"    
    else:
        closing_balance = total_balance1 - total_credit
        if (closing_balance < 0):
            closing_balance = -1*closing_balance
        type2="Cr"     



            


    context={
        'voucher' : voucher,
        'ledger' :ledger,
        
        'total_debit':total_debit,
        'total_credit':total_credit,
        'closing_balance':closing_balance,
        'type2':type2,
        'le':le
        
        
        
     }  


    return render(request,'account_books_ledger_show2.html',context) 





#leadger 

def account_books_create_ledger(request):
    group = Account_Books_Group_under.objects.all()
    

    context = {
        'group' : group ,
        
    }

    return render(request,'account_books_ledger_load_create_ledger.html',context) 

def account_books_ledger(request):
    ledger = Account_Books_Ledger.objects.all()
    

    context = {
        'ledger' :ledger,
        
    }

    return render(request,'account_books_ledger.html',context ) 



def cash_bank_books_ledger_monthly_summary(request,id):
    le = Account_Books_Ledger.objects.get(id=id)
    voucher = Account_books_Ledger_Voucher.objects.filter(ledger=le)
    ledger = Account_Books_Ledger.objects.filter(id=le.id)
    
    ledger_n = le.ledger_name

   
    le_id = le.id
    mo = Months.objects.all()
    lemo = cash_bank_books_Leger_Month_closing.objects.filter(Ledger=le)

   
    total_debit=0 
    total_credit=0 
    total_balance1 =0
    total_balance2 =0
    current_total1 = 0
    current_total2 =0
    open_balance = 0
    closing_balance=0
    closing_balance_debit=0
    closing_balance_credit=0


    for i in lemo:
        if i.debit :

            total_debit +=  i.debit
        if i.credit :
            total_credit = total_credit + i.credit

        if i.Closing_balance :
            if i.type == "Dr":
                closing_balance_debit += i.Closing_balance
            else:
                closing_balance_credit += i.Closing_balance

    closing_balance  =  closing_balance_debit - closing_balance_credit 

     
    

    open_balance = le.ledger_opening_bal

    
    type =le.ledger_opening_bal_type
    
    if cash_bank_books_TotalClosing_balance.objects.filter(ledger=le_id):

        tc = cash_bank_books_TotalClosing_balance.objects.get(ledger=le_id)
        
        tcl = Account_Books_Ledger.objects.get(id=id)
        tc.ledger=tcl
        
        if closing_balance < 0:
            closing_balance = -1*closing_balance
            print(closing_balance)  
            tc.Total_Closing_balance = closing_balance
            tc.type="Cr"
        else:
            tc.Total_Closing_balance = closing_balance
            print(closing_balance)
            tc.type="Dr"

        tc.save()
        

        
    else:
        tc = cash_bank_books_TotalClosing_balance()
        tcl = Account_Books_Ledger.objects.get(id=id)
        tc.ledger=tcl
        if closing_balance == - closing_balance:
            closing_balance = -1*closing_balance
            tc.Total_Closing_balance = closing_balance
            tc.type="Cr"
        else:
            tc.Total_Closing_balance = closing_balance
            tc.type="Dr"

        tc.save()
          
    tc_type = cash_bank_books_TotalClosing_balance.objects.get(ledger=le_id)
    type1 = tc_type.type 
    


    context={
        'voucher' : voucher,
        'ledger' :ledger,
        'ledger_name':ledger_n,
        'total_debit':total_debit,
        'total_credit':total_credit,
        'current_total1':current_total1,
        'current_total2':current_total2,
        'open_balance':open_balance,
        'le_id' :le_id,
        'type':type,
        'mo':mo,
        'lemo':lemo,
        'le':le,
        'closing_balance':closing_balance,
        'type1':type1


    }

    

    return render(request,'cash_bank_books_ledger_monthly_summary.html',context) 



  
def create_ledger(request):
    
        if request.method=='POST':
            nm=request.POST.get('name')
            als=request.POST.get('alias')
            under=request.POST.get('under')
            mname=request.POST.get('mailingname')
            adr=request.POST.get('address')
            st=request.POST.get('state')
            cntry=request.POST.get('country')
            pin=request.POST.get('pincode')
            pno=request.POST.get('pan_no')
            bdetls=request.POST.get('bank_details')
            rtype=request.POST.get('registration_type')
            gst_uin=request.POST.get('gst_uin')
            opnbn=request.POST.get('opening_blnc')
            type = request.POST['Type']

            spdl=request.POST.get('set_odl')
            achnm=request.POST.get('ac_holder_nm')
            acno=request.POST.get('acc_no')
            ifsc=request.POST.get('ifsc_code')
            scode=request.POST.get('swift_code')
            bn=request.POST.get('bank_name')
            brnch=request.POST.get('branch')
            sacbk=request.POST.get('SA_cheque_bk')
            ecp=request.POST.get('Echeque_p')
            sacpc=request.POST.get('SA_chequeP_con')

            typofled=request.POST.get('type_of_ledger')
            rometh=request.POST.get('rounding_method')
            rolmt=request.POST.get('rounding_limit')

            typdutytax=request.POST.get('type_duty_tax')
            taxtyp=request.POST.get('tax_type')
            valtype=request.POST.get('valuation_type')
            rateperu=request.POST.get('rate_per_unit')
            percalc=request.POST.get('percentage_of_calcution')
            rondmethod=request.POST.get('rond_method')
            roimlit=request.POST.get('rond_limit')

            gstapplicbl=request.POST.get('gst_applicable')
            sagatdet=request.POST.get('setalter_gstdetails')
            typsupply=request.POST.get('type_of_supply')
            asseval=request.POST.get('assessable_value')
            appropto=request.POST.get('appropriate_to')
            methcalcu=request.POST.get('method_of_calculation')

            balbillbybill=request.POST.get('balance_billbybill')
            credperiod=request.POST.get('credit_period')
            creditdaysvouch=request.POST.get('creditdays_voucher')
            
            ldr=tally_ledger(name=nm,alias=als,under=under,mname=mname,address=adr,state=st,country=cntry,
                            pincode=pin,pan_no=pno,bank_details=bdetls,registration_type=rtype,gst_uin=gst_uin,
                            opening_blnc=opnbn,
                            opening_blnc_type=type,
                            set_odl=spdl,ac_holder_nm=achnm,acc_no=acno,ifsc_code=ifsc,swift_code=scode,
                            bank_name=bn,branch=brnch,SA_cheque_bk=sacbk,Echeque_p=ecp,SA_chequeP_con=sacpc,
                            type_of_ledger=typofled,rounding_method=rometh,rounding_limit=rolmt,type_duty_tax=typdutytax,tax_type=taxtyp,
                            valuation_type=valtype,rate_per_unit=rateperu,percentage_of_calcution=percalc,rond_method=rondmethod,rond_limit=roimlit,
                            gst_applicable=gstapplicbl,setalter_gstdetails=sagatdet,type_of_supply=typsupply,assessable_value=asseval,
                            appropriate_to=appropto,method_of_calculation=methcalcu,balance_billbybill=balbillbybill,credit_period=credperiod,
                            creditdays_voucher=creditdaysvouch)

                            # ,company_id=t_id
            
            ldr.save()


            group_under = Account_Books_Group_under.objects.all()
            ad =""
            for i in group_under:
                if i.group_under_Name == under:

                    ad = under

                    gup=Account_Books_Group_under.objects.get(group_under_Name=under)

                    account_book_ledger = Account_Books_Ledger()
                    account_book_ledger.ledger_name = nm
                    account_book_ledger.group_under = gup
                    account_book_ledger.ledger_opening_bal = opnbn
                    account_book_ledger.ledger_opening_bal_type = type
                    account_book_ledger.save()
                
                
            if ad != under:
                account_book_group_under = Account_Books_Group_under()
            
                account_book_group_under.group_under_Name =under
                account_book_group_under.save()

                account_book_ledger = Account_Books_Ledger()
                account_book_ledger.ledger_name = nm
                gu =Account_Books_Group_under.objects.get(id=account_book_group_under.id)
                account_book_ledger.group_under = gu
                account_book_ledger.ledger_opening_bal = opnbn
                account_book_ledger.ledger_opening_bal_type = type
                account_book_ledger.save()           


            return render(request,'account_books_ledger.html')
        return redirect('/')




def group_alt(request):  
    return render(request,'test.html') 

def ledger_chequed(request):
    return render(request,'test.html') 


def ledger_chequebk(request):
    return render(request,'test.html') 

def ledger_bd(request):
    return render(request,'test.html')  

def ledger_gst(request):
    return render(request,'test.html')  

def ledger_taxgst    (request):
    return render(request,'test.html')     

    



     
