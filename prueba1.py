import tkinter as tk
from services.my_sql import conectar

def cargar_login(ventana):
    login_panel = tk.Frame(
        ventana,
        bg = "black",
        padx = 0,
        pady = 0,
        width = 1000,
        height = 540,
        )

#Formulario
    titulo = tk.Label(login_panel, text="Filtrar datos")
    titulo.pack()

#usario
    usuario = tk.Label(login_panel, text="Ingrese usuario")
    usuario.pack()

    entrada_usuario = tk.Entry(login_panel)
    entrada_usuario.pack()

    def funcion_boton():
        datousuario = entrada_usuario.get()
        print(conectar("SELECT * FROM usuario WHERE nombres ='Ana María'"))

    boton = tk.Button(login_panel, text="Consultar", command=funcion_boton)
    boton.pack()






    login_panel.pack()
    print("usuario cargado")

