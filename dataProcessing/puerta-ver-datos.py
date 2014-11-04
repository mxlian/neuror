import Gnuplot
import sqlite3

connection = sqlite3.connect('puerta-datos.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cursor = connection.cursor()

cursor.execute('SELECT * FROM datos')

g = Gnuplot.Gnuplot()
g('set data style lines')

d = []

for row in cursor:
	v = []
	i = 0
	for x in row[2].strip("\r\n-").split("-"):
		v.append([i, x])
		i = i + 1
	
	g.replot(Gnuplot.Data(v))

raw_input('Presione enter para terminar...\n')

cursor.close()
connection.close()

