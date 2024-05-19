import pyttsx3
# import customerdetails
from validation1 import *
import database1 as db
import maskpass
text_speech=pyttsx3.init()
msg="Welcome to SQUAD grocery store "
msg2="THANKU FOR VISITING OUR store "
# print('*******Welcome to SQUAD Grocery Store*******')

choice=0

while(choice!=4):
    print("\t\t================================================================")
    print("\t\t\t\t******* Welcome to SQUAD Grocery Store *******")
    print('\t\t\t\t1.Login')
    print('\t\t\t\t2.Signup')
    print('\t\t\t\t3.Exit') 
    print("\t\t================================================================")

    choice=int(input('Enter your choice:'))
    if choice==1:
        print('Login')
        print()
        while True:
            print("\t\t================================================================")
            print('\t\t\t\t1.Admin login')
            print('\t\t\t\t2.Customer Login')
            print('\t\t\t\t3.Exit')
            print("\t\t================================================================")
            choice=input('Enter your login choice:')

            #--------------------- Admin login----------------------------------#
            if choice=='1':
                print('\n-----<Admin Login Section>----\n')
                print()
                #Email validation
                while True:

                    Email=input('Enter your Email:')
                    if EmailValidation(Email):
                        break
                    else:
                        print('\n-----Invaild Email----\n')

                 #password validation
                while True:
                     Password=maskpass.askpass('Enter Your Password:',mask='*') 
                     if PasswordValidation(Password)==True:
                        break
                     else:
                         print('\n-----Invalid Password----\n')         
                
                data=db.Admin_Login(Email,Password)
                if data==True:
                    print('\n-----<Admin login successfully>----\n')
                    print()
                    while True:
                        print('\n--------<Admin Choice>-------------')
                        print()

                        print("\t\t=================================================================")
                        print("\t\t\t\tSQUAD Grocery Store")
                        print("\t\t_________________________________________________________________")
                        print("\t\t\t\t1.Add Products")
                        print("\t\t\t\t2.Show All Products")
                        print("\t\t\t\t3.Remove Product")
                        print("\t\t\t\t4.Exit")
                        print("\t\t================================================================")
                        choice=input('enter your Choice:')
                        if choice=='1':
                            print('\n---------<Add Product Details>--------\n')

                            #product_id
                            while True:
                                product_id=input('Enter product_id:')
                                if AddressValidation(product_id):
                                    break
                                else:
                                    print('\n-----------Product ID-----------\n') 

                            #pname name 
                            while True:
                                pname=input('Enter  Product Name:')
                                if AddressValidation(pname):
                                    break
                                else:
                                    print('\n-----------Invalid Product name-----------\n')

                            #quantity
                            while True:
                                quantity=input('Enter quantity:')
                                if AddressValidation(quantity):
                                    break
                                else:
                                    print('\n-----------Invalid quantity-----------\n')         

                            #price        
                            while True:
                                price=input('Enter price:')
                                if AddressValidation(price):
                                    break
                                else:
                                    print('\n-----------Invalid price-----------\n')                            

                            y=(product_id,pname,quantity,price)
                            db.details(y)
                            print()
                            print('-----------<Product Added Successfully>-------')
                            print()                        

                        elif choice=='2':
                            db.Show_All_Products()

                        elif choice=='3':
                            db.delete_products()

                        elif choice == '4':
                            print("------------------- Log Out from ADMIN Section ---------------------")
                            break     
                
                else:
                    print('-----Admin Email or Password wrong------')

            #------------- Customer Login ---------------------------
            if choice=='2':
                print("\t\t*________________________________________________________________*")
                print('\t\t\t\t-----< Customer Login Section >----')
                print("\t\t*________________________________________________________________*")
                #Email validation
                while True:
                    email=input('Enter your Email:')
                    if EmailValidation(email):
                        break                 
                    else:
                        print('\n-----Invaild Email----\n')

                 #password validation
                while True:
                     Password=maskpass.askpass('Enter Your Password:',mask='*') 
                     if PasswordValidation(Password)==True:
                        break
                     else:
                        print('\n-----Invalid Password----\n')         
                
                data=db.customer_Login(email,Password)
                 
                if data==True:
                    print('\n\t\t\t\t-----< Customer login successfully >----\n')
                    


                    while True:
                        print("\t\t=================================================================")
                        print("\t\t\t\tSQUAD Grocery Store")
                        print("\t\t________________________________________________________________")
                        print("\t\t\t\t1.Show All Products")
                        print("\t\t\t\t2.Buy Product")
                        # print("\t\t\t\t3.Remove Products from cart")
                        # arjun01@gmail.com
                        print("\t\t\t\t3.Show Order Details") 
                        print("\t\t\t\t4.Exit")
                        print("\t\t=================================================================")
                        print()
                        choice=input("Enter your choice:")
                        if choice=='1':
                            print('\n---------< All Products List >--------\n')
                            db.Show_All_Products()
                            print('='*10)

                        elif choice=="2":
                            db.Show_All_Products()
                            print('-'*100)

                            email = input("Enter Email: ")
                            product_id = input("Enter Product ID: ")
                            product_name = input("Enter Product Name: ")
                            quantity = int(input("Enter Quantity: "))
                            price = float(input("Enter Price: "))
                            z=(email,product_id,product_name,quantity,price)
                            db.order(z)
                            print("\t\t*________________________________________________________________*")
                            print('\t\t-----------<< Product ADDED in CART successfully >>-----------')
                            print("\t\t*________________________________________________________________*")                                   
                            text_speech.say("Product ADDED in CART successfully")
                            text_speech.runAndWait() 

                        elif choice=='3':
                            print()
                            print("\t\t*________________________________________________________________*")
                            bill= int(quantity)*price
                            print("\t\t\t\t(-----<< YOUR FINAL ORDER BILL = ",bill,">>----)")
                            text_speech.say("your final order bill is Rupees",bill)
                            text_speech.runAndWait()
                            
                        elif choice=='4':
                            print("\t\t-------------------------------------------------------")
                            print("\t\t\t\t THANKU FOR VISITING OUR Store:)")
                            print("\t\t-------------------------------------------------------")
                            text_speech.say("thanku for visiting our store please visit again")
                            text_speech.runAndWait()
                            break
                else:
                    print('-----Customer Email or Password wrong------')

