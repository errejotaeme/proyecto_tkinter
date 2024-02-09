
import tkinter as tk
from tkinter import messagebox
from app.gui.componentes import (
    BorrarCampo,
    CampoBooleano,
    CampoNumerico,
    CampoTexto,
    Encabezado,
    Exportar,
    OpcionesTabla,
    Ruta,
    VerDatos
)
from app.gui.elementos import Boton, NotaEmergente
from app.comunes.globales import gb
from app.comunes.idioma import alternar, leng


class Interface:
    """
    Clase encargada de gestionar la ubicación de los widgets principales
    en paneles y marcos anidados, el cambio de idioma y el arranque
    de la aplicación.
    """
    
    def __init__(self, raiz, gestor, reseteador):
        """
        Constructor de la clase Interface. Contiene las instancias
        de los componentes que permiten el ingreso y la vista de los datos.

        :param raiz: Instancia de la ventana principal (Tk).
        :type raiz: tk.Tk
        :param gestor: Instancia que comunica módulos, tabla y generador.
        :type gestor: Gestor
        :param reseteador: Instancia que permite el reinicio de la aplicación.
        :type reseteador: Reseteador
        """
        self.raiz = raiz
        self.gestor = gestor
        self.reseteador = reseteador

        # Ventana panelizada contiene a todos los widgets
        self.marco_raiz = tk.PanedWindow(
            self.raiz,
            orient=tk.VERTICAL,
            sashwidth=0,
            **gb.ESTILO_MARCO_MOD
        )        
        self.modulo_salir = tk.Frame(
            self.marco_raiz,
            **gb.ESTILO_MARCO_MOD
        )
        self._boton_salir = Boton(
            self.modulo_salir,
            leng.tex['btn_salir'],
            self._salir,
            gb.ESTILO_BTN_SALIR,
            lambda event=None: self._salir(),
            gb.fuente_boton_salir,
            gb.PACK_BTN_SALIR,
        )
        self._boton_idioma = Boton(
            self.modulo_salir,
            leng.tex['btn_idioma'],
            self.cambiar_idioma,
            gb.ESTILO_BTN_LENG,
            lambda event=None: self.cambiar_idioma(),
            gb.fuente_boton_salir,
            gb.PACK_BTN,
        )
        # Nota emergente sobre el boton cambio de idioma
        self._ne_idioma = NotaEmergente(
            self._boton_idioma.boton,
            leng.tex['ne_btn_idioma']
        )        
        # Asocia la nota emergente al boton
        self._boton_idioma.boton.bind("<Enter>", self._ne_idioma.mostrar)
        self._boton_idioma.boton.bind("<Leave>", self._ne_idioma.ocultar)

        # Título de la sección generar tabla
        self._eti_titulo_tabla = tk.Label(
            self.modulo_salir,
            text=leng.tex['titulo_generar'],
            **gb.ESTILO_ETIQ_TITULO
        )
        self._eti_titulo_tabla.configure(font=gb.fuente_titulo)
        self._eti_titulo_tabla.pack(**gb.PACK_ETIQ_APP)
        
        self.contenedor_ajustes_datos = tk.Frame(
            self.marco_raiz,
            **gb.ESTILO_MARCO_MOD
        )
        # Agrega los modulos al panel
        self.marco_raiz.add(self.modulo_salir)
        self.marco_raiz.add(self.contenedor_ajustes_datos)
        self.marco_raiz.pack(fill='both', expand=True)

        self.seccion_ajustes_datos = tk.PanedWindow(
            self.contenedor_ajustes_datos,
            orient=tk.HORIZONTAL,
            sashwidth=0,
            **gb.ESTILO_MARCO_MOD
        )
        self.modulo_ajustes = tk.Frame(
            self.seccion_ajustes_datos,
            **gb.ESTILO_MARCO_MOD
        )       
        self.seccion_modulos = tk.PanedWindow(
            self.modulo_ajustes,
            orient=tk.VERTICAL,
            sashwidth=0,
            **gb.ESTILO_MARCO_MOD
        )

        self.modulo_ruta = Ruta(
            self.modulo_ajustes,
            self.gestor,
            self
        )
        self.modulo_ruta.enfocar()

        self.modulo_encabezado = Encabezado(
            self.modulo_ajustes,
            self.gestor,
            self
        )
        
        self.modulo_opciones_tabla = OpcionesTabla(
            self.modulo_ajustes,
            self.gestor,
            self
        )
        
        self.modulo_campo_booleano = CampoBooleano(
            self.modulo_ajustes,
            self.gestor,
            self
        )
        
        self.modulo_campo_texto = CampoTexto(
            self.modulo_ajustes,
            self.gestor,
            self
        )
        
        self.modulo_campo_numerico = CampoNumerico(
            self.modulo_ajustes,
            self.gestor,
            self
        )
        # Trabaja junto con los modulos booleano, texto y numérico
        self.modulo_borrar_campo = BorrarCampo(
            self.modulo_ajustes,
            self.gestor
        )
        # Marco para la organización espacial del modulo exportar
        self.seccion_exportar = tk.Frame(
            self.modulo_ajustes,
            **gb.ESTILO_MARCO_MOD
        )
        self.seccion_exportar.pack(side='top', padx=0, pady=0)

        self.modulo_exportar = Exportar(
            self.seccion_exportar,
            self.gestor,
            self
        )
        self.seccion_modulos.add(self.modulo_ruta.marco_modulo)
        self.seccion_modulos.add(self.modulo_encabezado.marco_modulo)
        self.seccion_modulos.add(self.modulo_opciones_tabla.marco_modulo)
        self.seccion_modulos.add(self.modulo_campo_booleano.marco_modulo)
        self.seccion_modulos.add(self.modulo_campo_texto.marco_modulo)
        self.seccion_modulos.add(self.modulo_campo_numerico.marco_modulo)
        self.seccion_modulos.add(self.modulo_borrar_campo.marco_modulo)
        self.seccion_modulos.add(self.seccion_exportar)
        
        self.seccion_modulos.pack(fill='both', expand=True)

        self.modulo_vista = tk.Frame(
            self.seccion_ajustes_datos,
            **gb.ESTILO_MARCO_MOD
        )
        
        # Frame de relleno para ordenar visualmente
        self.ppp = tk.Frame(
            self.modulo_vista,
            height=30,
            **gb.ESTILO_MARCO_MOD)
        self.ppp.pack(fill='x')
       
        # Vista de los datos ingresados
        self.modulo_ver_datos = VerDatos(
            self.modulo_vista,
            self.raiz,
            self.gestor
        )

        self.seccion_ajustes_datos.add(self.modulo_ajustes)
        self.seccion_ajustes_datos.add(self.modulo_vista)

        self.seccion_ajustes_datos.pack(fill='both', expand=True)

    def ejecutar(self):
        """
        Inicia el bucle de la aplicación.

        :return: None
        """
        self.raiz.mainloop()


    def cambiar_idioma(self):
        """
        Llama a una función global de reinicio para cambiar el idioma
        y aplicar los cambios.

        :return: None
        """        
        alternar(self.raiz, self.reseteador)            


    def _salir(self):
        """
        Confirma el cierre de la aplicación.

        :return: None
        """
        confirmacion = messagebox.askyesno(
            leng.tex['vt_salida'],
            leng.tex['vt_salida_mensaje']
        )
        if confirmacion:
            self.raiz.destroy()

        
