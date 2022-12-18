def cifrado_cesar (txt):   #funcion cuyo argumento es el texto que se ingresara por consolda 
    posicion1 = int(input(("Ingrese la llave>>: "))) #solicita el numero de posiciones que se movera hacia la derecha
    alfabeto_min = "abcdefghijklmnopqrstuvwxyz"  #creamos variable con alfabetro en minusculas
    alfabeto_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #creamos variable con alfabeto en mayusculas
    longitud_alfabeto = len(alfabeto_min) #determinamos la longitud de la variable alfabeto
    codificado_cesar = ""  #variable que almacenara el mensaje cifrado
    for letra in txt:  #inicia una variable letra que ira recorriendo cada caracter del texto 
        if not letra.isalpha() or letra.lower() == 'ñ':  #si el texto contiene una letra ñ el codigo lo deja tal y como esta
            codificado_cesar += letra  #la variable codificado_cesar almacenara cada letra y las concatenara
            continue  #continua el proceso a la siguiente linea
        valor_letra = ord(letra)  #recibe un carácter y devuelve su representación en código unicode
        alfabeto_a_usar = alfabeto_min  #si el texto es minuscula utilizara el alfabeto en minuscula
        limite = 97   #limite unicode minuscula     
        if letra.isupper():     #si la letra es mayuscula
            limite = 65 #limiite unicode mayuscula
            alfabeto_a_usar = alfabeto_may #utilizara el alfabeto mayuscula
        posicion = (valor_letra - limite + posicion1) % longitud_alfabeto   #posicioin que movemos a la derecha
        codificado_cesar += alfabeto_a_usar[posicion]  #regresa los valores a letras y las concatena
    return codificado_cesar #devuelve la variable codificado_cesar

def descifrado_cesar(mensaje,clave):
    
    #posicion1 = int(input(("Ingrese la llave>>: "))) #solicita el numero de posiciones que se movio a la derecha el texto original
    alfabeto_min = "abcdefghijklmnopqrstuvwxyz" #creamos variable con alfabetro en minusculas
    alfabeto_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #creamos variable con alfabetro en minusculas
    longitud_alfabeto = len(alfabeto_min) #determinamos la longitud de la variable alfabeto
    decod_cesar = "" #variable que almacenara el mensaje descifrado
    for letra in mensaje: #inicia una variable letra que ira recorriendo cada caracter del texto 
        if not letra.isalpha() or letra.lower() == 'ñ':  #si el texto contiene una letra ñ el codigo lo deja tal y como esta
            decod_cesar += letra #la variable decod_cesar almacenara cada letra y las concatenara
            continue #continua el proceso a la siguiente linea
        valor_letra = ord(letra)  #recibe un carácter y devuelve su representación en código unicode
        alfabeto_a_usar = alfabeto_min   #si el texto es minuscula utilizara el alfabeto en minuscula
        limite = 97   #limite unicode minuscula 
        if letra.isupper():   #si la letra es mayuscula
            limite = 65  #limiite unicode mayuscula
            alfabeto_a_usar = alfabeto_may #utilizara el alfabeto mayuscula
        posicion = (valor_letra - limite +26-clave) % longitud_alfabeto #uso el complemento de 26-posicion

        
        decod_cesar += alfabeto_a_usar[posicion]  #regresa los valores a letras y las concatena   
    return (decod_cesar) #devuelve el texto cifrado en la variable decod_cesar

# creamos el menu de nuestro programa
def menu():  # creamos el menu de nuestro programa
    print("####################################################################")
    print("#                    PRACTICA 3 COMUNICACIONES 2                   #") #imprime el texto
    print("#                    WILSON SANTOS - 201907179                     #")     #imprime nombre y registro academico
    print("#                      Selecciona una opción                       #")         #imprime texto 
    print("#    \t1 - CIFRAR                                                 #")                  #opcion 1
    print("#    \t2 - DESCIFRAR                                              #")               #opcion 2
    print("####################################################################")

while (True):  ##se establece el ciclo infinito
    menu() # llamamos a la funcion menù
    opcion = int(input("inserta un numero valor>>: ")) #solicitamos al usuaro digitar una opcion
    if(opcion <= 1):  #primera opcion
        txt = input("Mensaje a trasnmitir: ") #------Mensaje que queremos enviar
        cifrado = cifrado_cesar(txt) #la variable cifrado contendra el mensaje cifrado que fue enviado a la funcion cifrado_cesar que contiene el argumento txt
        print("Mensaje cifrado: ",cifrado)      #imprime en consola el texto cifrado 
    elif(opcion == 2):  #segunda  opcion
        print("#############################################")
        print("#        PRACTICA 3 COMUNICACIONES 2        #") #imprime el texto
        print("#         WILSON SANTOS - 201907179         #")     #imprime nombre y registro academico
        print("#              Tiene la clave               #")         #imprime texto 
        print("#    \t1 - SI                              #")                  #opcion 1
        print("#    \t2 - NO                             #")               #opcion 2
        print("#############################################")
        print("Selecciona una opcion:  ") 
        opcion2=int(input("ingrese un numero:  "))
        if(opcion2<=1):
            txt = input("Mensaje a Descifrar: ") #------Mensaje que queremos descifrar
            clave=int(input("ingrese la clave: "))
            mensaje_cifrado_y_codificado = descifrado_cesar(txt,clave) #la variable mensaje_cifrado_y_codificado contendra el mensaje descifrado que fue enviado a la funcion descifrado_cesar que contiene el argumento txt
            print ("El mensaje decifrado es: ","".join(mensaje_cifrado_y_codificado)) #imprime en consola el texto descifrado
            #os.system('cls') # NOTA para windows tienes que cambiar clear por cls
        elif(opcion2<=2):
            print("Descifrando sin la clave")
            txt = input("Mensaje a Descifrar: ") #------Mensaje que queremos descifrar
            print("##################################################################################################################")
            print("\t Desencriptando utilizando las 26 posibles posiciones y determinar a juicio propio el mensaje recibido")
            for clave in range (0,26): 
                mensaje_cifrado_y_codificado = descifrado_cesar(txt,clave) #la variable mensaje_cifrado_y_codificado contendra el mensaje descifrado que fue enviado a la funcion descifrado_cesar que contiene el argumento txt
                print ("clave: ["+str(clave)+"] El mensaje decifrado es: ","".join(mensaje_cifrado_y_codificado)) #imprime en consola el texto descifrado
            #os.system('cls') # NOTA para windows tienes que cambiar clear por cls
            print("##################################################################################################################")
    else:
        tipo_cifrado = int(input("Elegir un cifrado valido: ")) #si ingresamos un numero invalido muestra mensaje




