from juegos import adivina_numero
from juegos import reflejos
from juegos import ahorcado


def mostrar_menu():
    print("###################")
    print("####  Juegos   ####")
    print("###################\n")
    print("Selecciona qué juego quieres jugar")
    print("      --------------------      ")
    print("1 .- Adivina el número")
    print("2 .- Juego de reflejos")
    print("3 .- Ahorcado")
    print("4 .- salir")

def elegir_juego():
    while True:
        mostrar_menu()
        opcion_usuario = input("Ingrese el número de la opción que quiera")
        match opcion_usuario:
            case "1":
                adivina_numero.jugar()
            case "2":
                reflejos.jugar()
            case "3":
                ahorcado.jugar()
            case "4":
                print("Que tengas un buen día")
                break
            case _:
                print("La opción seleccionada no es válida")


if __name__ == "__main__":
    elegir_juego()


