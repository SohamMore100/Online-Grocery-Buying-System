import mysql.connector as db
import pandas as pd
from models import customerdetails

con=db.connect(host="localhost", user="root",password='Soham@123',db="groceryms")
print('******** Connection Establish Successfully ********')
cursor=con.cursor()

#----------------------- Admin Table ----------------------------------------------

try:
    Admin_table='create table if not exists admin(Email text,Password text)'
    cursor.execute(Admin_table)
    con.commit()
except:
    print("Table already exists")

#=============== Customer Detail table ====================================================================
try:
    customerdetails='create table if not exists customerdetails(name varchar(20),email varchar(50),contact varchar(20),address text,Password text);'
    cursor.execute(customerdetails)
    con.commit()
except:
    print("Table already exists")

#---------------Product Details Table------------------------------------------------
try:
    product_table='create table if not exists product(product_id int(50),pname varchar(30),quantity int(20),price int(50))'
    cursor.execute(product_table)
    con.commit() 
except:
    print("Table already exists")   

#--------------- Order Details Table ------------------------------------------------
try:
    # order_table=' create table if not exists orderdetail(orderid int,email varchar(50),product_id int,product_name varchar(30),quantity int,price float(10,2),foreign key(email) references customerdetails(email),foreign key(product_id) references product(product_id),total-bill int)'
    order_table='create table if not exists orderdetail(order_id INT primary key AUTO_INCREMENT,email VARCHAR (50),product_id INT (50),product_name VARCHAR (50),quantity INT,price INT)'
    cursor.execute(order_table)
    con.commit() 
except:
    print("Table already exists")   

# =========================================================================================================================    

# def Register(x):
#     register_query='insert into customerdetails(name,email,contact,address,Password) values (%s,%s,%s,%s,%s)'
#     cursor.execute(register_query,x)
#     con.commit()

def Register(name,email,contact,address,Password):
    find1='select * from customerdetails where email=%s'
    register_query='insert into customerdetails(name,email,contact,address,Password) values(%s,%s,%s,%s,%s)'
    cursor.execute(find1,(email,))  
    existing_user=cursor.fetchone()
    if existing_user:
        print("Email ID already exists")
    else:
        cursor.execute(register_query,(name,email,contact,address,Password))
        con.commit()
        print('signup successfully')  

def details(y):
    details_query='insert into product(product_id,pname,quantity,price) values(%s,%s,%s,%s)'
    cursor.execute(details_query,y)
    con.commit()

def order(z):
    order_query='insert into orderdetail(email,product_id,product_name,quantity,price) values(%s,%s,%s,%s,%s)'
    cursor.execute(order_query,z)
    con.commit()    

# ================================== Admin login ===========================================================
    
def Admin_Login(Email,Password):
    select_query='Select * from admin where Email= %s and Password =%s'
    data=(Email,Password)
    cursor.execute(select_query,data)
    s=cursor.fetchone()

    try:    
        if s[0]==Email:
            if s[1]==Password:
                return True
    except:
        print('-----Invalid email or Password--------')    

#======================== Customer Details =============================================================================

def customer_Login(email,Password):
    select_query='select * from customerdetails where email=%s and Password=%s'
    data=(email,Password)    
    cursor.execute(select_query,data)
    s=cursor.fetchone()
     
    try:
        if s[1]==email:
            if s[4]==Password:
                return True
    except:
        print('-----Invalid Email or Password-----')

      

#------------------------- Functions for Admin choices------------------------------------- 

def Show_All_Products():  
    print('-'*120)    
    sql='select * from product'  
    cursor.execute(sql)  
    records=cursor.fetchall()  
    rec=pd.DataFrame(records,columns=['product_id','pname','quantity','price'])  
    pd.set_option('display.colheader_justify','center')  
    if rec.empty==True:
        print('\n no Products found')
    else:
        print(rec)


def delete_products():
    print('-'*100)
    ac=input('Enter Product name:')
    sql='delete from product where pname =%s'
    data=(ac,)
    cursor.execute(sql,data)
    con.commit()
    print('\n Product deleted successfully')
    wait=input('\n press any key to continue.....')

#------------------------- Functions for Customer choices------------------------------------- 

def Buy_Product():
    print('\n---------< BUY Products >--------\n')
    # print('-'*100)
    # b=print('Enter Your email:')
    # c=input('Enter Product_id:')
    # d=input('Enter Product name:')
    # e=input('Enter Product quantity:')
    
    # price='Select price from product where pname = %s'
    # cursor.execute(price)
    # price = cursor.fetchone()

    # total_bill=int(price[0])
    # total_bill = int(e)*price
    # print("\t\t\t\t(( YOUR FINAL ORDER BILL ))",total_bill)
    # z= (c,d,e,price,total_bill)
    # db.order(z)
    # print()
    # print('\n Product ADDED in CART successfully')

    # email,product_id,product_name,quantity,price  ||  'mysql.connector' has no attribute 'order_details'

# price='Select price from product where pname = product_name'
# cursor.execute(price)
# price = cursor.fetchone()

# def bill():
#     print()
#     print("\t\t*________________________________________________________________*")
#     total_bill=int(price[0])
#     total_bill = int(quantity)*price
#     z= (total_bill)
#     db.order(z)
#     print("\t\t\t\t(( YOUR FINAL ORDER BILL ))",total_bill)
#     print("\t\t\t\t(( YOUR FINAL ORDER BILL ))")
