import random 
 
VERSION = 0.1 
print("Bienvenido a Piedra, Papel o Tijera v", VERSION, sep = "") 
 
print("Las jugadas disponibles son Piedra, Papel y Tijera") 

ganada_jug = 0
ganada_cpu = 0
ronda = 0

max_rondas = int(input("¿Cuántas rondas quiere jugar? "))
print()

while ronda < max_rondas and abs(ganada_jug - ganada_cpu) < (max_rondas - ronda):
  print("Ronda ", ronda+1,":", sep="")
  print("Eligiendo la jugada del ordenador ...") 
  jugCPU = random.choice(["Piedra","Papel","Tijera"]) 
 
  jugJug = input("¿Cuál es su jugada? ")

  print()
  print("Ha elegido", jugJug)
  print("El ordenador había elegido", jugCPU)

  if jugJug == jugCPU:
    print("Empate :|")
  elif (jugJug == "Piedra" and jugCPU == "Tijera") or (jugJug == "Tijera" and jugCPU == "Papel") or (jugJug == "Papel" and jugCPU == "Piedra"):
    print("Ha ganado :)")
    ganada_jug += 1
  else:
    print("Ha perdido :(")
    ganada_cpu += 1
  ronda += 1
  print()

print("Tanteo final: Jugador",ganada_jug,"-", ganada_cpu, "CPU")
if ganada_jug > ganada_cpu:
  print("Enhorabuena, ¡has vencido a Skynet!")
elif ganada_jug == ganada_cpu:
  print("Ambos os retiráis pensando en la próxima vez tras el empate")
else:
  print("¡Fracaso absoluto! Skynet domina el mundo")
