from colorama import Fore, Style, init
init()
# Rango de valores que puede tomar cada posición
MIN_VALORES = 3
MAX_VALORES = 9
# Rango de números de posiciones válidos
MIN_POSICIONES = 4
MAX_POSICIONES = 12
# Rango de números de intentos
MIN_INTENTOS = 5
MAX_INTENTOS = 99

# Colores
ROJO = Fore.RED
AMARILLO = Fore.YELLOW
VERDE = Fore.GREEN
NORMAL = Style.RESET_ALL

# "Borra" la pantalla
def borrar_pantalla():
    for i in range(80):
        print()

# Cambia de color el texto
def cambiar_color(color):
    print(color, end="")
    
# Información:
def imprimir_información():
    banner = """ ███▄ ▄███▓ ▄▄▄        ██████ ▄▄▄█████▓▓█████  ██▀███   ███▄ ▄███▓ ██▓ ███▄    █ ▓█████▄ 
▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▒██▀ ██▌
▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒▓██    ▓██░▒██▒▓██  ▀█ ██▒░██   █▌
▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ▒██    ▒██ ░██░▓██▒  ▐▌██▒░▓█▄   ▌
▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒▒██▒   ░██▒░██░▒██░   ▓██░░▒████▓ 
░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ 
░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒ 
░      ░     ░   ▒   ░  ░  ░    ░         ░     ░░   ░ ░      ░    ▒ ░   ░   ░ ░  ░ ░  ░ 
       ░         ░  ░      ░              ░  ░   ░            ░    ░           ░    ░    
                                                                                  ░      """
    borrar_pantalla()
    cambiar_color(ROJO)
    print(banner)
    cambiar_color(AMARILLO)
    print("INFORMACIÓN:")
    cambiar_color(VERDE)
    print("* El juego consiste en adivinar una serie de números (que se pueden repetir)")
    print("* Tras indicar una posible combinación se te mostrará dicha combinación de forma coloreada con el siguiente significado: ")
    print("\t * Si es verde es que has acertado esa posición")
    print("\t * Si es amarillo es que ese número aparece pero no en esa posición")
    print("\t * Si es rojo es que ese número no aparece en ningún sitio")
    input("Pulse el ENTER para continuar ...")
    borrar_pantalla()
    cambiar_color(NORMAL)
    
    

