import mysql.connector as db
import re
import os
import time
from multipledispatch import dispatch



class Admin:
    #create database ...............
    def __init__(self):
        #create directory to store files
        try:
            os.mkdir("AllFiles")
        except:
            pass
        mydb = db.connect(host='localhost',user='root',port='3306',passwd='root')
        query = '''create database if not exists HotelDB;'''
        cur = mydb.cursor()
        cur.execute(query)
        mydb.close()


    #create table for admin...............
        self.connection()
        query = '''create table if not exists Admin_ritesh11(a_id int primary key unique , a_username varchar(50),a_password varchar(50));'''
        self.cur.execute(query)
        self.mydb.close()

    
        #Admin Default Data
        self.a_id = 1
        self.a_username = 'admin'
        self.a_password = 'admin'
        self.Add_AdminValue(self.a_id,self.a_username,self.a_password)
    
    #This is is used to connect Python to Mysql in HotelDB as database name
    def connection(self):
        self.mydb = db.connect(host='localhost',user='root',port='3306',passwd='root',database='HotelDB')
        self.cur = self.mydb.cursor()

    #This method is used to add default admin data ................
    def Add_AdminValue(self,a_id,a_username,a_password):
        self.connection()
        try:
            data = (a_id,a_username,a_password)
            query = '''insert into Admin_ritesh11(a_id,a_username,a_password) values (%s,%s,%s);'''
            self.cur.execute(query,data)
            self.cur.execute("commit;")
            self.mydb.close()

        except:
            pass
       

    
    def AdminLogIn(self,a_username,a_password):
        self.connection()
        data = (a_username,)
        query =''' select a_username,a_password from Admin_ritesh11 where a_username = %s;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

  

    def CheckInfo(self , c_contact = None, c_email = None):
        self.connection()

        data = (c_contact , c_email)

        query = '''select contact , email from user where contact = %s or email = %s;'''

        self.cur.execute(query , data)
        
        record = self.cur.fetchone()

        # print(record)

        self.mydb.close()

        if record == None:
            return True

        elif record[0] == c_contact:
            return "Contact Already Exists"

        elif record[1] == c_email:
            return "\n**********Email Already Exists***********\n"

    def View_CustomerInfo(self):
        self.connection()
        query = '''select * from user;'''
        self.cur.execute(query)
        record = self.cur.fetchall()
        self.mydb.close()
        return record


    def Delete_customer_Info(self,delete_cust_id):
        self.connection()
        data = (delete_cust_id,)
        query ='''delete from user  where cid = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True




    

class Hotel(Admin):
    def __init__(self):
        super().__init__()
#--------------------------------------------------------------------------------------#
         # Created Luxury room type 
        # self.connection()
        # query = '''
        #     create table if not exists Luxury(
        #         Room_id int primary key auto_increment ,
        #         customer_name varchar (50) not null,
        #         Tv varchar (50) not null default "Yes",
        #         Bed varchar(50) not null default "Three Bed  & Two Sofa ",
        #         Iron varchar(50) not null default "Yes",
        #         Bath_room varchar(50) not null default "Separate",
        #         AC varchar(50) not null default "Yes",
        #         Wifi varchar(50) not null default "Yes",
        #         Price bigint not null default "7000",
        #         Check_in date ,
        #         Check_out date  );'''
        # self.cur.execute(query)
        # self.mydb.close()



        self.connection()
        query = '''
            create table if not exists Luxury(
                Room_id int primary key auto_increment ,
                customer_name varchar (50) not null,
                Tv varchar (50) not null default "Yes",
                Bed varchar(50) not null default "Three Bed  & Two Sofa ",
                Iron varchar(50) not null default "Yes",
                Bath_room varchar(50) not null default "Separate",
                AC varchar(50) not null default "Yes",
                Wifi varchar(50) not null default "Yes",
                Price bigint not null default "7000",
                hmd varchar(59) not null  );'''
        self.cur.execute(query)
        self.mydb.close()
#--------------------------------------------------------------------------------------#
        # Created delux room type 
        self.connection()
        query = '''
                create table if not exists delux(
                Room_id int primary key auto_increment ,
                customer_name varchar (50) not null,
                Tv varchar (50) not null default "Yes",
                Bed varchar(50) not null default "Double Bed ",
                Bath_room varchar(50) not null default "Standard",
                AC varchar(50) not null default "Yes",
                Wifi varchar(50) not null default "Yes",
                Price bigint not null  default "4000",
                hmd varchar(59) not null  );'''
                
                
        
        self.cur.execute(query)
        self.mydb.close()
        
