
import pymysql
from pymysql.cursors import Cursor


class AccessData(object):
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root",password="admin123",database="cdap",charset="utf8");
        self.cursor = self.conn.cursor()
    
        
    def addUser(self,userid,uname,upassword,ustatus):
        i_sql = "insert into user(userid,uname,upassword,ustatus) values ('"+userid+"','"+uname+"','"+upassword+"','"+ustatus+"')"
        print(i_sql)
        self.cursor.execute(i_sql)
        self.conn.commit()


    def updateUserById(self,userid,uname,upassword,ustatus):
        u_sql = "update user set uname="+"'"+uname+"'"+","+"upassword="+"'"+upassword+"'"+","+"ustatus="+"'"+ustatus+"'" +"where userid="+"'"+userid+"'"       
        print(u_sql)
        self.cursor.execute(u_sql)
        self.conn.commit()
    
    def updateUserByName(self,uname,newpass):
        u_sql=f"update user set upassword = '{newpass}' where uname = '{uname}'"
        print(u_sql)
        self.cursor.execute(u_sql)
        self.conn.commit()
        
    def deleteUserByName(self,uname):
        d_sql = "update user set ustatus="+"'"+"frozen"+"'" +" where uname="+"'"+uname+"'"
        print(d_sql)
        self.cursor.execute(d_sql)
        self.conn.commit()
    def queryUserByName(self,uname):
        q_sql = "select * from user where uname = "+"'"+uname+"'"
        print(q_sql)
        self.cursor.execute(q_sql)
        data = self.cursor.fetchall()
        return data
    def queryUser(self):
        q_sql="select * from user where ustatus != 'manager'"
        print(q_sql)
        self.cursor.execute(q_sql)
        data = self.cursor.fetchall()
        return data
    
    



    def addCar(self,cID,cName,cType,cPrice=1.0,cFuel=1.0,cSpace=1.0,cPower=1.0,cControl=1.0,cComfort=1.0,cExterior=1.0,cInterior=1.0,cCostPerformance=1.0,cImage="null"):
        a_sql = "INSERT INTO car(cID,cName,cType,cPrice,cFuel,cSpace,cPower,cControl,cComfort,cExterior,cInterior,cCostPerformance,cImage) VALUES ('"+cID+"','"+cName+"','"+cType+"',"+str(cPrice)+","+str(cFuel)+","+str(cSpace)+","+str(cPower)+","+str(cControl)+","+str(cComfort)+","+str(cExterior)+","+str(cInterior)+","+str(cCostPerformance)+",'"+cImage+"')"
        print(a_sql)
        self.cursor.execute(a_sql)
        self.conn.commit()
    
    def queryCarByName(self,cName):
        q_sql = "select * from car where cName = '"+cName+"'"
        print(q_sql)
        self.cursor.execute(q_sql)
        data = self.cursor.fetchall()
        print(data)
        return data

    def queryCarByID(self,cID):
        q_sql = "select * from car where cID = "+str(cID)
        print(q_sql)
        self.cursor.execute(q_sql)
        data = self.cursor.fetchall()
        print(data)
        return data
    
    def queryCar(self):
        q_sql="select * from car"
        self.cursor.execute(q_sql)
        data = self.cursor.fetchall()
        return data

    
    def addNeaten(self,dnID,userID,dnTime,dnNote,dnPath):
        a_sql="INSERT INTO neaten(dnID,userID,dnTime,dnNote,dnPath) VALUES("+"'"+dnID+"','"+userID+"','"+dnTime+"','"+dnNote+"','"+dnPath+"')"
        print(a_sql)
        self.cursor.execute(a_sql)
        self.conn.commit()

    def qureyNeaten(self):
        q_sql="select * from neaten"
        self.cursor.execute(q_sql)
        data = self.cursor.fetchall()
        print(data)
        return data

    #未测试
    def addPurpose(self,purpose={}):
        a_sql="INSERT INTO purpose(cID,commute,shopping,pickup,tour,longway,business,crosscountry,bdate,racing,pullon,hailing,motorcade,modifyc) VALUES("+purpose["cID"]+","+purpose["commute"]+","+purpose["shopping"]+","+purpose["pickup"]+","+purpose["tour"]+","+purpose["longway"]+","+purpose["business"]+","+purpose["crosscountry"]+","+purpose["bdate"]+","+purpose["racing"]+","+purpose["pullon"]+","+purpose["hailing"]+","+purpose["motorcade"]+","+purpose["modifyc"]+")"
        self.cursor.execute(a_sql)
        self.conn.commit()
    
    def queryPurpose(self,cID):
        q_sql="select * from purpose where cID ="+"'"+cID+"'"
        self.cursor.execute(q_sql)
        data = self.cursor.fetchall()
        print(data)
        return data
    

    def querySale_year(self,cID):
        q_sql="select * from sale_year where cID ="+"'"+cID+"'"
        self.cursor.execute(q_sql)
        data = self.cursor.fetchall()
        print(data)
        return data


    




