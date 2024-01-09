# installed library mysql-connector-python
import mysql.connector

#creating connection 
import mysql.connector

class read:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "123yaseen",
                database = "banks"
                )
    
    def specific_info(self,customer_id,table_name):
        cur = self.conn.cursor()
        if table_name=='personal_details' or table_name=='bank_details':
            cur.execute(f"SELECT * FROM {table_name} WHERE CUSTOMERID={customer_id}")
            print(cur.fetchall())