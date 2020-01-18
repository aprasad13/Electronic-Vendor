# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:04:33 2019

@author: 13129
"""
import sqlite3
from sqlite3 import Error
import datetime
from random import randrange
 


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn

conn = create_connection(r"/Users/amanprasad/Desktop/Vaibhav/pythonsqlite_2.db")

def create_cursor(conn):
   try:
       cursor = conn.cursor()
   except Error as e:
       print(e)
   return cursor  



def totalcategory(conn):
    conn.row_factory = lambda cursor, row: row[0]
    c = create_cursor(conn)
    ids = c.execute('Select distinct category from Item').fetchall()
    return ids
        
def totalbrand(conn):      
    conn.row_factory = lambda cursor, row: row[0]
    c = create_cursor(conn)
    ids = c.execute('Select distinct brand from Item').fetchall()
    return ids 

def totalcolour(conn):
    conn.row_factory = lambda cursor, row: row[0]
    c = create_cursor(conn)
    ids = c.execute('Select distinct colour from Item').fetchall()
    return ids 

def totalmanufacturer(conn):
    conn.row_factory = lambda cursor, row: row[0]
    c = create_cursor(conn)
    ids = c.execute('Select distinct name from Manufacturer').fetchall()
    return ids 
temp = totalmanufacturer(conn)
print(temp)

def get_item(cat):
    conn.row_factory = lambda cursor, row: row[0:7]
    c = create_cursor(conn)
    sql=("SELECT Item.itemid, Item.name,category,brand,colour,Manufacturer.name,unitprice FROM Item left join Manufacturer on Item.manid=Manufacturer.manid where category = ? ")
    ids= c.execute(sql,(cat,)).fetchall()
    return ids

def get_item_id(cat):
    conn.row_factory = lambda cursor, row: row[0:7]
    c = create_cursor(conn)
    sql=("SELECT * FROM Item left join Manufacturer on Item.manid=Manufacturer.manid where category = ? ")
    ids= c.execute(sql,(cat,)).fetchall()
    return ids

def itemselect(cat,brand,colour,manu):
    conn.row_factory = lambda cursor, row: row[0:7]
    c = create_cursor(conn)
    sql=("SELECT Item.itemid, Item.name,category,brand,colour,Manufacturer.name,unitprice FROM Item left join Manufacturer on Item.manid=Manufacturer.manid where category = ? and brand = ? and colour = ? and Manufacturer.name = ?")
    ids= c.execute(sql,(cat,brand,colour,manu)).fetchall()
    return ids 
    

def cardcredit(cardno):
    conn.row_factory = lambda cursor, row: row[0]
    c = create_cursor(conn)
    sql = ('Select credit from cardcredit where cardno = ?')
    ids= c.execute(sql,(cardno,)).fetchone()
    return ids

def get_card_details():
    pass

def insert_order (totalcost,type_order,ad1,ad2,city,state,zipcode,paymenttype,cardno):
    c= create_cursor(conn)
    date_time =datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    sql=('insert into ordertable (datetime ,totalcost,type ,AdressLine1 ,AddressLine2 ,city ,state ,zipcode ,paymenttype ,cardno ) values(?,?,?,?,?,?,?,?,?,?)')
    c.execute(sql,(date_time,totalcost,type_order,ad1,ad2,city,state,zipcode,paymenttype,cardno))
    conn.commit()


def getmaxstoreorderid():
    conn.row_factory = lambda cursor, row: row[0]
    c = create_cursor(conn)
    ids = c.execute("Select max(orid) from ordertable where type='store'").fetchall()
    return ids

def getmaxonlineorderid():
    conn.row_factory = lambda cursor, row: row[0]
    c = create_cursor(conn)
    ids = c.execute("Select max(orid) from ordertable where type='online'").fetchall()
    return ids  
 
maxorder = getmaxstoreorderid()
print(maxorder) 

def insertonlinetransaction(itemid,quantity):
     c= create_cursor(conn)
     max_id = getmaxonlineorderid()[0]
     sql = 'insert into onlinetransaction values(1,?,?,?)'
     c.execute(sql,(itemid,max_id,quantity))
     conn.commit()
  
def insertofflinetransaction(storeid,itemid,quantity):
    c= create_cursor(conn)
    max_id = getmaxstoreorderid()[0]
    sql = 'insert into onlinetransaction values(?,?,?,?)'
    c.execute(sql,(itemid,max_id,quantity))
    conn.commit()
    
def insert_shipment(customerid):
    c= create_cursor(conn)
    max_id = getmaxonlineorderid()[0]
    ship_id = randrange(6)
    sql = 'insert into shipment values(?,?,?)'
    c.execute(sql,(customerid,max_id,ship_id))
    conn.commit()      

def orderview(customerid):
     conn.row_factory = lambda cursor, row: row[0:11]
     c= create_cursor(conn)
     sql = ('Select ordertable.orid,datetime,totalcost,type ,AdressLine1 ,AddressLine2 ,city ,state ,zipcode ,paymenttype ,cardno  from shipment inner join ordertable on shipment.orid=ordertable.orid where cid = ?')
     ids= c.execute(sql,(customerid,)).fetchall()
     return ids 

def thismonthcost(cid):
     conn.row_factory = lambda cursor, row: row[0]
     c= create_cursor(conn)
     month= datetime.datetime.now().month
     date_check = "%-" + str('%02d' % month) +"-%"
     sql = ("select sum(totalcost) from ordertable inner join shipment on ordertable.orid = shipment.orid where shipment.cid= ? and ordertable.datetime like ? and where type= 'credit' group by shipment.cid ")
     ids= c.execute(sql,(cid,date_check)).fetchall()
     return ids 
def insertcustomer(name,AdressLine1,AddressLine2,city,State,zipcode,phoneno,emailid,password,accno):
    c= create_cursor(conn)
    sql = 'insert into Customer (name,AdressLine1,AddressLine2,city,State,zipcode,phoneno,emailid,password,accno) values(?,?,?,?,?,?,?,?,?,?); '
    #print(name,AdressLine1,AddressLine2,city,State,zipcode,phoneno,emailid,password,accno)
    c.execute(sql,(name,AdressLine1,AddressLine2,city,State,zipcode,phoneno,emailid,password,accno))
    conn.commit()
def updatecustomer(cid,name,AdressLine1,AddressLine2,city,State,zipcode,phoneno,emailid,password,accno):
    c= create_cursor(conn)
    sql = 'Update customer  set name= ? , AdressLine1 = ? ,  AddressLine2 = ? ,  city = ?,  State  = ? ,  zipcode = ? ,  phoneno = ? ,  emailid = ? ,  password = ?,accno=? where cid = ?'
    c.execute(sql,(name,AdressLine1,AddressLine2,city,State,zipcode,phoneno,emailid,password,accno,cid))
    conn.commit()
def storeinvent():
    conn.row_factory = lambda cursor, row: row[0:3]
    c = create_cursor(conn)
    sql = ('Select storeid,Item.name,quantity from Item  join storeinventory on storeinventory.itemid = Item.itemid ')
    ids= c.execute(sql).fetchall()
    return ids
def warehouseinvent():
    conn.row_factory = lambda cursor, row: row[0:3]
    c = create_cursor(conn)
    sql = ('Select Item.name,quantity from Item  join warehouseinventory on warehouseinventory.itemid = Item.itemid where wid=1')
    ids= c.execute(sql).fetchall()
    return ids

def get_cid(user_name, password):
    conn.row_factory = lambda cursor, row: row[0]
    c = create_cursor(conn)
    sql =('Select cid from customer where emailid = ? and password = ?')
    ids = c.execute(sql,(user_name,password)).fetchall()
    return ids

def orderviewonline(customerid):
     conn.row_factory = lambda cursor, row: row[0:13]
     c= create_cursor(conn)
     sql = ('Select  distinct name,quantity,ordertable.orid,ordertable.datetime,totalcost,type ,AdressLine1 ,AddressLine2 ,city ,state ,zipcode ,paymenttype ,cardno  from shipment inner join ordertable on shipment.orid=ordertable.orid  inner join onlinetransaction on ordertable.orid=onlinetransaction.orid inner join Item on Item.itemid = onlinetransaction.itemid where cid = ?')
     ids= c.execute(sql,(customerid,)).fetchall()
     return ids

def orderviewoffline(customerid):
     conn.row_factory = lambda cursor, row: row[0:13]
     c= create_cursor(conn)
     sql = ('Select  distinct name,quantity,ordertable.orid,ordertable.datetime,totalcost,type ,AdressLine1 ,AddressLine2 ,city ,state ,zipcode ,paymenttype ,cardno  from shipment inner join ordertable on shipment.orid=ordertable.orid  inner join offlinetransaction on ordertable.orid=offlinetransaction.orid inner join Item on Item.itemid = offlinetransaction.itemid where cid = ?')
     ids= c.execute(sql,(customerid,)).fetchall()
     return ids   
def orderviewtable(cid):
    list_new = orderviewonline(cid)+(orderviewoffline(cid))
    return list_new
    