#--------------------------------------------------------------------------------------#
         # Created Standard room type 

            
        self.connection()
        query = '''
            create table if not exists Standard(
                Room_id int primary key auto_increment ,
                customer_name varchar (50) not null,
                Tv varchar (50) not null default "Yes",
                Bed varchar(50) not null default "Two Single Bed ",
                Bath_room varchar(50) not null default "Yes",
                AC varchar(50) not null default "Yes",
                Price bigint not null default "5000",
                hmd varchar(59) not null  );'''
                
        self.cur.execute(query)
        self.mydb.close()

#--------------------------------------------------------------------------------------#
             # Created Quad room type 
    
        self.connection()
        query = '''
            create table if not exists Quad(
                Room_id int primary key auto_increment ,
                customer_name varchar (50) not null,
                Tv varchar (50) not null default "Yes",
                Bed varchar(50) not null default "Single Bed ",
                Bath_room varchar(50) not null default "Yes",
                Fan varchar(50) not null default "Yes",
                Price bigint not null default "2000",
                hmd varchar(59) not null  );'''
                
        self.cur.execute(query)
        self.mydb.close()

#--------------------------------------------------------------------------------------#
# this is booking section 

    def Room_Book_Luxury(self,customer_name,hmd):
        self.connection()
        data = (customer_name,hmd)
        query = '''insert into Luxury(customer_name,hmd) values (%s,%s);'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True

    def Room_Book_Delux(self,customer_name,hmd):
        self.connection()
        data = (customer_name,hmd)
        query = '''insert into Delux(customer_name,Check_in,Check_out) values (%s,%s);'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True

    def Room_Book_Standard(self,customer_name,hmd):
        self.connection()
        data = (customer_name,hmd)
        query = '''insert into Standard(customer_name,Check_in,Check_out) values (%s,%s);'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True

    def Room_Book_Quad(self,customer_name,hmd):
        self.connection()
        data = (customer_name,hmd)
        query = '''insert into Quad(customer_name,Check_in,Check_out) values (%s,%s);'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True

    
# this is room view function code      

    def View_Luxury_Room(self):
        self.connection()
        query = '''select * from luxury;'''
        self.cur.execute(query)
        record = self.cur.fetchall()
        self.mydb.close()
        return record

    def View_Delux_Room(self):
        self.connection()
        query = '''select * from Delux;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        self.mydb.close()
        return record

    def View_Standard_Room(self):
        self.connection()
        query = '''select * from Standard;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        self.mydb.close()
        return record

    def View_Quad_Room(self):
        self.connection()
        query = '''select * from Quad;'''
        self.cur.execute(query)
        record = self.cur.fetchall()
        self.mydb.close()
        return record

    # this is update section 
    
    def Update_Luxury_Info(self,update_check_in,update_check_out,update_luxury_id):
        self.connection()
        data = (update_check_in,update_check_out,update_luxury_id)
        query = '''update Luxury set check_in= %s, check_out = %s where Room_id = %s'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()

    def Update_Delux_Info(self,update_check_in,update_check_out,update_Delux_id):
        self.connection()
        data = (update_check_in,update_check_out,update_Delux_id)
        query = '''update Delux set check_in= %s, check_out = %s where Room_id = %s'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
    
    def Update_Standard_Info(self,update_check_in,update_check_out,update_Standard_id):
        self.connection()
        data = (update_check_in,update_check_out,update_Standard_id)
        query = '''update Standard set check_in= %s, check_out = %s where Room_id = %s'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()

    def Update_Quad_Info(self,update_check_in,update_check_out,update_Quad_id):
        self.connection()
        data = (update_check_in,update_check_out,update_Quad_id)
        query = '''update Quad set check_in= %s, check_out = %s where Room_id = %s'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()


    # this is view section for unautrized user those who have not account view here details
    def View_Luxury_Unauth(self):
            self.connection()
            query = '''select Tv,Bed,Iron,Bath_room,Ac,Wifi,Price from luxury;'''
            self.cur.execute(query,)
            record = self.cur.fetchone()
            self.mydb.close()
            return record
    
    def View_Delux_Unauth(self):
        self.connection()
        # query = '''select Tv,Bed,Bath_room,Ac,Wifi,Price from delux;'''
        query = ''' select Tv,Bed,Bath_room,Ac,Wifi,Price from delux; '''
        self.cur.execute(query,)
        record = self.cur.fetchone()
        self.mydb.close()
        return record
        # print(record)
    
    def View_Standard_Unauth(self):
        self.connection()
        query = '''select Tv,Bed,Bath_room,Ac,Price from standard;'''
        self.cur.execute(query,)
        record = self.cur.fetchone()
        self.mydb.close()
        return record
    
    def View_Quad_Unauth(self):
        self.connection()
        # Tv  | Bed         | Bath_room | Fan | Price 
        query = '''select Tv,Bed,Bath_room,Fan,Price from Quad;'''
        self.cur.execute(query,)
        record = self.cur.fetchone()
        self.mydb.close()
        return record
        

    def Delete_Luxury_Info(self,delete_luxury_id):
        self.connection()
        data = (delete_luxury_id,)
        query ='''delete from luxury  where Room_id = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True


    def Delete_Delux_Info(self,delete_luxury_id):
        self.connection()
        data = (delete_luxury_id,)
        query ='''delete from delux  where Room_id = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True

    def Delete_Standard_Info(self,delete_luxury_id):
        self.connection()
        data = (delete_luxury_id,)
        query ='''delete from standard  where Room_id = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True
    
    def Delete_Quad_Info(self,delete_luxury_id):
        self.connection()
        data = (delete_luxury_id,)
        query ='''delete from Quad  where Room_id = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True
    
