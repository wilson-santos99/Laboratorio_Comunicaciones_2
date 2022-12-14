import tkinter as tk
from PIL import ImageTk, Image
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

    def encriptar_callback(self):
        clave = self.obtener_clave()
        texto_cifrado = cifrado_cesar(self.plain_entry.get(), clave)
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
###################################################################################3333333333333333333333


if __name__ == "__main__":
    root = tk.Tk()
    caesar = Interfaz(root)
    root.mainloop()