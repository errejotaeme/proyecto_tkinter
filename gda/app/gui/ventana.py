import tkinter as tk
from tkinter import font
from app.comunes.globales import gb
from app.comunes.idioma import leng
from app.gui.interface import Interface
from app.logica.generador import Generador
from app.logica.gestor import Gestor
from app.logica.tabla import Tabla


class Reseteador:
    """
    Clase que gestiona el reinicio de la aplicación
    y evita la importación circular.
    """
    def reiniciar(self):
        """
        Construye de nuevo la interface cada vez que se modifica el idioma.

        :return: None
        """
        main()
                    

def main():
    # Ventana principal
    raiz = tk.Tk()
    raiz.geometry("1100x640")
    raiz.resizable(True, True)
    x_pantalla = raiz.winfo_screenwidth()
    y_pantalla = raiz.winfo_screenheight()
    raiz.maxsize(x_pantalla,y_pantalla)
    raiz.configure(**gb.ESTILO_MARCO_MOD)
    raiz.title(leng.tex['titulo_app'])

    # Diccionarios que defienen estilos de fuente
    gb.fuente_principal = tk.font.Font(family="Monospace",
                                   size=9,
                                   weight="bold",
                                   slant="roman")

    gb.fuente_titulo = tk.font.Font(family="Monospace",
                                 size=8,
                                 weight="bold",
                                 slant="roman")

    gb.fuente_etiqueta = tk.font.Font(family="Monospace",
                                   size=8,
                                   weight="bold",
                                   slant="roman")

    gb.fuente_entrada = tk.font.Font(family="Monospace",
                                  size=8,
                                  weight="normal",
                                  slant="italic")

    gb.fuente_boton = tk.font.Font(family="Monospace",
                                size=7,
                                weight="normal",
                                slant="roman")

    gb.fuente_boton_salir = tk.font.Font(family="Monospace",
                                      size=7,
                                      weight="normal",
                                      slant="roman")

    # Instancias de las clases de la parte lógica
    gestor = Gestor()
    tabla = Tabla()
    generador = Generador()
    reseteador = Reseteador()

    # Conecta las instancias de la parte lógica
    gestor.enlazar_raiz(raiz)
    gestor.enlazar_tabla(tabla)
    gestor.enlazar_generador(generador)  
    tabla.enlazar_gestor(gestor)

    # Instancia de la clase principal de la parte gráfica
    interface = Interface(raiz, gestor, reseteador)
    
    # Conecta la parte lógica con la gráfica
    gestor.enlazar_interface(interface)
    
    # Inicio del bucle de la aplicación
    interface.ejecutar()
