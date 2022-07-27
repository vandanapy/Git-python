# Update customer pincode for all the customers whose address is ongole
import mysql.connector
from DBconnection import *
try:
    con=customer_db_details()
    cursor=con.cursor()
    query_string=("update tbl_customer_info SET pincode=563101 where Address='kolar';")
    cursor.execute(query_string)
    con.commit()
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem in sql:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()