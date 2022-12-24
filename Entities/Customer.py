import sqlite3
import csv

def createCustomerTable():
    conn = sqlite3.connect("Gas_Station.db")
    c = conn.cursor()
    with conn:
        try:
            c.execute('''CREATE TABLE CUSTOMER
                        (Email              TEXT        NOT NULL,
                        Fname               TEXT        NOT NULL,
                        Lname               TEXT        NOT NULL,
                        Birth_Date          TEXT        NOT NULL,
                        Phone_Number        INTEGER     NOT NULL,
                        Longitude           REAL        NOT NULL,
                        Latitude            REAL        NOT NULL,
                        Remaining_Points    INTEGER     DEFAULT 0,
                        PRIMARY KEY (Email)
                        );''')
            insertFromCsv("Datasets/customer.csv")
        except Exception as e:
            pass # Database created
    conn.close()

def insertFromCsv(fileName):
    conn = sqlite3.connect("Gas_Station.db")
    with open(fileName, newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for tuple in spamreader:
            insertInto(tuple['Email'], tuple['Fname'], tuple['Lname'],
                       tuple['Birth_Date'],tuple['Phone_Number'],
                       tuple['Longitude'],tuple['Latitude'],
                       tuple['Remaining_Points'], conn)
    conn.close()

def insertInto(email, fname, lname, birth_date, phone_number, longitude, latitude, 
        rem_points, conn=False):
    if (conn == False):
        conn = sqlite3.connect("Gas_Station.db")
        c = conn.cursor()
        with conn:
            try:
                c.execute('''INSERT INTO CUSTOMER
                            VALUES (?,?,?,?,?,?,?,?);''', 
                            (email, fname, lname, birth_date, phone_number,
                            longitude, latitude, rem_points))
            except Exception as e:
                pass # tuple already added
        conn.close()
    else:
        c = conn.cursor()
        with conn:
            try:
                c.execute('''INSERT INTO CUSTOMER
                            VALUES (?,?,?,?,?,?,?,?);''', 
                            (email, fname, lname, birth_date, phone_number,
                            longitude, latitude, rem_points))
            except Exception as e:
                pass

def retrieveAllColumns():
    conn = sqlite3.connect("Gas_Station.db")
    c = conn.cursor()
    c.execute("select * from CUSTOMER")
    data = c.fetchall()
    conn.close()
    return data