from json import load

f = open("songs.txt")
SONGS = load(f)
f.close()

# 1
print("1.- Título de la canción 79:", SONGS[78]["title"])
# 2
print("2.- Género de la última canción:", SONGS[-1]["top genre"])
# 3
print("3.- Cantidad de canciones:", len(SONGS))
# 4
tiempo = 0
for s in SONGS:
    tiempo += s["length"]
print("4.- Tiempo en segundo:", tiempo)
print("4.- Tiempo:", tiempo//3600,":", (tiempo%3600)//60,":", tiempo %60, sep="")
# 5
canciones_2021 = 0
for s in SONGS:
    if s["year"] == 2021:
        canciones_2021 += 1
print("5.- Cantidad de canciones de 2021: ", canciones_2021)
# 6 
tempo = 0
cantidad = 0
for s in SONGS:
    if s["top genre"] == "dance pop":
        cantidad += 1
        tempo += s["beats.per.minute"]
print(f"6.- Tempo medio de dance pop: {tempo/cantidad:.2f}")
# 7
antigua = SONGS[0]
for s in SONGS:
    if s["year"] < antigua["year"]:
        antigua = s
print("7.- La más antigua:", antigua["title"],antigua["year"])
# 8
corta = SONGS[0]
for s in SONGS:
    if s["length"] <= corta["length"]:
        corta = s
print("8.- La más corta:", corta["title"],corta["length"])
# 9
enérgica = SONGS[0]
for s in SONGS:
    if s["energy"] > enérgica["energy"]:
        enérgica = s
print("9.- La más enérgica:", enérgica["title"])
# 10
artistas = []
for s in SONGS:
    if s["artist"] not in artistas:
        artistas.append(s["artist"])
print("10.- Cantidad de artistas:", len(artistas))
# 11
print("11.- 10 últimos artistas:", ":-:".join(artistas[-10:]))
# 12
can_gen = {}
for s in SONGS:
    genero = s["top genre"]
    if genero in can_gen:
        can_gen[genero] += 1
    else:
        can_gen[genero] = 1
print("12.- Cantidad de canciones de pop:", can_gen["pop"])
# 13
gen_max = ""
canciones = 0
for gen, can in can_gen.items():
    if can > canciones:
        gen_max = gen
        canciones = can
print("13.- Género con más canciones:", gen_max, canciones)

        

