import sqlite3
# import csv
with sqlite3.connect('new.db') as conn:
	c = conn.cursor()
	c.execute("CREATE TABLE if not exists population(city TEXT, capital TEXT, pop INT)")
	data = [('Boston','MA',	600000),
	('Los Angeles','CA', 38000000),
	('Houston',	'TX',	2100000),
	('Philadelphia',	'PA',	1500000),
	('San Antonio',	'TX',	1400000),
	('San Diego',	'CA',	130000),
	('Dallas',	'TX',	1200000),
	('San Jose',	'CA',	900000),
	('Jacksonville',	'FL',	800000),
	('Indianapolis',	'IN',	800000),
	('Austin',	'TX',	800000),
	('Detroit',	'MI',	700000)]

	c.executemany("INSERT INTO population VALUES (?, ?, ?) ",data)
	c.execute("SELECT * from  population where pop > 1000000")
	f = c.fetchall()
	for r in f:
		print(r[0],r[1],r[2])