#------------------------ Signup for Customer -----------------------#        

    elif choice==2:
        print('----------- Create New Account -----------')

        #Name Validate
        while True:
            name=input('Enter your Name:')
            if NameValidation(name):
                break
            else:
                print('Please type valid name')

        #email validation
        while True:
            email=input('Enter your Email:')
            if EmailValidation(email):
                break
            else:
                print('\n-------Invalid Email--------\n')
        
        #Contact Validation
        while True:
            contact=input('Enter you contact number:')
            if ConatactValidation(contact):
                break
            else:
                print("Enter valid contact number")
        
        #Address validation
        while True:
            address=input("Enter your Address:")
            if AddressValidation(address):
                break
            else:
                print("please enter valid address")
                
        #Password validation
        while True:
            Password=maskpass.askpass('Enter your Password: ',mask='*')
            if PasswordValidation(Password)==True:
                break
            else:
                print('\n-------Invalid Password------\n')       
                
        # x= (name,email,contact,address,Password)
        db.Register(name,email,contact,address,Password)
        print("\t\t*________________________________________________________________*")
        print('---------------------< Account Created Successfully >-----------------')
        print("\t\t*________________________________________________________________*")
        print()

    # elif choice==3:
        
            
    else:
        print("\t\t-------------------------------------------------------")
        print("\t\t\t\t THANKU FOR VISITING OUR Store:)")
        print("\t\t\t\t Visit Again")
        print("\t\t-------------------------------------------------------")
        break
