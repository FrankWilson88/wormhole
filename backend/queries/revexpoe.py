from django.db.models import Sum, OuterRef, Subquery, F
from backend.models import MCapital, MDrawings, MSalesRevenue, MSuppliesExpense, MUtilitiesExpense, MTravelExpense, MDeliveryExpense, MCapital, MDrawings, MRentExpense, MSalaryExpense
'''
Revenue
'''
#Sales Revenue
def sr():
    sr = MSalesRevenue.objects.all()
    return sr
def srDebit():
    srDebit = sr().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
    return srDebit
def srCredit():
    srCredit = sr().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
    return srCredit


'''
Expenses
'''
#Supplies Expense
def supex():
    supex = MSuppliesExpense.objects.all()
    return supex
def supexDebit():
    supexDebit = supex().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
    return supexDebit
def supexCredit():
    supexCredit = supex().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
    return supexCredit

#Utilities Expense
def ue():
    ue = MUtilitiesExpense.objects.all()
    return ue
def ueDebit():
    ueDebit = ue().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
    return ueDebit
def ueCredit():
    ueCredit = ue().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
    return ueCredit
def ueDif():
    ueDif = ueDebit() - ueCredit()
    return ueDif

#Travel Expense
def te():
    te = MTravelExpense.objects.all()
    return te
def teDebit():
    teDebit = te().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
    return teDebit
def teCredit():
    teCredit = te().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
    return teCredit
def teDif():
    teDif = teDebit() - teCredit()
    return teDif

#Delivery Expense
def de():
    de = MDeliveryExpense.objects.all()
    return de
def deDebit():
    deDebit = de().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
    return deDebit
def deCredit():
    deCredit = de().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
    return deCredit
def deDif():
    deDif = deDebit() - deCredit()
    return deDif

#Rent Expense
def re():
    re = MRentExpense.objects.all()
    return re
def reDebit():
    reDebit = re().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
    return reDebit
def reCredit():
    reCredit = re().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
    return reCredit
def reDif():
    reDif = reDebit() - reCredit()
    return reDif

#Salary Expense
def salexp():
    salexp = MSalaryExpense.objects.all()
    return salexp
def salexpDebit():
    salexpDebit = salexp().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
    return salexpDebit
def salexpCredit():
    salexpCredit = salexp().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
    return salexpCredit

'''
Owners Equity
'''
#Capital
def c():
    c = MCapital.objects.all()
    return c
def cDebit():
    cDebit = c().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
    return cDebit
def cCredit():
    cCredit = c().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
    return cCredit
def cDif():
    cDif = cDebit() - cCredit()
    return cDif

#Drawings
def d():
    d = MDrawings.objects.all()
    return d
def dDebit():
    dDebit = d().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
    return dDebit
def dCredit():
    dCredit = d().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
    return dCredit
def dDif():
    dDif = dDebit() - dCredit()
    return dDif
