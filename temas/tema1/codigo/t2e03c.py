from turtle import *

print("Dibujando un pentágono")

lado = 5
angulo = 360 / lado

for i in range(lado):
	forward(80)
	left(angulo)
