from django.db.models import Sum, OuterRef, Subquery, F
from backend.models import MStoreEquipment, MMachineryEquipment, MOfficeEquipment, MComputerEquipment, MShopEquipment

#Store Equipment
def se():
    return MStoreEquipment.objects.all()
seDepCost = Subquery(se().filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('debit') / Sum('depreciationLife')).values('sum')[0:]) or 0
def seDebit():
    return se().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
def seCredit():
    return se().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
def seDif():
    return seDebit() - seCredit()
def seSum():
    seSum = se().values('timestamp', 'snid', 'description', 'debit', 'credit', 'purchaseDate', 'depreciationLife', 'receiptID').annotate(seDepCost=seDepCost)
    return seSum

#Machinery & Equipment
def me():
    return MMachineryEquipment.objects.all()
meDepCost = Subquery(me().filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('debit') / Sum('depreciationLife')).values('sum')[0:]) or 0
def meDebit():
    return me().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
def meCredit():
    return me().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
def meDif():
    return meDebit() - meCredit()
def meSum():
    meSum = me().values('timestamp', 'snid', 'description', 'debit', 'credit', 'purchaseDate', 'depreciationLife', 'receiptID').annotate(meDepCost=meDepCost)
    return meSum

#Office Equipment
def oe():
    return MOfficeEquipment.objects.all()
oeDepCost = Subquery(oe().filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('debit') / Sum('depreciationLife')).values('sum')[0:]) or 0
def oeDebit():
    return oe().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
def oeCredit():
    return oe().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
def oeDif():
    return oeDebit() - oeCredit()
def oeSum():
    oeSum = oe().values('timestamp', 'snid', 'description', 'debit', 'credit', 'purchaseDate', 'depreciationLife', 'receiptID').annotate(oeDepCost=oeDepCost)
    return oeSum

#Computer Equipment
def ce():
    return MComputerEquipment.objects.all()
ceDepCost = Subquery(ce().filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('debit') / Sum('depreciationLife')).values('sum')[0:])
def ceDebit():
    return ce().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
def ceCredit():
    return ce().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
def ceDif():
    return ceDebit() - ceCredit()
def ceSum():
    ceSum = ce().values('timestamp', 'snid', 'description', 'debit', 'credit', 'purchaseDate', 'depreciationLife', 'receiptID').annotate(ceDepCost=ceDepCost)
    return ceSum

#Shop Equipment
def she():
    return MShopEquipment.objects.all()
sheDepCost = Subquery(she().filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('debit') / Sum('depreciationLife')).values('sum')[0:]) or 0
def sheDebit():
    return she().values('snid').aggregate(Sum('debit'))['debit__sum'] or 0
def sheCredit():
    return she().values('snid').aggregate(Sum('credit'))['credit__sum'] or 0
def sheDif():
    return sheDebit() - sheCredit()
def sheSum():
    sheSum = she().values('timestamp', 'snid', 'description', 'debit', 'credit', 'purchaseDate', 'depreciationLife', 'receiptID').annotate(sheDepCost=sheDepCost)
    return sheSum

#Furniture & Fixtures
def ffDebit():
    return ceDebit() + seDebit() + meDebit() + oeDebit() + sheDebit()
def ffCredit():
    return ceCredit() + seCredit() + meCredit() + oeCredit() + sheCredit()
def ffDif():
    return ffDebit() - ffCredit()
