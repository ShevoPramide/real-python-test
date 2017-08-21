import sqlite3

conn = sqlite3.connect('new.db')

cursor = conn.cursor()

cursor.execute(""" CREATE TABLE POPULATION
                   (CITY TEXT, state TEXT, count INT)
               """)
conn.close()

