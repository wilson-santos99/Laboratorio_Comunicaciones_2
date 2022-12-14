import tkinter as tk
from PIL import ImageTk, Image
from operator import xor
import random
from sympy import Matrix
import numpy as np
FONT = ("calbri", 20, "bold")
class Interfaz:
    def __init__(self, master):
        ancho = 1000    
        alto = 500
        tamaño = str(ancho)+"x"+str(alto)
        master.geometry(tamaño)
        master.title("CHAT GUI")
        master.iconbitmap('C:/Users/santo/Documents/GitHub/Laboratorio_Comunicaciones_2/Practica 3/icono.ico')
        master.resizable(False,False)
        master.eval('tk::PlaceWindow . center')
        self.texto_plano = tk.StringVar(master, value="")
        self.texto_cifrado = tk.StringVar(master, value="")
        self.clave = tk.IntVar(master)
        # Create an object of tkinter ImageTk

        # Create a photoimage object of the image in the path
        image1 = Image.open("C:/Users/santo/Documents/GitHub/Laboratorio_Comunicaciones_2/Practica 3/rsz_logo1.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.image = test
        # Position image
        label1.grid(row=0,column=1)
        # texto_plano controls
        self.plain_label = tk.Label(master, text="Texto a Cifrar", fg="black", font=FONT).grid(row=1, column=0)
        self.plain_entry = tk.Entry(master,
                                    textvariable=self.texto_plano, width=50, font=FONT)
        self.plain_entry.grid(row=1, column=1, padx=20)
        self.button_encriptar = tk.Button(master, text="Encriptar",
                                        command=lambda: self.encriptar_callback(), font=FONT).grid(row=2, column=1)
        self.borrar_texto_a_cifrar = tk.Button(master, text="Borrar",
                                     command=lambda: self.vaciar('texto_a_cifrar'), font=FONT).grid(row=2, column=0)

        # clave controls
        self.clave_label = tk.Label(master, text="clave", font=FONT).grid(row=3, column=0)
        self.clave_entry = tk.Entry(master, textvariable=self.clave, width=10, font=FONT).grid(row=3, column=1,
                                                                                           sticky=tk.W, padx=20)

        # texto_cifrado controls
        self.cifrado_label = tk.Label(master, text="texto cifrado", fg="black", font=FONT).grid(row=4, column=0)
        self.texto_cifrado_entry = tk.Entry(master,
                                     textvariable=self.texto_cifrado, width=50, font=FONT)
        self.texto_cifrado_entry.grid(row=4, column=1, padx=20)
        self.desencriptar_button = tk.Button(master, text="Desencriptar",
                                        command=lambda: self.decrypt_callback(), font=FONT).grid(row=5, column=1)
        self.borrar_cifrado = tk.Button(master, text="Borrar",
                                      command=lambda: self.vaciar('texto_cifrado'), font=FONT).grid(row=5, column=0)

    def vaciar(self, str_val):
        if str_val == 'texto_cifrado':
            self.texto_cifrado_entry.delete(0, 'end')
        elif str_val == 'texto_a_cifrar':
            self.plain_entry.delete(0, 'end')

    def obtener_clave(self):
        try:
            clave_val = self.clave.get()
            return clave_val
        except tk.TclError:
            pass
###########################


######
    def encriptar_callback(self):
        cifrado_tipo=random.randint(0,2)
        print()
        if cifrado_tipo == 0:
            print("ha seleccionado cifrado cesar")
            clave = self.obtener_clave()
            texto_cifrado = cifrado_cesar(self.plain_entry.get()+'c', clave)
            self.texto_cifrado_entry.delete(0, tk.END)
            self.texto_cifrado_entry.insert(0, texto_cifrado)
           
        if cifrado_tipo==1: 
            print("ha seleccionado cifrado Hill")
            clave = self.obtener_clave()
            texto_cifrado = cifradohill(self.plain_entry.get()+'h', clave)
            self.texto_cifrado_entry.delete(0, tk.END)
            self.texto_cifrado_entry.insert(0, texto_cifrado)
        if cifrado_tipo ==2:
            print("ha seleccionado cifrado propio")
            clave = self.obtener_clave()
            texto_cifrado = cifradopropio(self.plain_entry.get()+'p', clave)
            self.texto_cifrado_entry.delete(0, tk.END)
            self.texto_cifrado_entry.insert(0, texto_cifrado)
    
    def decrypt_callback(self):
        clave = self.obtener_clave()
        texto_plano = descifrado_cesar(self.texto_cifrado_entry.get(), clave)
        self.plain_entry.delete(0, tk.END)
        self.plain_entry.insert(0, texto_plano)


###################################################################################3333333333333333333333
def cifrado_cesar (plaintext, clave):   #funcion cuyo argumento es el texto que se ingresara por consolda 
    #posicion1 = int(input(("Ingrese la llave>>: "))) #solicita el numero de posiciones que se movera hacia la derecha
    alfabeto_min = "abcdefghijklmnopqrstuvwxyz"  #creamos variable con alfabetro en minusculas
    alfabeto_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #creamos variable con alfabeto en mayusculas
    longitud_alfabeto = len(alfabeto_min) #determinamos la longitud de la variable alfabeto
    texto_cifrado= ""  #variable que almacenara el mensaje cifrado
    
    for letra in plaintext:  #inicia una variable letra que ira recorriendo cada caracter del texto 
        if not letra.isalpha() or letra.lower() == 'ñ':  #si el texto contiene una letra ñ el codigo lo deja tal y como esta
            texto_cifrado+= letra  #la variable texto_cifradoalmacenara cada letra y las concatenara
            continue  #continua el proceso a la siguiente linea
        valor_letra = ord(letra)  #recibe un carácter y devuelve su representación en código unicode
        alfabeto_a_usar = alfabeto_min  #si el texto es minuscula utilizara el alfabeto en minuscula
        limite = 97   #limite unicode minuscula     
        if letra.isupper():     #si la letra es mayuscula
            limite = 65 #limiite unicode mayuscula
            alfabeto_a_usar = alfabeto_may #utilizara el alfabeto mayuscula
        posicion = (valor_letra - limite + clave) % longitud_alfabeto   #posicioin que movemos a la derecha
        texto_cifrado+= alfabeto_a_usar[posicion]  #regresa los valores a letras y las concatena
    return texto_cifrado #devuelve la variable codificado_cesar

def descifrado_cesar(texto_cifrado, clave):
    texto_descifrado = "" #variable que almacenara el mensaje descifrado
    #posicion1 = int(input(("Ingrese la llave>>: "))) #solicita el numero de posiciones que se movio a la derecha el texto original
    alfabeto_min = "abcdefghijklmnopqrstuvwxyz" #creamos variable con alfabetro en minusculas
    alfabeto_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #creamos variable con alfabetro en minusculas
    longitud_alfabeto = len(alfabeto_min) #determinamos la longitud de la variable alfabeto
    
    for letra in texto_cifrado : #inicia una variable letra que ira recorriendo cada caracter del texto 
        if not letra.isalpha() or letra.lower() == 'ñ':  #si el texto contiene una letra ñ el codigo lo deja tal y como esta
            texto_descifrado += letra #la variable texto_cifrado  almacenara cada letra y las concatenara
            continue #continua el proceso a la siguiente linea
        valor_letra = ord(letra)  #recibe un carácter y devuelve su representación en código unicode
        alfabeto_a_usar = alfabeto_min   #si el texto es minuscula utilizara el alfabeto en minuscula
        limite = 97   #limite unicode minuscula 
        if letra.isupper():   #si la letra es mayuscula
            limite = 65  #limiite unicode mayuscula
            alfabeto_a_usar = alfabeto_may #utilizara el alfabeto mayuscula
        posicion = (valor_letra - limite +26-clave) % longitud_alfabeto #uso el complemento de 26-posicion
        texto_descifrado  += alfabeto_a_usar[posicion]  #regresa los valores a letras y las concatena
    return texto_descifrado #devuelve el texto cifrado en la variable decod_cesar
###################################################################################3333333333333333333333###################################################################################3333333333333333333333
separador = " " 

diccionario_encryt = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
            'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
            '0':26, '1': 27, '2':28, '3':29, '4':30, '5':31, '6':32, '7':33, '8':34, '9':35, '.': 36, ',': 37, ':': 38, '?': 39 , ' ': 40}

