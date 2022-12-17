import tkinter as tk #importamos las librerias necesarias para implementar la interfaz grafica
from PIL import ImageTk, Image  #importamos las librerias necesarias para implementar la interfaz visua y manejo de imagenes
FONT = ("calbri", 20, "bold") #se establece la fuente y tamaño de letra
class Interfaz: #se crea la clase interfaz
    def __init__(self, master): #se define la funcion principal
        ancho = 1000     #se define el ancho de la ventana
        alto = 500      #se define el alto de la ventana
        tamaño = str(ancho)+"x"+str(alto) #se determina el tamaño de la ventana, dado el ancho y alto
        master.geometry(tamaño)#se implementa el tamaño de la ventana
        master.title("PRACTICA #3 COMUNICACIONES 2") #se coloca el titulo de la ventana
        master.iconbitmap('C:/Users/santo/Documents/GitHub/Laboratorio_Comunicaciones_2/Practica 3/icono.ico') #se implementa el icono de la ventana
        master.resizable(False,False) #se bloquea la propiedad de cambio de tamaño de ventana, el tamaño es fijo
        master.eval('tk::PlaceWindow . center')# se establece que la ventana sea centrada
        self.texto_plano = tk.StringVar(master, value="") #se crea la variable string que obtendra los parametros necesarios de texto plano
        self.texto_cifrado = tk.StringVar(master, value="") #se crea la variable string que obtendra el texto cifrado en cesar
        self.clave = tk.IntVar(master) #se crea la variable que obtendra la clave, es decir el numero de espacios desplazados de cesar
        # Crea el objeto de tkinter ImageTk
        # Cree un objeto de fotoimagen de la imagen en la ruta
        image1 = Image.open("C:/Users/santo/Documents/GitHub/Laboratorio_Comunicaciones_2/Practica 3/rsz_logo1.png") #se crea una variable con el path del logo de EIME
        test = ImageTk.PhotoImage(image1) #se crea la imagen
        label1 = tk.Label(image=test) #se crea label 1 y se aplica el parametro imagen
        label1.image = test #se asigna l aimagen al label1
        # Position image
        label1.grid(row=0,column=1) #se determina la ubicacion de la imagen en la columna 1 y fila 0
        # texto_plano controls
        self.plain_label = tk.Label(master, text="Texto a Cifrar", fg="black", font=FONT).grid(row=1, column=0) #se crea un objeto que mostrara el texto a cifrar
        self.plain_entry = tk.Entry(master,  textvariable=self.texto_plano, width=50, font=FONT) #se crea la caja de texto en la que ingresara el texto plano sin cifrar
        self.plain_entry.grid(row=1, column=1, padx=20) #se asigna la ubicacion de la caja de texto  a fila 1 y columa 1
        self.button_encriptar = tk.Button(master, text="Encriptar",command=lambda: self.encriptar_callback(), font=FONT).grid(row=2, column=1) #se crea el button que ejecutara la funcion que se encaraga de encriptar el mensaje
        self.borrar_texto_a_cifrar = tk.Button(master, text="Borrar",command=lambda: self.vaciar('texto_a_cifrar'), font=FONT).grid(row=2, column=0)#se crea el button que ejecutara la funcion de limpiar el campo de texto
        # clave controls
        self.clave_label = tk.Label(master, text="clave", font=FONT).grid(row=3, column=0) #se crea el campo de texto que mostrara el texto "clave"
        self.clave_entry = tk.Entry(master, textvariable=self.clave, width=10, font=FONT).grid(row=3, column=1, sticky=tk.W, padx=20) #se crea la entrada de texto en la que escribiremos la clave de cifrado cesar
        # texto_cifrado controls
        self.cifrado_label = tk.Label(master, text="texto cifrado", fg="black", font=FONT).grid(row=4, column=0) #se crea el campo de texto que imprimira el texto "texto cifrado"
        self.texto_cifrado_entry = tk.Entry(master,textvariable=self.texto_cifrado, width=50, font=FONT)#se crea la entrada del texto cifrado
        self.texto_cifrado_entry.grid(row=4, column=1, padx=20) #se asigna la posicion de la entrada del texto cifrado
        self.desencriptar_button = tk.Button(master, text="Desencriptar", command=lambda: self.decrypt_callback(), font=FONT).grid(row=5, column=1)#se crea el button que ejecutara la funcioin que se encargara de desencriptar el mensaje

        self.borrar_cifrado = tk.Button(master, text="Borrar",command=lambda: self.vaciar('texto_cifrado'), font=FONT).grid(row=5, column=0) #se crea el button que ejecutara la funcion de limpiar el campo de texto


    def vaciar(self, str_val): #funcion que se encargara de limpiar los campos de entrada de texto en la interfaz
        if str_val == 'texto_cifrado': #si se da click en el button que texto_cifrado se vaciara(eliminara) el contenido de entrada de texto cifrado
            self.texto_cifrado_entry.delete(0, 'end') #Vacia la entrada de texto cifrado
        elif str_val == 'texto_a_cifrar': #si se da click en el button que esta en texto a cifrar
            self.plain_entry.delete(0, 'end') #se varia la entrada de campo de texto plano

    def obtener_clave(self): #se crea la funcion que obtendra la clave del cifrado cesar
        try: #si se previenen los posibles ingresos de letras o caracteres invaidos
            clave_val = self.clave.get() #se obtiene la clav e
            return clave_val #retorna la clave
        except tk.TclError: #si ocurre una excepcion se muestra pero no se detiene el programa
            pass

    def encriptar_callback(self): #funcion que se encarga de ejecutar el cifrado cesar
        clave = self.obtener_clave() #obtiene la clave contenida en la entrada de clave
        texto_cifrado = cifrado_cesar(self.plain_entry.get(), clave) #ejecuta la funcion cifrado_cesar, enviando parametros del texto plano y la clave
        self.texto_cifrado_entry.delete(0, tk.END) #borra el contenido en el campo de texto cifrado
        self.texto_cifrado_entry.insert(0, texto_cifrado) #inserta el contenido de la variable texto cifrado en el campo de texto cifrado

    def decrypt_callback(self): #funcioin que se encargara de ejecutar el descifrado cesar
        clave = self.obtener_clave() #obtiene la clave contenida en la entrada de la clave
        texto_plano = descifrado_cesar(self.texto_cifrado_entry.get(), clave) #ejecuta la funcion cifrado_cesar, enviando parametros del texto cifrado en cesar y la clave de descifrado
        self.plain_entry.delete(0, tk.END) #vacia o elimina el contenido de campo de entrada de texto plano
        self.plain_entry.insert(0, texto_plano) #inserta el contenido de la variable texto plano en el campo de entrada de texto plano


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
###################################################################################3333333333333333333333


if __name__ == "__main__": #si _name es igual a __main entonces ejecuta
    root = tk.Tk() #se crea el objeto root que es la ventana visual
    caesar = Interfaz(root) #se ejecuta la clase interfaz y se envia el nombre de la ventana
    root.mainloop() #se muestra la ventana, sin esta linea no se muestra la interfaz visual