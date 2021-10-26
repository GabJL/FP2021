import random 
 
VERSION = 0.1 
print("Bienvenido a Piedra, Papel o Tijera v", VERSION, sep = "") 
 
print("Las jugadas disponibles son Piedra, Papel y Tijera") 
 
print("Eligiendo la jugada del ordenador ...") 
jugCPU = random.choice(["Piedra","Papel","Tijera"]) 
 
# Complete el resto del código a partir de aquí
jugJug = input("¿Cuál es su jugada? ")
print()
print("Ha elegido", jugJug)
print("El ordenador había elegido", jugCPU)

if jugJug == jugCPU:
  print("Empate :|")
elif (jugJug == "Piedra" and jugCPU == "Tijera") or (jugJug == "Tijera" and jugCPU == "Papel") or (jugJug == "Papel" and jugCPU == "Piedra"):
  print("Ha ganado :)")
else:
  print("Ha perdido :(")