diccionario_decrypt = {'0' : 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M',
            '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z', '26': '0',
            '27': '1', '28': '2', '29': '3', '30': '4', '31': '5', '32' : '6', '33' : '7', '34' : '8', '35' : '9', '36' : '.', '37' : ',', '38' : ':', '39' : '?', '40' : ' '}

#----------------------Funciones ----------------------------------

def binario_a_ascii(binario):
    # Convertir binario a decimal
    valor = int(binario, 2)
    # Convertir el decimal a su representación ASCII
    return chr(valor)

def ascii_a_binario(letra):
    # Extraer su valor entero
    valor = ord(letra)
    # Convertirlo a binario
    return "{0:08b}".format(valor)

def texto_a_binario(texto):
    texto_binario = ""  # El resultado
    contador = 0
    for letra in texto:
        texto_binario += ascii_a_binario(letra)
        # Agregar un espacio entre binarios, excepto si es el último carácter
        if contador + 1 < len(texto):
            texto_binario += separador
        contador += 1
    return texto_binario

def binario_a_texto(texto_binario):
    texto_plano = ""
    for binario in texto_binario.split(separador):
        texto_plano += binario_a_ascii(binario)
    return texto_plano
######## Función convertir binario a decimal
def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    binario = binario[::-1]
    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

