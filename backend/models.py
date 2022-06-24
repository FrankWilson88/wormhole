from django.db import models
from django.urls import reverse
from django.forms import ModelForm

# Create your models here.
'''
Accounts Receivable
'''
class MAccountsReceivable(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True, unique=True)
    description = models.CharField(max_length=50)
    valueLoaned = models.DecimalField(max_digits=10, decimal_places=2)
    default = models.DecimalField(max_digits=10, decimal_places=2)
    unitsLoaned = models.IntegerField()
    valuePayed = models.DecimalField(max_digits=10, decimal_places=2)
    dateOpened = models.DateField(null=True)
    dateClosed = models.DateField(null=True)
    dueDate = models.DateField(null=True)
    customerID = models.IntegerField()
    recieptID = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Accounts Receivable'
    def __str__(self):
        return f'{self.snid} {self.description}'
    def get_absolute_url(self):
        return reverse('inventory', args=[str(self.snid)])

class FAccountsReceivable(ModelForm):
    model = MAccountsReceivable
    fields = '__all__'

'''
Building/Building Improvements
'''
class MBuilding(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True, unique=True)
    description = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    purchaseDate = models.DateField(null=True)
    depreciationLife = models.DecimalField(max_digits=10, decimal_places=2)
    receiptID = models.CharField(max_length=50)
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Building'
    def __str__(self):
        return f'{self.snid} {self.description} {self.purchaseDate}'
    def get_absolute_url(self):
        return reverse('inventory', args=[str(self.snid)])

class FBuilding(ModelForm):
    model = MBuilding
    fields = '__all__'

