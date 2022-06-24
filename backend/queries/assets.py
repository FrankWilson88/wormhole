from django.db.models import Sum, OuterRef, Subquery, F
from backend.models import MAccountsReceivable, MBuilding, MBuildingImprovements, MLandImprovements

#Accounts Receivable
ar = MAccountsReceivable.objects.all()
araggDebit = Sum('valueLoaned')
araggCredit = Sum('valuePayed') - Sum('default')
def araggDif():
    araggDif = ar.aggregate(s=Sum('valueLoaned') - Sum('valuePayed'))['s'] or 0
    return araggDif
arunits = Sum('unitsLoaned')
def arSum():
    sum = ar.values('snid', 'description', 'valueLoaned', 'default', 'unitsLoaned', 'valuePayed', 'dateOpened',
                    'dateClosed', 'dueDate', 'customerID', 'recieptID').aggregate(aggDebit=araggDebit, aggCredit=araggCredit, units=arunits)
    return sum

#Building/Building Improvements
b = MBuilding.objects.all()
def bDebit():
    bDebit = b.values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
    return bDebit
def bCredit():
    bCredit = b.values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
    return bCredit
def bDif():
    return bDebit() - bCredit()
depreciationCost = Subquery(b.filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('debit') / Sum('depreciationLife')).values('sum')[0:])
def bSum():
    sum = b.values('timestamp', 'snid', 'description', 'debit', 'credit', 'purchaseDate',
                  'depreciationLife', 'receiptID').annotate(depreciationCost=depreciationCost)
    return sum

bi = MBuildingImprovements.objects.all()
def biDebit():
    biDebit = bi.values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
    return biDebit
def biCredit():
    biCredit = bi.values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
    return biCredit
def biDif():
    return biDebit() - biCredit()
biDepCost = Subquery(bi.filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('debit') / Sum('depreciationLife')).values('sum')[0:])
def biSum():
    biSum = bi.values('timestamp', 'snid', 'description', 'debit', 'credit', 'purchaseDate', 'depreciationLife', 'receiptID').annotate(biDepCost=biDepCost)
    return biSum

#Land Improvements
li = MLandImprovements.objects.all()
def liDebit():
    liDebit = li.values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
    return liDebit
def liCredit():
    liCredit = li.values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
    return liCredit
def liDif():
    liDif = liDebit() - liCredit()
    return liDif
