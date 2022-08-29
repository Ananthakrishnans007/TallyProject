from calendar import month, month_name
from contextlib import closing
from msilib.schema import Class
from xml.parsers.expat import model
from django.db import models

# Create your models here.



class Group_under(models.Model):
    group_under_Name = models.CharField(max_length=225,default="Null",blank=True)
    
    def __str__(self):
        return self.group_under_Name



class Ledger(models.Model):
    ledger_name = models.CharField(max_length=225,default="Null",blank=True)
    ledger_alias = models.CharField(max_length=225,default="Null",blank=True)
    group_under =  models.ForeignKey(Group_under,on_delete=models.CASCADE , null=True, blank=True)
    ledger_opening_bal = models.IntegerField(default="Null",blank=True)
    ledger_opening_bal_type = models.CharField(max_length=225,default="Null",blank=True)
    ledger_type = models.CharField(max_length=225,default="Null",blank=True)
    provide_banking_details =  models.CharField(max_length=225,default="Null",blank=True)

    

    def __str__(self):
        return self.ledger_name



class Ledger_Banking_Details(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    od_limit = models.CharField(max_length=225,default="Null",blank=True)
    holder_name =models.CharField(max_length=225,default="Null",blank=True)
    ac_number =models.CharField(max_length=225,default="Null",blank=True)
    ifsc =models.CharField(max_length=225,default="Null",blank=True)
    swift_code =models.CharField(max_length=225,default="Null",blank=True)
    bank_name = models.CharField(max_length=225,default="Null",blank=True)
    branch_name = models.CharField(max_length=225,default="Null",blank=True)
    alter_chk_bks =  models.CharField(max_length=225,default="Null",blank=True)
    enbl_chk_printing =  models.CharField(max_length=225,default="Null",blank=True)
    chqconfg= models.CharField(max_length=225,default="Null",blank=True)

class Ledger_Mailing_Address(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225,default="Null",blank=True)
    address = models.CharField(max_length=225,default="Null",blank=True)
    state = models.CharField(max_length=225,default="Null",blank=True)
    country =models.CharField(max_length=225,default="Null",blank=True)
    pincode =models.CharField(max_length=225,default="Null",blank=True)


class Ledger_Tax_Register(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    gst_uin = models.CharField(max_length=225,default="Null",blank=True)
    register_type =models.CharField(max_length=225,default="Null",blank=True)
    pan_no = models.CharField(max_length=225,default="Null",blank=True)
    alter_gst_details = models.CharField(max_length=225,default="Null",blank=True)


class Ledger_Satutory(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    assessable_calculation = models.CharField(max_length=225,default="Null",blank=True)
    Appropriate_to =models.CharField(max_length=225,default="Null",blank=True)
    gst_applicable = models.CharField(max_length=225,default="Null",blank=True)
    Set_alter_GST =models.CharField(max_length=225,default="Null",blank=True)
    type_of_supply = models.CharField(max_length=225,default="Null",blank=True)
    Method_of_calc=models.CharField(max_length=225,default="Null",blank=True)

class Ledger_Rounding(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    Round_limit = models.CharField(max_length=22,default="Null",blank=True)

class ledger_tax(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    type_of_duty_or_tax =models.CharField(max_length=225,default="Null",blank=True)
    type_of_tax =models.CharField(max_length=225,default="Null",blank=True)
    valuation_type=models.CharField(max_length=225,default="Null",blank=True)
    rate_per_unit =models.CharField(max_length=225,default="Null",blank=True)
    Persentage_of_calculation=models.CharField(max_length=225,default="Null",blank=True)
   

class Ledger_sundry(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    maintain_balance_bill_by_bill =models.CharField(max_length=225,default="Null",blank=True)
    Default_credit_period=models.CharField(max_length=225,default="Null",blank=True)
    Check_for_credit_days=models.CharField(max_length=225,default="Null",blank=True)
    



class Group_Under_closing_balance(models.Model):
    group_under = models.ForeignKey(Group_under,on_delete=models.CASCADE)
    total_closing_balance_debit = models.IntegerField(default="",null=True,blank=True)
    total_closing_balance_credit = models.IntegerField(default="",null=True,blank=True)

    def __str__(self):
        return self.group_under.group_under_Name

class LedgerMonths (models.Model):
    month_name=models.CharField(max_length=255)
    def __str__(self):
        return self.month_name

class Leger_Month_closing(models.Model):
    Ledger = models.ForeignKey(Ledger,on_delete=models.CASCADE, null=True, blank=True)  
    month = models.ForeignKey(LedgerMonths,on_delete=models.CASCADE, null=True, blank=True)   
    Closing_balance = models.IntegerField(default="",null=True,blank=True)
    type = models.CharField(max_length=225)
    debit = models.IntegerField(default="",null=True,blank=True)
    credit =models.IntegerField(default="",null=True,blank=True)

    def __str__(self):
        return self.ledger.ledger_name

    
         
class Ledger_Voucher(models.Model):
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    
    Date = models.DateField()
    Particualrs = models.CharField(max_length=225)
    Vch_Type = models.CharField(max_length=225)
    Vch_No = models.CharField(max_length=225)
    Debit = models.IntegerField(default="",null=True,blank=True)
    Credit = models.IntegerField(default="",null=True,blank=True)
    month = models.ForeignKey(LedgerMonths,on_delete=models.CASCADE, null=True, blank=True)   

    def __str__(self):
        return self.ledger.ledger_name

class TotalClosing_balance(models.Model):
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    Total_Closing_balance = models.IntegerField(default="",null=True,blank=True)
    type = models.CharField(max_length=225)

    def __str__(self):
        return self.ledger.ledger_name
