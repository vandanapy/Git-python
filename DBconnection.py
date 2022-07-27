# Create a common function to get database connection
import mysql.connector
def customer_db_details():
    con=mysql.connector.connect(user='root',password='Nix@123root',host='localhost',database='python_community',port=3306)
    return con