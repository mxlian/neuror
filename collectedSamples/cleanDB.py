#!/usr/bin/env python

import sqlite3

con1 = sqlite3.connect("data.db")
con2 = sqlite3.connect("dataClean2.db")

cur1 = con1.cursor()
cur2 = con2.cursor()

cur2.execute ("create table lecturas (id integer primary key, time timestamp, value integer)")

cur1.execute ("select * from lecturas")

for r in cur1:
    if r[2] == "x\r":
        cur2.execute("insert into lecturas values (" + str(r[0]) + ",'" + r[1] + "', 65535);")
    else:  
        cur2.execute("insert into lecturas values (" + str(r[0]) + ",'" + r[1] + "', " + r[2] + ");")
    print r[0]
    if not( r[0] % 20000):
        con2.commit() 
con2.commit()
cur2.close()
cur1.close()
print "Job done"
