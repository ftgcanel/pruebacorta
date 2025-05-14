import tkinter as tk
from pruebacorta.prueba1 import cargar_login
ventana = tk.Tk()
ventana.title("Filtrar datos")
ventana.geometry("800x500")

cargar_login(ventana)


ventana.mainloop()
