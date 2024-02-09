
import tkinter as tk
from app.comunes.globales import gb



class EntradaTexto:
    """
    Clase encargada de gestionar y generar un Entry
    junto con sus elementos asociados.
    """
    def __init__(
        self,
        ubicacion,
        texto_etiqueta:str,
        texto_base_entrada:str="",
        evento_enter = lambda event=None: lambda *args: None,
        pack_entrada=gb.PACK_ENT_TEX,
        pack_etiqueta=gb.PACK_ETIQ_ENT,
        estilo_entrada=gb.ESTILO_TX_ENTRADA):
        """
        Constructor de la clase EntradaTexto para crear un widget
        de entrada con etiqueta asociada dentro de un contenedor.

        :param ubicacion: Marco donde se anidará el módulo.
        :type ubicacion: tk.Frame
        :param texto_etiqueta: Contenido de la etiqueta.
        :type texto_etiqueta: str
        :param texto_base_entrada: Texto por defecto de la entrada.
        :type texto_base_entrada: str
        :param evento_enter: Función asociada al evento <Return> en la entrada.
        :type evento_enter: function or None
        :param pack_entrada: Configuración para ubicar el widget entrada.
        :type pack_entrada: dict
        :param pack_etiqueta: Configuración para ubicar el widget etiqueta.
        :type pack_etiqueta: dict      
        """
        self.pack_eti_base = pack_etiqueta
        self.pack_entrada_base = pack_entrada

        self._contenedor_ingreso = tk.Frame(ubicacion, **gb.ESTILO_MARCO_MOD)
        self._contenedor_ingreso.pack(**gb.PACK_MARCO_ENT)

        self._eti_ingreso = tk.Label(
            self._contenedor_ingreso,
            text=texto_etiqueta,
            **gb.ESTILO_ETIQ
        )
        self._eti_ingreso.config(font=gb.fuente_etiqueta)
        self._eti_ingreso.pack(**self.pack_eti_base)

        # Almacena el valor ingresado
        self._valor_ingresado = tk.StringVar()        
        self.entrada = tk.Entry(
            self._contenedor_ingreso,
            textvariable=self._valor_ingresado,
            justify="center"
        )
        self.entrada.configure(
            font=gb.fuente_entrada,
            **estilo_entrada)
        self.entrada.insert(0, texto_base_entrada)
        self.entrada.pack(**self.pack_entrada_base)
        self.entrada.bind("<Return>", evento_enter)

    def borrar_valor(self):
        """
        Vacía el texto del widget de entrada.

        :return: None
        """
        self.entrada.delete(0, "end")

    def obtener_valor(self) -> str:
        """
        Retorna el texto ingresado en el widget de entrada.

        :return: Cadena de texto con el valor ingresado.
        :rtype: str
        """
        return self._valor_ingresado.get()

    def establecer_valor(self, valor:str):
        """
        Establece el valor de texto del widget de entrada.

        :param valor: Valor de texto a establecer.
        :type valor: str
        :return: None
        """
        self._valor_ingresado.set(valor)

    def enfocar_entrada(self):
        """
        Establece el enfoque del teclado en el widget de entrada.

        :return: None
        """
        self.entrada.focus_set()

    def mostrar_elemento(self):
        """
        Vuelve visible el elemento si está oculto.

        :return: None
        """
        self._contenedor_ingreso.pack(**gb.PACK_MARCO_ENT)
        self._eti_ingreso.pack(**self.pack_eti_base)
        self.entrada.pack(**self.pack_entrada_base)

    def ocultar_elemento(self):
        """
        Oculta el elemento si está visible.

        :return: None
        """
        self._contenedor_ingreso.pack_forget()
        self._eti_ingreso.pack_forget()
        self.entrada.pack_forget()


