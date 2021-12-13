libro1 = {
    "título": "El Marciano",
    "autor": "Andy Weir",
    "editorial": "Nova",
    "precio": 20.5,
    "páginas": 407
    }
print(libro1["autor"])

texto = "Dune # Frank Herbert # Debolsillo (Pengun Ed.) 784 11.35"

título, autor, resto = texto.split("#")

libro2 = {
    "título": título.strip(),
    "autor": autor.strip()
    }

d = resto.split()
libro2["precio"] = float(d[-1])
libro2["páginas"] = int(d[-2])
libro2["editorial"] = " ".join(d[:-2])

print(libro2)

if libro1["páginas"] > libro2["páginas"]:
    print(f"El libro {libro1['título']} tiene más páginas ({libro1['páginas']})")
else:
    print(f"El libro {libro2['título']} tiene más páginas ({libro2['páginas']})")

print(libro1)
if libro1["precio"] > libro2["precio"]:
    libro1["precio"] = libro1["precio"]*0.95
else:
    libro2["precio"] *= 0.95 # libro2["precio"] = libro2["precio"]*0.95

print(libro1)
