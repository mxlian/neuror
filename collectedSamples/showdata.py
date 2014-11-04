#!/usr/bin/env python

# +-------------------------- show data ---------------------------------------
# |
# |
# |
# | maximiliano padulo - 25.04.2011
# +----------------------------------------------------------------------------

import sqlite3
import datetime
from pylab import *
from matplotlib.dates import *

databaseFile = "dataClean2.db"


connection = sqlite3.connect(databaseFile)
cur = connection.cursor()

query = cur.execute("select time, value from lecturas")

aperturas = []
aperturas.append([])
i=0

for fila in query:
    if fila[1]==65535:
        aperturas.append([])
        i += 1
    else:
        aperturas[i].append((fila[0], fila[1]))

print len(aperturas)
figure(figsize=(18,5))
gcf().subplots_adjust(left=0.05, right=0.99)

time=[]
values=[]
for r in aperturas[int(sys.argv[1])]:
    #time.append(r[0])
    time.append(date2num(datetime.datetime.strptime(r[0], "%Y-%m-%d %H:%M:%S.%f")))
    values.append(r[1])

plot_date(time, values, 'r-', linewidth=1.0, alpha=0.6, label="Internal sensor")

gca().xaxis.set_major_locator(SecondLocator(arange(0,60,2)))
gca().xaxis.set_minor_locator(SecondLocator(arange(1,60)))
gca().xaxis.set_major_formatter(DateFormatter('%S'))

axis([None, None, 0, 1024])
grid(alpha=0.7)
#legend() #loc=4)

xlabel(r"Time", fontsize = 12)
ylabel("Value", fontsize = 12)

title(aperturas[int(sys.argv[1])][0][0])

show()



