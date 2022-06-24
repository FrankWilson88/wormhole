from django.db.models import Sum, OuterRef, Subquery, F
from backend.models import MAccountsPayable, MUnearnedSalesRevenue, MAllowanceForDoubtfulAccounts


#Accounts Payable
ap = MAccountsPayable.objects.all()
def apDebit():
    apDebit = ap.values('snid').aggregate(Sum('valueLoaned'))['valueLoaned__sum'] or 0
    return apDebit
def apCredit():
    apCredit = ap.values('snid').aggregate(Sum('valuePayed'))['valuePayed__sum'] or 0
    return apCredit
def apDif():
    apDif = apDebit() - apCredit()
    return apDif

#Unearned Sales Revenue
usr = MUnearnedSalesRevenue.objects.all()
def usrDebit():
    usrDebit = usr.values('snid').aggregate(Sum('owed'))['owed__sum'] or 0
    return usrDebit
def usrCredit():
    usrCredit = usr.values('snid').aggregate(Sum('payed'))['payed__sum'] or 0
    return usrCredit
def usrDif():
    usrDif = usrDebit() - usrCredit()
    return usrDif

#Allowance For Doubtful Accounts
ada = MAllowanceForDoubtfulAccounts.objects.all()
def adaDebit():
    adaDebit = ada.values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
    return adaDebit
def adaCredit():
    adaCredit = ada.values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
    return adaCredit
def adaDif():
    adaDif = adaDebit() - adaCredit()
    return adaDif
