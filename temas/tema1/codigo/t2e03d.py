from turtle import *

lado = int(input("Indique el número de lados del polígono: "))
angulo = 360 / lado

for i in range(lado):
	forward(80)
	left(angulo)
