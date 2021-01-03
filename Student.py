import mysql.connector
from prettytable import PrettyTable
import os
import time

class Student:
    def __init__(self):
        pass

    def sHeader(self):
        print("\n\n\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|****   MAHAKAL  INSTITUTE  OF  TECHNOLOGY   ****|")
        print("\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|*********    --->     Home     <---    *********|")
        print("\t\t\t\t\t\t\t|************************************************|")
        print("\n\n\t\t\t\t1. Insert Data")
        print("\n\t\t\t\t2. Search Data")
        print("\n\t\t\t\t3. Update Data")
        print("\n\t\t\t\t4. Delete Data")
        print("\n\t\t\t\t5. Back")
        n=int(input("\n\n\t\t\t\t Enter your Choice : "))
        if n==1:
            self.insertData()
        elif n==2:
            self.searchData()
        elif n==3:
            self.updateData()
        elif n==4:
            self.deleteData()
        elif n==5:
            exit(0)
        else:
            print("\n\n\t\t\t\t ************** INVALID CHOICE **************\n\n")
            time.sleep(3)
            self.sHeader()
        
        

    def insertData(self):
        os.system('cls')
        print("\n\n\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|****   MAHAKAL  INSTITUTE  OF  TECHNOLOGY   ****|")
        print("\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|*****   --->  Store Student details  <---  *****|")
        print("\t\t\t\t\t\t\t|************************************************|")
        print("\n\n\t\t\t\t1.Store Single Student data")
        print("\n\t\t\t\t2.Store Multiple Student data")
        n=int(input("\n\n\t\t\t\t Enter your Choice : "))
        if n==1:
            no=1
        elif n==2:
            no=int(input("\n\n\t\t\t\t Enter total numbers of Students : "))
        else:
            print("\n\n\t\t\t\t ************** INVALID CHOICE **************\n\n")
            time.sleep(3)
            self.insertData()
        for i in range(1,no+1):
            data=[]
            os.system('cls')
            print("\n\n\t\t\t\t\t\t\t|************************************************|")
            print("\t\t\t\t\t\t\t|****   MAHAKAL  INSTITUTE  OF  TECHNOLOGY   ****|")
            print("\t\t\t\t\t\t\t|************************************************|")
            print("\t\t\t\t\t\t\t|*****   --->  Store Student details  <---  *****|")
            print("\t\t\t\t\t\t\t|************************************************|")
            print("\n\n\t\t\t\t Enter the information of",i,"Student :-")
            data.append(input("\n\t\t\t\t Enter student name :"))
            data.append(input("\n\t\t\t\t Enter Enrollement Number :"))
            data.append(input("\n\t\t\t\t Enter Father Name :"))
            data.append(input("\n\t\t\t\t Enter Mother Name :"))
            data.append(input("\n\t\t\t\t Enter Addhar Number  :"))
            data.append(input("\n\t\t\t\t Enter Full Address :"))
            data.append(int(input("\n\t\t\t\t Enter Age :")))
            data.append(input("\n\t\t\t\t Enter Mobile Number :"))
            data.append(int(input("\n\t\t\t\t Enter total marks of 10th class :")))
            data.append(int(input("\n\t\t\t\t Enter total marks of 12th class :")))
            print("\n\n\n\t\t\t ! PLEASE CHECKOUT ALL ABOVE ENTERED INORMATION.....\n\n")
            print("\t\t\t ! IF BY MISTAKE YOU ENTERED ANY THING WRONG INFORMATION, THEN USE 'UPDATE' OPTION TO CORRECT IT.....\n\n")
            
            os.system('pause')
            try:
                con=mysql.connector.connect(host='localhost',user='root',password='root1799@',database='college')
                cur=con.cursor()
                qry="insert into student(sname,enroll_no,sfname,smname,addh_no,adds,age,mob_no,ten_marks,twe_marks)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                data=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9])
                cur.execute(qry,data)
                con.commit()
                print("\n\t\t\t ******** Recorded Added Successfully..  ***********\n\n")
                time.sleep(1)    
            except Exception as er:
                print(er)
            finally:
                if (con.is_connected()):
                    cur.close()
                    con.close()
        os.system('pause')

    def searchData(self):
        os.system('cls')
        print("\n\n\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|****   MAHAKAL  INSTITUTE  OF  TECHNOLOGY   ****|")
        print("\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|*******     --->  Search details  <---   *******|")
        print("\t\t\t\t\t\t\t|************************************************|")
        
        try:
            print("\n\n\t\t\t\t1.Search by Enrollement Number ")
            print("\n\t\t\t\t2.Search by Addhar number")
            print("\n\t\t\t\t3.Search by Father Name")
            print("\n\t\t\t\t4.Show All Data")
            n=int(input("\n\n\t\t\t\t Enter Your Choice :"))
            con=mysql.connector.connect(host='localhost',user='root',password='root1799@',database='college')
            cur=con.cursor()
            cur.execute("desc student")
            coln=[]
            for i in cur.fetchall():
                coln.append(i[0])
            
            if n==1:
                dt=input("\n\n\t\t\t\t Enter Enrollement Number :")
                qry="select * from student where enroll_no = %s"
                cur.execute(qry,(dt,))
            elif n==2:
                dt=input("\n\n\t\t\t\t Enter Addhar Number :")
                qry="select * from student where addh_no = %s"
                cur.execute(qry,(dt,))
            elif n==3:
                dt=input("\n\n\t\t\t\t Enter Father Name :")
                qry="select * from student where sfname = %s"
                cur.execute(qry,(dt,))
            elif n==4:
                qry="select * from student"
                cur.execute(qry)
            else:
                print("\n\t\t\t\t ! Invalid Choice...")
                time.sleep(3)
                self.searchData()
                
            t = PrettyTable(coln)
            rdt=cur.fetchall()
            if len(rdt)!=0:
                for i in rdt:
                    t.add_row(i)
                print(t)
                
            else:
                print("\n\n\t\t\t\t ! INVALID INPUT... DATA NOT FOUND !!!")
        except Exception as er:
            print(er)
        finally:
            if (con.is_connected()):
                cur.close()
                con.close()
        print("\n")
        os.system('pause')
            
    def updateData(self):
        os.system('cls')
        print("\n\n\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|****   MAHAKAL  INSTITUTE  OF  TECHNOLOGY   ****|")
        print("\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|*******     --->  Update details  <---   *******|")
        print("\t\t\t\t\t\t\t|************************************************|")
        
        try:
            en=input("\n\n\t\t\t\t Enter Student's Enrollement Number :")
            con=mysql.connector.connect(host='localhost',user='root',password='root1799@',database='college')
            cur=con.cursor()
            cur.execute("desc student")
            coln=[]
            for i in cur.fetchall():
                coln.append(i[0])
            t = PrettyTable(coln)
            qry="select * from student where enroll_no = %s"
            cur.execute(qry,(en,))
            rdt=cur.fetchall()
            if len(rdt)!=0:
                for i in rdt:
                    t.add_row(i)
                print("\n\n\t\t\t\t\t\t  ***************** Student's details *****************\n")
                print(t)
                print("\n\n\t\t\t\t1.Update Name \t\t\t\t\t\t 6.Update Age")
                print("\n\t\t\t\t2.Update Father Name \t\t\t\t\t 7.Update Mobile number")
                print("\n\t\t\t\t3.Update Mother Name \t\t\t\t\t 8.Update 10th Marks")
                print("\n\t\t\t\t4.Update Addhar Number \t\t\t\t\t 9.Update 12th Marks")
                print("\n\t\t\t\t5.Update Address ")
                ch=int(input("\n\t\t\t\t Enter your Choice :"))
                if ch==1:
                    updt=input("\n\n\t\t\t\t Enter Name for Updation :")
                    qry="update student set sname= %s where enroll_no = %s"
                elif ch==2:
                    updt=input("\n\n\t\t\t\t Enter Father Name for Updation :")
                    qry="update student set sfname= %s where enroll_no = %s"
                elif ch==3:
                    updt=input("\n\n\t\t\t\t Enter Mother Name for Updation :")
                    qry="update student set smname= %s where enroll_no = %s"
                elif ch==4:
                    updt=input("\n\n\t\t\t\t Enter Aadhar Number for Updation :")
                    qry="update student set addh_no= %s where enroll_no = %s"
                elif ch==5:
                    updt=input("\n\n\t\t\t\t Enter Address for Updation :")
                    qry="update student set adds= %s where enroll_no = %s"
                elif ch==6:
                    updt=input("\n\n\t\t\t\t Enter Age for Updation :")
                    qry="update student set age= %s where enroll_no = %s"
                elif ch==7:
                    updt=input("\n\n\t\t\t\t Enter Mobile Number for Updation :")
                    qry="update student set mob_no= %s where enroll_no = %s"
                elif ch==8:
                    updt=input("\n\n\t\t\t\t Enter 10th Marks for Updation :")
                    qry="update student set ten_marks= %s where enroll_no = %s"
                elif ch==9:
                    updt=input("\n\n\t\t\t\t Enter 12th Marks for Updation :")
                    qry="update student set twe_marks= %s where enroll_no = %s"
                upi=(updt,en)
                cur.execute(qry,upi)
                con.commit()
                print("\n\t\t\t\t ************ INFORMATION UPDATED SUCCESSFULLY.... ************")
                qry="select * from student where enroll_no = %s"
                t = PrettyTable(coln)
                cur.execute(qry,(en,))
                rdt=cur.fetchall()
                if len(rdt)!=0:
                    for i in rdt:
                        t.add_row(i)
                    print("\n\n\t\t\t\t\t\t  ***************** Student's details after Updation *****************\n")
                    print(t)
            else:
                print("\n\n\t\t\t\t ! INVALID INPUT... DATA NOT FOUND !!!")
        except Exception as er:
            print(er)
        finally:
            if (con.is_connected()):
                cur.close()
                con.close()
        print("\n")
        os.system('pause')

    def deleteData(self):
        os.system('cls')
        print("\n\n\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|****   MAHAKAL  INSTITUTE  OF  TECHNOLOGY   ****|")
        print("\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|*******     --->  Delete details  <---   *******|")
        print("\t\t\t\t\t\t\t|************************************************|")
        print("\n\n\t\t\t\t1.Delete Single Information")
        print("\n\t\t\t\t2.Delete Multiple Information")
        print("\n\t\t\t\t3.Delete All")
        n=int(input("\n\t\t\t\tEnter Your Choice :"))
        if n==1:
            en=input("\n\n\t\t\t\tEnter Enrollement number :")
            try:
                con=mysql.connector.connect(host='localhost',user='root',password='root1799@',database='college')
                cur=con.cursor()
                qry="delete from student where enroll_no = %s"
                cur.execute(qry,(en,))
                con.commit()
                print("\n\n\t\t\t ************* INFORMATION DELETED SUCCESSFULLY... *************")
            except Exception as e:
                print(e)
        
        elif n==2:
            n=int(input("\n\n\t\t\t\tEnter total numbers of Enrollement numbers to delete them :"))
            enl=[]
            for i in range(1,n+1):
                enl.append(input("\n\t\t\t\tEnter Enrollement number :"))
                
            try:
                con=mysql.connector.connect(host='localhost',user='root',password='root1799@',database='college')
                cur=con.cursor()
                for i in enl:
                    qry="delete from student where enroll_no = %s"
                    cur.execute(qry,(i,))
                    con.commit()
                print("\n\n\t\t\t ************* INFORMATION DELETED SUCCESSFULLY... *************")
            except Exception as e:
                print(e)
        
        elif n==3:
            inp=input("\n\t\t\t\tAre you sure to delete all information.(Y/N) :")
            if inp=='Y' or inp=='y':
                try:
                    con=mysql.connector.connect(host='localhost',user='root',password='root1799@',database='college')
                    cur=con.cursor()
                    qry="delete from student"
                    cur.execute(qry)
                    con.commit()
                    print("\n\n\t\t\t ************* INFORMATION DELETED SUCCESSFULLY... *************")
                except Exception as e:
                    print(e)
        
        print("\n")
        os.system('pause')    
while True:
    os.system('cls')
    Student().sHeader()
    print("\n\n")
#    os.system('pause')

