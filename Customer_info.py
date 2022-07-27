# Create a program to create customers table with all fields from python code and insert 4 records
import mysql.connector
from DBconnection import *
try:
    con=customer_db_details()
    cursor = con.cursor()
    create_query_string = ("create table tbl_customer_info(Customer_ID int primary key,First_Name varchar(100),Last_Name varchar(100),Mobile_Number decimal(15,0),Address varchar(200),pincode int);")
    cursor.execute(create_query_string)
    query_string = "insert into tbl_customer_info(Customer_ID,First_Name,Last_Name,Mobile_Number,Address,pincode) values (%s,%s,%s,%s,%s,%s)"
    values = [('1234', 'VAndana', 'M', '1234567890', 'ongole',523003),
              ('2345', 'Manju', 'B M', '2087654321', 'Kolar',500037),
              ('4567', 'Devansh', 'Gowda', '38632980', 'banglore',600018),
              ('8907', 'Monika', 'N', '490764321', 'kolar',520001)]
    cursor.executemany(query_string, values)
    con.commit()
    print("Inserted successfully")
except Exception as e:
    if con:
        con.rollback()
        print('problem with sql', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()