class MBuildingImprovements(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    purchaseDate = models.DateField()
    depreciationLife = models.DecimalField(max_digits=10, decimal_places=2)
    receiptID = models.CharField(max_length=50)
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Building Improvements'
    def __str__(self):
        return f'{self.snid} {self.description}'

'''
Raw Materials
'''
class MRawMaterials(models.Model):
    CATEGORY = (
        ('Clear', 'Clear'),
        ('Color', 'Color'),
        ('Joint', 'Joint'),
        ('Dichro', 'Dichro'),
        ('Opal', 'Opal'),
    )
    MODEL = (
        ('Tube', 'Tube'),
        ('Rod', 'Rod'),
        ('Frit', 'Frit'),
        ('Sheets', 'Sheets'),
        ('Strips', 'Strips'),
        ('Image', 'Image'),
        ('Shaped', 'Shaped'),
        ('Tumbled/Polished', 'Tumbled/Polished'),
        ('Crushed/Rough', 'Crushed/Rough'),
        ('Sample', 'Sample'),
    )
    snid = models.BigAutoField(primary_key=True, unique=True)
    category = models.CharField(max_length=10, choices=CATEGORY, default='Clear', null=False, help_text='Choose a Category...', )
    make = models.CharField(max_length=30, null=False, default='Pyrex', help_text='The Brand of Glass.')
    model = models.CharField(max_length=20, choices=MODEL, default='Tube', null=False, help_text='Choose the Model...', )
    diameter = models.DecimalField(max_digits=10, null=True, decimal_places=2, default='0.00', help_text='Outer Diameter of the Tube.')
    thickness = models.DecimalField(max_digits=10, null=True, decimal_places=2, default='0.00', help_text='Thickness of the Tube.')
    inchesPerUnit = models.DecimalField(max_digits=5, decimal_places=2, default='0.00', null=True, help_text='Break the Tube into 1/4s.')
    inchesPerPc = models.DecimalField(max_digits=5, decimal_places=2, default='0.00',null=True, help_text='Full length of the Item.')
    pcsPerCs = models.DecimalField(max_digits=5, decimal_places=2, default='0.00',null=True, help_text='Total Items in a Case.')
    oz = models.IntegerField(help_text='Total Ounces of Frit.', null=True)

    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Raw Materials'

    def get_absolute_url(self):
        return reverse('inventory', args=[str(self.snid)])

    def __str__(self):
        return f'{self.snid} | {self.make}, {self.model} {self.diameter}x{self.thickness}| {self.inchesPerUnit}\"/unit {self.inchesPerPc}\"/pc. {self.pcsPerCs} pcs./cs. {self.oz}oz.'

class MrmIn(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    description = models.ForeignKey(MRawMaterials, on_delete=models.RESTRICT)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    pcsIn = models.DecimalField(max_digits=5, decimal_places=2, default='0.00')
    invoiceID = models.CharField(max_length=100)
    purchaseDate = models.DateField()
    class Meta:
        ordering = ['timestamp']
        verbose_name_plural = 'RM In'
    def __str__(self):
        return f'{self.description}'

class MrmOut(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    description = models.ForeignKey(MRawMaterials, on_delete=models.RESTRICT)
    units = models.DecimalField(max_digits=5, decimal_places=2, default='0.00')
    waste = models.DecimalField(max_digits=5, decimal_places=2, default='0.00')
    rnd = models.DecimalField(max_digits=5, decimal_places=2, default='0.00')
    class Meta:
        ordering = ['timestamp']
        verbose_name_plural = 'RM Out'
    def __str__(self):
        return f'{self.description}'

class FRawMaterials(ModelForm):
    class Meta:
        model = MRawMaterials
        fields = '__all__'

'''
Custom Work
'''
class MCustomWork(models.Model):
    IO = (
        (0, 'Out'),
        (1, 'In'),
    )
    snid = models.BigAutoField(primary_key=True, unique=True)
    timestamp = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    pcIn = models.IntegerField(verbose_name='In', null=True, default=0, choices=IO)
    pcOut = models.IntegerField(verbose_name='Out', null=True, default=0, choices=IO)
    mfgDate = models.DateField()
    image = models.ImageField(upload_to='custom/img/')
    qrcode = models.ImageField(upload_to='custom/qrcodes/')
    squareLink = models.CharField(max_length=500)
    invoiceID = models.IntegerField(null=True)#add FK
    customerID = models.IntegerField(null=True)#add FK
    employeeID = models.IntegerField(null=True)#add FK
    class Meta:
        ordering = ['snid']
        verbose_name = 'Custom Work'
    def get_absolute_url(self):
        return reverse('inventory', args=[str(self.snid)])
    def __str__(self):
        return f'{self.snid} {self.title} | {self.description}'

class FCustomWork(ModelForm):
    class Meta:
        model = MCustomWork
        fields = '__all__'

'''
Production Work
'''
class MProductionWork(models.Model):
    snid = models.BigAutoField(primary_key=True, unique=True)
    model = models.CharField(max_length=25)
    description = models.CharField(max_length=500)
    msrp = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    wholesale = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    inchesPerUnit = models.IntegerField()
    image = models.ImageField(upload_to='prodo/img/', null=True)
    image2 = models.ImageField(upload_to='prodo/img/', null=True)
    image3 = models.ImageField(upload_to='prodo/img/', null=True)
    image4 = models.ImageField(upload_to='prodo/img/', null=True)
    image5 = models.ImageField(upload_to='prodo/img/', null=True)
    qrcode = models.ImageField(upload_to='prodo/qrcodes/', null=True)
    squareLink = models.CharField(max_length=500, null=True)
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Production Work'
    def get_absolute_url(self):
        return reverse('prodo-detail', args=[str(self.snid)])
    def __str__(self):
        return f'{self.snid} | {self.description} MSRP: ${self.msrp} WS: ${self.wholesale} {self.inchesPerUnit}\"'

class FProductionWork(ModelForm):
    class Meta:
        model = MProductionWork
        fields = '__all__'

class MpwIn(models.Model):
    snid = models.ForeignKey(MProductionWork, on_delete=models.RESTRICT)
    timestamp = models.DateField(auto_now_add=True)
    unitsIn = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'PW In'
    def __str__(self):
        return f'{self.snid} {self.timestamp} {self.unitsIn}'

class FpwIn(ModelForm):
    class Meta:
        model = MpwIn
        fields = '__all__'

class MpwOut(models.Model):
    snid = models.ForeignKey(MProductionWork, on_delete=models.RESTRICT)
    timestamp = models.DateField(auto_now_add=True)
    unitsOut = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'PW Out'
    def __str__(self):
        return f'{self.snid} {self.timestamp} Units Out:{self.unitsOut}'

class FpwOut(ModelForm):
    class Meta:
        model = MpwOut
        fields = '__all__'

'''
Prototypes
'''
class MPrototypes(models.Model):
    snid = models.BigAutoField(primary_key=True, unique=True)
    description = models.CharField(max_length=25)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='proto/img/')
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Prototypes'
    def __str__(self):
        return f'{self.snid} {self.description} | Dr: ${self.debit} | Cr: ${self.credit}'
    def get_absolute_url(self):
        return reverse('inventory', args=[str(self.snid)])

class FPrototypes(ModelForm):
    model = MPrototypes
    fields = '__all__'

'''
Store Inventory
'''
class MStoreInventory(models.Model):
    snid = models.BigAutoField(primary_key=True, unique=True)
    description = models.CharField(max_length=50)
    msrp = models.DecimalField(max_digits=10, decimal_places=2)
    unitsPerCs = models.IntegerField()
    image = models.ImageField(upload_to='storeInventory/img/')
    qrcode = models.ImageField(upload_to='storeInventory/qrcodes/')
    squareLink = models.CharField(max_length=500)
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Store Inventory'
    def __str__(self):
        return f'{self.snid} {self.description} | ${self.msrp} {self.unitsPerCs}'
    def get_absolute_url(self):
        return reverse('inventory', args=[str(self.snid)])

class FStoreInventory(ModelForm):
    model = MStoreInventory
    fields = '__all__'

class MsiIn(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.ForeignKey(MStoreInventory, on_delete=models.RESTRICT)
    description = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    purchaseDate = models.DateField()
    unitsIn = models.IntegerField()
    invoiceID = models.CharField(max_length=50)
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'SI In'
    def __str__(self):
        return f'{self.timestamp} {self.snid} {self.description}'

class FsiIn(ModelForm):
    model = MsiIn
    fields = '__all__'

class MsiOut(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.ForeignKey(MStoreInventory, on_delete=models.RESTRICT)
    description = models.CharField(max_length=50)
    unitsOut = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'SI Out'
    def __str__(self):
        return f'{self.timestamp} {self.snid} {self.description}'

class FsiOut(ModelForm):
    model = MsiOut
    fields = '__all__'

'''
Land Improvements
'''
class MLandImprovements(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    purchaseDate = models.DateField()
    receiptID = models.CharField(max_length=50)
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Land Improvements'
    def __str__(self):
        return f'{self.snid} {self.description}'

'''
Computer Equipment
'''
class MComputerEquipment(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    purchaseDate = models.DateField()
    depreciationLife = models.DecimalField(max_digits=5, decimal_places=2)
    receiptID = models.CharField(max_length=50)
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Computer Equipment'
    def __str__(self):
        return f'{self.snid} {self.description}'

'''
Store Equipment
'''
class MStoreEquipment(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    purchaseDate = models.DateField()
    depreciationLife = models.DecimalField(max_digits=10, decimal_places=2)
    receiptID = models.CharField(max_length=50)
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Store Equipment'
    def __str__(self):
        return f'{self.snid} {self.description}'

'''
Machinery & Equipment
'''
class MMachineryEquipment(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    purchaseDate = models.DateField()
    depreciationLife = models.DecimalField(max_digits=10, decimal_places=2)
    receiptID = models.CharField(max_length=50)
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Machinery & Equipment'
    def __str__(self):
        return f'{self.snid} {self.description}'

'''
Office Equipment
'''
class MOfficeEquipment(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    purchaseDate = models.DateField()
    depreciationLife = models.DecimalField(max_digits=10, decimal_places=2)
    receiptID = models.CharField(max_length=50)
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Office Equipment'
    def __str__(self):
        return f'{self.snid} {self.description}'

'''
Shop Equipment
'''
class MShopEquipment(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    purchaseDate = models.DateField()
    depreciationLife = models.DecimalField(max_digits=10, decimal_places=2)
    receiptID = models.CharField(max_length=50)
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Shop Equipment'
    def __str__(self):
        return f'{self.snid} {self.description}'

class MAccountsPayable(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True, unique=True)
    description = models.CharField(max_length=50)
    valueLoaned = models.DecimalField(max_digits=10, decimal_places=2)
    valuePayed = models.DecimalField(max_digits=10, decimal_places=2)
    dateOpened = models.DateField(null=True)
    dateClosed = models.DateField(null=True)
    dueDate = models.DateField(null=True)
    customerID = models.IntegerField()
    receiptID = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Accounts Payable'
    def __str__(self):
        return f'{self.snid} {self.description}'
    def get_absolute_url(self):
        return reverse('inventory', args=[str(self.snid)])

class MSuppliesExpense(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    purchaseDate = models.DateField()
    customerID = models.IntegerField()
    receiptID = models.IntegerField()
    accountID = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Supplies Expense'
    def __str__(self):
        return f'{self.snid} {self.description}'

class MUtilitiesExpense(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    billDate = models.DateField()
    dueDate = models.DateField()
    customerID = models.IntegerField()
    receiptID = models.IntegerField()
    accountID = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Utilities Expense'
    def __str__(self):
        return f'{self.snid} {self.description}'

class MTravelExpense(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    purchaseDate = models.DateField()
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    customerID = models.IntegerField()
    receiptID = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Travel Expense'
    def __str__(self):
        return f'{self.snid} {self.description}'

class MUnearnedSalesRevenue(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    owed = models.DecimalField(max_digits=10, decimal_places=2)
    payed = models.DecimalField(max_digits=10, decimal_places=2)
    customerID = models.IntegerField()
    receiptID = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Unearned Sales Revenue'
    def __str__(self):
        return f'{self.snid} {self.description}'

class MDeliveryExpense(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    customerID = models.IntegerField()
    receiptID = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Delivery Expense'
    def __str__(self):
        return f'{self.snid} {self.description}'

class MAllowanceForDoubtfulAccounts(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    customerID = models.IntegerField()
    receiptID = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Allowance For Doubtful Accounts'
    def __str__(self):
        return f'{self.snid} {self.description}'

class MCapital(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    transactionDate = models.DateField()
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    customerID = models.IntegerField()
    receiptID = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Capital'
    def __str__(self):
        return f'{self.snid} {self.description}'

class MDrawings(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    transactionDate = models.DateField()
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    customerID = models.IntegerField()
    receiptID = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Drawings'
    def __str__(self):
        return f'{self.snid} {self.description}'

class MSalesRevenue(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    saleDate = models.DateField()
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    customerID = models.IntegerField()
    receiptID = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Sales Revenue'
    def __str__(self):
        return f'{self.snid} {self.description}'

class MRentExpense(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    payDate = models.DateField()
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    customerID = models.IntegerField()
    receiptID = models.IntegerField()
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Rent Expense'
    def __str__(self):
        return f'{self.snid} {self.description}'

class MSalaryExpense(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    snid = models.BigAutoField(primary_key=True)
    fullname = models.CharField(max_length=50)
    payPerHour = models.DecimalField(max_digits=10, decimal_places=2)
    totalHours = models.DecimalField(max_digits=10, decimal_places=2)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        ordering = ['snid']
        verbose_name_plural = 'Salary Expense'
    def __str__(self):
        return f'{self.snid} {self.fullname}'

