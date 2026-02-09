import random
puntos = 0 #UN PUNTO POR CADA LETRA ADIVINADA, AL SER IGUAL A PUNTOS_PALABRA, SE GANA EL JUEGO
letras_seleccionadas = [] #LISTA

def elegir_palabra(palabras): # RECIBE LA LISTA DE PALABRAS Y RETORNA UNA LISTA CON LAS LETRAS DA UNA PALABRA
    seleccion = palabras[random.randint(0, len(palabras) - 1 )] #SELECCIONA UN NÚMERO AL AZAR, ESE SERÁ EL INDICE DE LA PALABRA SELECCIONADA
    return  list(seleccion) #RETORNA UNA LISTA CON LAS LETRAS DE LA PALABRA DEL SUBINDICE ELEGIDO CON RANDOM

def ocultar_letras(palabra_elegida): #RECIBE UNA LISTA CON LAS LETRAS DE LA PALABRA Y RETORNA UNA LISTA CON CADA UNA DE LAS LETRAS OCULTAS
    palabra_oculta = palabra_elegida.copy()
    contador = 0 #CONTAMOS PARA ACCEDER A LOS SUBINDICES DE CADA LETRA
    for letra in palabra_oculta: #RECORREMOS LAS LETRAS DE LA PALABRA
        palabra_oculta[contador] = " _ " #REMPLAZAMOS CADA LETRA POR UN " _ "
        contador +=1 #AUMENTAMOS EL CONTADOR PARA EL SIGUIENTE
    return palabra_oculta #RETORNA UNA LISTA CON LAS LETRAS DE LA PALABRA REMPLAZADAS POR UN _

def mostrar_lista(lista): #RECIBE UNA LISTA Y RETORNA LOS ELEMENTOS CONCATENADOS
    mostrar = ""
    for item in lista:
        mostrar += item #CONCATENA LOS ELEMENTOS DE LA LISTA PARA QUE QUEDEN TODOS EN UNA CADENA
    return mostrar 

def input_letra(): #EL USUARIO INGRESA UNA LETRA, LA VALIDA Y RETORNA LA LETRA SELECCIONADA
    while True:
        letra_usuario = input("Ingrese una letra: ")
        if not se_repite(letra_usuario,letras_seleccionadas):
            if len(letra_usuario) == 1:
                return letra_usuario.upper() #SI EL USUARIO INGRESÓ UN SOLO CARACTER, CONTINUA EL PROGRAMA
            else:
                print("Debe ingresar una sola letra") #PIDE INGRESAR UNA SOLA LETRA
        else:
            print("Ya seleccionaste esa letra") #AVISO AL USUARIO QUE ESTÁ REPITIENDO LA LETRA

def se_repite(letra, letras_seleccionadas): #RECIBE LA LETRA SELECCIONADA Y LA LISTA DE LETRAS SELECCIONADAS, RETORNA TRUE O FALSE
    for letra_seleccionada in letras_seleccionadas: #RECORREMOS LA LISTA DE LAS LETRAS SELECCIONADAS
        if letra.upper() == letra_seleccionada: #SI LA LETRA ELEGIDA SE ENCUENTRA DENTRO DE LA LISTA
            return True
    return False

def mostrar_incognita(letra_seleccionada, palabra, palabra_oculta): #RECIBE LA LETRA SELECCIONADA, LA LISTA DE LAS LETRAS DE LA PALABRA PARA MODIFICAR LA LISTA DE LETRAS OCULTA
    contador = 0 #COINTADOR PARA LLAMAR A LOS SUBINDICES DE LAS LISTAS
    for letra in palabra: #RECORREMOS LAS LETRAS DE LA PALABRA
        if letra == letra_seleccionada: #SI LA LETRA SELECCIONADA POR EL USUARIO COINCIDE CON ALGUNA LETRA DE LA PALABRA
            if palabra_oculta[contador] != letra_seleccionada: #SI LA LETRA ESTÁ OCULTA ( _ )
                palabra_oculta[contador] = letra_seleccionada #REMPLAZAMOS EL _ POR LA LETRA
                global puntos #MODIFICAMOS LOS PUNTOS DE FORMA GLOBAL POR CONVENIENCIA
                puntos += 1 #SE AUMENTA UN PUNTO POR CADA LETRA QUE SE ADIVINE
        contador += 1

