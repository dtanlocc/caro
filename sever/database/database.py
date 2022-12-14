import mysql.connector

class Database:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(host='localhost', user = 'root', password='',database = 'caro')
        self.cur = self.mydb.cursor()

    def signin(self,user,pas): #sign thanh cong -> return true, nguoc lai return false
        try:
            syntax = "INSERT INTO account (username,password) VALUES (%s,%s)"
            value = (user,pas)
            self.cur.execute(syntax,value)
            self.mydb.commit()
            return True
        except:
            return False

    def login(self,user,pas): # login thanh cong -> return true, nguoc lai return false
        try:
            syntax = "SELECT password FROM account WHERE username=%s"
            value = (user,)
            self.cur.execute(syntax,value)
            
            self.password = self.cur.fetchone()
            
            if pas == self.password[0]:
                return True
            return False
        except:
            return False
            