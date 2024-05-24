class admin:
    def __init__(self,Email,Password):
        self.Email=Email
        self.Password=Password

    def __repr__(self):
        return f'admin[{self.Email},{self.Password}]'  
    
#===============================================================================================================
    
class customerdetails:
    def __init__(self,name=None,email=None,contact=None,address=None,Password=None):
        self.name=name
        self.email=email
        self.contact=contact
        self.address=address
        self.Password=Password
        
    def __repr__(self):
        return f'customerdetails[{self.name},{self.email},{self.contact},{self.address},{self.Password}]'    

#=================================================================================================================

class product:
    def __init__(self,product_id,pname,quantity,price):
        self.product_id=product_id
        self.pname=pname
        self.quantity=quantity
        self.price=price
        
    def __repr__(self):
        return f'product[{self.product_id},{self.pname},{self.quantity},{self.price}]'    
    
#=================================================================================================================

class orders:
    def __init__(self,orderid,email,product_id,product_name,quantity,price,total_bill):
        self.orderid=orderid
        self.email=email
        self.product_id=product_id
        self.product_name=product_name
        self.quantity=quantity
        self.price=price
        self.total_bill=total_bill
    def __repr__(self):
        return f'orderdetail[{self.orderid},{self.email},{self.product_id},{self.product_name},{self.quantity},{self.price},{self.total_bill}]'          