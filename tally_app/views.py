from multiprocessing import context
from tokenize import group
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def Index(request):
    return render(request,'index.html')


# Cash in Hand    


def cash_bank_summary(request):

    group = Group_under.objects.all()

    balance = Group_Under_closing_balance.objects.all()
    total_debit=0
    total_credit=0

    for i in balance:
        total_debit += i.total_closing_balance_debit
        total_credit += i.total_closing_balance_credit

    
    
    context = {
        
        'group':group,
        'total_debit':total_debit,
        'total_credit':total_credit


        

    }

    # print(dct_group)
    
    return render(request,'cash_bank_summary.html',context)

def group_summary(request):
    return render(request,'group_summary.html')    
    

def ledger_cash(request):
    voucher = Ledger_Voucher.objects.filter(ledger=1)
    ledger = Ledger.objects.filter(id=1)
    
    
    context={
        'voucher' : voucher,
        'ledger' :ledger,
        

    }


    return render(request,'ledger_cash.html',context)    
       

# Bank Accounts

def cash_bank_summary2(request,id):
    ledger = Ledger.objects.filter(group_under=id)
    
    total_debit=0
    total_credit=0

    for i in ledger:
        if i.ledger_opening_bal_type == 'Dr':
            clo =TotalClosing_balance.objects.filter(ledger= i.id)
            for j in clo:
                if j.Total_Closing_balance :
                    total_debit += j.Total_Closing_balance

                
        else:
            clo =TotalClosing_balance.objects.filter(ledger= i.id)
            for j in clo:
                if j.Total_Closing_balance :
                    total_credit += j.Total_Closing_balance


         

    if Group_Under_closing_balance.objects.filter(group_under=id):

        gp = Group_Under_closing_balance.objects.get(group_under=id)
        group = Group_under.objects.get(id=id)
        gp.group_under= group
        gp.total_closing_balance_debit = total_debit
        gp.total_closing_balance_credit =  total_credit
        gp.save()

       
        
    else:
        gp = Group_Under_closing_balance()
        group = Group_under.objects.get(id=id)
        gp.group_under= group
        gp.total_closing_balance_debit = total_debit
        gp.total_closing_balance_credit =  total_credit
        gp.save()


        

    

    context ={
        'ledger' :ledger,
        'total_debit':total_debit,
        'total_credit':total_credit,
        


    }



    return render(request,'cash_bank_summary2.html',context)    

def ledger_show(request,id,pk):
    
    le = Ledger.objects.get(id=id)
    voucher = Ledger_Voucher.objects.filter(ledger=le,month=pk)
    ledger = Ledger.objects.filter(id=le.id)
    
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
                if Leger_Month_closing.objects.filter(Ledger=le,month=pk):
                    cl = Leger_Month_closing.objects.get(Ledger=le,month=pk)
                    cl.Ledger = le
                    mon = LedgerMonths.objects.get(id=pk)
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
                    cl = Leger_Month_closing()
                    cl.Ledger = le
                    mon = LedgerMonths.objects.get(id=pk)
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
                if Leger_Month_closing.objects.filter(Ledger=le,month=pk):
                    cl = Leger_Month_closing.objects.get(Ledger=le,month=pk)
                    cl.Ledger = le
                    mon = LedgerMonths.objects.get(id=pk)
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
                    cl = Leger_Month_closing()
                    cl.Ledger = le
                    mon = LedgerMonths.objects.get(id=pk)
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
            current_total2 = total_balance2 - total_debit
            if (current_total2 < 0):
                current_total2 = -1*current_total2
                if Leger_Month_closing.objects.filter(Ledger=le,month=pk):
                    cl = Leger_Month_closing.objects.get(Ledger=le,month=pk)
                    cl.Ledger = le
                    mon = LedgerMonths.objects.get(id=pk)
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
                    cl = Leger_Month_closing()
                    cl.Ledger = le
                    mon = LedgerMonths.objects.get(id=pk)
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
                if Leger_Month_closing.objects.filter(Ledger=le,month=pk):
                    cl = Leger_Month_closing.objects.get(Ledger=le,month=pk)
                    cl.Ledger = le
                    mon = LedgerMonths.objects.get(id=pk)
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
                    cl = Leger_Month_closing()
                    cl.Ledger = le
                    mon = LedgerMonths.objects.get(id=pk)
                    cl.month = mon 
                    cl.Closing_balance = current_total2
                    if total_balance2 >total_debit:
                        cl.type = 'Cr'
                    else:
                        cl.type = 'Dr'
                    cl.debit = total_debit
                    cl.credit =total_credit
                    cl.save()





                
            
       
    tcl1 = Leger_Month_closing.objects.get(Ledger=le,month=pk)
    type = tcl1.type
    closing_balance = tcl1.Closing_balance 

    # mon = LedgerMonths.objects.get(id=pk)

    # if mon.month_name =="April":





    

    

      

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
    

    return render(request,'ledger_show.html',context)  

     

