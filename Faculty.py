import mysql.connector
from prettytable import PrettyTable
import os
import time

class Faculty:
    def __init__(self):
        pass

    def fHeader(self):
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
            self.finsertData()
        elif n==2:
            self.fsearchData()
        elif n==3:
            self.fupdateData()
        elif n==4:
            self.fdeleteData()
        elif n==5:
            exit(0)
        else:
            print("\n\n\t\t\t\t ************** INVALID CHOICE **************\n\n")
            time.sleep(3)
            self.sHeader()
        
        

    def finsertData(self):
        os.system('cls')
        print("\n\n\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|****   MAHAKAL  INSTITUTE  OF  TECHNOLOGY   ****|")
        print("\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|*****   --->  Store Faculty details  <---  *****|")
        print("\t\t\t\t\t\t\t|************************************************|")
        print("\n\n\t\t\t\t1.Store Single Faculty data")
        print("\n\t\t\t\t2.Store Multiple Faculties data")
        n=int(input("\n\n\t\t\t\t Enter your Choice : "))
        if n==1:
            no=1
        elif n==2:
            no=int(input("\n\n\t\t\t\t Enter total numbers of Faculties : "))
        else:
            print("\n\n\t\t\t\t ************** INVALID CHOICE **************\n\n")
            time.sleep(3)
            self.finsertData()
        for i in range(1,no+1):
            data=[]
            os.system('cls')
            print("\n\n\t\t\t\t\t\t\t|************************************************|")
            print("\t\t\t\t\t\t\t|****   MAHAKAL  INSTITUTE  OF  TECHNOLOGY   ****|")
            print("\t\t\t\t\t\t\t|************************************************|")
            print("\t\t\t\t\t\t\t|*****   --->  Store Faculty details  <---  *****|")
            print("\t\t\t\t\t\t\t|************************************************|")
            print("\n\n\t\t\t\t Enter the information of",i,"Faculty :-")
            data.append(input("\n\t\t\t\t Enter Faculty name :"))
            data.append(input("\n\t\t\t\t Enter Id Number :"))
            data.append(input("\n\t\t\t\t Enter Father Name :"))
            data.append(input("\n\t\t\t\t Enter Mother Name :"))
            data.append(input("\n\t\t\t\t Enter Addhar Number  :"))
            data.append(input("\n\t\t\t\t Enter Full Address :"))
            data.append(int(input("\n\t\t\t\t Enter Age :")))
            data.append(input("\n\t\t\t\t Enter Faculty departement :"))
            data.append(input("\n\t\t\t\t Enter Faculty qualification :"))
            data.append(input("\n\t\t\t\t Enter Mobile Number :"))
            print("\n\n\n\t\t\t ! PLEASE CHECKOUT ALL ABOVE ENTERED INORMATION.....\n\n")
            print("\t\t\t ! IF BY MISTAKE YOU ENTERED ANY THING WRONG INFORMATION, THEN USE 'UPDATE' OPTION TO CORRECT IT.....\n\n")
            
            os.system('pause')
            try:
                con=mysql.connector.connect(host='localhost',user='root',password='root1799@',database='college')
                cur=con.cursor()
                qry="insert into Faculty(fname,fid,ffname,fmname,faddh_no,fadds,fage,fdepartmnt,fqualtn,fmob_no)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
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

    def fsearchData(self):
        os.system('cls')
        print("\n\n\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|****   MAHAKAL  INSTITUTE  OF  TECHNOLOGY   ****|")
        print("\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|*******     --->  Search details  <---   *******|")
        print("\t\t\t\t\t\t\t|************************************************|")
        
        try:
            print("\n\n\t\t\t\t1.Search by Id Number ")
            print("\n\t\t\t\t2.Search by Addhar number")
            print("\n\t\t\t\t3.Search by Father Name")
            print("\n\t\t\t\t4.Show All Data")
            n=int(input("\n\n\t\t\t\t Enter Your Choice :"))
            con=mysql.connector.connect(host='localhost',user='root',password='root1799@',database='college')
            cur=con.cursor()
            cur.execute("desc Faculty")
            coln=[]
            for i in cur.fetchall():
                coln.append(i[0])
            
            if n==1:
                dt=input("\n\n\t\t\t\t Enter Id Number :")
                qry="select * from Faculty where fid = %s"
                cur.execute(qry,(dt,))
            elif n==2:
                dt=input("\n\n\t\t\t\t Enter Addhar Number :")
                qry="select * from Faculty where faddh_no = %s"
                cur.execute(qry,(dt,))
            elif n==3:
                dt=input("\n\n\t\t\t\t Enter Father Name :")
                qry="select * from Faculty where ffname = %s"
                cur.execute(qry,(dt,))
            elif n==4:
                qry="select * from Faculty"
                cur.execute(qry)
            else:
                print("\n\t\t\t\t ! Invalid Choice...")
                time.sleep(3)
                self.fsearchData()
                
            t = PrettyTable(coln)
            rdt=cur.fetchall()
            if len(rdt)!=0:
                for i in rdt:
                    t.add_row(i)
                print(t)
                
            else:
                print("\n\n\t\t\t\t !  DATA NOT FOUND !!!")
        except Exception as er:
            print(er)
        finally:
            if (con.is_connected()):
                cur.close()
                con.close()
        print("\n")
        os.system('pause')
            
    def fupdateData(self):
        os.system('cls')
        print("\n\n\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|****   MAHAKAL  INSTITUTE  OF  TECHNOLOGY   ****|")
        print("\t\t\t\t\t\t\t|************************************************|")
        print("\t\t\t\t\t\t\t|*******     --->  Update details  <---   *******|")
        print("\t\t\t\t\t\t\t|************************************************|")
        
        try:
            en=input("\n\n\t\t\t\t Enter Faculty's Id Number :")
            con=mysql.connector.connect(host='localhost',user='root',password='root1799@',database='college')
            cur=con.cursor()
            cur.execute("desc Faculty")
            coln=[]
            for i in cur.fetchall():
                coln.append(i[0])
            t = PrettyTable(coln)
            qry="select * from Faculty where fid = %s"
            cur.execute(qry,(en,))
            rdt=cur.fetchall()
            if len(rdt)!=0:
                for i in rdt:
                    t.add_row(i)
                print("\n\n\t\t\t\t\t\t  ***************** Faculty's details *****************\n")
                print(t)
                print("\n\n\t\t\t\t1.Update Name \t\t\t\t\t\t 6.Update Age")
                print("\n\t\t\t\t2.Update Father Name \t\t\t\t\t 7.Update Mobile number")
                print("\n\t\t\t\t3.Update Mother Name \t\t\t\t\t 8.Update department")
                print("\n\t\t\t\t4.Update Addhar Number \t\t\t\t\t 9.Update Qualification")
                print("\n\t\t\t\t5.Update Address ")
                ch=int(input("\n\t\t\t\t Enter your Choice :"))
                if ch==1:
                    updt=input("\n\n\t\t\t\t Enter Name for Updation :")
                    qry="update Faculty set fname= %s where fid = %s"
                elif ch==2:
                    updt=input("\n\n\t\t\t\t Enter Father Name for Updation :")
                    qry="update Faculty set ffname= %s where fid = %s"
                elif ch==3:
                    updt=input("\n\n\t\t\t\t Enter Mother Name for Updation :")
                    qry="update Faculty set fmname= %s where fid = %s"
                elif ch==4:
                    updt=input("\n\n\t\t\t\t Enter Aadhar Number for Updation :")
                    qry="update Faculty set faddh_no= %s where fid = %s"
                elif ch==5:
                    updt=input("\n\n\t\t\t\t Enter Address for Updation :")
                    qry="update Faculty set fadds= %s where fid = %s"
                elif ch==6:
                    updt=input("\n\n\t\t\t\t Enter Age for Updation :")
                    qry="update Faculty set fage= %s where fid = %s"
                elif ch==7:
                    updt=input("\n\n\t\t\t\t Enter Mobile Number for Updation :")
                    qry="update Faculty set fmob_no= %s where fid = %s"
                elif ch==8:
                    updt=input("\n\n\t\t\t\t Enter department for Updation :")
                    qry="update Faculty set fdepartmnt= %s where fid = %s"
                elif ch==9:
                    updt=input("\n\n\t\t\t\t Enter qualification for Updation :")
                    qry="update Faculty set fqualtn= %s where fid = %s"
                upi=(updt,en)
                cur.execute(qry,upi)
                con.commit()
                print("\n\t\t\t\t ************ INFORMATION UPDATED SUCCESSFULLY.... ************")
                qry="select * from Faculty where fid = %s"
                t = PrettyTable(coln)
                cur.execute(qry,(en,))
                rdt=cur.fetchall()
                if len(rdt)!=0:
                    for i in rdt:
                        t.add_row(i)
                    print("\n\n\t\t\t\t\t\t  ***************** Faculty's details after Updation *****************\n")
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

    def fdeleteData(self):
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
            en=input("\n\n\t\t\t\tEnter Id number :")
            try:
                con=mysql.connector.connect(host='localhost',user='root',password='root1799@',database='college')
                cur=con.cursor()
                qry="delete from Faculty where fid = %s"
                cur.execute(qry,(en,))
                con.commit()
                print("\n\n\t\t\t ************* INFORMATION DELETED SUCCESSFULLY... *************")
            except Exception as e:
                print(e)
        
        elif n==2:
            n=int(input("\n\n\t\t\t\tEnter total numbers of Id numbers to delete them :"))
            enl=[]
            for i in range(1,n+1):
                enl.append(input("\n\t\t\t\tEnter Id number :"))
                
            try:
                con=mysql.connector.connect(host='localhost',user='root',password='root1799@',database='college')
                cur=con.cursor()
                for i in enl:
                    qry="delete from Faculty where fid = %s"
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
                    qry="delete from Faculty"
                    cur.execute(qry)
                    con.commit()
                    print("\n\n\t\t\t ************* INFORMATION DELETED SUCCESSFULLY... *************")
                except Exception as e:
                    print(e)
        
        print("\n")
        os.system('pause')    
while True:
    os.system('cls')
    Faculty().fHeader()
    print("\n\n")
#    os.system('pause')

