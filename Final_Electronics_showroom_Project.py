import mysql.connector as c
import pyfiglet
import random
import pandas as pd
import pymysql
from pymysql import connect
import sqlalchemy
from sqlalchemy import *

engine=sqlalchemy.create_engine('mysql+pymysql://root:MyNewPass@localhost:3306/electronics')
class dbh:
    def __init__(self):
        self.con=c.connect(host='localhost',port='3306',user='root',password='MyNewPass',database='electronics')

        query = 'create table if not exists customer(customer_id int primary key, customer_name varchar(100), customer_address varchar(100),customer_phone_no int)'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

        query1 = 'create table if not exists product(product_id int primary key, product_type varchar(100), product_des varchar(100), product_price int, product_quantity int)'
        cur1 = self.con.cursor()
        cur1.execute(query1)

        query2 = 'create table if not exists payment(payment_id varchar(100) primary key, customer_id int, foreign key(customer_id) references customer(customer_id), customer_name varchar(100),total int,tax real(10,3),grandtotal real(10,3),payment_type varchar(100), payment_date varchar(100))'
        cur2 = self.con.cursor()
        cur2.execute(query2)

        query3 = 'create table if not exists warehouse(warehouse_no int, warehouse_name varchar(100), warehouse_address varchar(100),product_id int, foreign key(product_id) references product(product_id),product_type varchar(100), product_des varchar(100), product_quantity int)'
        cur3 = self.con.cursor()
        cur3.execute(query3)

        query4 = 'create table if not exists branch(branch_no int primary key, branch_address varchar(100))'
        cur4 = self.con.cursor()
        cur4.execute(query4)

        query5 = 'create table if not exists employee(employee_id int primary key,emloyee_name varchar(100), salary int, branch_no int, foreign key(branch_no) references branch(branch_no))'
        cur5 = self.con.cursor()
        cur5.execute(query5)

        query6 = 'create table if not exists salesperson(employee_id int,foreign key(employee_id) references employee(employee_id),emloyee_name varchar(100), salary int, branch_no int, foreign key(branch_no) references branch(branch_no),attendance int,sales int)'
        cur6 = self.con.cursor()
        cur6.execute(query6)

        query7 = 'create table if not exists other_staff(employee_id int,foreign key(employee_id) references employee(employee_id),emloyee_name varchar(100), salary int, branch_no int, foreign key(branch_no) references branch(branch_no),attendance int)'
        cur7 = self.con.cursor()
        cur7.execute(query7)

        query8 = 'create table if not exists delivery(tracking_id varchar(100) primary key, dispatch_date varchar(100),delivery_date varchar(100),delivery_boy varchar(100)) '
        cur8 = self.con.cursor()
        cur8.execute(query8)

        # Insert

    def insert_customer(self, customer_id, customer_name, customer_address, customer_phone_no):
        query = "insert into customer(customer_id,customer_name,customer_address,customer_phone_no)values({},'{}','{}',{})".format(
            customer_id, customer_name, customer_address, customer_phone_no)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Customer information saved to database")

    # Fetch
    def fetch_customer(self):
        # db_connection = c.connect(host='localhost', user='root', password='avneesh@777',database='Electronics_Showroom')
        # engine = sqlalchemy.create_engine('mysq1+pymysq1://root:avneesh@777@localhost:3306/electronics_showroom')
        # db_connection_str = 'mysq1+pymysq1://root:avneesh@777@localhost:3306/electronics_showroom'
        # db_connection = create_engine(db_connection_str)
        query = "select * from customer"
        read_customer = pd.read_sql_query(query, engine)
        print(read_customer)
        # df = pd.read_sql('SELECT * FROM table_name', con=db_connection)

        # cur = db_connection.cursor()
        # cur.execute(query)
        # result = pd.read_sql(query,con=db_connection)
        # print(result)
        # db_connection.close()
        # for row in cur:
        #     print("Customer ID: ", row[0])
        #     print("Customer Name: ", row[1])
        #     print("Customer Address: ", row[2])
        #     print("Customer Phone Number: ", row[3])

    # delete
    def delete_customer(self, customer_id):
        query = "delete from customer where customer_id={}".format(customer_id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")

    # update
    def update_customer(self, customer_id, new_name, new_address, new_phone):
        query = "update customer set customer_name= '{}',customer_address= '{}', customer_phone_no= {} where customer_id= {}".format(
            new_name, new_address, new_phone, customer_id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def insert_product(self, product_id, product_type, product_des, product_price, product_quantity):
        query = "insert into product(product_id,product_type,product_des,product_price,product_quantity)values({},'{}','{}',{},{})".format(
            product_id, product_type, product_des, product_price, product_quantity)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Product information saved to database")

    def fetch_product(self):
        query = "select * from product"
        cur = self.con.cursor()
        cur.execute(query)
        # for row in cur:
        #     print("Product ID: ", row[0])
        #     print("Product Type: ", row[1])
        #     print("Product Description: ", row[2])
        #     print("Product Price: ", row[3])
        #     print("Product Quantity: ", row[4])
        read_product = pd.read_sql_query(query, engine)
        print(read_product)

    def delete_product(self, product_id):
        query = "delete from product where product_id={}".format(product_id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")

    def update_product(self, product_id, new_type, new_des, new_price, new_quantity):
        query = "update product set product_type= '{}',product_des= '{}',product_price= {}, product_quantity= {} where product_id= {}".format(
            new_type, new_des, new_price, new_quantity, product_id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def insert_warehouse(self, warehouse_id, warehouse_name, warehouse_address,product_id,product_type,product_des, product_quantity):
        query = "insert into warehouse(warehouse_id, warehouse_name, warehouse_address,product_id,product_type,product_des, product_quantity)values({},'{}','{}',{},'{}','{}',{})".format(
            warehouse_id, warehouse_name, warehouse_address,product_id,product_type,product_des, product_quantity)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Warehouse information saved to database")

    def fetch_warehouse(self):
        query = "select * from warehouse"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Warehouse No: ", row[0])
        #     print("Warehouse Name: ", row[1])
        #     print("Warehouse address: ", row[2])
        #     print("Product ID: ",row[3])
        #     print("Product Type: ", row[4])
        #     print("Product Description: ", row[5])
        #     print("Product Quantity: ", row[6])
        read_warehouse = pd.read_sql_query(query, engine)
        print(read_warehouse)

    def delete_warehouse(self, product_id):
        query = "delete from warehouse where product_id={}".format(product_id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")

    def update_warehouse(self, warehouse_no, warehouse_name, warehouse_address,product_id,product_type,product_des, product_quantity):
        query = "update product set warehouse_no= '{}',warehouse_no= '{}',warehouse_address= '{}',product_type= '{}',product_des = '{}',product_quantity = {} where product_id= {}".format(
            warehouse_no, warehouse_name, warehouse_address,product_id,product_type,product_des, product_quantity)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def fetch_tv(self):
        query = "select *,product_type from warehouse where product_type = 'Television'"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Warehouse No: ", row[0])
        #     print("Warehouse Name: ", row[1])
        #     print("Warehouse address: ", row[2])
        #     print("Product ID: ", row[3])
        #     print("Product Type: ", row[4])
        #     print("Product Description: ", row[5])
        #     print("Product Quantity: ", row[6])
        read_tv = pd.read_sql_query(query, engine)
        print(read_tv)

    def fetch_ac(self):
        query = "select * from warehouse where product_type ='AC'"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Warehouse No: ", row[0])
        #     print("Warehouse Name: ", row[1])
        #     print("Warehouse address: ", row[2])
        #     print("Product ID: ", row[3])
        #     print("Product Type: ", row[4])
        #     print("Product Description: ", row[5])
        #     print("Product Quantity: ", row[6])
        read_ac = pd.read_sql_query(query, engine)
        print(read_ac)
    def fetch_ref_and_wm(self):
        query = "select * from warehouse where product_type = 'Refrigerator' or product_type = 'Washing Machine'"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Warehouse No: ", row[0])
        #     print("Warehouse Name: ", row[1])
        #     print("Warehouse address: ", row[2])
        #     print("Product ID: ", row[3])
        #     print("Product Type: ", row[4])
        #     print("Product Description: ", row[5])
        #     print("Product Quantity: ", row[6])
        read_ref_wm = pd.read_sql_query(query, engine)
        print(read_ref_wm)

    def insert_branch(self,branch_no,branch_add):
        query = "insert into branch(branch_no,branch_add)values({},'{}')".format(
            branch_no,branch_add)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Customer information saved to database")

    def fetch_branch(self):
        query = "select * from branch"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Branch Number: ", row[0])
        #     print("Branch address: ", row[1])
        read_branch = pd.read_sql_query(query, engine)
        print(read_branch)

    def delete_branch(self, branch_no):
        query = "delete from branch where branch_no={}".format(branch_no)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")

    def update_branch(self, branch_no,branch_add):
        query = "update product set branch_no= {},branch_add= '{}',where branch_no= {}".format(
           branch_no,branch_add)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def fetch_branch_and_product(self):
        query = "select * from branch natural join product"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Branch Number: ", row[0])
        #     print("Branch address: ", row[1])
        #     print("Product ID: ",row[2])
        #     print("Product Type: ",row[3])
        #     print("Product Description: ",row[4])
        #     print("Product Price: ",row[5])
        #     print("Product Quantity :",row[6])
        read_branch_product = pd.read_sql_query(query, engine)
        print(read_branch_product)

    def fetch_branch_and_warehouse(self):
        query = "select * from branch natural join warehouse"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Branch Number: ", row[0])
        #     print("Branch address: ", row[1])
        #     print("Product ID: ",row[2])
        #     print("Product Type: ", row[3])
        #     print("Product Description: ", row[4])
        #     print("Product Price: ", row[5])
        #     print("Product Quantity :", row[6])
        read_branch_warehouse = pd.read_sql_query(query, engine)
        print(read_branch_warehouse)

    def insert_employee(self, emp_id,emp_name,emp_sal,branch_no):
        query = "insert into customer(emp_id,emp_name,emp_sal,branch_no)values({},{},'{}',{})".format(
            emp_id,emp_name,emp_sal,branch_no)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Customer information saved to database")

        # Fetch Branch

    def fetch_employee(self):
        query = "select * from employee"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Employee ID: ", row[0])
        #     print("Employee Name: ", row[1])
        #     print("Employee Salary: ", row[2])
        #     print("Branch Number: ", row[3])
        read_employee = pd.read_sql_query(query, engine)
        print(read_employee)

        # Delete Employee

    def delete_employee(self, emp_id):
        query = "delete from employee where employee_id={}".format(emp_id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")

        # update

    def update_employee(self, emp_id,emp_name,emp_sal,branch_no):
        query = "update customer set employee_name= '{}',employee_sal= {}, branch_no= {} where employee_id= {}".format(
            emp_id,emp_name,emp_sal,branch_no)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def fetch_avg_salary(self):
        query = "select avg(salary) as average_salary from employee "
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Average Salary: ", row[0])
        read_avg_salary = pd.read_sql_query(query, engine)
        print(read_avg_salary)

    def fetch_total_salary(self):
        query = "select sum(salary) as total_salary from employee "
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Total Salary given to Employees: ", row[0])
        read_total_salary = pd.read_sql_query(query, engine)
        print(read_total_salary)

    def fetch_employee_start_with_m(self):
        query = "select * from employee where emloyee_name like 'm%%' "
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Employee ID: ", row[0])
        #     print("Employee Name: ", row[1])
        #     print("Employee Salary: ", row[2])
        #     print("Branch Number: ", row[3])
        read_employee_start_m = pd.read_sql_query(query, engine)
        print(read_employee_start_m)

    def fetch_employee_end_with_a(self):
        query = "select * from employee where emloyee_name like'%%a'"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Employee ID: ", row[0])
        #     print("Employee Name: ", row[1])
        #     print("Employee Salary: ", row[2])
        #     print("Branch Number: ", row[3])
        read_employee_end_a = pd.read_sql_query(query, engine)
        print(read_employee_end_a)

    def insert_salesperson(self, emp_id,emp_name,emp_sal,branch_no,attendance,sales):
        query = "insert into salesperson(emp_id,emp_name,emp_sal,branch_no,attendance,sales)values({},{},'{}','{}',{},{})".format(
            emp_id,emp_name,emp_sal,branch_no,attendance,sales)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Salesperson information saved to database")

        # Fetch Branch

    def fetch_salesperson(self):
        query = "select * from salesperson"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Employee ID: ", row[0])
        #     print("Employee Name: ", row[1])
        #     print("Employee Salary: ", row[2])
        #     print("Branch Number: ", row[3])
        #     print("Attendance: ", row[4])
        #     print("Sales: ", row[5])
        read_salesperson = pd.read_sql_query(query, engine)
        print(read_salesperson)

        # Delete Employee

    def delete_salesperson(self, emp_id):
        query = "delete from salesperson where employee_id={}".format(emp_id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")

        # update

    def update_salesperson(self, emp_id,emp_name,emp_sal,branch_no,attendance,sales):
        query = "update customer set employee_name= '{}',employee_sal= {}, branch_no= {},attendance = '{}',sales = {} where employee_id= {}".format(
            emp_id,emp_name,emp_sal,branch_no,attendance,sales)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def fetch_greater_attendance(self):
        query = "select * from salesperson where attendance>=24"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Employee ID: ", row[0])
        #     print("Employee Name: ", row[1])
        #     print("Employee Salary: ", row[2])
        #     print("Branch Number: ", row[3])
        #     print("Attendance: ", row[4])
        #     print("Sales: ", row[5])
        read_greater_attendance = pd.read_sql_query(query, engine)
        print(read_greater_attendance)

    def fetch_greater_sales(self):
        query = "select * from salesperson where sales>=30"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Employee ID: ", row[0])
        #     print("Employee Name: ", row[1])
        #     print("Employee Salary: ", row[2])
        #     print("Branch Number: ", row[3])
        #     print("Attendance: ", row[4])
        #     print("Sales: ", row[5])
        read_greater_sales = pd.read_sql_query(query, engine)
        print(read_greater_sales)

    def fetch_total_salesperson(self):
        query = "select count(*) from salesperson "
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Total Salesperson: ", row[0])
        read_total_salesperson = pd.read_sql_query(query, engine)
        print(read_total_salesperson)

    def insert_other_staff(self, emp_id,emp_name,emp_sal,branch_no,attendance):
        query = "insert into other_staff(emp_id,emp_name,emp_sal,branch_no,attendance,sales)values({},{},'{}','{}',{})".format(
            emp_id,emp_name,emp_sal,branch_no,attendance)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("other staff information saved to database")

        # Fetch Branch

    def fetch_other_staff(self):
        query = "select * from other_staff"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Employee ID: ", row[0])
        #     print("Employee Name: ", row[1])
        #     print("Employee Salary: ", row[2])
        #     print("Branch Number: ", row[3])
        #     print("Attendance: ", row[4])
        read_other_staff = pd.read_sql_query(query, engine)
        print(read_other_staff)

        # Delete Employee

    def delete_other_staff(self, emp_id):
        query = "delete from other_staff where employee_id={}".format(emp_id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")

        # update

    def update_other_staff(self, emp_id,emp_name,emp_sal,branch_no,attendance):
        query = "update customer set employee_name= '{}',employee_sal= {}, branch_no= {},attendance = '{}' where employee_id= {}".format(
            emp_id,emp_name,emp_sal,branch_no,attendance)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def fetch_total_other_staff(self):
        query = "select count(*) from other_staff "
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Total other Staff: ", row[0])
        read_total_other_staff = pd.read_sql_query(query, engine)
        print(read_total_other_staff)

    def fetch_other_staff_by_branch(self):
        query = "select count(*),branch_no from other_staff group by branch_no"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Total Employees: ", row[0])
        #     print("Branch Number: ", row[1])
        read_other_staff_branch = pd.read_sql_query(query, engine)
        print(read_other_staff_branch)

    def order(self):
        a = int(input("Enter product-id of product that you want to add to the cart: "))
        b = int(input("Enter quantity: "))
        c = int(input("Enter your customer_id: "))
        query3 = "select customer_name from customer where customer_id={}".format(c)
        cur3 = self.con.cursor()
        cur3.execute(query3)
        for row in cur3:
            w = row[0]
        query1 = "select product_quantity,product_price from product where product_id={}".format(a)
        cur1 = self.con.cursor()
        cur1.execute(query1)
        for row in cur1:
            z = row[0]
            y = row[1]
        read_product= pd.read_sql_query(query1, engine)
        print(read_product)
        if z >= b:

            query5 = "select concat(length(customer_name),customer_name,customer_phone_no) from customer where customer_id={}".format(
                c)
            cur5 = self.con.cursor()
            cur5.execute(query5)
            for row in cur5:
                t = row[0]
                t = t + str(random.randint(1, 10000))
            query6 = "select curdate()"
            cur6 = self.con.cursor()
            cur6.execute(query6)
            for row in cur6:
                u = row[0]
            z = z - b
            query = "update product set product_quantity={} where product_id='{}'".format(z, a)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            x = b * y
            v = input("Enter payment type: ")
            query2 = "insert into payment(payment_id,customer_id,customer_name,total,tax,grandtotal,payment_type,payment_date)values('{}',{},'{}',{},{},{},'{}','{}')".format(
                t, c, w, x, x * 0.18, x + x * 0.18, v, u)
            cur2 = self.con.cursor()
            cur2.execute(query2)
            self.con.commit()
        else:
            print("OUT OF STOCK!!!")

    def display_payment(self):
        query = "select * from payment"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Payment ID: ", row[0])
        #     print("customer Type: ", row[1])
        #     print("customer Name: ", row[2])
        #     print("Total: ", row[3])
        #     print("Tax: ", row[4])
        #     print("Grand Total: ", row[5])
        #     print("Payment Type: ", row[6])
        #     print("Current date Type: ", row[7])
        read_payment = pd.read_sql_query(query, engine)
        print(read_payment)

    def deliver_my_stuff(self):
        a = int(input("Enter your customer id to check delivery status: "))
        query = "select RPAD(round(grandtotal,0),15,'x') from payment where payment_id in(select payment_id from payment where customer_id={})".format(
            a)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            b = row[0]
            b = b + str(random.randint(1, 10000))
        query2 = "select date_add(payment_date,interval +2 day) from payment where customer_id={}".format(a)
        cur2 = self.con.cursor()
        cur2.execute(query2)
        for row in cur2:
            c = row[0]
        query3 = "select date_add(payment_date,interval +3 day) from payment where customer_id={}".format(a)
        cur3 = self.con.cursor()
        cur3.execute(query3)
        for row in cur3:
            d = row[0]
        query4 = "select emloyee_name from employee where employee_id={}".format(random.randint(501, 515))
        cur4 = self.con.cursor()
        cur4.execute(query4)
        for row in cur4:
            e = row[0]
        query5 = "insert into delivery(tracking_id,dispatch_date,delivery_date,delivery_boy)values('{}','{}','{}','{}')".format(
            b, c, d, e)
        cur5 = self.con.cursor()
        cur5.execute(query5)
        self.con.commit()

    def display_delivery(self):
        query = "select * from delivery"
        # cur = self.con.cursor()
        # cur.execute(query)
        # for row in cur:
        #     print("Tracking-id: ", row[0])
        #     print("Dispatch Date: ", row[1])
        #     print("Delivery Date: ", row[2])
        #     print("Delivery Boy: ", row[3])
        read_delivery = pd.read_sql_query(query, engine)
        print(read_delivery)

def main():
    db = dbh()
    while True:
        print("****WELCOME****")
        print()
        figure = pyfiglet.figlet_format("Electronics Showroom", font="bubble")
        print(figure)

        print("Press 1 to access Customer Tab")
        print("Press 2 to access Product Tab")
        print("Press 3 to access Payment Tab")
        print("Press 4 to access warehouse Tab")
        print("Press 5 to access branch Tab")
        print("Press 6 to access employee Tab")
        print("Press 7 to access salesperson Tab")
        print("Press 8 to access other_staff Tab")
        print("Press 9 to access delivery Tab")
        print("Press 0 to exit")
        try:
            choice = int(input())
            if choice == 1:  # Customer Table
                while True:
                    print("******WELCOME*****")
                    print()
                    print("Press 1 to insert new customer details")
                    print("Press 2 to display customer details")
                    print("Press 3 to delete customer details")
                    print("Press 4 to update customer details")
                    print("Press 5 to exit program")
                    print()
                    try:
                        choice = int(input())
                        if choice == 1:
                            # insert customer
                            cid = int(input("Enter customer id: "))
                            cname = input("Enter new customer name: ")
                            cadd = input("Enter new customer address: ")
                            cphone = int(input("Enter new customer phone number: "))
                            db.insert_customer(cid, cname, cadd, cphone)
                            pass
                        elif choice == 2:
                            db.fetch_customer()
                            # display customer
                            pass
                        elif choice == 3:
                            cid = int(input("Enter customer id of customer to be deleted: "))
                            db.delete_customer(cid)
                            # delete customer
                            pass
                        elif choice == 4:
                            cid = int(input("Enter customer id of customer to be updated: "))
                            cname = input("Enter new customer name: ")
                            cadd = input("Enter new customer address: ")
                            cphone = int(input("Enter new customer phone number: "))
                            db.update_customer(cid, cname, cadd, cphone)
                            # update customer
                            pass
                        elif choice == 5:
                            # exit program
                            break
                        else:
                            print("Invalid Input!!! Try Again")
                    except Exception as e:
                        print(e)
                        print("Invalid Details! Try Again")
            elif choice == 2:  # Product Table
                while True:
                    print("******WELCOME*****")
                    print()
                    print("Press 1 to insert product details")
                    print("Press 2 to display product details")
                    print("Press 3 to delete product details")
                    print("Press 4 to update product details")
                    print("Press 5 to exit program")
                    print()
                    try:
                        choice = int(input())
                        if choice == 1:
                            # insert product
                            pid = int(input("Enter product id: "))
                            ptype = input("Enter product type: ")
                            pdes = input("Enter product description: ")
                            pprice = int(input("Enter product price: "))
                            pqt = int(input("Enter product quantity: "))
                            db.insert_product(pid, ptype, pdes, pprice, pqt)
                            pass
                        elif choice == 2:
                            db.fetch_product()
                            # display product
                            pass
                        elif choice == 3:
                            pid = int(input("Enter customer id of customer to be deleted: "))
                            db.delete_branch(pid)
                            # delete product
                            pass
                        elif choice == 4:
                            pid = int(input("Enter product id of product to be updated: "))
                            ptype = input("Enter new product type: ")
                            pdes = input("Enter new product description: ")
                            pprice = int(input("Enter new product price: "))
                            pqt = int(input("Enter new product quantity: "))
                            db.update_product(pid, ptype, pdes, pprice, pqt)
                            # update product
                            pass
                        elif choice == 5:
                            # exit program
                            break
                        else:
                            print("Invalid Input!!! Try Again")
                    except Exception as e:
                        print(e)
                        print("Invalid Details! Try Again")


            elif choice == 3:  # payment Table

                while True:

                    print("***WELCOME**")

                    print()
                    print("Press 1 to add items to cart")
                    print("Press 2 to display details of all payments")
                    print("Press 3 to exit program")
                    try:
                        choice = int(input())
                        if choice == 1:
                            db.order()
                            pass
                        elif choice == 2:
                            db.display_payment()
                            pass
                        elif choice == 3:
                            break
                    except Exception as e:
                        print(e)
                        print("Invalid Details! Try Again")

            elif choice == 4: # Warehouse Tab
                print("******WELCOME*****")
                print()
                print("Press 1 to insert Warehouse Details")
                print("Press 2 to display Warehouse details")
                print("Press 3 to delete Warehoouse details")
                print("Press 4 to update Warehouse details")
                print("Press 5 to see all stock of television")
                print("press 6 to see all the stock of AC")
                print("Press 7 to see all the stock of Washing Machine and Refrigerator")
                print("Press 8 to exit program")
                print()
                try:
                    choice = int(input())
                    if choice == 1:
                        # insert warehouse
                        w_no= int(input("Enter Warehouse number: "))
                        w_name = input("Enter Warehouse Name: ")
                        w_add = input("Enter Warehouse address: ")
                        pid = int(input("Enter Product ID: "))
                        p_type = input("Enter product Type: ")
                        p_des = input("Enter Product description: ")
                        pqt = int(input("Enter product quantity: "))
                        db.insert_warehouse(w_no,w_name,w_add,pqt)
                        pass
                    elif choice == 2:
                        db.fetch_warehouse()
                        # display product
                        pass
                    elif choice == 3:
                        pid = int(input("Enter product id of product to be deleted from Warehouse: "))
                        db.delete_warehouse(pid)
                        # delete product
                        pass
                    elif choice == 4:
                        w_no = int(input("Enter Warehouse number to be updated: "))
                        w_name = input("Enter Warehouse Name to be updated: ")
                        w_add = input("Enter Warehouse address to be updated: ")
                        pid = int(input("Enter Product ID to be updated: "))
                        p_type = input("Enter product Type to be updated: ")
                        p_des = input("Enter Product description to be updated: ")
                        pqt = int(input("Enter product quantity to be updated: "))
                        db.update_product(pid, ptype, pdes, pprice, pqt)

                    elif choice == 5:
                        db.fetch_tv()

                    elif choice == 6:
                        db.fetch_ac()

                    elif choice ==7:
                        db.fetch_ref_and_wm()

                    elif choice == 8:
                        break

                    else:
                        print("Invalid Details! Try Again")


                except Exception as e:
                    print(e)
                    print("Invalid Details! Try Again")

            elif choice == 5:
                while True:
                    print("******WELCOME*****")
                    print()
                    print("Press 1 to insert Branch details")
                    print("Press 2 to display Branch details")
                    print("Press 3 to delete Branch details")
                    print("Press 4 to update Branch details")
                    print("Press 5 to display Branch details with Product details")
                    print("Press 6 to display Branch details with Warehouse details")
                    print("Press 7 to exit program")
                    print()
                    try:
                        choice = int(input())
                        if choice == 1:
                            # insert Branch
                            b_no = int(input("Enter Branch number: "))
                            b_add = input("Enter Branch address: ")
                            db.insert_branch(b_no, b_add)
                            pass
                        elif choice == 2:
                            db.fetch_branch()
                            # display product
                            pass
                        elif choice == 3:
                            pid = int(input("Enter customer id of customer to be deleted: "))
                            db.delete_product(pid)
                            # delete product
                            pass
                        elif choice == 4:
                            b_no = int(input("Enter Branch number to be updated: "))
                            b_add = input("Enter Branch address to be updated: ")
                            pid = int(input("Enter Product ID to be updated: "))
                            db.update_branch(b_no,b_add,pid)

                        elif choice == 5:
                            db.fetch_branch_and_product()

                        elif choice ==6:
                            db.fetch_branch_and_warehouse()
                        elif choice == 7:
                            break
                    except Exception as e:
                        print(e)
                        print("Invalid Details! Try Again")
            elif choice == 6:
                while True:
                    print("******WELCOME*****")
                    print()
                    print("Press 1 to insert Employee details")
                    print("Press 2 to display Employee details")
                    print("Press 3 to delete Employee details")
                    print("Press 4 to update Employee details")
                    print("Press 5 to find average salary of employees")
                    print("Press 6 to find total salary given to all Employees")
                    print("Press 7 to find all Employees whose name starts with m")
                    print("Press 8 to find all Employees whose name ends with a")
                    print("Press 9 to exit program")
                    print()
                    try:
                        choice = int(input())
                        if choice == 1:
                            # insert employee
                            e_id = int(input("Enter Employee id: "))
                            e_name = input("Enter new Employee name: ")
                            e_sal = input("Enter new Salary: ")
                            b_no = int(input("Enter new Branch number: "))
                            db.insert_customer(e_id,e_name,e_sal,b_no)
                            pass
                        elif choice == 2:
                            db.fetch_employee()
                            # display employee
                            pass
                        elif choice == 3:
                            eid = int(input("Enter customer id of customer to be deleted: "))
                            db.delete_employee(eid)
                            # delete employee
                            pass
                        elif choice == 4:
                            e_id = int(input("Enter Employee id to be updated: "))
                            e_name = input("Enter new employee name: ")
                            e_sal = int(input("Enter new employee salary: "))
                            b_no = int(input("Enter new Branch number: "))
                            db.update_customer(eid,e_name,e_sal,b_no)
                            # update customer
                        elif choice == 5:
                            db.fetch_avg_salary()
                        elif choice ==6:
                            db.fetch_total_salary()
                        elif choice == 7:
                            db.fetch_employee_start_with_m()
                        elif choice == 8:
                            db.fetch_employee_end_with_a()
                        elif choice ==9:
                            break
                    except Exception as e:
                        print(e)
                        print("Invalid Details! Try Again")
            elif choice == 7:
                while True:
                    print("******WELCOME*****")
                    print()
                    print("Press 1 to insert Salesperson details")
                    print("Press 2 to display Salesperson details")
                    print("Press 3 to delete Salesperon details")
                    print("Press 4 to update Salesperson details")
                    print("Press 5 to find total number of Salesperson")
                    print("Press 6 to find details of salesperson having attendance greater than 24")
                    print("Press 7 to find details of salesperson having sales greater than 30")
                    print("Press 8 to exit program")
                    print()
                    try:
                        choice = int(input())
                        if choice == 1:
                            # insert employee
                            e_id = int(input("Enter Employee id: "))
                            e_name = input("Enter new staff name: ")
                            e_sal = input("Enter new Salary: ")
                            b_no = int(input("Enter new Branch number: "))
                            attendance = input("Enter Attendance of staff: ")
                            salary = int(input("Enter Salary: "))
                            db.insert_other_staff(e_id, e_name, e_sal, b_no,attendance,salary)
                            pass
                        elif choice == 2:
                            db.fetch_salesperson()
                            # display employee
                            pass
                        elif choice == 3:
                            eid = int(input("Enter employee id of employee to be deleted: "))
                            db.delete_salesperson(eid)
                            # delete employee
                            pass
                        elif choice == 4:
                            e_id = int(input("Enter Employee id to be updated: "))
                            e_name = input("Enter new Staff name: ")
                            e_sal = int(input("Enter new Staff salary: "))
                            b_no = int(input("Enter new Branch number: "))
                            attendance = input("Enter new attendance: ")
                            db.update_salesperson(e_id, e_name, e_sal, b_no,attendance)
                            # update customer
                        elif choice ==5:
                            db.fetch_total_salesperson()
                        elif choice ==6:
                            db.fetch_greater_attendance()
                        elif choice == 7:
                            db.fetch_greater_sales()
                        elif choice == 8:
                            break
                    except Exception as e:
                        print(e)
                        print("Invalid Details! Try Again")

            elif choice == 8:
                while True:
                    print("******WELCOME*****")
                    print()
                    print("Press 1 to insert other Staff details")
                    print("Press 2 to display other staff details")
                    print("Press 3 to delete other staff details")
                    print("Press 4 to update other staff details")
                    print("Press 5 to find total number of Staff")
                    print("Press 6 to find number of other staff for each branch")
                    print("Press 7 to exit program")
                    print()
                    try:
                        choice = int(input())
                        if choice == 1:
                            # insert employee
                            e_id = int(input("Enter Employee id: "))
                            e_name = input("Enter new staff name: ")
                            e_sal = input("Enter new Salary: ")
                            b_no = int(input("Enter new Branch number: "))
                            attendance = input("Enter Attendance of staff: ")
                            salary = int(input("Enter Salary: "))
                            db.insert_other_staff(e_id, e_name, e_sal, b_no,attendance)
                            pass
                        elif choice == 2:
                            db.fetch_other_staff()
                            # display employee
                            pass
                        elif choice == 3:
                            eid = int(input("Enter employee id of other staff to be deleted: "))
                            db.delete_other_staff(eid)
                            # delete employee
                            pass
                        elif choice == 4:
                            e_id = int(input("Enter Employee id to be updated: "))
                            e_name = input("Enter new Staff name: ")
                            e_sal = int(input("Enter new Staff salary: "))
                            b_no = int(input("Enter new Branch number: "))
                            attendance = input("Enter new attendance: ")
                            db.update_other_staff(e_id, e_name, e_sal, b_no,attendance)
                            # update customer
                        elif choice ==5:
                            db.fetch_total_other_staff()

                        elif choice ==6:
                            db.fetch_other_staff_by_branch()

                        elif choice == 7:
                            break
                    except Exception as e:
                        print(e)
                        print("Invalid Details! Try Again")

            elif choice == 9:  # Delivery Table
                while True:
                    print("***WELCOME**")
                    print()
                    print("Press 1 to check delivery status")
                    print("Press 2 to display details of all deliveries")
                    print("Press 3 to exit program")
                    try:
                        choice = int(input())
                        if choice == 1:
                            db.deliver_my_stuff()
                            pass
                        elif choice == 2:
                            db.display_delivery()
                            pass
                        elif choice == 3:
                            break
                    except Exception as e:
                        print(e)
                        print("Invalid Details! Try Again")

            elif choice==0:
                break

        except Exception as e:
            print(e)
            print("Invalid Details! Try Again")


if __name__ == "__main__":
    main()