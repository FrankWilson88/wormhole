from django.contrib import admin
from backend.models import MRawMaterials, MCustomWork, MrmIn, MrmOut, MProductionWork, MpwIn, MpwOut, MPrototypes, \
    MStoreInventory, MsiIn, MsiOut, MAccountsReceivable, MBuilding, MBuildingImprovements, MLandImprovements, MComputerEquipment, \
    MStoreEquipment, MMachineryEquipment, MOfficeEquipment, MShopEquipment, MAccountsPayable, MSuppliesExpense, MUtilitiesExpense, \
    MTravelExpense, MUnearnedSalesRevenue, MDeliveryExpense, MAllowanceForDoubtfulAccounts, MCapital, MDrawings, MSalesRevenue, \
    MRentExpense, MSalaryExpense

# Register your models here.
admin.site.register(MRawMaterials)
admin.site.register(MrmIn)
admin.site.register(MrmOut)
admin.site.register(MCustomWork)
admin.site.register(MProductionWork)
admin.site.register(MpwIn)
admin.site.register(MpwOut)
admin.site.register(MPrototypes)
admin.site.register(MStoreInventory)
admin.site.register(MsiIn)
admin.site.register(MsiOut)
admin.site.register(MAccountsReceivable)
admin.site.register(MBuilding)
admin.site.register(MBuildingImprovements)
admin.site.register(MLandImprovements)
admin.site.register(MComputerEquipment)
admin.site.register(MStoreEquipment)
admin.site.register(MMachineryEquipment)
admin.site.register(MOfficeEquipment)
admin.site.register(MShopEquipment)
admin.site.register(MAccountsPayable)
admin.site.register(MSuppliesExpense)
admin.site.register(MUtilitiesExpense)
admin.site.register(MTravelExpense)
admin.site.register(MUnearnedSalesRevenue)
admin.site.register(MDeliveryExpense)
admin.site.register(MAllowanceForDoubtfulAccounts)
admin.site.register(MCapital)
admin.site.register(MDrawings)
admin.site.register(MSalesRevenue)
admin.site.register(MRentExpense)
admin.site.register(MSalaryExpense)