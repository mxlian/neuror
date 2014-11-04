import datetime
import serial
import sqlite3
import time

connection = sqlite3.connect('puerta-datos.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cursor = connection.cursor()

## To create the database the first time uncomment this
#print "Creando base de datos..."
#cursor.execute('DROP TABLE datos')
#cursor.execute('CREATE TABLE datos (id INTEGER PRIMARY KEY, fecha TIMESTAMP, datos VARCHAR(320))')  #320 ==> "9999-"x64
#connection.commit()

## To print all the data use this
#print "Visualizando datos:"
#cursor.execute('SELECT * FROM datos')
#for row in cursor:
	#print row

s = serial.Serial('/dev/ttyS0', 9600)
print "Port in use:", s.portstr

while True:
	cursor.execute('INSERT INTO datos(fecha, datos) values (?, ?)',
                    (datetime.datetime.now(), s.readline())
                  )
	connection.commit()

#cursor.close()
#connection.close()
#s.close()
