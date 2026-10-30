import mysql.connector

# CLASS 1 - DATABASE
class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abceef123",
            database="testDBLloyds2"
        )


# CLASS 2 - CUSTOMER
class Customer:
    def __init__(self, database):
        self.db = database.db

    def showCustomers(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM Customer")

        for customer in cursor.fetchall():
            print(customer)

    def addCustomer(self, name, city):
        cursor = self.db.cursor()
        sql = "INSERT INTO Customer (CustomerName, City) VALUES (%s, %s)"
        cursor.execute(sql, (name, city))
        self.db.commit()


# CLASS 3 - DELIVERY
class Delivery:
    def __init__(self, database):
        self.db = database.db

    def showDeliveries(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM Delivery")

        for delivery in cursor.fetchall():
            print(delivery)
            