def esta_en_palabra(letra, palabra): #RECIBE UNA LETRA Y UNA LISTA CON LAS LETRAS DE LA PALABRA Y RETORNA TRUE O FALSE
    for caracter in palabra: #RECORREMOS LAS LETRAS DE LA LISTA
        if caracter == letra: #SI LA LETRA INGRESADA SE ENCUENTRA DENTRO DE LA LISTA
            return True 
    return False


def jugar(): #FUNCION PRINCIPAL DEL JUEGO
    #FIJAMOS LOS VALORES DE LAS VARIABLES
    global puntos #TRABAJAMOS CON LOS PUNTOS DE FORMA GLOBAL POR CONVENIENCIA
    puntos = 0 #PUNTAJE (CANTIDAD DE LETRAS ADIVINADAS)
    vidas = 4 #CANTIDAD DE VIDAS CON LAS QUE COMIENZA
    letras_seleccionadas.clear() #VACIAMOS LA LISTA SI ES QUE ES LA SEGUNDA VEZ QUE JUGAMOS

    #ELEGIMOS LA PALABRA A ADIVINAR, EL PUNTAJE ASIGNADO Y OCULTAMOS LAS LETRAS
    palabras = ["CABEZA", "JUEGO", "SALTAR", "AUDIO", "ELEMENTO", "VOLAR", "CUADERNO", "TECLADO", "DIBUJO"] #LISTA CON LAS PALABRAS QUE PUEDEN SALIR
    palabra = elegir_palabra(palabras) #LISTA CON LAS LETRAS DE LA PALABRA SELECCIONADA
    puntos_palabra = len(palabra) #CANTIDAD DE LETRAS QUE HAY QUE ADIVINAR
    palabra_incognita = ocultar_letras(palabra) #LISTA

    # ----- COMIENZA EL JUEGO --------
    print("Se ha seleccionado una palabra!")
    #CICLO EN EL QUE SE JUEGA
    while vidas > 0: #MIENTRAS NO PIERDA TODAS LAS VIDAS
        #MOSTRAMOS EL HUD VIDAS ---- LETRAS QUE YA SELECCIONAMOS
        print(f"Vidas restantes: {vidas}       Letras seleccionadas: {mostrar_lista(letras_seleccionadas)} ") 
        
        #MOSTRAMOS LA PALABRA INCOGNITA ( _ _ _ _ _)
        print(f"La palabra es:{mostrar_lista(palabra_incognita)}\n")

        #EL USUARIO INGRESA UNA LETRA
        letra_seleccionada = input_letra() #EL USUARIO INGRESA UNA LETRA
        print(f"Eligió la letra {letra_seleccionada.upper()} ...") #MENSAJE PARA EL USUARIO
        letras_seleccionadas.append(letra_seleccionada.upper()) #AGREGAMOS LA LETRA A LA LISTA DE LETRAS SELECCIONADAS

        #SI LA LETRA SE ENCUENTRA EN LA PALABRA
        if esta_en_palabra(letra_seleccionada, palabra): #DETERMINAMOS SI LA LETRA SE ENCUENTRA EN LA PALABRA
            print("La letra se encuentra en la palabra") 

            #MOSTRAMOS EL DISPLAY DE LA INCOGNITA ACTUALIZADO
            mostrar_incognita(letra_seleccionada, palabra, palabra_incognita) 

            #SI CON LA LETRA OBTIENE TODOS LOS PUNTOS
            if puntos == puntos_palabra: #SI LOS PUNTOS OBTENIDOS SON IGUALES A LOS DE LA PALABRA
                break #SALIMOS DEL CICLO DEL JUEGO PORQUE SE GANÓ
    
        #SI LA LETRA NO SE ENCUENTRA EN LA PALABRA
        else:
            #QUITAMOS UNA VIDA
            vidas -= 1
            print("La letra no se encuentra en la palabra, pierdes una vida")

    #AL SALIR DEL CICLO DEL JUEGO
    if vidas == 0: #SI PIERDE TODAS LAS VIDAS --GAME OVER --
        print("""
¡Lo lamento!
Te quedaste sin vidas.""")
        print(f"La palabra era {mostrar_lista(palabra)}") #MOSTRAMOS LA PALABRA

    else: #SI OBTIENE TODOS LOS PUTNOS DE LA PALABRA -- ADIVINÓ LA PALABRA
        print("""
¡Lo has logrado!
¡Encontraste la palabra!
""")
        print(f"La palabra era :{mostrar_lista(palabra_incognita)}\n") 
