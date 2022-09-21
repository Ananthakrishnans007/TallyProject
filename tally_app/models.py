from calendar import month, month_name
from contextlib import closing
from msilib.schema import Class
from xml.parsers.expat import model
from django.db import models

# Create your models here.






class Companies(models.Model):
    d_path=models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=255)
    mailing_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=20,null=True)
    mobile = models.CharField(max_length=15,null=True)
    fax = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=240, null=True)
    website = models.CharField(max_length=100,null=True)
    currency_symbol = models.CharField(max_length=20)
    formal_name = models.CharField(max_length=20)
    fin_begin = models.DateField()
    books_begin = models.DateField()
    fin_end = models.DateField()
    status=models.BooleanField(default=True)


class tally_group(models.Model):
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    group_name = models.CharField(max_length=255,null=True,blank=True)
    group_alias = models.CharField(max_length=255,null=True,blank=True)
    group_under = models.CharField(max_length=255,null=True,blank=True)
    nature = models.CharField(max_length=255,null=True,blank=True)
    gross_profit = models.CharField(max_length=255,null=True,blank=True)
    sub_ledger = models.CharField(max_length=255,null=True,blank=True)
    debit_credit = models.CharField(max_length=255,null=True,blank=True)
    calculation = models.CharField(max_length=255,null=True,blank=True)
    invoice = models.CharField(max_length=255,null=True,blank=True)    

class tally_ledger(models.Model):
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    alias = models.CharField(max_length=255,null=True,blank=True,)
    under = models.CharField(max_length=255,blank=True,null=True)
    grp = models.ForeignKey(tally_group,on_delete = models.CASCADE,null = True,blank=True)
    mname = models.CharField(max_length=255,null=True,blank=True,)
    address = models.CharField(max_length=255,null=True,blank=True,)
    state = models.CharField(max_length=255,null=True,blank=True,)
    country = models.CharField(max_length=255,null=True,blank=True,)
    pincode = models.CharField(max_length=6,null=True,blank=True,)
    bank_details = models.CharField(max_length=20,null=True,blank=True,)
    pan_no = models.CharField(max_length=100,null=True,blank=True,)
    registration_type = models.CharField(max_length=100,null=True,blank=True)
    gst_uin = models.CharField(max_length=100,null=True,blank=True,)
    set_alter_gstdetails = models.CharField(max_length=100,null=True)
    opening_blnc = models.IntegerField(null=True,blank=True,)
    opening_blnc_type = models.CharField(max_length=100,blank=True,null=True)


    set_odl = models.CharField(max_length=255,null=True,blank=True,)
    ac_holder_nm = models.CharField(max_length=255,null=True,blank=True,)
    acc_no = models.CharField(max_length=255,null=True,blank=True,)
    ifsc_code = models.CharField(max_length=255,null=True,blank=True,)
    swift_code = models.CharField(max_length=255,null=True,blank=True,)
    bank_name = models.CharField(max_length=255,null=True,blank=True,)
    branch = models.CharField(max_length=255,null=True,blank=True,)
    SA_cheque_bk = models.CharField(max_length=20,null=True,blank=True,)
    Echeque_p = models.CharField(max_length=20,null=True,blank=True,)
    SA_chequeP_con = models.CharField(max_length=20,null=True,blank=True,)
    
    type_of_ledger = models.CharField(max_length=100,null=True,blank=True,)
    rounding_method = models.CharField(max_length=100,null=True,blank=True,)
    rounding_limit = models.IntegerField(blank=True, null=True, default=None)

    type_duty_tax = models.CharField(max_length=100,null=True,blank=True,)
    tax_type = models.CharField(max_length=100,null=True,blank=True,)
    valuation_type = models.CharField(max_length=100,null=True,blank=True,)
    rate_per_unit = models.IntegerField(blank=True, null=True, default=None,)
    percentage_of_calcution = models.CharField(max_length=100,null=True,blank=True,)
    rond_method = models.CharField(max_length=100,null=True,blank=True,)
    rond_limit = models.IntegerField(blank=True, null=True, default=None)

    gst_applicable = models.CharField(max_length=100,null=True,blank=True,)
    setalter_gstdetails = models.CharField(max_length=20,null=True,blank=True,)
    type_of_supply = models.CharField(max_length=100,null=True,blank=True,)
    assessable_value = models.CharField(max_length=100,null=True,blank=True,)
    appropriate_to = models.CharField(max_length=100,null=True,blank=True,)
    method_of_calculation = models.CharField(max_length=100,null=True,blank=True,)

    balance_billbybill = models.CharField(max_length=100,null=True,blank=True,)
    credit_period = models.CharField(max_length=100,null=True,blank=True,)
    creditdays_voucher = models.CharField(max_length=100,null=True,blank=True,)

    def __str__(self):
        return self.name




class Account_Books_Group_under(models.Model):
    group_under_Name = models.CharField(max_length=225,default="Null",blank=True)
    
    def __str__(self):
        return self.group_under_Name



class Account_Books_Ledger(models.Model):
    ledger_name = models.CharField(max_length=225,default="Null",blank=True)
    group_under =  models.ForeignKey(Account_Books_Group_under,on_delete=models.CASCADE , null=True, blank=True)
    ledger_opening_bal = models.IntegerField(default="Null",blank=True)
    ledger_opening_bal_type = models.CharField(max_length=225,default="Null",blank=True)
    
    def __str__(self):
        return self.ledger_name


class cash_bank_books_Group_Under_closing_balance(models.Model):
    
    group_under = models.ForeignKey(Account_Books_Group_under,on_delete=models.CASCADE)
    total_closing_balance_debit = models.IntegerField(default="",null=True,blank=True)
    total_closing_balance_credit = models.IntegerField(default="",null=True,blank=True)
    def __str__(self):
        return self.group_under.group_under_Name
    
    

class Months (models.Model):
    month_name=models.CharField(max_length=255)
    def __str__(self):
        return self.month_name

class cash_bank_books_Leger_Month_closing(models.Model):
    Ledger = models.ForeignKey(Account_Books_Ledger,on_delete=models.CASCADE, null=True, blank=True)  
    month = models.ForeignKey(Months,on_delete=models.CASCADE, null=True, blank=True)   
    Closing_balance = models.IntegerField(default="",null=True,blank=True)
    type = models.CharField(max_length=225)
    debit = models.IntegerField(default="",null=True,blank=True)
    credit =models.IntegerField(default="",null=True,blank=True)


         
class Account_books_Ledger_Voucher(models.Model):
    ledger = models.ForeignKey(Account_Books_Ledger, on_delete=models.CASCADE, null=True, blank=True)
    
    Date = models.DateField()
    Particualrs = models.CharField(max_length=225)
    Vch_Type = models.CharField(max_length=225)
    Vch_No = models.CharField(max_length=225)
    Debit = models.IntegerField(default="",null=True,blank=True)
    Credit = models.IntegerField(default="",null=True,blank=True)
    month = models.ForeignKey(Months,on_delete=models.CASCADE, null=True, blank=True)   

    def __str__(self):
        return self.ledger.ledger_name

class cash_bank_books_TotalClosing_balance(models.Model):
    ledger = models.ForeignKey(Account_Books_Ledger, on_delete=models.CASCADE, null=True, blank=True)
    Total_Closing_balance = models.IntegerField(default="",null=True,blank=True)
    type = models.CharField(max_length=225)

    def __str__(self):
        return self.ledger.ledger_name
