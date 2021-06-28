from tkinter import *
import sys
from tkinter import filedialog as fd
import md4
import md5
import sha1
import sha2


def b_MD4():
    d = entrada.get()
    texto_salida.delete(0, "end")
    texto_salida.insert(0,"MD4: "+ md4.MD4(d.encode()).hexdigest())
    texto_salida.grid(row=4, column=2, padx=10, pady=10, ipadx=130, ipady=60, columnspan=4)


def b_MD5():
    d = entrada.get()
    texto_salida.delete(0, "end")
    texto_salida.insert(0,"MD5: "+md5.MD5(d.encode()).hexdigest())
    texto_salida.grid(row=4, column=2, padx=10, pady=10, ipadx=130, ipady=60, columnspan=4)


def b_SHA1():
    d = entrada.get()
    texto_salida.delete(0, "end")
    texto_salida.insert(0,"SHA1: "+sha1.SHA1(d.encode()).hexdigest())
    texto_salida.grid(row=4, column=2, padx=10, pady=10, ipadx=130, ipady=60, columnspan=4)


def b_SHA256():
    d = entrada.get()
    texto_salida.delete(0, "end")
    texto_salida.insert(0,"SHA256:\n "+sha2.SHA2_256(d.encode()).hexdigest())
    texto_salida.grid(row=4, column=2, padx=10, pady=10, ipadx=130, ipady=60, columnspan=4)



def HMAC():
    d = entrada.get()
    c = clave.get()
    texto_salida.delete(0, "end")
    texto_salida.insert(0,"HMAC: ")
    texto_salida.grid(row=4, column=2, padx=10, pady=10, ipadx=130, ipady=60, columnspan=4)

#------------------------------------------------------------------------------------------

def agregar_menu():
    menubar1 = Menu(ventana)
    ventana.config(menu=menubar1)
    opciones1 = Menu(menubar1, tearoff=0)
    opciones1.add_command(label="Cargar archivo", command=recuperar)
    opciones1.add_command(label="Limpiar", command=limpiar)
    opciones1.add_separator()
    opciones1.add_command(label="Salir", command=salir)
    menubar1.add_cascade(label="Archivo", menu=opciones1)

def salir():
    sys.exit()


def recuperar():
    nombrearch = fd.askopenfilename(initialdir="/", title="Seleccione archivo",
                                    filetypes=(("txt files", "*.txt"), ("todos los archivos", "*.*")))
    if nombrearch != '':
        archi1 = open(nombrearch, "r", encoding="utf-8")
        contenido = archi1.read()
        archi1.close()
        texto_entrada.insert(0, contenido)

def limpiar():
    texto_entrada.delete(0, "end")
    texto_salida.delete(0, "end")


#Dimensiones de los botones
ancho_boton = 11
alto_boton = 3

ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("520x400")
agregar_menu()

#labels
Label(ventana, text="Texto de entrada: ").grid(row=1,column=1)

#texto entrada
entrada = StringVar()
texto_entrada = Entry(ventana, textvariable=entrada)
texto_entrada.grid(row=1,column=2, padx=10, pady=10, ipadx=130, ipady=30, columnspan=4 )



#botones

Button(ventana, text="MD4",bg="grey",  width=ancho_boton, height=alto_boton, command=b_MD4).grid(row=2, column="1",  padx=5, pady=5)
Button(ventana, text="MD5",bg="grey",  width=ancho_boton, height=alto_boton, command=b_MD5).grid(row=2, column="2", padx=5, pady=5)
Button(ventana, text="SHA1",bg="grey",  width=ancho_boton, height=alto_boton, command=b_SHA1).grid(row=2, column="3", padx=5, pady=5)
Button(ventana, text="SHA256",bg="grey",  width=ancho_boton, height=alto_boton, command=b_SHA256).grid(row=2, column="4", padx=5, pady=5)
Button(ventana, text="HMAC",bg="grey",  width=ancho_boton, height=alto_boton, command=HMAC).grid(row=2, column="5", padx=5, pady=5)

#labels
Label(ventana, text="Clave ").grid(row=3,column=1)
#clave para HMAC
clave = StringVar()
texto_clave = Entry(ventana, textvariable=clave, state='disable')
texto_clave.grid(row=3,column=2, padx=10, pady=10, ipadx=130, ipady=5, columnspan=4 )



#labels
Label(ventana, text="Texto de salida: ").grid(row=4,column=1)
texto_salida = Entry(ventana)
texto_salida.grid(row=4, column=2, padx=10, pady=10, ipadx=130, ipady=60, columnspan=4,sticky=W)


ventana.mainloop()