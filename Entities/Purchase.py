import sqlite3
import csv

def createPurchaseTable():
    conn = sqlite3.connect("Gas_Station.db")
    c = conn.cursor()
    with conn:
        try:
            c.execute('''CREATE TABLE PURCHASE
                        (Id                 INTEGER     NOT NULL,
                        Purchase_Date       TEXT        NOT NULL,
                        Type_of_Payment     TEXT        NOT NULL,
                        Cus_Email           TEXT        NOT NULL,
                        GS_Longitude        REAL        NOT NULL,
                        GS_Latitude         REAL        NOT NULL,
                        Pump_ID             INTEGER     NOT NULL,
                        PRIMARY KEY (Id),
                        FOREIGN KEY (Cus_Email) REFERENCES CUSTOMER(Email) ON UPDATE CASCADE ON DELETE CASCADE,
                        FOREIGN KEY (GS_Longitude, GS_Latitude) REFERENCES GAS_STATION(Longitude, Latitude) ON UPDATE CASCADE ON DELETE NO ACTION,
                        FOREIGN KEY (Pump_ID) REFERENCES PUMP(Id) ON UPDATE CASCADE ON DELETE CASCADE
                        );''')
            insertFromCsv("Datasets/purchase.csv")
        except Exception as e:
            pass
    conn.close()

def insertFromCsv(fileName):
    conn = sqlite3.connect("Gas_Station.db")
    with open(fileName, newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for tuple in spamreader:
            insertInto(tuple['Id'], tuple['Purchase_Date'],
                       tuple['Type_of_Payment'], tuple['Cus_Email'],
                       tuple['GS_Longitude'], tuple['GS_Latitude'],
                       tuple['Pump_ID'], conn)
    conn.close()

def insertInto(id, purchase_date, type_of_payment, cus_email, gs_longitude, gs_latitude, pump_id, conn=False):
    if (conn == False):
        conn = sqlite3.connect("Gas_Station.db")
        c = conn.cursor()
        with conn:
            try:
                c.execute('''INSERT INTO PURCHASE
                            VALUES (?,?,?,?,?,?,?);''',
                            (id, purchase_date, type_of_payment, cus_email,
                             gs_longitude, gs_latitude, pump_id))
            except Exception:
                pass # tuple already added
        conn.close()
    else:
        c = conn.cursor()
        with conn:
            try:
                c.execute('''INSERT INTO PURCHASE
                            VALUES (?,?,?,?,?,?,?);''',
                            (id, purchase_date, type_of_payment, cus_email,
                             gs_longitude, gs_latitude, pump_id))
            except Exception as e:
                pass

def retrieveAllColumns():
    conn = sqlite3.connect("Gas_Station.db")
    c = conn.cursor()
    c.execute("select * from PURCHASE")
    data = c.fetchall()
    conn.close()
    return data