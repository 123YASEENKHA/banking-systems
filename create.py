import mysql.connector

class insert:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "123yaseen",
                database = "banks"
                )
        
    def personal_details(self,cid,fname,lname,addr,pn,an,pan):
        cur = self.conn.cursor() # creating cursor
        cur.execute(f"INSERT INTO PERSONAL_DETAILS VALUES({cid},'{fname}','{lname}','{addr}',{pn},'{an}','{pan}')")
        self.conn.commit()
        print("-----------------personal information has been saved sucessful:------------------")
    def bank_details(self,acn,cid,ifsc,actype):
        cur=self.conn.cursor()
        cur.execute(f"insert into bank_details values({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print('-------------------bank details has been sucessful saved-------------------')
    def transaction_details(self,tid,sacct,racct,amt,method):
        cur=self.conn.cursor()
        cur.execute(f"insert into transaction_details values({tid},{sacct},{racct},{amt},'{method}')")
        self.conn.commit()
        print("-----------transaction detils has been sucessfullly saved------------")
    def account_details(self,actno,tid,amt,csbal,ttype):
        cur=self.conn.cursor()
        cur.execute(f"insert into account_details values({actno},{tid},{amt},{csbal},'{ttype}')")
        self.conn.commit()
        print("-------------account details has been sucessfully saved------")
