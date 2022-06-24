from django.db.models import Sum, OuterRef, Subquery, F
from backend.models import MRawMaterials, MrmIn, MrmOut, MProductionWork, MpwIn, MpwOut, MCustomWork, MPrototypes, MStoreInventory, MsiIn, MsiOut

#Custom Work
cw = MCustomWork.objects.all()

#Prototypes
proto = MPrototypes.objects.all()

#Raw Materials
rm = MRawMaterials.objects.all()
model1 = MrmIn
rmin = model1.objects.all()
annDebit = Subquery(rmin.filter(description=OuterRef('snid')).values('description').annotate(sum=Sum(F('debit'))).values('sum')[0:]) or 0
annPcsIn = Subquery(rmin.filter(description=OuterRef('snid')).values('description').annotate(sum=Sum(F('pcsIn'))).values('sum')[0:]) or 0
aggDebit = rmin.aggregate(Sum('debit'))['debit__sum'] or 0
aggPcsIn = rmin.aggregate(Sum('pcsIn'))['pcsIn__sum'] or 0
model2 = MrmOut
rmout = model2.objects.all()
annUnits = Subquery(rmout.filter(description=OuterRef('snid')).values('description').annotate(sum=Sum('units')).values('sum')[0:]) or 0
annWaste = Subquery(rmout.filter(description=OuterRef('snid')).values('description').annotate(sum=Sum('waste')).values('sum')[0:]) or 0
annRND = Subquery(rmout.filter(description=OuterRef('snid')).values('description').annotate(sum=Sum('rnd')).values('sum')[0:]) or 0
aggUnits = rmout.aggregate(Sum('units'))['units__sum'] or 0
aggWaste = rmout.aggregate(Sum('waste'))['waste__sum'] or 0
aggRND = rmout.aggregate(Sum('rnd'))['rnd__sum'] or 0
costPerPc = Sum('mrmin__debit') / Sum('mrmin__pcsIn') or 0
unitsPerPc = Subquery(rm.filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum(F('inchesPerPc')) / Sum(F('inchesPerUnit'))).values('sum')[0:]) or 0
unitsOut = Subquery(rmout.filter(description=OuterRef('snid')).values('description').annotate(sum=Sum(F('units')) + Sum(F('waste')) + Sum(F('rnd'))).values('sum')[0:])
unitsIn = unitsPerPc * annPcsIn
unitsOH = unitsIn - unitsOut
unitsPerCs = unitsPerPc * Subquery(rm.filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum(F('pcsPerCs'))).values('sum')[0:]) or 0
costPerUnit = annDebit / unitsIn
inchesPerUnit = Subquery(rm.filter(snid=OuterRef('snid')).values('snid').annotate(c=Sum('inchesPerUnit')).values('c')[0:]) or 0
unitsOH = unitsIn - unitsOut
annCredit = unitsOut * costPerUnit
UDr = costPerUnit * annUnits
WDr = costPerUnit * annWaste
rndDR = costPerUnit * annRND
aggCredit = rm.aggregate(s=Sum(annCredit))['s'] or 0
def aggrndDR():
    aggrndDR = rm.aggregate(s=Sum(rndDR))['s'] or 0
    return aggrndDR
dif = aggDebit - aggCredit
def sum():
    sum = rm.values('snid', 'make', 'model', 'diameter', 'thickness').annotate(
        costPerPc=costPerPc, unitsPerPc=unitsPerPc, annDebit=annDebit, annCredit=annCredit, unitsIn=unitsIn, unitsOut=unitsOut,
        unitsOH=unitsOH, costPerUnit=costPerUnit, annPcsIn=annPcsIn, inchesPerUnit=inchesPerUnit, annUnits=annUnits,
        annWaste=annWaste, annRND=annRND, unitsPerCs=unitsPerCs)
    return sum

#Production Work
pw = MProductionWork.objects.all()
pwIn = MpwIn.objects.all()
pwannUnitsIn = Subquery(pw.filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('mpwin__unitsIn')).values('sum')[0:])
pwaggUnitsIn = pw.aggregate(s=Sum(pwannUnitsIn))['s'] or 0
pwOut = MpwOut.objects.all()
pwannUnitsOut = Subquery(pw.filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('mpwout__unitsOut')).values('sum')[0:])
pwaggUnitsOut = pw.aggregate(s=Sum(pwannUnitsOut))['s'] or 0
pwannDebit = Subquery(pw.filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('wholesale') * pwannUnitsIn).values('sum')[0:])
pwaggDebit = pw.aggregate(s=Sum(pwannDebit))['s'] or 0
pwannCredit = Subquery(pw.filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('wholesale') * pwannUnitsOut).values('sum')[0:])
pwaggCredit = pw.aggregate(s=Sum(pwannCredit))['s'] or 0
pwannUnitsOH = Subquery(pw.filter(snid=OuterRef('snid')).values('snid').annotate(sum=pwannUnitsIn - pwannUnitsOut).values('sum')[0:])
pwaggUnitsOH = pwaggUnitsIn - pwaggUnitsOut
retailValue = Subquery(pw.filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('msrp') * pwannUnitsOH).values('sum')[0:])
aggRetailValue = pw.aggregate(s=Sum(retailValue))['s'] or 0
def pwsum():
    sum = pw.values('snid', 'description', 'wholesale', 'msrp').annotate(annUnitsIn=pwannUnitsIn, annUnitsOut=pwannUnitsOut, annDebit=pwannDebit,
                                                    annCredit=pwannCredit, annUnitsOH=pwannUnitsOH, retailValue=retailValue)
    return sum
def pwtemplate():
    sum = pw.values('snid', 'description', 'image', 'wholesale', 'msrp').annotate(annDebit=pwannDebit,
                                                    annCredit=pwannCredit, retailValue=retailValue)
    return sum

#Store Inventory
si = MStoreInventory.objects.all()
siIn = MsiIn.objects.all()
siannDebit = Subquery(si.filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('msiin__debit')).values('sum')[0:])
siaggDebit = si.values('snid').aggregate(sum=Sum(siannDebit))['sum'] or 0
siannUnitsIn = Subquery(si.filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('msiin__unitsIn')).values('sum')[0:])
siaggUnitsIn = si.values('snid').aggregate(sum=Sum(siannUnitsIn))['sum'] or 0
siannUnitsOut = Subquery(si.filter(snid=OuterRef('snid')).values('snid').annotate(sum=Sum('msiout__unitsOut')).values('sum')[0:])
siaggUnitsOut = si.values('snid').aggregate(sum=Sum(siannUnitsOut))['sum'] or 0
siunitsOH = siannUnitsIn - siannUnitsOut
sicostPerUnit = siannDebit / siannUnitsIn
siannCredit = sicostPerUnit * siannUnitsOut
siaggCredit = si.values('snid').aggregate(s=Sum(siannCredit))['s'] or 0
siOut = MsiOut.objects.all()
def sisum():
    sisum = si.values('snid', 'description', 'msrp', 'unitsPerCs').annotate(
        annDebit=siannDebit, annCredit=siannCredit, annUnitsIn=siannUnitsIn, annUnitsOut=siannUnitsOut, unitsOH=siunitsOH, costPerUnit=sicostPerUnit,
    )
    return sisum

#Inventory
def debit():
    debit = aggDebit + siaggDebit
    return debit
def credit():
    credit = aggCredit + siaggCredit
    return credit
def dif():
    dif = debit() - credit()
    return dif
