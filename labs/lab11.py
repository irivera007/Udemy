import mysql.connector
class DAO():
    def __init__(self):
        self.connect()
        return
    def connect(self):
        try:
            self.dao=mysql.connector.connect(**config)
        except:
            print"Error while connecting"
        return self.dao.cursor()
    
    def query(self,query):
        self.quer=query
        conn=self.connect()
        conn.execute(query)
        row=conn.fetchall()
        print row
        conn.close()
    
statement= ("Select * From Writers;" 
                    )

config={
            'user':'adm1n',
            'password':'Welcome@dm1n',
            'host':'localhost',
            'database':'users',
            
            }
db=DAO()
db.query(statement)