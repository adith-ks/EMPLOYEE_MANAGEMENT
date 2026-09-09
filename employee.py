import mysql.connector

import datetime

class Dbconnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Adith@123",
                database="company_db"
            )
            return self.connection
            print("Connected successfully")

        except Exception as e:
            print(e)

class Employee_manager(Dbconnect):
    def post(self,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "insert into employee (name,place,mobile,email,departement,salary,joining_date)values(%s,%s,%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connect.commit()

            print("Member added successfully")
        except Exception as e:
            print(e)

    def get(self):
        self.connect = super().get_connection()
        self.cursor = self.connect.cursor()
        query= "select * from employee"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        for i in record:
            print(i)

    def retrieve(self,id=None):
        try:
            record= self.get_object(id=id)
            # self.connect = super().get_connection()
            # self.cursor = self.connect.cursor()
            # query = "select * from employee where id =%s"
            # value = (id,)
            # self.cursor.execute(query, value)
            # record = self.cursor.fetchone()
            print(record)

        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            record = self.get_object(id=id)
            # self.connect = super().get_connection()
            # self.cursor = self.connect.cursor()
            if record!=None:
                query = "delete from employee where id=%s"
                value = (id,)
                self.cursor.execute(query, value)
                self.connect.commit()
                print("Employee data deleted successfully")
        except Exception as e:
            print(e)

    def get_object(self,id=None):
        self.connect = super().get_connection()
        self.cursor = self.connect.cursor()
        query = "select * from employee where id=%s"
        value=(id,)
        self.cursor.execute(query,value)
        record=self.cursor.fetchone()
        return record

    def put(self,id=None,**kwargs):
        try:
            record = self.get_object(id=id)

            if record!=None:
                placeholder=""

                for k in kwargs.keys():
                    placeholder+= k+ "=%s,"
                    # placeholder = placeholder.rstrip(",")       #removing last ,
                    query = f"update employee set {placeholder} where id = %s"
                    value = [v for v in kwargs.values()]
                    value.append(id)
                    self.cursor.execute(query,value)
                    self.connect.commit()
                    print("Employee details updated")

            else:
                print("Employee not found")

        except Exception as e:
            print(e)

connection_instance = Dbconnect()       #parent object
connection_instance.get_connection()

employee_instance =Employee_manager()   #child object
# employee_instance.post(name="Anandhu",place="Karimugal",mobile="9876543211",email="anandhu@gmail.com",departement="Businesss",salary=55000,joining_date=datetime.datetime.today())
# employee_instance.post(name="Basil",place="Muvathupuzha",mobile="9876543212",email="basil@gmail.com",departement="Businesss",salary=56000,joining_date=datetime.datetime.today())
# employee_instance.post(name="Anass",place="Perumbavoor",mobile="9876543213",email="anass@gmail.com",departement="Developer",salary=56000,joining_date=datetime.datetime.today())


# employee_instance.get()
# employee_instance.retrieve(1)
# employee_instance.delete(6)
employee_instance.put(id=1,name="Adith")
employee_instance.get()
