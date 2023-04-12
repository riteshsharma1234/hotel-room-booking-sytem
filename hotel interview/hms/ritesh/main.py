import mysql.connector as db
import re
import os
import time
from hotel import Regx
from prettytable import PrettyTable
from time import sleep
# application start with here...........

App = Regx()

while True:
    print("\n|------*******-------------------------- Hotel Room Booking System ----------------------******------------------|\n")
    print("1- Admin Login \n2- Customer Login & Register \n3 View Rooms Type \n4 -Exit  \n")
    ch = input("Enter Your Choice :")

     
    if ch =="1":
        print("\n-----------------------------Admin Login Section---------------------------------------------------n")
        a_username = input("Enter Your Username :")
        a_password = input("Enter Your Password :")
        admin = App.AdminLogIn(a_username,a_password)
        if admin ==None:
            print("\n-------------------------Invalid UserName------------------------------------------------------\n")
        
        else:
            if a_password !=admin[1]:
                print("----------------------Invalid Password --------------------------------------------------------\n")
            else:
                print("\n|-------------------- SuccessFully Logged In --------------------------------------------------|\n")


        # admin Authentication
                
                while True:
                    print("|***************************  customer Section **********************************************|")
                    print("\n1- Customer Details \n2- Book Rooms Type  \n3- Room  Information \n4- Admin Logout \n")

                    ach = input("Enter Your Choice :")


                    #Customer Information section..........
                    if ach =="1":
                        print("\n|--------------------------------- Create customer Detail Section --------------------| \n")
                        print("\n1 -Add customer\n2 -view customer\n3update customer\n4-Remove customer\n5-Exit")
                        c_choice = input("enter your choice :")
                        
                        if c_choice == "1":
                            print("\n-------------------- Add customer section ------------------------------\n")
                         # name Validation 
                            while True:
                                c_name = input("Enter Your Name :")
                                x = App.NameValidation(c_name)
                                if x == True:
                                    break
                                else:
                                    print("\n---------------Invalid Name -------------------------------------\n")

                            # contact Validation 
                            while True:
                                c_contact = input("Enter Your Contact :")
                                x = App.ContactValidation(c_contact)
                                if x == True:
                                    break

                                else:
                                    print("\n****************** Invalid Contact*******************\n")

                            
                            #Email Validation 
                            while True:
                                c_email = input("Enter Your Email :")
                                x = App.EmailValidation(c_email)
                                if x == True:
                                    break

                                else:
                                    print("\n****************** Invalid Email *******************\n")

                            #address field
                            address = input("Enter Address :")

                            #register_date_
                            register_date = time.strftime("%Y-%m-%d")

                            #password
                            passwd=(input("Enter passwd:"))


                            
                            check_info = App.CheckInfo(c_contact , c_email)

                            if check_info == True:

                                Register = App.cus_Detail(c_name , c_contact , c_email , address ,register_date,passwd)

                                if Register== True:

                                    #create file to store user info
                                    with open(f"UserAccount/{c_email}.txt" , "a") as file:
                                        file.write(f"User Name : {c_name}\n")
                                        file.write(f"User Contact : {c_contact}\n")
                                        file.write(f"User Email-ID : {c_email}\n")
                                        file.write(f"User Address : {address}\n")
                                        file.write(f"register_date : {register_date}\n")
                                        file.write(f"passwd : {passwd}\n")
                                        
                                    print("\n------------------------- sucessfullly Register ----------------------------------\n")

                            else:
                                print(f"**************** {check_info} ******************\n")

                        elif c_choice == "2":
                            print("\n----------------------view customer section----------------------------\n")
                            View_Customer = App.View_CustomerInfo()
                            #| cid | cname | contact    | email           | address | register_date | passwd
                            x = PrettyTable()
                            x.field_names = ["Customer ID","Customer Name","Customer Contact ","Customer Email","Customer Address","Customer Register Date","Customer Password "]
                            x.add_rows(View_Customer)
                            print(x)

                        elif c_choice == "3":
                            print("\n-----------------------Update customer section ------------------------------\n")
                            print("\n*********** User Updating Section **********\n")
                            while True:
                                print("\n1 - Update contact \n2 - Update Name & Address \n3-Exit\n")

                                uch = input("Enter Update Choice :")

                                if uch == "1":
                                    cus_id = int(input("Enter your cust_id:"))
                                    new_contact = input("Enter Your New contact :")
                                    App.Update(new_contact , cus_id)
                                    print("\n******** Successfully contact Updated *******\n")

                                elif uch == "2":
                                    cus_id = int(input("Enter your cust_id:"))
                                    new_address = input("Enter Your New address:")
                                    new_passwd = input("Enter Your New passwd :")
                                    App.Update(new_address , new_passwd ,cus_id)
                                    print("\n******** Successfully address & pass Updated *******\n")

                                elif uch == "3":
                                    print("\n************ Exit from Update Details **********\n")
                                    break

                                else:
                                    print("\n************* Invalid Option *******\n")


                        elif c_choice == "4":
                            print("\n-------------------------remove customer section-------------------\n")
                            cust_id = input("Enter customer id :")
                                
                           
                            print("\n---------------Delete Luxury Customer Section ---------------- \n")
                            delete_cust_id = input("Enter Customer ID want to delete : ")
                            dch = input("Are Your sure want to Delete Customer Account  :(Y/N)")
                            if (dch =="Y" or dch =="yes" or "Yes" or "YES"):
                                        App.Delete_customer_Info(delete_cust_id)
                                        print(f"\n**********************Successfully Deleted ***********************\n")

                            
                            else:
                                print("\n********************* Process Has Been Cancelled ************************\n")



                        elif c_choice == "5":
                            print("\n--------------------------Exit ----------------------------------\n")
                            break
                        else:
                            print("\n----------------Invalid choice--------------------------------\n")

                   
                    elif ach=="2":
                        print("\n------------This is Room Booking Section -------------------\n")
                        while True:
                                print("\n1-Luxury Room \n2- Delux Room \n3- Standard ROom \n4- Quad Room \n5- Exit  \n")
                                room_type = input("Enter Your Room Choice :")
                               
                                if (room_type=="1"):
                                    print("\n---------Luxury Room Book Section ------------\n")
                                    customer_name = input("Enter Customer Name :")
                                    
                                    # Check_in = input("Enter Customer Check In Date :")
                                    # Check_out = input("Enter Customer Check Out Date :")
                                    hmd=input("How Many Days You Want To Stay:")
                                    x = ("Admin")
                                    App.Room_Book_Luxury(customer_name,hmd)
                                    print(f"\n---------------Hello {x} SuccessFully  Luxury Room Booked to {customer_name}----------\n")
                                
                                
                                    
                                elif (room_type=="2"):
                                    print("\n---------Delux Room Book Section ------------\n")
                                    customer_name = input("Enter Customer Name :")
                                    # Check_in = input("Enter Customer Check In Date :")
                                    # Check_out = input("Enter Customer Check Out Date :")
                                    hmd=input("How Many Days You Want To Stay:")
                                    x = ("Admin")
                                    App.Room_Book_Delux(customer_name,hmd)
                                    print(f"\n---------------Hello {x} SuccessFully  Luxury Room Booked to {customer_name}----------\n")
                                
                                
                              
                                elif (room_type=="3"):
                                    print("\n---------Standard Room Book Section ------------\n")
                                    customer_name = input("Enter Customer Name :")
                                    # Check_in = input("Enter Customer Check In Date :")
                                    # Check_out = input("Enter Customer Check Out Date :")
                                    hmd=input("How Many Days You Want To Stay:")
                                    x = ("Admin")
                                    App.Room_Book_Standard(customer_name,hmd)
                                    print(f"\n---------------Hello {x} SuccessFully  Luxury Room Booked to {customer_name}----------\n")
                                
                                
                                elif (room_type=="4"):
                                    print("\n---------Quad Room Book Section ------------\n")
                                    customer_name = input("Enter Customer Name :")
                                    # Check_in = input("Enter Customer Check In Date :")
                                    # Check_out = input("Enter Customer Check Out Date :")
                                    hmd=input("How Many Days You Want To Stay:")
                                    x = ("Admin")
                                    App.Room_Book_Delux(customer_name,hmd)
                                    print(f"\n---------------Hello {x} SuccessFully  Luxury Room Booked to {customer_name}----------\n")
                                
                                elif (room_type =="5"):
                                    print("-----------Exit the Room Bookin Section -----------------")
                                    break
                                else:
                                    print("---------------Invalid Choice ")

                    
                    elif ach=="3":
                        print("\n---------------------Room Info Section ---------------\n")
                        print("\n1- View Customer Room Info \n2-Update Customer Room Info \n3-Delete Customer Room Info  \n4-Exit \n")
                        room_info = input("Enter Your Info Choice : ")
                        
                        
                        if (room_info =="1"):  
                            print("\n--------------this is Room View Section ------------\n")
                            while True:
                                print("\n1-Luxury Room \n2- Delux Room \n3- Standard Room \n4- Quad Room \n5- Exit \n")
                                room_view = input("Enter Room View CHoice :")

                                # Luxury view Section 
                                if(room_view =="1"):
                                    print("\n--------------Luxury Room View Section ------------\n")
                                    Luxury_info= App.View_Luxury_Room()
                                    # Room_id | customer_name | Tv  | Bed                    | Iron | Bath_room | AC  | Wifi | Price | Check_in   | Check_out 
                                    x = PrettyTable()
                                    x.field_names=["Room ID ","Customer Names","TV Faculty","Bed Faculty","Iron Faculty","Wash Room Faculty","AC Faculty","WiFi Faculty","Room Price","hmd"]
                                    x.add_rows(Luxury_info)
                                    print(x)
                                
                                # Delux View Section 
                                elif(room_view =="2"):
                                    print("\n-----------Delux View Section ------------\n")
                                    Delux_info= App.View_Delux_Room()
                                    #| Room_id | customer_name | Tv  | Bed         | Bath_room | AC  | Wifi | Price | Check_in   | Check_out
                                    x = PrettyTable()
                                    x.field_names=["Room ID","Customer Name ","TV Faculty","Bed Faculty","Wash Room Faculty ","AC Faculty","WiFi Faculty","Room Price ","Check In Date","hmd"]
                                    x.add_rows(Delux_info)
                                    print(x)
                            
                                elif(room_view =="3"):
                                    print("\n-----------Standard View Section ------------\n")
                                    Standard_info= App.View_Standard_Room()
                                   #Room_id | customer_name | Tv  | Bed             | Bath_room | AC  | Price | Check_in   | Check_out
                                    x = PrettyTable()
                                    x.field_names=["Room ID","Customer Name","TV Faculty","Bed Faculty","Wash Room Faculty","AC Faculty","Room Price","hmd"]
                                    x.add_rows(Standard_info)
                                    print(x)
                                    
                            
                                elif(room_view =="4"):
                                    print("\n-----------Quad View Section ------------\n")
                                    Quad_info= App.View_Quad_Room()
                                   #Room_id | customer_name | Tv  | Bed         | Bath_room | Fan | Price | Check_in   | Check_out
                                    x = PrettyTable()
                                    x.field_names=["Room Id","Custmer Name","TV Faculty","Bed Faculty","Wash Room Faculty","Fan Faculty","Room Price","hmd"]
                                    x.add_rows(Quad_info)
                                    print(x)
                                
                                elif(room_view =="5"):
                                    print("\n-----------Exit  View Section ------------\n")
                                    break

                                else:
                                    print("\n------------Invalid View Section\n")

                        
                        elif(room_info =="2"):
                            print("\n------------Update Room Section -----------\n")
                            while True:
                                print("\n1-Luxury Room \n2- Delux Room \n3- Standard Room \n4- Quad Room \n5- Exit \n")
                                room_update = input("Enter Room View CHoice :")
                                
                                # Update Luxury Room 
                                if(room_update=="1"):
                                    print("\n----------Update Luxury Room Section ----------------\n")
                                    update_luxury_id = input("Enter Customer ID You want to Update Details :")
                                    update_check_in = input("Enter Check in Date :")
                                    update_check_out = input("Enter Check Out Date :")
                                    dch = input("Are Your sure want to Delete Luxury Customer Account  :(Y/N)")
                                    if (dch =="Y" or dch =="yes" or "Yes" or "YES"):
                                        App.Update_Luxury_Info(update_check_in,update_check_out,update_luxury_id)
                                        print(f"\n**********************Successfully Updated ***********************\n")

                            
                                    else:

                                        print("\n********************* Process Has Been Cancelled ************************\n")




                                 # Update Luxury Room 
                                elif(room_update=="2"):
                                    print("\n----------Update Delux Room Section ----------------\n")
                                    update_Delux_id = input("Enter Customer ID You want to Update Details :")
                                    update_check_in = input("Enter Check in Date :")
                                    update_check_out = input("Enter Check Out Date :")
                                    dch = input("Are Your sure want to Delete Delux Customer Account  :(Y/N)")
                                    if (dch =="Y" or dch =="yes" or "Yes" or "YES"):
                                        App.Update_Delux_Info(update_check_in,update_check_out,update_Delux_id )
                                        print(f"\n**********************Successfully Updated ***********************\n")

                            
                                    else:

                                        print("\n********************* Process Has Been Cancelled ************************\n")


                                 # Update Luxury Room 
                                elif(room_update=="3"):
                                    print("\n----------Update Standard Room Section ----------------\n")
                                    update_standard_id = input("Enter Customer ID You want to Update Details :")
                                    update_check_in = input("Enter Check in Date :")
                                    update_check_out = input("Enter Check Out Date :")
                                    dch = input("Are Your sure want to Delete standard Customer Account  :(Y/N)")
                                    if (dch =="Y" or dch =="yes" or "Yes" or "YES"):
                                        App.Update_Standard_Info(update_check_in,update_check_out,update_standard_id )
                                        print(f"\n**********************Successfully Updated ***********************\n")

                            
                                    else:

                                        print("\n********************* Process Has Been Cancelled ************************\n")


                                 # Update Luxury Room 
                                elif(room_update=="4"):
                                    print("\n----------Update Quad Room Section ----------------\n")
                                    update_Quad_id = input("Enter Customer ID You want to Update Details :")
                                    update_check_in = input("Enter Check in Date :")
                                    update_check_out = input("Enter Check Out Date :")
                                    dch = input("Are Your sure want to Delete Quad Customer Account  :(Y/N)")
                                    if (dch =="Y" or dch =="yes" or "Yes" or "YES"):
                                        App.Update_Quad_Info(update_check_in,update_check_out,update_Quad_id )
                                        print(f"\n**********************Successfully Updated ***********************\n")

                            
                                    else:

                                        print("\n********************* Process Has Been Cancelled ************************\n")


                                 # Update Luxury Room 
                                elif(room_update=="5"):
                                    print("\n-----------Exit Update Section \n")
                                    break
                                else:
                                    print("\n-----------  Invalid Section  -------------\n")

                        
                        elif (room_info =="3"):
                            print("\n----------------Remove Customer  Section  --------------\n")
                            while True:
                                print("\n1-Luxury Room \n2- Delux Room \n3- Standard Room \n4- Quad Room \n5- Exit \n")
                                room_delete = input("Enter Room View CHoice :")
                                
                                if(room_delete =="1"):
                                    print("\n---------------Delete Luxury Customer Section ---------------- \n")
                                    delete_luxury_id = input("Enter Customer ID want to delete : ")
                                    dch = input("Are Your sure want to Delete Luxury Customer Account  :(Y/N)")
                                    if (dch =="Y" or dch =="yes" or "Yes" or "YES"):
                                        App.Delete_Luxury_Info(delete_luxury_id)
                                        print(f"\n**********************Successfully Deleted ***********************\n")

                            
                                    else:

                                        print("\n********************* Process Has Been Cancelled ************************\n")


                                elif(room_delete =="2"):
                                    print("\n---------------Delete Delux Customer Section ----------------\n")
                                    delete_delux_id = input("Enter Customer ID want to delete : ")
                                    dch = input("Are Your sure want to Delete Luxury Customer Account  :(Y/N)")
                                    if (dch =="Y" or dch =="yes" or "Yes" or "YES"):
                                        App.Delete_Delux_Info(delete_delux_id)
                                        print(f"\n**********************Successfully Deleted ***********************\n")

                            
                                    else:

                                        print("\n********************* Process Has Been Cancelled ************************\n")

                                elif(room_delete =="3"):
                                    print("\n---------------Delete Luxury Customer Section ----------------\n")
                                    delete_delux_id = input("Enter Customer ID want to delete : ")
                                    dch = input("Are Your sure want to Delete Luxury Customer Account  :(Y/N)")
                                    if (dch =="Y" or dch =="yes" or "Yes" or "YES"):
                                        App.Delete_Standard_Info(delete_delux_id)
                                        print(f"\n**********************Successfully Deleted ***********************\n")

                            
                                    else:

                                        print("\n********************* Process Has Been Cancelled ************************\n")

                                elif(room_delete =="4"):
                                    print("\n---------------Delete Luxury Customer Section ---------------- \n")
                                    delete_delux_id = input("Enter Customer ID want to delete : ")
                                    dch = input("Are Your sure want to Delete Luxury Customer Account  :(Y/N)")
                                    if (dch =="Y" or dch =="yes" or "Yes" or "YES"):
                                        App.Delete_Quad_Info(delete_delux_id)
                                        print(f"\n**********************Successfully Deleted ***********************\n")

                            
                                    else:

                                        print("\n********************* Process Has Been Cancelled ************************\n")
                                    

                                elif(room_delete =="5"):
                                    print("\n---------------Thank You Room Delete Section ---------------- \n")
                                    break
                                else:
                                    print("\n-------------------Invalid Choice \n")

                        
                        #Exit Section 
                        elif (room_info =="4"):
                            print("\n----------Exit Section ----------------\n")
                            break
                        else:
                            print("\n--------------invalid Room Info Section ------------------\n")
                
                    # Admin Log Out
                    elif ach=="4":
                        print("n..........................................  Thank you Admin  Section    ......................................................\n")
                        break
                    
                    else:
                        print("*********** invalid choice ************")


    
    elif(ch=="2"):
        while True:
            print("\n----------------------Customer Register Section ----------------------")
            print("\n1 - Register \n2 - Login \n3 - exit \n")

            uch = input("Enter Your Choice :")

            # user register section
            if uch == "1":
                print("\n**** Registration section *******\n")
                while True:
                    c_name = input("Enter Your Name :")
                    x = App.NameValidation(c_name)
                    if x == True:
                        break
                    else:
                        print("\n ************** Invalid Name **************** \n")

                # contact Validation 
                while True:
                    c_contact = input("Enter Your Contact :")
                    x = App.ContactValidation(c_contact)
                    if x == True:
                        break

                    else:
                        print("\n****************** Invalid Contact*******************\n")

                
                    #Email Validation 
                while True:
                    c_email = input("Enter Your Email :")
                    x = App.EmailValidation(c_email)
                    if x == True:
                        break

                    else:
                        print("\n****************** Invalid Email *******************\n")

                #address field
                address = input("Enter Address :")

                #register_date
                register_date = time.strftime("%Y-%m-%d")

                #password
                passwd=(input("Enter passwd:"))


                
                check_info = App.CheckInfo(c_contact , c_email)

                if check_info == True:

                    Register = App.cus_Detail(c_name , c_contact , c_email , address ,register_date,passwd)

                    if Register== True:

                        #create file to store user info
                        with open(f"AllFiles/{c_email}.txt" , "a") as file:
                            file.write(f"User Name : {c_name}\n")
                            file.write(f"User Contact : {c_contact}\n")
                            file.write(f"User Email-ID : {c_email}\n")
                            file.write(f"User Address : {address}\n")
                            file.write(f"register_date : {register_date}\n")
                            file.write(f"passwd : {passwd}\n")
                            
                        print("\n****************** sucessfullly Register ***********\n")
                        print("\n------------------------------Now You Can login ---------------------\n")
                       
                    

                else:
                    print(f"**************** {check_info} ******************\n")

            # this is  customer login  section if login then show whole the hotel info .................
            elif uch =="2":
                print("\n*************** Login Section **************\n")
                while True:
                #     email = input("Enter Your Email-ID To Login :")
                #     x = App.EmailValidation(email)
                #     if x == True:
                #         break
                #     else:
                #         print("\n********* Invalid Email-ID *********\n")
                # passwd = input("Enter Your Password :")
                # x1 = App.UserLogin(email,passwd)
                # if x1 == None:
                #     print("\n***** Incorrect Details ******\n")
                # else:
                #     print("\n************ Login Succesfully **********\n")

                
                    c_email = input("Enter Your Email-ID to Login :")
                    x = App.EmailValidation(c_email)
                    if x == True:
                        break
                    else:
                        print("\n***** Invalid Email -ID ***********\n")
                c_password = input("Enter Your Password : ")
                x = App.UserLogin(c_email,c_password)
                if x == None:
                    print("--------------- incorrect details -----------------")
                else:
                    print("\n******  SuccessFully User Login **********\n")
                    while True:
                        print(f"-------------  Hello Sir ----{c_email} --- This is your Profile here -----")
                        # optional you can add view our booked room  if any query than contact me 
                        print("\n1 - Customer Profile \n2 - Room Type \n3 - Book Room \n4 - Update User Details \n5- Exit")
                        
                        uch = input("Enter Your Choice :")

                        
                        if uch == "1":
                            print("\n----------------- View Customer Information ---------------\n")
                            profile = App.Customer_Info(c_email)
                            x = PrettyTable()
                            x.index_names = ["Customer ID","Customer Name","Customer Contact","Customer Email","Customer Address","Account Created ","Password"]
                            x.add_row(profile)
                            print(x)

                        elif uch == "2":
                            print("\n---------------------- This is Unauthorized User Section to View Rooms ----------------------\n")
                            while True:
                                print("\n1-Luxury Room \n2- Delux Room \n3- Standard Room \n4- Quad Room \n5- Exit \n")
                                room_view = input("Enter Room View CHoice :")
                                s = time.strftime("%Y-%m-%d %H:%M:%S")
                            

                                # Luxury view Section 
                                if(room_view =="1"):
                                    print(f"\n----------- These all Faculty We Are Provide in the Hotel If You Want Then login Now  Time is  {s} ------------\n")
                                    Luxury_info= App.View_Luxury_Unauth()
                                    print(Luxury_info)
                                ## Tv  | Bed                    | Iron | Bath_room | AC  | Wifi | Price 
                                    x = PrettyTable()
                                    x.field_names=["TV Faculty","Bed Faculty","Iron Faculty","Wash Room Faculty","AC Faculty","WiFi Faculty","Room Price"]
                                    x.add_row(Luxury_info)
                                    print(x)
                                
                                # Delux View Section 
                                elif(room_view =="2"):
                                    print(f"\n----------- These all Faculty We Are Provide in the Hotel If You Want Then login  Now  Time is  {s}  ------------\n")
                                    Delux_info= App.View_Delux_Unauth()
                                    print(Delux_info)
                                    #Tv  | Bed         | Bath_room | AC  | Wifi | Price
                                    x = PrettyTable()
                                    x.field_names=["TV Faculty","Bed Faculty","Wash Room Faculty ","AC Faculty","WiFi Faculty","Room Price "]
                                    x.add_row(Delux_info)
                                    print(x)
                            
                                elif(room_view =="3"):
                                    print(f"\n----------- These all Faculty We Are Provide in the Hotel If You Want Then login  Now  Time is  {s}  ------------\n")
                                    Standard_info1= App.View_Standard_Unauth()
                                    #Tv  | Bed             | Bath_room | AC  | Price 
                                    x = PrettyTable()
                                    x.field_names=["TV Faculty","Bed Faculty","Wash Room Faculty","AC Faculty","Room Price"]
                                    x.add_row(Standard_info1)
                                    print(x)
                                    
                            
                                elif(room_view =="4"):
                                    print(f"\n----------- These all Faculty We Are Provide in the Hotel If You Want Then login  Now  Time is  {s}  ------------\n")
                                    Quad_info1= App.View_Quad_Unauth()
                                    # Tv  | Bed         | Bath_room | Fan | Price 
                                    x = PrettyTable()
                                    x.field_names=["TV Faculty","Bed Faculty","Wash Room Faculty","Fan Faculty","Room Price"]
                                    x.add_row(Quad_info1)
                                    print(x)
                                
                                elif(room_view =="5"):
                                    print("\n-----------Exit  View Section ------------\n")
                                    break

                                else:
                                    print("\n------------Invalid View Section\n")
                        
                        
                        elif uch == "3":
                            print("\n------------This is Room Booking Section -------------------\n")
                            while True:
                                print("\n1-Luxury Room \n2- Delux Room \n3- Standard ROom \n4- Quad Room \n5- Exit  \n")
                                room_type = input("Enter Your Room Choice :")
                                
                                if (room_type=="1"):
                                    print("\n---------Luxury Room Book Section ------------\n")
                                    # customer_name = input("Enter Customer Name :")
                                    
                                    Room="Luxury"
                                    # Check_in = input("Enter Customer Check In Date :")
                                    rch= int(input("Enter count of Day you want to stay:"))
                                    name=App.fetch_r_N(c_email)
                                    print(f"you have choosed a {Room} Room")
                                    price=App.fetch_r_price()
                                    print(price)
                                    Total = rch*price
                                    print(f"your room rent for choosen category will be : {Total}")


                                    bch=input("are you sure you want to book your room y/n:").upper()
                                    name=App.fetch_u_n(c_email)
                                    
                                    
                                    # Check_out = input("Enter Customer Check Out Date :")
                                    # App.Room_Book_Luxury(customer_name,Check_in,Check_out)

                                    # print(f"\n---------------Hello {customer_name} SuccessFully Your Luxury Room Booked  ----------\n")
                                    # ich=int(input("Enter your room_id you want to book:"))
                                    # x = App.check_room(ich)
                                    # if x==None:
                                    #     print("\n--------------------- please  Enter a valid id ----------------------\n")
                                    # else:

                                    if bch == "Y":
                                        print("Please Wait...\n")
                                        sleep(2)
                                        print("\n------------------ sucessfully Room Booked------------------------\n")
                                        sleep(5)
                                        print("|---------------------------| YOUR BILL |----------------------------|")
                                        print("|--------------------------------------------------------------------|")
                                        print("|---------------------------|Customer Details| ----------------------|")
                                        print("|--------------------------------------------------------------------|")
                                        print(f"\n--------> Name is :{name}")
                                        print(f"\n--------> Email is :{c_email}")
                                        print(f"\n--------> staying_Days :{rch}")
                                        print(f"\n--------> Room Name is :{Room}")
                                        print(f"\n--------> Room Price :{price}")
                                        print(f"\n--------> Grand Total :{Total}")
                                        print("|--------------------------------------------------------------------|")
                                
                                   
                                elif (room_type=="2"):
                                    print("\n---------Delux Room Book Section ------------\n")
                                    customer_name = input("Enter Customer Name :")
                                    Check_in = input("Enter Customer Check In Date :")
                                    Check_out = input("Enter Customer Check Out Date :")
                                    App.Room_Book_Delux(customer_name,Check_in,Check_out)
                                    print(f"\n---------------Hello {customer_name} SuccessFully Your Luxury Room Booked  ----------\n")
                                
                                
                                
                                
                                elif (room_type=="3"):
                                    print("\n---------Standard Room Book Section ------------\n")
                                    customer_name = input("Enter Customer Name :")
                                    Check_in = input("Enter Customer Check In Date :")
                                    Check_out = input("Enter Customer Check Out Date :")
                                    App.Room_Book_Standard(customer_name,Check_in,Check_out)
                                    print(f"\n---------------Hello {customer_name} SuccessFully Your Luxury Room Booked  ----------\n")
                                
                                
                                
                                elif (room_type=="4"):
                                    print("\n---------Quad Room Book Section ------------\n")
                                    customer_name = input("Enter Customer Name :")
                                    Check_in = input("Enter Customer Check In Date :")
                                    Check_out = input("Enter Customer Check Out Date :")
                                    App.Room_Book_Delux(customer_name,Check_in,Check_out)
                                    print(f"\n---------------Hello {customer_name} SuccessFully Your Luxury Room Booked  ----------\n")
                                
                                
                                elif (room_type =="5"):
                                    print("-----------Exit the Room Bookin Section -----------------")
                                    break
                                else:
                                    print("---------------Invalid Choice ")

                        elif uch == "4":
                            print("\n*********** User Updating Section **********\n")
                            while True:
                                print("\n1 - Update Name \n2 - Update Name & Address \n")

                                uch = input("Enter Update Choice :")

                                if uch == "1":
                                    new_name = input("Enter Your New Name :")
                                    App.UpdateUserDetails(new_name , c_email)
                                    print("\n******** Successfully Name Updated *******\n")

                                elif uch == "2":
                                    new_name = input("Enter Your New Name :")
                                    new_address = input("Enter Your New Address :")
                                    App.UpdateUserDetails(new_name , new_address ,c_email)
                                    print("\n******** Successfully Name & Address Updated *******\n")

                                elif uch == "3":
                                    print("\n************ Exit from Update Details **********\n")
                                    break

                                else:
                                    print("\n************* Invalid Option *******\n")


                        elif uch == "5":
                            print("\n*********** Exit  *******\n")
                            break
                        else:
                            print("\n********** Enter A Valid Choice ********\n")
   

            elif uch == "3":
                print("\n****** Exit ******\n")
                break
            else:
                print("\n************ invalid choice **********\n")

    
    elif ch=="3":
            print("\n---------------------- This is Unauthorized User Section to View Rooms ----------------------\n")
            while True:
                print("\n1-Luxury Room \n2- Delux Room \n3- Standard Room \n4- Quad Room \n5- Exit \n")
                room_view = input("Enter Room View CHoice :")
                s = time.strftime("%Y-%m-%d %H:%M:%S")
               

                # Luxury view Section 
                if(room_view =="1"):
                    print(f"\n----------- These all Faculty We Are Provide in the Hotel If You Want Then login Now  Time is  {s} ------------\n")
                    Luxury_info= App.View_Luxury_Unauth()
                   ## Tv  | Bed                    | Iron | Bath_room | AC  | Wifi | Price 
                    x = PrettyTable()
                    x.field_names=["TV Faculty","Bed Faculty","Iron Faculty","Wash Room Faculty","AC Faculty","WiFi Faculty","Room Price"]
                    x.add_row(Luxury_info)
                    print(x)
                
                # Delux View Section 
                elif(room_view =="2"):
                    print(f"\n----------- These all Faculty We Are Provide in the Hotel If You Want Then login  Now  Time is  {s}  ------------\n")
                    Delux_info= App.View_Delux_Unauth()
                     #Tv  | Bed         | Bath_room | AC  | Wifi | Price
                    x = PrettyTable()
                    # x.field_names=["TV Faculty","Bed Faculty","Wash Room Faculty ","AC Faculty","WiFi Faculty","Room Price "]
                    x.field_names =["TV Faculty","Bed Faculty","Wash Room Faculty","AC Faculty","WiFi Faculty","Room Price"]
                    x.add_row(Delux_info)
                    print(x)
            
                elif(room_view =="3"):
                    print(f"\n----------- These all Faculty We Are Provide in the Hotel If You Want Then login  Now  Time is  {s}  ------------\n")
                    Standard_info= App.View_Standard_Unauth()
                    #Tv  | Bed             | Bath_room | AC  | Price 
                    x = PrettyTable()
                    x.field_names=["TV Faculty","Bed Faculty","Wash Room Faculty","AC Faculty","Room Price"]
                    x.add_row(Standard_info)
                    print(x)
                    
                # Pending data because data is not fetched by non auth or admin or with user plz check 
                elif(room_view =="4"):
                    print(f"\n----------- These all Faculty We Are Provide in the Hotel If You Want Then login  Now  Time is  {s}  ------------\n")
                    Quad_info= App.View_Quad_Unauth()
                     # Tv  | Bed         | Bath_room | Fan | Price 
                    x = PrettyTable()
                    x.field_names=["TV Faculty","Bed Faculty","Wash Room Faculty","Fan Faculty","Room Price"]
                    x.add_row(Quad_info)
                    print(x)
                
                elif(room_view =="5"):
                    print("\n-----------Exit  View Section ------------\n")
                    break

                else:
                    print("\n------------Invalid View Section\n")


    elif ch == "4":
        print("\n********** Thank-You,Visit Again *************\n")
        break
    
    else:
        print("--------------------------- Invalid SyntaX--------------------------------")
                     