class EntradaOpciones:
    """
    Clase encargada de gestionar y generar un OptionMenu
    junto con sus elementos asociados.
    """

    def __init__(
        self,
        ubicacion,
        texto_etiqueta:str,
        opciones_base:list=[],
        funcion_rastrear_opciones=lambda *args: None,
        estilo_opc=gb.ESTILO_BTN_OPC,
        pack_cont_ingreso=gb.PACK_MARCO_ENT):
        """
        Constructor de la clase EntradaOpciones para crear un widget
        de opciones con etiqueta asociada dentro de un contenedor.

        :param ubicacion: Marco donde se anidará el módulo.
        :type ubicacion: tk.Frame
        :param texto_etiqueta: Contenido de la etiqueta.
        :type texto_etiqueta: str
        :param opciones_base: Opciones del widget.
        :type opciones_base: list
        :param funcion_rastrear_opciones: Función asociada al valor seleccionado.
        :type funcion_rastrear_opciones: function or None
        :param estilo_opc: Configuración del aspecto visual del widget de opciones.
        :type estilo_opc: dict
        :param pack_cont_ingreso: Configuración para ubicar el marco del widget.
        :type pack_cont_ingreso: dict      
        """
        self._contenedor_ingreso = tk.Frame(ubicacion, **gb.ESTILO_MARCO_MOD)
        self._contenedor_ingreso.pack(**pack_cont_ingreso)

        self._eti_ingreso = tk.Label(
            self._contenedor_ingreso,
            text=texto_etiqueta,
            **gb.ESTILO_ETIQ
        )
        self._eti_ingreso.config(font=gb.fuente_etiqueta)
        self._eti_ingreso.pack(**gb.PACK_ETIQ_ENT)

        self._opciones = opciones_base
        # Almacena el seleccionado
        self._valor_ingresado = tk.StringVar()
        # Establece el valor incial
        self._valor_ingresado.set(self._opciones[0])

        self.entrada_opciones = tk.OptionMenu(
            self._contenedor_ingreso,
            self._valor_ingresado,
            *self._opciones
        )
        self.entrada_opciones.config(font=gb.fuente_boton, **estilo_opc)
        self.entrada_opciones.pack(**gb.PACK_ENT_OPC)
        
        self._valor_ingresado.trace("w", funcion_rastrear_opciones)

    def obtener_valor(self) -> str:
        """
        Retorna la opción seleccionada en el widget de opción.

        :return: Cadena de texto con el valor ingresado.
        :rtype: str
        """
        return self._valor_ingresado.get()

    def actualizar_opciones(self, nuevas_opciones:list):
        """
        Establece nuevas opciones en el OptionMenu.

        :param nuevas_opciones: Las nuevas opciones.
        :type nuevas_opciones: list
        :return: None
        """
        if nuevas_opciones:
            menu = self.entrada_opciones["menu"]
            menu.delete(0, "end")
            for opcion in nuevas_opciones:
                menu.add_command(
                    label=opcion,
                    command=lambda opc=opcion: self._valor_ingresado.set(opc)
                )
            self._valor_ingresado.set(nuevas_opciones[0])

    def reiniciar_opciones(self):
        """
        Establece como opción seleccionada el primer item
        de la lista de opciones disponibles.

        :return: None
        """
        self._valor_ingresado.set(self._opciones[0])

    def mostrar_elemento(self):
        """
        Ver EntradaTexto.mostrar_elemento()
        """
        self._contenedor_ingreso.pack(**pack_cont_ingreso)
        self._eti_ingreso.pack(**gb.PACK_ETIQ_ENT)
        self.entrada_opciones.pack(**gb.PACK_ENT_OPC)

    def ocultar_elemento(self):
        """
        Ver EntradaTexto.ocultar_elemento()
        """
        self._contenedor_ingreso.pack_forget()
        self._eti_ingreso.pack_forget()
        self.entrada_opciones.pack_forget()


class Boton:
    """
    Clase encargada de gestionar y generar un Button.
    """
    def __init__(
        self,
        ubicacion,
        texto_boton:str,
        funcion_comando,
        estilo_boton,
        evento_enter = lambda event=None: lambda *args: None,
        fuente_boton=gb.fuente_boton,
        pack_variable=gb.PACK_BTN):
        """
        Constructor de la clase Boton.

        :param ubicacion: Marco donde se anidará el módulo.
        :type ubicacion: tk.Frame
        :param texto_boton: Texto del boton.
        :type texto_boton: str
        :param funcion_comando: Función asociada al boton.
        :type funcion_comando: function
        :param estilo_boton: Configuración del aspecto visual del widget.
        :type estilo_boton: dict
        :param evento_enter: Función asociada al evento <Return> en el boton.
        :type evento_enter: function or None
        :param fuente_boton: Configuración de la fuente.
        :type fuente_boton: tk.Font
        :param pack_cont_ingreso: Configuración para ubicar el marco del widget.
        :type pack_cont_ingreso: dict    
        """    
        self.boton = tk.Button(
            ubicacion,
            text=texto_boton,
            command=funcion_comando,
            **estilo_boton
        )
        self.boton.configure(font=fuente_boton)
        self.boton.pack(**pack_variable)
        self.boton.bind("<Return>", evento_enter)

    def enfocar_boton(self):
        """
        Establece el enfoque del teclado en el widget.

        :return: None
        """
        self.boton.focus_set()

class NotaEmergente:
    """
    Clase encargada de gestionar y generar una nota emergente.
    """
    
    def __init__(self, elemento_asociado, texto:str):
        """
        Constructor de la clase NotaEmergente.

        :param elemento_asociado: Widget sobre el cual será visible la nota.
        :type elemento_asociado: tk.Widget
        :param texto: Contenido de la nota.
        :type texto: str
        """    
        self.elemento_asociado = elemento_asociado
        self.texto = texto
        self.nota = None

    def mostrar(self, evento=None):
        """
        Vuelve visible la nota emergente si está oculta.

        :param evento: Señala que el cursor entra en el widget.
        :return: None
        """
        x, y, _, _ = self.elemento_asociado.bbox("insert")
        x += self.elemento_asociado.winfo_rootx() + 25
        y += self.elemento_asociado.winfo_rooty() + 25

        self.nota = tk.Toplevel(self.elemento_asociado)
        self.nota.wm_overrideredirect(True)
        self.nota.wm_geometry(f"+{x}+{y}")

        info = tk.Label(
            self.nota,
            text=self.texto,
            background="#ffffe0",
            relief="solid",
            borderwidth=1
        )
        info.pack(ipadx=1)

    def ocultar(self, evento=None):
        """
        Oculta la nota emergente si está visible.

        :param evento: Señala que el cursor sale del widget.
        :return: None
        """
        if self.nota:
            self.nota.destroy()
            self.nota = None
