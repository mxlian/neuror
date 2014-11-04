from ffnet import ffnet, mlgraph
from ffnet.tools import drawffnet
from random import *
import math
import Gnuplot

# Generate standard layered network architecture and create network
net = ffnet(mlgraph((64,1)))

# Define training data
input = [[], [], [], [], [], []]
prueba = [[], []]
for x in range(-32, 32):
	input[0].append(eval("2./(1+pow(math.e, -x/10.))/17.+1./20."))
	input[1].append(eval("2./(1+pow(math.e, -x/10.))/17."))
	input[2].append(eval("2./(1+pow(math.e, -x/10.))/17.-1./20."))
	input[3].append(eval("16./(1+pow(math.e, -x/10.))/17.+1./20."))
	input[4].append(eval("16./(1+pow(math.e, -x/10.))/17."))
	input[5].append(eval("16./(1+pow(math.e, -x/10.))/17.-1./20."))

prueba[0].extend(input[1])
prueba[1].extend(input[4])

for i in range(0, 63):
	prueba[0][i] = prueba[0][i] + float(randint(-17, 17))/(3.*17.)
	prueba[1][i] = prueba[1][i] + float(randint(-17, 17))/(3.*17.)

#target  = [[0., 1.], [0., 1.], [0., 1.], [1., 0.], [1., 0.], [1., 0.]]
target  = [[0.], [0.], [0.], [1.], [1.], [1.]]

# Train network
net.randomweights()
#then train with scipy tnc optimizer
print "TRAINING NETWORK..."
net.train_tnc(input, target, maxfun=10000000, messages=1)

# Test network
print
print "TESTING NETWORK..."
output, regression = net.test(input, target, iprint = 2)

print "VALOR DE PRUEBA..."
for p in prueba:
	print net(p)

g = Gnuplot.Gnuplot()
g('set data style lines')

for i in range(0, len(prueba)):
	g.replot(Gnuplot.Data(prueba[i]))
for i in range(0, len(input)):
	g.replot(Gnuplot.Data(input[i]))

raw_input('Presione enter para continuar...\n')

#drawffnet.drawffnet(net)
#drawffnet.show()
#raw_input('Presione enter para continuar...\n')