##########################################CIFRADO  Y DeSCIFRADO PROPIO
def cifradopropio (txt):
    tipcifra = random.randint(0,2)
    print("")
    if tipcifra  == 0:
        txt= txt.replace("m","0")
        txt= txt.replace("u","1")
        txt= txt.replace("r","2")
        txt= txt.replace("c","3")
        txt= txt.replace("i","4")
        txt= txt.replace("e","5")
        txt= txt.replace("l","6")
        txt= txt.replace("a","7")
        txt= txt.replace("g","8")
        txt= txt.replace("o","9")
    if tipcifra  == 1:
        txt= txt.replace("n","0")
        txt= txt.replace("e","1")
        txt= txt.replace("u","2")
        txt= txt.replace("m","3")
        txt= txt.replace("a","4")
        txt= txt.replace("t","5")
        txt= txt.replace("i","6")
        txt= txt.replace("c","7")
        txt= txt.replace("o","8")
        txt= txt.replace("s","9")

    if tipcifra  == 2:
        txt= txt.replace("e","0")
        txt= txt.replace("u","1")
        txt= txt.replace("c","2")
        txt= txt.replace("a","3")
        txt= txt.replace("l","4")
        txt= txt.replace("i","5")
        txt= txt.replace("p","6")
        txt= txt.replace("t","7")
        txt= txt.replace("o","8")
        txt= txt.replace("s","9")
    msg = txt+str(tipcifra)
    return (msg)

def descifrado_propio(txt):
	ultcar = txt[-1]
	if ultcar == '0':
		txt= txt.replace("0","m")
		txt= txt.replace("1","u")
		txt= txt.replace("2","r")
		txt= txt.replace("3","c")
		txt= txt.replace("4","i")
		txt= txt.replace("5","e")
		txt= txt.replace("6","l")
		txt= txt.replace("7","a")
		txt= txt.replace("8","g")
		txt= txt.replace("9","o")
	if ultcar == '1':
		txt= txt.replace("0","n")
		txt= txt.replace("1","e")
		txt= txt.replace("2","u")
		txt= txt.replace("3","m")
		txt= txt.replace("4","a")
		txt= txt.replace("5","t")
		txt= txt.replace("6","i")
		txt= txt.replace("7","c")
		txt= txt.replace("8","o")
		txt= txt.replace("9","s")
	if ultcar == '2':
		txt= txt.replace("0","e")
		txt= txt.replace("1","u")
		txt= txt.replace("2","c")
		txt= txt.replace("3","a")
		txt= txt.replace("4","l")
		txt= txt.replace("5","i")
		txt= txt.replace("6","p")
		txt= txt.replace("7","t")
		txt= txt.replace("8","o")
		txt= txt.replace("9","s")
	final_str = txt[:-1] 
	return (final_str)


#############################CODIGO HAMMING
def xor_5(num1,num2,num3,num4,num5):
    a = xor(num1,num2)
    b = xor(a,num3)
    c = xor(b,num4)
    d = xor(c,num5)
    return (d)

def xor_3(num1,num2,num3):
    a = xor(num1,num2)
    b = xor(a,num3)
    return (b)

def hamming(mensaje_a_codificar):
    arreglo = list(mensaje_a_codificar)
    letra_a_binario = [ascii_a_binario(num) for num in arreglo]
    for index, value in enumerate(letra_a_binario):        
        l = str(value)
        letra = l[1:]
        letra_a_binario[index] = letra
        d1 = int(letra[0])
        d2 = int(letra[1])
        d3 = int(letra[2])
        d4 = int(letra[3])
        d5 = int(letra[4])
        d6 = int(letra[5])
        d7 = int(letra[6])
        p1 = xor_5(d1,d2,d4,d5,d7)
        p2 = xor_5(d1,d3,d4,d6,d7)
        p3 = xor_3(d2,d3,d4)
        p4 = xor_3(d5,d6,d7)
        letraH = str(p1)+str(p2)+str(d1)+str(p3)+str(d2)+str(d3)+str(d4)+str(p4)+str(d5)+str(d6)+str(d7)
        letra_a_binario[index] = letraH
    return (letra_a_binario)

    ###############################################################CIFRADO Y DESCIFRADO CESAR
