import random

def jugar():
# Generar número secreto entre 1 y 100
    numero_secreto = random.randint(1, 100)

    print("🎮 Bienvenido al juego: Adivina el número")
    print("Estoy pensando en un número entre 1 y 100")

    # Bucle infinito hasta que el usuario adivine
    while True:
        numero_usuario = int(input("Ingresa tu número: "))

        if numero_usuario > numero_secreto:
            print("📉 El número secreto es MENOR")
        elif numero_usuario < numero_secreto:
            print("📈 El número secreto es MAYOR")
        else:
            print("🎉 ¡Correcto! Adivinaste el número")
            break # Sale del bucle cuando acierta