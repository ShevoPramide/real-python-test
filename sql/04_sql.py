import sqlite3

with sqlite3.connect('new.db') as conn:
	c = conn.cursor()
	c.execute("SELECT population.city, population.pop, regions.region FROM population, regions WHERE population.city = regions.city")
	f = c.fetchall()
	# print(f)
	for r in f:
		print(r[0],r[1],r[2])