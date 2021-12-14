t = "Stan Lee: 1922, 96"
nombre, resto = t.split(":")
nac, edad = resto.split(",")
print(f"{nombre} vivió desde {int(nac)} hasta {int(nac) + int(edad)}")