def ledger_show2(request,id):
    voucher = Ledger_Voucher.objects.filter(ledger=id)
    ledger = Ledger.objects.filter(id=id)
    le = Ledger.objects.get(id=id)


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


    return render(request,'ledger_show2.html',context) 





#leadger 

def create_ledger(request):
    group = Group_under.objects.all()
    

    context = {
        'group' : group ,
        
    }

    return render(request,'load_create_ledger.html',context) 

def ledger(request):
    ledger = Ledger.objects.all()
    

    context = {
        'ledger' :ledger,
        
    }

    return render(request,'ledger.html',context ) 

# def ledger_bank(request):
#     return render(request,'ledger_bank.html') 


def ledger_monthly_summary(request,id):
    le = Ledger.objects.get(id=id)
    voucher = Ledger_Voucher.objects.filter(ledger=le)
    ledger = Ledger.objects.filter(id=le.id)
    
    ledger_n = le.ledger_name

   
    le_id = le.id
    mo = LedgerMonths.objects.all()
    lemo = Leger_Month_closing.objects.filter(Ledger=le)

   
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

     
    


    # total_balance1 = le.ledger_opening_bal+total_debit

    # total_balance2 = le.ledger_opening_bal+total_credit
    
    # current_total1 =total_balance1-total_credit
    # current_total2 =total_balance2-total_credit


    open_balance = le.ledger_opening_bal

    
    type =le.ledger_opening_bal_type
    
    if TotalClosing_balance.objects.filter(ledger=le_id):

        tc = TotalClosing_balance.objects.get(ledger=le_id)
        
        tcl = Ledger.objects.get(id=id)
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
        tc = TotalClosing_balance()
        tcl = Ledger.objects.get(id=id)
        tc.ledger=tcl
        if closing_balance == - closing_balance:
            closing_balance = -1*closing_balance
            tc.Total_Closing_balance = closing_balance
            tc.type="Cr"
        else:
            tc.Total_Closing_balance = closing_balance
            tc.type="Dr"

        tc.save()
          
    tc_type = TotalClosing_balance.objects.get(ledger=le_id)
    type1 = tc_type.type 
    print(type1)


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

    

    return render(request,'ledger_monthly_summary.html',context) 


