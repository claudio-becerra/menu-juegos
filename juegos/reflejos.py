import time, random

def jugar():
    print('''
    😱JUEGO DE REFLEJOS
    Cuando veas en la pantalla la palabra "YA!"
    Presiona enter lo mas rapido posible
    Preparate....
    ''')

    esperar = random.randint(3, 10)
    time.sleep(esperar)

    print("🤯YA!")

    inicio = time.time()

    input()

    fin = time.time()

    tiempo_reaccion = fin - inicio

    print(f"Tu tiempo de reaccion fue de {tiempo_reaccion:3f} segundos")

    if tiempo_reaccion < 0.3:
        print("😱 Estas para a F1🏎️")
    elif tiempo_reaccion < 0.6:
        print("😎 Buenos reflejos")
    else:
        print("🐢 Se puede mejorar")