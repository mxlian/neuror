import Gnuplot
import sqlite3
import kohonen
import Image, ImageDraw, ImageTk
import Tkinter
import sys
import time

connection = sqlite3.connect('puerta-datos.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cursor = connection.cursor()
cursor.execute('SELECT * FROM datos')
r=[]
for res in cursor:
	r.append([int(x) for x in res[2].strip("\r\n-").split("-")])
cursor.close()
connection.close()

window = Tkinter.Tk()
canvas = Tkinter.Canvas(window, width = 512, height = 512)
canvas.pack()

params=dict(
	dimension         = 1,
	shape             = (64, 64),
	learning_rate     = kohonen.ExponentialTimeseries(-5e-4, 1, 0.1),
	neighborhood_size = 1,
	noise_variance    = 0.2,
	)


m = kohonen.Map(kohonen.Parameters(**params))

for i in range(1, 1000):
	print i,
	sys.stdout.flush()

	for r1 in r:
		m.learn(r1)

	if i % 3 == 0:
		tkim = ImageTk.PhotoImage(m.neuron_heatmap().resize((512,512), Image.NEAREST))
		item = canvas.create_image(0,0,image=tkim,anchor='nw')
		canvas.update()

print
g = Gnuplot.Gnuplot()
g('set data style lines')
red=255
for i in range(0, len(r)-1):
	g.plot(Gnuplot.Data(r[i]))
	img = m.distance_heatmap(0)
	w = m.flat_to_coords(m.winner(r[i]))
	draw = ImageDraw.Draw(img)
	draw.line([w[0]-1, w[1]-1, w[0]+1, w[1]+1], red)
	draw.line([w[0]-1, w[1]+1, w[0]+1, w[1]-1], red)
	tkim = ImageTk.PhotoImage(img.resize((512, 512), Image.NEAREST))
	canvas.create_image(0,0,image=tkim,anchor='nw')
	canvas.update()
	print "entrada", i
	print "neurona ganadora", w
	print "vector", r[i]
	print
	raw_input("Presione una tecla para continuar con las pruebas")

