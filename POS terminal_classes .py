class Admin:
    def __init__(self, adminID, adminName, adminUsername, adminPassword):
        self.adminID = adminID
        self.adminName = adminName
        self.adminUsername = adminUsername
        self.adminPassword = adminPassword
        
    def validatepassword():
        print('''You are logged in successfully - password validated''')
        
    def additems(x):
        print(f'{x} added successfully')
    def updateitems(x):
        print(f'{x} updated successfully')
    def deleteitems(x):
        print(f'{x} deleted successfully')
    def viewsalesreport(date1, date2):
        print(f'sales report of {date1} to {date2}')
    def managesales():
        print('manage sales')
        
        
        
class Productcatalouge:
    def __init__(self,PcataID, PcataIDtype):
        self.PcataID = PcataID
        self.PcataIDtype = PcataIDtype
        
        
    def showallpdt(n):
        print(f'Showing all {n} products')
    def addnewpdt(x,xprice):
        print(f'product {x} added successfully - assigned price{xprice}.')
        

class Productspecification:
    def __init__(self,productSpecID, productSpecName, productSpecDescription, productSpecPrice):
        self.productSpecID = productSpecID
        self.productSpecName = productSpecName
        self.productSpecDescription = productSpecDescription
        self.productSpecDescription = productSpecDescription
        
        
    def Viewproductdescription():
        print(f'Shows all specs and description with price')
        
class store:
    def __init__ (self,storeName, storeAddress, storeID):
        self.storeName = storeName
        self.storeAddress = storeAddress
        self.storeID = storeID
        
    def viewstock():
        print('shows item and quantity of all items')
    def addstock():
        print('item name and quantity is added successfully')
    def customername(customerid):
        print(f'shows name of {customerid} ')
        
class items:
    def __init__(self, itemcode, itemname):
        self.itemcode = itemcode
        self.itemname = itemname
        
        
class POSTerminal:
    def __init__(self, POSTerminalID):
        self.POSTerminalID = POSTerminalID
        
    def PurchaseDetails(orderID):
        print(f'Items list and their quantity with price in the given order id :{orderID}')
        

class Sale:
    def __inint__(self, Trid, TrDate, TrTime):
        self.Trid = Trid
        self.TrDate = TrDate
        self.TrTime = TrTime
        
    def gettotal(**arg):
        print(f'sub total without taxes : {sum(args)}.')
    def printorder():
        print('printing order details')
    def viewsales():
        print('displays sales overview of the same day')