def cifradohill(message, key):
    ciphertext = ''
    matrix_mensaje = []
    list_temp = []
    cifrado_final = ''
    ciphertext_temp = ''
    cont = 0
    # Convertir el mensaje a mayusculas
    message = message.upper()
    # Si el tamaño del mensaje es menor o igual al tamaño de la clave
    if len(message) <= len(key):
        # Convertir el tamaño del mensaje al tamaño de la clave, si no es igual, se añaden 'X' hasta que sean iguales los tamaños.
        while len(message) < len(key):
            message = message + 'X'

        # Crear la matriz para el mensaje

        for i in range(0, len(message)):
            matrix_mensaje.append(diccionario_encryt[message[i]])

        # Se crea la matriz

        matrix_mensaje = np.array(matrix_mensaje)

        # Se multiplica la matriz clave por la de mensaje

        cifrado = np.matmul(key, matrix_mensaje)

        # Se obtiene el modulo sobre el diccionario de cada celda

        cifrado = cifrado % 41

        # Se codifica de valores numericos a los del diccionario, añadiendo a ciphertext el valor en el diccionario pasandole como indice la i posicion de la variable cifrado

        for i in range(0, len(cifrado)):
            ciphertext += diccionario_decrypt[str(cifrado[i])]
    else:

    # Si el tamaño del mensaje es menor o igual al tamaño de la clave

        # Si al dividir en trozos del tamaño de la clave, existe algun trozo que tiene menos caracteres que la long. de la clave se añaden tantas 'X' como falten

        while len(message) % len(key) != 0:
            message = message + 'X'

        # Se troce el mensaje en subsstrings de tamaño len(key) y se alamcenan como valores de un array

        matrix_mensaje = [message[i:i + len(key)] for i in range(0,
                          len(message), len(key))]

        # Para cada valor del array (grupo de caracteres de la longitud de la clave)

        for bloque in matrix_mensaje:

            # Crear la matriz para el bloque

            for i in range(0, len(bloque)):
                list_temp.append(diccionario_encryt[bloque[i]])

            # Se crea la matriz de ese bloque

            matrix_encrypt = np.array(list_temp)

            # Se multiplica la matriz clave por la del bloque

            cifrado = np.matmul(key, matrix_encrypt)

            # Se obtiene el modulo sobre el diccionario de cada celda

            cifrado = cifrado % 41

            # Se codifica de valores numericos a los del diccionario, añadiendo a ciphertext el valor en el diccionario pasandole como indice la i posicion de la variable cifrado

            for i in range(0, len(cifrado)):
                ciphertext_temp += diccionario_decrypt[str(cifrado[i])]

            # Se inicializan las variables para el nuevo bloque

            matrix_encrypt = []
            list_temp = []

        # Se añade el mensaje encriptado a la variable que contiene el mensaje encriptado completo

        ciphertext = ciphertext_temp

    # --------------------------------

    return ciphertext
###################################################################################################################
def descifrado_hill(message, key):


    plaintext = ''

    matrix_mensaje = []
    plaintext_temp = ''
    list_temp = []
    matrix_inversa = []
    matrix_mensaje = [message[i:i + len(key)] for i in range(0,
                      len(message), len(key))]

    # Se calcula la matriz inversa aplicando el modulo 41

    matrix_inversa = Matrix(key).inv_mod(41)

    # Se transforma en una matriz

    matrix_inversa = np.array(matrix_inversa)

    # Se pasan los elementos a float

    matrix_inversa = matrix_inversa.astype(float)

    # Para cada bloque

    for bloque in matrix_mensaje:

        # Se encripta el mensaje encriptado

        for i in range(0, len(bloque)):
            list_temp.append(diccionario_encryt[bloque[i]])

        # Se convierte a matriz

        matrix_encrypt = np.array(list_temp)

        # Se multiplica la matriz inversa por el bloque

        cifrado = np.matmul(matrix_inversa, matrix_encrypt)

        # Se le aplica a cada elemento el modulo 41

        cifrado = np.remainder(cifrado, 41).flatten()

        # Se desencripta el mensaje

        for i in range(0, len(cifrado)):
            plaintext_temp += diccionario_decrypt[str(int(cifrado[i]))]

        matrix_encrypt = []
        list_temp = []
    plaintext = plaintext_temp

    # Se eleminan las X procedentes de su addicion en la encriptacion para tener bloques del tamaño de la clave

    while plaintext[-1] == 'X':
        plaintext = plaintext.rstrip(plaintext[-1])

    return plaintext

#------------Mensaje recibido----------------#
###################################################################################3333333333333333333333###################################################################################3333333333333333333333
if __name__ == "__main__":
    root = tk.Tk()
    caesar = Interfaz(root)
    root.mainloop()