ciudades = {
    "Madrid":3266126,
    "Barcelona":1636762,
    "Valencia":794288,
    "Sevilla":688592,
    "Zaragoza":674997,
    "Málaga":574654,
    "Murcia":453258,
    "Palma de Mallorca": 416065,
    "Las Palmas de Gran Canarias": 379925,
    "Bilbao":346843
}
print(ciudades)
poblacion = 0
for k,v in ciudades.items():
    poblacion += v
    
poblacion_media = poblacion / len(ciudades)

print ( poblacion_media)

    