def save_ledger(request):
    if request.method == 'POST':
        # Ledger Basic
        Lname = request.POST.get('ledger_name', False)
        Lalias = request.POST.get('ledger_alias', False)

        c = request.POST['group_under']
        group =Group_under.objects.get(id=c)

        
        


        Lunder = group



        Lopening_bal = request.POST.get('ledger_opening_bal', False)
        L_ob_type = request.POST['Type']

        typ_of_ledg = request.POST.get('ledger_type', False)
        provide_banking = request.POST.get('provide_banking_details', False)

        # Banking_details
        B_od_limit = request.POST.get('od_limit', False)
        B_ac_holder_name =request.POST.get('holder_name', False)
        B_ac_no = request.POST.get('ac_number', False)
        B_ifsc = request.POST.get('ifsc', False)
        B_swift_code =request.POST.get('swift_code', False)
        B_name = request.POST.get('bank_name', False)
        B_branch = request.POST.get('branch_name', False)
        B_alter_chq_bks =request.POST.get('alter_chk_bks', False)
        B_name_enbl_chq_prtg = request.POST.get('enbl_chk_printing', False) 
        B_chqconfg= request.POST.get('chqconfg', False) 
        # Mailing_details
        Mname = request.POST.get('name', False)
        Maddress = request.POST.get('address', False)
        Mstate =request.POST.get('state', False)
        Mcountry = request.POST.get('country', False)
        Mpincode = request.POST.get('pincode', False)

        # Tax_Registration_Details
        Tgst_uin = request.POST.get('gst_uin', False)
        Treg_typ = request.POST.get('register_type', False)
        Tpan_no = request.POST.get('pan_no', False)
        T_alter_gst =request.POST.get('alter_gst_details', False)

        # Satutory Details
        assessable_calculationn = request.POST.get('assessable_calculation', False)
        Appropriate_too =request.POST.get('Appropriate_to', False)
        gst_applicablee = request.POST.get('is_gst_applicable',False)
        Set_alter_GSTT=request.POST.get('Set_alter_GST', False)
        type_of_supplyy = request.POST.get('type_of_supply',False)
        Method_of_calcc=request.POST.get('Method_of_calc', False)

        #leadger Rounding
        ledger_idd=request.POST.get('useadvc', False)
        Rounding_Methodd=request.POST.get('Rounding_Method', False)
        Round_limitt =request.POST.get('Round_limit', False)

        #ledger_tax 
        type_of_duty_or_taxx=request.POST.get('type_of_duty_or_tax', False)
        type_of_taxx=request.POST.get('type_of_tax', False)
        valuation_typee=request.POST.get('valuation_type', False)
        rate_per_unitt=request.POST.get('rate_per_unit', False)
        Persentage_of_calculationn=request.POST.get('Persentage_of_calculation', False)

        #sundry
        maintain_balance_bill_by_billl=request.POST.get('maintain_balance_bill_by_bill', False)
        Default_credit_periodd=request.POST.get('Default_credit_period', False)
        Check_for_credit_dayss=request.POST.get('Check_for_credit_days', False)

        if Ledger.objects.filter(ledger_name = Lname ).exists():
                messages.info(request,'This Name is already taken...!')
                return redirect('load_create_ledger.html')

        Lmdl = Ledger(
            ledger_name=Lname,
            ledger_alias=Lalias,
            group_under=Lunder,
            ledger_opening_bal=Lopening_bal,
            ledger_type=typ_of_ledg,
            provide_banking_details=provide_banking,
            ledger_opening_bal_type = L_ob_type,
        )
        Lmdl.save()
        idd = Lmdl
        Bmdl = Ledger_Banking_Details(
        
            ledger_id=idd,
            od_limit=B_od_limit,
            holder_name=B_ac_holder_name,
            ac_number=B_ac_no,
            ifsc=B_ifsc,
            swift_code=B_swift_code,
            bank_name=B_name,
            branch_name=B_branch,
            alter_chk_bks=B_alter_chq_bks,
            enbl_chk_printing=B_name_enbl_chq_prtg,

        )
        Bmdl.save()
        M_mdl = Ledger_Mailing_Address(

            name=Mname,
            address=Maddress,
            state=Mstate,
            country=Mcountry,
            pincode=Mpincode,
        )
        M_mdl.save()
        T_mdl = Ledger_Tax_Register(
           
          
            gst_uin=Tgst_uin,
            register_type=Treg_typ,
            pan_no=Tpan_no,
            alter_gst_details=T_alter_gst,

        )
        T_mdl.save()
        LS_mdl = Ledger_Satutory(

            ledger_id=idd,
            assessable_calculation=assessable_calculationn,
            Appropriate_to =Appropriate_too ,
            gst_applicable=gst_applicablee,
            Set_alter_GST = Set_alter_GSTT,
            type_of_supply=type_of_supplyy,
            Method_of_calc = Method_of_calcc,


        )
        LS_mdl.save()

        rnd_mdl = Ledger_Rounding(
            ledger_id=idd,
            Rounding_Method=Rounding_Methodd,
            Round_limit =Round_limitt,

        )
        rnd_mdl.save()

        tax_mdl = ledger_tax(
            ledger_id=idd,
            type_of_duty_or_tax=type_of_duty_or_taxx,
            type_of_tax =type_of_taxx,
            valuation_type=valuation_typee,
            rate_per_unit=rate_per_unitt,
            Persentage_of_calculation=Persentage_of_calculationn,
        )
        tax_mdl.save()

        sndry_mdl = Ledger_sundry(
            ledger_id=idd,
            maintain_balance_bill_by_bill=maintain_balance_bill_by_billl,
            Default_credit_period=Default_credit_periodd,
            Check_for_credit_days =Check_for_credit_dayss,
        )
        sndry_mdl.save()
        messages.info(request,'LEDGER CREATED SUCCESSFULLY')
        return redirect('create_ledger')

  
    