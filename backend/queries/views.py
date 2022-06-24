import datetime
from django.shortcuts import render
import backend.queries.inventory as i
import backend.queries.ff as ff
import backend.queries.assets as a
import backend.queries.liabilities as l
import backend.queries.revexpoe as oe

'''
Notes:
Fix Building= having trouble with dates and times.
'''


# Create your views here.


def inventory(request):
    context = {
        'rawmaterials': i.sum(),
        'aggDebit': i.aggDebit,
        'aggCredit': i.aggCredit,
        'aggUnits': i.aggUnits,
        'aggWaste': i.aggWaste,
        'aggRND': i.aggRND,
        'productionwork': i.pwsum(),
        'pwUnitsIn': i.pwaggUnitsIn,
        'pwUnitsOut':  i.pwaggUnitsOut,
        'pwUnitsOH': i.pwaggUnitsOH,
        'pwDebit': i.pwaggDebit,
        'pwCredit': i.pwaggCredit,
        'pwRetailValue': i.aggRetailValue,
        'prototypes': i.pw,
        'customwork': i.cw,
        'storeinventory': i.sisum(),
    }
    print(request.user.username, 'opened Inventory.')
    return render(request, 'inventory.html', context)

def furniturefixtures(request):
    context ={
        'customwork': i.cw,
        'ceSum': ff.ceSum(),
        'ceDebit': ff.ceDebit(),
        'ceCredit': ff.ceCredit(),
        'seSum': ff.seSum(),
        'seDebit': ff.seDebit(),
        'seCredit': ff.seCredit(),
        'meSum': ff.meSum(),
        'meDebit': ff.meDebit(),
        'meCredit': ff.meCredit(),
        'oeSum': ff.oeSum(),
        'oeDebit': ff.oeDebit(),
        'oeCredit': ff.oeCredit(),
        'sheSum': ff.sheSum(),
        'sheDebit': ff.sheDebit(),
        'sheCredit': ff.sheCredit(),
        'ffDebit': ff.ffDebit(),
        'ffCredit': ff.ffCredit(),
        'ffDif': ff.ffDif(),
    }
    print(request.user.username, 'opended Furnitures & Fixtures.')
    return render(request, 'ff.html', context)

def assets(request):
    context = {
        'customwork': i.cw,
        'accountsreceivable': a.ar,
        'arSum': a.arSum(),
        'iDebit': i.debit,
        'iCredit': i.credit,
        'iDif': i.dif,
        'building': a.b,
        'bSum': a.bSum(),
        'aggDebit': a.bDebit,
        'aggCredit': a.bCredit,
        'biSum': a.biSum,
        'biDebit': a.biDebit,
        'biCredit': a.biCredit,
        'li': a.li,
        'liDebit': a.liDebit(),
        'liCredit': a.liCredit(),
        'ffDif': ff.ffDif(),
        'ffDebit': ff.ffDebit(),
        'ffCredit': ff.ffCredit(),
    }
    print(request.user.username, 'opened Assets.')
    return render(request, 'assets.html', context)

def liabilities(request):
    context = {
        'customwork': i.cw,
        'ap': l.ap,
        'apDebit': l.apDebit(),
        'apCredit': l.apCredit(),
        'usr': l.usr,
        'usrDebit': l.usrDebit(),
        'usrCredit': l.usrCredit(),
        'ada': l.ada,
        'adaDebit': l.adaDebit(),
        'adaCredit': l.adaCredit(),
    }
    print(request.user.username, 'opened Liabilities.')
    return render(request, 'liabilities.html', context)

def revexpoe(request):
    context ={
        'customwork': i.cw,
        'sr': oe.sr,
        'srDebit': oe.srDebit(),
        'srCredit': oe.srCredit(),
        're': oe.re,
        'reDebit': oe.reDebit(),
        'reCredit': oe.reCredit(),
        'supex': oe.supex,
        'supexDebit': oe.supexDebit(),
        'supexCredit': oe.supexCredit(),
        'ue': oe.ue,
        'ueDebit': oe.ueDebit(),
        'ueCredit': oe.ueCredit(),
        'te': oe.te,
        'teDebit': oe.teDebit(),
        'teCredit': oe.teCredit(),
        'de': oe.de,
        'deDebit': oe.deDebit(),
        'deCredit': oe.deCredit(),
        'cogs': i.credit,
        'salexp': oe.salexp,
        'salexpDebit': oe.salexpDebit(),
        'salexpCredit': oe.salexpCredit(),
        'c': oe.c(),
        'cDebit': oe.cDebit(),
        'cCredit': oe.cCredit(),
        'cDif': oe.cDif(),
        'd': oe.d(),
        'dDebit': oe.dDebit(),
        'dCredit': oe.dCredit(),
        'dDif': oe.dDif(),
    }
    print(request.user.username, 'opened RevExpOE.')
    return render(request, 'revexpoe.html', context)

def reports(request):
    cashDebit = oe.cDebit() + oe.srDebit() + l.apDebit() - i.debit()
    cashCredit = a.araggDif() + a.bDebit() + a.biDebit() + a.liDebit() + ff.ffDebit() + l.apCredit() + oe.supexDebit() + oe.ueDebit() + oe.teDebit() + oe.deDebit() + l.adaDebit() + oe.dDebit() + oe.reDebit() + oe.salexpDebit()
    cashDif = cashDebit - cashCredit
    totalassets = cashDif + a.araggDif() + i.dif() + a.bDif() + a.biDif() + a.liDif() + ff.ffDif()- i.aggrndDR()
    salesRev = oe.srDebit()
    totalExp = oe.reDebit() + a.bCredit() + a.biCredit() + ff.ffCredit() + i.credit() + i.aggrndDR() + oe.salexpDebit() + oe.supexDebit() + oe.ueDebit() + oe.teDebit() + oe.deDebit()
    incomeloss = salesRev - totalExp
    total = oe.cDebit() + incomeloss
    agCap = total - oe.dDebit()
    totalLiab = l.apDif() + l.usrDif() + l.adaDif()
    cDebit = oe.cDebit()
    dDebit = oe.dDebit()
    context = {
        'customwork': i.cw,
        'cashDif': cashDif,
        'salesRev': salesRev,
        'reDebit': oe.reDebit(),
        'cogs': i.credit(),
        'invDif': i.dif() - i.aggrndDR(),
        'salexpDebit': oe.salexpDebit(),
        'supexDebit': oe.supexDebit(),
        'ueDebit': oe.ueDebit(),
        'teDebit': oe.teDebit(),
        'deDebit': oe.deDebit(),
        'aggrndDR': i.aggrndDR(),
        'araggDif': a.araggDif(),
        'bDebit': a.bDebit(),
        'bCredit': a.bCredit(),
        'bDif': a.bDif(),
        'biDebit': a.biDebit(),
        'biCredit': a.biCredit(),
        'biDif': a.biDif(),
        'liDebit': a.liDebit(),
        'ffDebit': ff.ffDebit(),
        'ffCredit': ff.ffCredit(),
        'ffDif': ff.ffDif(),
        'apDif': l.apDif(),
        'usrDif': l.usrDif(),
        'adaDif': l.adaDif(),
        'cDebit': cDebit,
        'dDebit': dDebit,
        'totalExp': totalExp,
        'incomeloss': incomeloss,
        'total': total,
        'agCap': agCap,
        'totalassets': totalassets,
        'totalLiab': totalLiab,
        'totalLiabOE': total + totalLiab,
        'year': datetime.datetime.now().year
    }
    print(request.user.username, 'opened Reports.')
    return render(request, 'reports.html', context)