#................................................................
#   here Top Admin Section ALl Done .......................

class User(Hotel):
    
    def __init__(self):
        super().__init__()
    
        #create table user
        self.connection()
        query = '''
            create table if not exists user(cid int primary key auto_increment ,
            cname varchar(50) not null,
            contact varchar(20) not null unique , 
            email varchar(100) not null unique,
            address text not null,
            register_date  varchar(80) not null,
            passwd  varchar (90) not null );
        '''
        self.cur.execute(query)
        self.mydb.close()



    def cus_Detail (self, c_name , c_contact , c_email , address  ,register_date,passwd):

        self.connection()
        try:
            os.mkdir("UserAccount")
        except:
            pass

        query = '''insert into user(cname , contact , email , address ,register_date,passwd) values ( %s , %s ,%s ,%s ,%s ,%s);'''

        data = (c_name , c_contact , c_email , address  ,register_date,passwd)
        self.cur.execute(query , data)
        self.cur.execute("commit;")

        self.mydb.close()

        return True



   
    def UserLogin(self,email,passwd):
        self.connection()
        data = (email,passwd)
        query = '''select email from user where email = %s && passwd = %s;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        # print(record)
        return record
    
  

    def Customer_Info(self,email):
        self.connection()
        data = (email,)
        query = '''select * from user where email = %s'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

     
    @dispatch(str , int)
    def Update(self , new_contact, cust_id):
        self.connection()

        data = (new_contact , cust_id)
        query = '''update user set contact = %s where cid= %s;'''

        self.cur.execute(query , data)
        self.cur.execute("commit;")
        self.mydb.close()

      
    @dispatch(str ,str, int)
    def Update(self ,new_address , new_passwd,cust_id):
        self.connection()

        data = (new_address , new_passwd,cust_id)
        query = '''update user set address = %s, passwd = %s where cid= %s;'''

        self.cur.execute(query , data)
        self.cur.execute("commit;")
        self.mydb.close()







    
    # @dispatch(str , str)
    # def UpdateUserDetails(self , new_name , email):
    #     self.connection()

    #     data = (new_name , email)
    #     query = '''update user set cname = %s where email = %s;'''

    #     self.cur.execute(query , data)
    #     self.cur.execute("commit;")
    #     self.mydb.close()

    @dispatch(str , str , str)
    def UpdateUserDetails(self , new_name , new_address , email):
        self.connection()

        data = (new_name ,new_address , email)
        query = '''update user set cname = %s , address = %s where email = %s;'''

        self.cur.execute(query , data)
        self.cur.execute("commit;")
        self.mydb.close()
   
    
    def check_room(self,rch):
        self.connection()
        data = (rch,)
        query = ''' select Room_id from room where Room_id = %s;'''
        self.cur.execute(query , data)
        id=self.cur.fetchone()
        self.mydb.close()
        # print(id)
        return id

    def fetch_r_N(self,c_email):
        self.connection()
        data = (c_email,)
        query = ''' select cname from user where email = %s;'''
        self.cur.execute(query,data)
        r_name=self.cur.fetchone()
        self.mydb.close()
        return r_name

    def fetch_r_price(self):
        self.connection()
        
        query = ''' select Price from Luxury;'''
        self.cur.execute(query)
        r_price=self.cur.fetchone()
        self.mydb.close()
        x=list(r_price)
        ls=[int(i) for i in x]
        a=ls[0]
        return a

    def fetch_u_n(self,c_email):
        self.connection()
        data = (c_email,)
        query = ''' select cname  from User where email = %s;'''
        self.cur.execute(query,data)
        u_name=self.cur.fetchone()
        self.mydb.close()
        return u_name

        
   

        





class Regx(User):
    def __init__(self):
        super().__init__()

    def NameValidation(self,c_name):
        p = "^[a-zA-Z\ ]+$"
        if re.match(p,c_name):
            return True

        else:
            return False

    def ContactValidation(self,c_contact):
        p = "^[6-9]\d{9}"
        if re.match(p,c_contact):
            return True

        else:
            return False



    def EmailValidation(self,c_email):
        p = "^[a-zA-Z0-9\_\.]+@[a-z]+\.[a-z]+$"
        if re.match(p,c_email):
            return True

        else:
            return False
    

   