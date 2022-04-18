import sqlite3
import datetime


class Database:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cur = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        try:
            self.conn.rollback()
        except sqlite3.OperationalError as exec:
            print('Rollback Multiple')


class CustomerDatabase(Database):
    def add_user(self, name, gender, phonenumber, email, address, postalcode, userid, password):
        try:
            customerid = str(datetime.datetime.now())
            query = f"INSERT INTO customers (CustomerID, Name, Gender,PhoneNumber, Email, Address, Postal_Code, User_ID, Password) VALUES ('{customerid}', '{name}', '{gender}', {phonenumber}, '{email}', '{address}', {postalcode}, {userid}, '{password}')"
            print(query)
            self.cur.execute(query)
            self.commit()
            return True, customerid
        except Exception as ex:
            print(f'Error occurred while inserting {ex}')
            self.rollback()
            return False, 'Error occurred while inserting'

    def fetch_user(self, username, password):
        query = f"SELECT * from customers where Name='{username}' and Password='{password}'"
        print(query)
        self.cur.execute(query)
        result = self.cur.fetchall()
        if len(result) == 0:
            return False, ''
        if len(result[0]) == 0:
            return False, ''
        CustomerID = result[0][0]
        return True, CustomerID
    
    def fetch_all_user(self):
        query = f"SELECT * from customers"
        print(query)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result
    
    def get_user(self, customerid):
        try:
            query = f"Select Name from customers where CustomerID = '{customerid}'"
            print(query)
            self.cur.execute(query)
            result = self.cur.fetchall()
            if len(result) == 0:
                return False, ''
            if len(result[0]) == 0:
                return False, ''
            return result[0][0]
        except Exception as ex:
            print(f'Error occurred while fetching {ex}')
            self.rollback()
            return ''


class DressDatabase(Database):
    def add_dress(self, storeid, categoryid, Name, size, color, idealfor, Rental_Rate, Description):
        try:
            dressid = str(datetime.datetime.now())
            query = f"INSERT INTO dress (DressId, StoreID, CategoryID,Name, size, color, Ideal_For, Rental_Rate, Description) VALUES ('{dressid}', {storeid}, {categoryid}, '{Name}', '{size}', '{color}', '{idealfor}', {Rental_Rate}, '{Description}')"
            print(query)
            self.cur.execute(query)
            self.commit()
            return True, dressid
        except Exception as ex:
            msg = "Error occurred while inserting"
            print(f'Error occurred while inserting {ex}')
            self.rollback()
            return False, msg

    def fetch_dress(self, Name=None):
        if Name is None:
            query = "Select * from dress"
        else:
            query = f"Select * from dress where Name='{Name}'"
        print(query)
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def delete_dress(self, dressid):
        try:
            query = f"Delete from dress where DressId='{dressid}'"
            self.cur.execute(query)
            self.commit()
            return True
        except:
            self.rollback()
            return False


class BookingDatabase(Database):
    def book_dress(self, customerid, dressid, booking_date, amount, des):
        try:
            bookingid = str(datetime.datetime.now())
            query = f"INSERT INTO booking (BookingID, CustomerID, DressID,Booking_Date, Total_Amount, Description) VALUES ('{bookingid}', '{customerid}', '{dressid}', '{booking_date}', {float(amount)}, '{des}')"
            print(query)
            self.cur.execute(query)
            self.commit()

            PaymentId = str(datetime.datetime.now())
            status = 'Completed'
            query = f"INSERT INTO Payment (PaymentId, BookingID, Payment_Date_Time, Total_Amount,Status) VALUES ('{PaymentId}', '{bookingid}', '{booking_date}', {float(amount)},'{status}')"
            print(query)
            self.cur.execute(query)
            self.commit()
            return True, bookingid
        except Exception as ex:
            print(f'Error occurred while inserting {ex}')
            self.rollback()
            return False, 'Error occurred while inserting'

    def fetch_booking(self):
        query = 'Select * from booking'
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def fetch_customer_booking(self, customer_id):
        try:
            query = f"SELECT * FROM booking where CustomerID='{customer_id}'"
            self.cur.execute(query)
            result = self.cur.fetchall()
            return result
        except:
            self.rollback()
            return []

    def delete_booking(self, bookingid):
        try:
            query = f"Delete from booking where BookingID='{bookingid}'"
            self.cur.execute(query)
            self.commit()
            return True
        except:
            self.rollback()
            return False

name = 'datasource'
dress_db = DressDatabase(name)
book_db = BookingDatabase(name)
customer_db = CustomerDatabase(name)