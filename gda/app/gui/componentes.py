import tkinter as tk
from tkinter import filedialog, messagebox
from app.comunes.idioma import leng
from app.comunes.globales import gb
from app.gui.elementos import (
    EntradaTexto, EntradaOpciones,
    Boton, NotaEmergente
)



class VerDatos:
    """
    Clase encargada de gestionar la vista de los datos ingresados.
    """

    def __init__(self, ubicacion, m_raiz, gestor):
        """
        Constructor de la clase VerDatos. Permite ver y evaluar
        los datos ingresados antes de exportar la tabla.

        :param ubicacion: Marco donde se anidará el módulo.
        :type ubicacion: tk.Frame 
        :param m_raiz: Instancia de la ventana principal (Tk).
        :type m_raiz: tk.Tk
        :param gestor: Instancia que comunica componentes, tabla y generador.
        :type gestor: Gestor
        """
        self.gestor = gestor
        
        self.marco_modulo = tk.Frame(ubicacion, **gb.ESTILO_MARCO_MOD)
        self.marco_modulo.pack(
            side="top",
            fill="both",
            expand=True,
        )
        # Barra de desplazamiento vertical
        self._b_vertical = tk.Scrollbar(
            self.marco_modulo,
            command=self.desplazar
        )
        self._b_vertical.pack(side="right", fill="y")

        # Cuadro texto donde se verán los datos ingresados
        self._contenedor_texto = tk.Text(
            self.marco_modulo,
            wrap="word",
            yscrollcommand=self._b_vertical.set
        )
        self._contenedor_texto.pack(
            side="top",
            fill="both",
            expand=True)
        self._contenedor_texto.configure(**gb.ESTILO_TX_VISTA)
        self._contenedor_texto.tag_configure("clave", **gb.ESTILO_TX_CLAVE)
        self._contenedor_texto.tag_configure("valor", **gb.ESTILO_TX_VALOR)

        # Previene que se oculte la barra de desplazamiento
        m_raiz.bind("<Configure>", self.barra_visible)
        # Previene el ingreso de datos en el panel de vista
        self._contenedor_texto.insert("1.0", leng.tex['aclaracion'], "clave")
        self._contenedor_texto.configure(state='disabled')        
    
    def insertar_datos(self, datos):
        """
        Recibe del gestor los datos cargados por el usuario y
        los inserta en el cuadro de texto.

        :param datos: Valores ingresados y almacenados en la tabla.
        :type datos: list
        :return: None
        """
        self._contenedor_texto.configure(state='normal')
        self._contenedor_texto.delete("1.0", "end")
        self._contenedor_texto.insert("1.0", leng.tex['aclaracion'], "clave")
        for indice, item in enumerate(datos):
            if indice%2 == 0:
                self._contenedor_texto.insert("end", item, "clave")
            else:
                self._contenedor_texto.insert("end", item, "valor")
        self._contenedor_texto.configure(state='disabled')


    def desplazar(self, *args):
        """
        Asocia la barra de desplazamiento vertical al cuadro de texto.

        :param args: Señal de desplazamiento vertical en el cuadro de texto.
        :return: None
        """
        self._contenedor_texto.yview(*args)

    def barra_visible(self, *args):
        """
        Mantiene visible la barra de desplazamiento vertical
        aunque se modifiquen las dimensiones de la ventana.

        :param args: Señal de modificación del tamaño de la ventana.
        :return: None
        """
        self._contenedor_texto.pack_configure(
            side="left",
            fill="both",
            expand=True
        )


class Ruta:
    """
    Clase encargada de gestionar el ingreso de la ruta de salida.
    """

    def __init__(self, ubicacion, gestor, interface):
        """
        Constructor de la clase Ruta. Administra el ingreso o selección
        de la ruta de salida, ya sea para un directorio o un archivo CSV.

        :param ubicacion: Marco donde se anidará el módulo.
        :type ubicacion: tk.Frame
        :param gestor: Instancia que comunica componentes, tabla y generador.
        :type gestor: Gestor
        :param interface: Instancia que contiene a los componentes principales.
        :type interface: Interface
        """
        self.gestor = gestor
        self.interface = interface
        
        self.marco_modulo = tk.Frame(ubicacion, **gb.ESTILO_MARCO_MOD)
        self.marco_modulo.pack(**gb.PACK_MARCO_MODULO)

        # Crea el Entry que recibe la ruta de entrada
        self._elemento_entrada_ruta = EntradaTexto(
            self.marco_modulo,
            leng.tex['ruta'], # Texto de etiqueta
            leng.tex['ruta_def'], # Ruta de ejemplo
            lambda event=None: self._confirmar_ruta()
        )
        self._contenedor_boton_ruta = tk.Frame(
            self.marco_modulo,
            **gb.ESTILO_MARCO_MOD
        )
        self._contenedor_boton_ruta.pack(**gb.PACK_MARCO_BTN)

        self._boton_seleccionar_ruta = Boton(
            self._contenedor_boton_ruta,
            leng.tex['btn_ubicacion'],
            self._seleccionar_ruta,
            gb.ESTILO_BTN_OK,
            lambda event=None: self._seleccionar_ruta(),
            gb.fuente_boton
        )      
        self._boton_confirmar_ruta = Boton(
            self._contenedor_boton_ruta,
            leng.tex['btn_ok'],
            self._confirmar_ruta,
            gb.ESTILO_BTN_OK,
            lambda event=None: self._confirmar_ruta(),
            gb.fuente_boton
        )
        
    def limpiar_entrada(self):
        """
        Elimina el contenido actual del widget de entrada.

        :return: None
        """        
        self._elemento_entrada_ruta.borrar_valor()

    def enfocar(self):
        """
        Dirige el enfoque del teclado al widget principal del módulo.

        :return: None
        """    
        self._elemento_entrada_ruta.enfocar_entrada()

    def _seleccionar_ruta(self):
        """
        Despliega una ventana que permite seleccionar el directorio
        o archivo CSV de salida.

        :return: None
        """
        ruta_elegida = filedialog.askdirectory()
        self._elemento_entrada_ruta.establecer_valor(ruta_elegida)

    def _confirmar_ruta(self):
        """
        Envía al gestor la ruta ingresada para su validación.
        Si fue exitosa, establece el enfoque del teclado
        en la entrada de texto del módulo siguiente.

        :return: None
        """   
        respuesta:bool = self.gestor.recibir(
            "m_ruta",
            self._elemento_entrada_ruta.obtener_valor()
        )
        if respuesta:
            self.interface.modulo_encabezado.enfocar()


class Encabezado:
    """
    Clase encargada de gestionar el ingreso de los campos de la tabla.
    """

    def __init__(self, ubicacion, gestor, interface):
        """
        Constructor de la clase Encabezado. Gestiona el ingreso
        de campos de la tabla y actualiza las opciones de los modulos
        que los utilizan.

        :param ubicacion: Marco donde se anidará el módulo.
        :type ubicacion: tk.Frame
        :param gestor: Instancia que comunica componentes, tabla y generador.
        :type gestor: Gestor
        :param interface: Instancia que contiene a los componentes principales.
        :type interface: Interface
        """
        self.gestor = gestor
        self.interface = interface
        
        self.marco_modulo = tk.Frame(ubicacion, **gb.ESTILO_MARCO_MOD)
        self.marco_modulo.pack(**gb.PACK_MARCO_MODULO)

        self._elemento_entrada_encabezado = EntradaTexto(
            self.marco_modulo,
            leng.tex['encabezado'], # Texto de etiqueta
            leng.tex['campos_def'], # Campos de ejemplo
            lambda event=None: self._confirmar_encabezado()
        )
        self._contenedor_botones_encabezado = tk.Frame(
            self.marco_modulo,
            **gb.ESTILO_MARCO_MOD
        )
        self._contenedor_botones_encabezado.pack(**gb.PACK_MARCO_BTN)

        self._boton_borrar_encabezado = Boton(
            self._contenedor_botones_encabezado,
            leng.tex['btn_encabezado'],
            self._borrar_campos_ingresados,
            gb.ESTILO_BTN_NO_OK,
            lambda event=None: self._borrar_campos_ingresados(),
            gb.fuente_boton
        )
        self._boton_confirmar_encabezado = Boton(
            self._contenedor_botones_encabezado,
            leng.tex['btn_ok'],
            self._confirmar_encabezado,
            gb.ESTILO_BTN_OK,
            lambda event=None: self._confirmar_encabezado(),
            gb.fuente_boton
        )

    def limpiar_entrada(self):
        """
        Ver Ruta.limpiar_entrada()
        """     
        self._elemento_entrada_encabezado.borrar_valor()

    def enfocar(self):
        """
        Ver Ruta.enfocar()
        """       
        self._elemento_entrada_encabezado.enfocar_entrada()
    
    def _confirmar_encabezado(self):
        """
        Envía al gestor los campos ingresados para su validación.
        Si fue exitosa, actualiza las opciones de los componentes que podrían
        utilizarlos y luego establece el enfoque del teclado en el widget
        principal del módulo siguiente.

        :return: None
        """
        respuesta:bool = self.gestor.recibir(
            "m_encabezado",
            self._elemento_entrada_encabezado.obtener_valor()
        )
        if respuesta:
            self.gestor.actualizar_opciones()
            self.interface.modulo_opciones_tabla.enfocar()

    def _borrar_campos_ingresados(self):
        """
        Vacia el widget de entrada y elimina los campos previamente definidos.
        
        :return: None
        """
        self.limpiar_entrada()
        self.gestor.borrar_encabezado()


class OpcionesTabla:
    """
    Clase encargada de administrar las opciones de formato de la tabla.
    """
    
    def __init__(self,ubicacion, gestor, interface):
        """
        Constructor de la clase OpcionesTabla. Gestiona la entrada de
        delimitadores, tipo de orden, campo de referencia, librería y seed
        (estado inicial para 'random').

        :param ubicacion: Marco donde se anidará el módulo.
        :type ubicacion: tk.Frame
        :param gestor: Instancia que comunica componentes, tabla y generador.
        :type gestor: Gestor
        :param interface: Instancia que contiene a los componentes principales.
        :type interface: Interface
        """
        self.gestor = gestor
        self.interface = interface
        
        self.marco_modulo = tk.Frame(ubicacion, **gb.ESTILO_MARCO_MOD)
        self.marco_modulo.pack(**gb.PACK_MARCO_MODULO)
  
        self._elemento_entrada_delimitador = EntradaTexto(
            self.marco_modulo,
            leng.tex['delimitador'],
            ",",
            lambda event=None: self._confirmar_opciones()
        )
        # Lista con las formas de ordenar la tabla
        self._opc_orden_base:list = [
            leng.tex['orden_opc_2'],
            leng.tex['orden_opc_0'],
            leng.tex['orden_opc_1'],
            leng.tex['orden_opc_3'],
            leng.tex['orden_opc_4']
        ]
        # Crea el OptionMenu de las formas de ordenar y su etiqueta        
        self._elemento_opcion_orden = EntradaOpciones(
            self.marco_modulo,
            leng.tex['orden'],
            self._opc_orden_base
        )
        # Nota emergente sobre las formas de ordenar el archivo
        self._ne_orden = NotaEmergente(
            self._elemento_opcion_orden.entrada_opciones,
            leng.tex['ne_opc_orden']
        )       
        # Muestra la nota cuando se ubica el cursor en el widget
        self._elemento_opcion_orden.entrada_opciones.bind(
            "<Enter>",
            self._ne_orden.mostrar
        )      
        # Oculta la nota cuando se retira el cursor del widget
        self._elemento_opcion_orden.entrada_opciones.bind(
            "<Leave>",
            self._ne_orden.ocultar
        )       
        self._opc_criterio_base:list = [leng.tex['criterio_opc_base']]
        self._elemento_opcion_criterio = EntradaOpciones(
            self.marco_modulo,
            leng.tex['criterio'],
            self._opc_criterio_base
        )     
        self._opc_modo_base = ["random", "secrets"]
        self._elemento_opcion_modo = EntradaOpciones(
            self.marco_modulo,
            leng.tex['modo'],
            self._opc_modo_base,
            self._rastrear_opcion_aleatoriedad
        )      
        self._elemento_entrada_semilla = EntradaTexto(
            self.marco_modulo,
            leng.tex['semilla'], # Texto de etiqueta
            leng.tex['semilla_def'], # Valor por defecto
            lambda event=None: self._confirmar_opciones()
        )      
        self._contenedor_boton_opciones_tabla = tk.Frame(
            self.marco_modulo,
            **gb.ESTILO_MARCO_MOD
        )       
        self._contenedor_boton_opciones_tabla.pack(**gb.PACK_MARCO_BTN)

        self._boton_confirmar_opciones = Boton(
            self._contenedor_boton_opciones_tabla,
            leng.tex['btn_ok'],
            self._confirmar_opciones,
            gb.ESTILO_BTN_OK,
            lambda event=None: self._confirmar_opciones(),
            gb.fuente_boton
        )

    def limpiar_entrada(self):
        """
        Ver Ruta.limpiar_entrada()
        """     
        self._elemento_entrada_delimitador.borrar_valor()

    def enfocar(self):
        """
        Ver Ruta.enfocar()
        """     
        self._elemento_entrada_delimitador.enfocar_entrada()

    def actualizar_opciones_criterio(self):
        """
        Actualiza las opciones de campos de referencia para ordenar la tabla
        con los campos existentes.

        :return: None
        """        
        nuevos_campos:list = self.gestor.ver_encabezado()
        if len(nuevos_campos) == 0:
            nuevos_campos = [leng.tex['opc_vacio']]
        self._elemento_opcion_criterio.actualizar_opciones(nuevos_campos)
        return None

    def _rastrear_opcion_aleatoriedad(self, *args):
        """
        Rastrea el modo de aleatoriedad seleccionado. Si es 'secrets',
        oculta la opción de ingresar 'seed' y la de número decimal
        en el módulo campo numérico.
        
        :param args: Señal de cambio en la opción del modo de aleatoriedad.
        :return: None
        """
        modo:str = self._elemento_opcion_modo.obtener_valor()
        if modo == "random":
            self._elemento_entrada_semilla.mostrar_elemento()
            self.interface.modulo_campo_numerico.actualizar_opciones_numero(
                [leng.tex['opc_num_int'], leng.tex['opc_num_float']]
            )
        else:
            self._elemento_entrada_semilla.ocultar_elemento()
            self._elemento_entrada_semilla.establecer_valor(leng.tex['semilla_def'])
            self.interface.modulo_campo_numerico.actualizar_opciones_numero(
                [leng.tex['opc_num_int']]
            )

    def _confirmar_opciones(self):
        """
        Reúne las opciones definidas y las envía al gestor para su
        validación. Si fue exitosa, establece el enfoque del teclado
        en el widget principal del módulo siguiente.

        return: None
        """
        aux_opc:list = []
        aux_opc.append(self._elemento_entrada_delimitador.obtener_valor())
        aux_opc.append(self._elemento_opcion_orden.obtener_valor())
        aux_opc.append(self._elemento_opcion_criterio.obtener_valor())
        aux_opc.append(self._elemento_opcion_modo.obtener_valor())
        aux_opc.append(self._elemento_entrada_semilla.obtener_valor())
        respuesta:bool = self.gestor.recibir("m_opciones_tabla", aux_opc)
        if respuesta:
            self.interface.modulo_campo_booleano.enfocar()


class CampoBooleano:
    """
    Clase que gestiona la definción de un campo ingresado como booleano.
    """

    def __init__(self, ubicacion, gestor, interface):
        """
        Constructor de la clase CampoBooleano. Permite seleccionar
        el campo a definir y los posibles valores (True, False, None) de
        sus celdas.

        :param ubicacion: Marco donde se anidará el módulo.
        :type ubicacion: tk.Frame
        :param gestor: Instancia que comunica componentes, tabla y generador.
        :type gestor: Gestor
        :param interface: Instancia que contiene a los componentes.
        :type interface: Interface
        """
        self.gestor = gestor
        self.interface = interface
        
        self.marco_modulo = tk.Frame(ubicacion, **gb.ESTILO_MARCO_MOD)
        self.marco_modulo.pack(**gb.PACK_MARCO_MODULO)

        self._contenedor_boton_definir_campo_booleano = tk.Frame(
            self.marco_modulo,
            **gb.ESTILO_MARCO_MOD
        )
        self._contenedor_boton_definir_campo_booleano.pack(**gb.PACK_MARCO_BTN)

        self._boton_confirmar_campo_booleano = Boton(
            self._contenedor_boton_definir_campo_booleano,
            leng.tex['btn_ok'],
            self._confirmar_campo_booleano,
            gb.ESTILO_BTN_OK,
            lambda event=None: self._confirmar_campo_booleano(),
            gb.fuente_boton
        )
        # Lista con campos de ejemplo
        self._opc_elegir_campo_base:list = [
            leng.tex['campo_def_0'],
            leng.tex['campo_def_1'],
            leng.tex['campo_def_2'],
            leng.tex['campo_def_3']
        ]        
        self._elemento_elegir_campo = EntradaOpciones(
            self.marco_modulo,
            leng.tex['selecc_campo_bool'],
            self._opc_elegir_campo_base,
            lambda *args: None,
            gb.ESTILO_BTN_OPC,
            gb.PACK_MARCO_ENT_BOOL
        )
        # Lista con las opciones de campo booleano
        self._opc_logica_base: list = ["True, False", "True, False, None"]
        self._elemento_elegir_logica = EntradaOpciones(
            self.marco_modulo,
            leng.tex['logica'],
            self._opc_logica_base,
            lambda *args: None,
            gb.ESTILO_BTN_OPC,
            gb.PACK_MARCO_ENT_BOOL
        )
        
    def enfocar(self):
        """
        Ver Ruta.enfocar()
        """     
        self._boton_confirmar_campo_booleano.enfocar_boton()
        return None

    def actualizar_opciones_campo(self):
        """
        Actualiza la opción de campo a elegir con campos aun no definidos.

        :return: None        
        """
        nuevos_campos:list = self.gestor.ver_campos_sin_definir()
        if len(nuevos_campos) == 0:
            nuevos_campos = [leng.tex['opc_vacio']]
        self._elemento_elegir_campo.actualizar_opciones(nuevos_campos)

    def _confirmar_campo_booleano(self):
        """
        Reúne los valores definidos y los envía al gestor para su
        validación. Si fue exitosa, actualiza las opciones y luego
        establece el enfoque del teclado en el widget principal
        del módulo siguiente.

        return: None
        """       
        mensaje:list = []
        mensaje.append(self._elemento_elegir_campo.obtener_valor())
        mensaje.append(self._elemento_elegir_logica.obtener_valor())
        respuesta:bool = self.gestor.recibir("m_campo_booleano", mensaje)
        if respuesta:
            self.gestor.actualizar_opciones()
            self.interface.modulo_exportar.enfocar()


class CampoTexto:
    """
    Clase encargada de gestionar la definción de un campo como de texto.
    """
    
    def __init__(self,ubicacion, gestor, interface):
        """
        Constructor de la clase CampoTexto. Permite seleccionar
        el campo a definir e ingresar los posibles valores de texto
        de sus celdas.

        :param ubicacion: Marco donde se anidará el módulo.
        :type ubicacion: tk.Frame
        :param gestor: Instancia que comunica componentes, tabla y generador.
        :type gestor: Gestor
        :param interface: Instancia que contiene a los componentes.
        :type interface: Interface
        """
        self.gestor = gestor
        self.interface = interface
        
        self.marco_modulo = tk.Frame(ubicacion, **gb.ESTILO_MARCO_MOD)
        self.marco_modulo.pack(**gb.PACK_MARCO_MODULO)

        self._elemento_entrada_valores_texto = EntradaTexto(
            self.marco_modulo,
            leng.tex['valores_texto'], # Texto de etiqueta
            leng.tex['valores_tex_def'], # Valores de ejemplo
            lambda event=None: self._confirmar_campo_texto()
        )
        self._contenedor_boton_texto = tk.Frame(
            self.marco_modulo,
            **gb.ESTILO_MARCO_MOD
        )
        self._contenedor_boton_texto.pack(**gb.PACK_MARCO_BTN)

        self._boton_borrar_valores_texto = Boton(
            self._contenedor_boton_texto,
            leng.tex['btn_borrar_tex'],
            self.limpiar_entrada,
            gb.ESTILO_BTN_NO_OK,
            lambda event=None: self.limpiar_entrada(),
            gb.fuente_boton
        )
        self._boton_confirmar_texto = Boton(
            self._contenedor_boton_texto,
            leng.tex['btn_ok'],
            self._confirmar_campo_texto,
            gb.ESTILO_BTN_OK,
            lambda event=None: self._confirmar_campo_texto(),
            gb.fuente_boton
        )
        # Lista con campos de ejemplo
        self._opc_elegir_campo_base = [
            leng.tex['campo_def_0'],
            leng.tex['campo_def_1'],
            leng.tex['campo_def_2'],
            leng.tex['campo_def_3']
        ]
        self._elemento_elegir_campo = EntradaOpciones(
            self.marco_modulo,
            leng.tex['selecc_campo'],
            self._opc_elegir_campo_base,
            lambda *args: None,
            gb.ESTILO_BTN_OPC,
            gb.PACK_MARCO_ENT_BOOL
        )

    def limpiar_entrada(self):
        """
        Ver Ruta.limpiar_entrada()
        """     
        self._elemento_entrada_valores_texto.borrar_valor()

    def enfocar(self):
        """
        Ver Ruta.enfocar()
        """     
        self._elemento_entrada_valores_texto.enfocar_entrada()

    def actualizar_opciones_campo(self):
        """
        Ver CampoBooleano.actualizar_opciones_campo()
        """
        nuevos_campos:list = self.gestor.ver_campos_sin_definir()
        if len(nuevos_campos) == 0:
            nuevos_campos = [leng.tex['opc_vacio']]
        self._elemento_elegir_campo.actualizar_opciones(nuevos_campos)

    def _confirmar_campo_texto(self):
        """
        Ver CampoBooleano._confirmar_campo_booleano()
        """   
        mensaje:list = []
        mensaje.append(self._elemento_elegir_campo.obtener_valor())
        mensaje.append(self._elemento_entrada_valores_texto.obtener_valor())
        respuesta:bool = self.gestor.recibir("m_campo_texto", mensaje)
        if respuesta:
            self.gestor.actualizar_opciones()
            self.interface.modulo_exportar.enfocar()


class CampoNumerico:
    """
    Clase encargada de gestionar la definción de un campo como numérico.
    """

    def __init__(self,ubicacion, gestor, interface):
        """
        Constructor de la clase CampoNumerico. Permite seleccionar
        el campo a definir, establecer el rango de posibles valores
        y el tipo numérico (entero o decimal).

        :param ubicacion: Marco donde se anidará el módulo.
        :type ubicacion: tk.Frame
        :param gestor: Instancia que comunica componentes, tabla y generador.
        :type gestor: Gestor
        :param interface: Instancia que contiene a los componentes.
        :type interface: Interface
        """
        self.gestor = gestor
        self.interface = interface
        
        self.marco_modulo = tk.Frame(ubicacion, **gb.ESTILO_MARCO_MOD)
        self.marco_modulo.pack(**gb.PACK_MARCO_MODULO)
  
        self._elemento_entrada_rango_inicio = EntradaTexto(
            self.marco_modulo,
            leng.tex['rango_desde'],
            "0", # Opción por defecto
            lambda event=None: self._confirmar_rango()
        )        
        self._elemento_entrada_rango_fin = EntradaTexto(
            self.marco_modulo,
            leng.tex['rango_hasta'],
            "100", # Opción por defecto
            lambda event=None: self._confirmar_rango()
        )
        # Nota emergente rango inicio 
        self._ne_digitos_ini = NotaEmergente(
            self._elemento_entrada_rango_inicio.entrada,
            leng.tex['ne_digitos']
        )
        self._elemento_entrada_rango_inicio.entrada.bind(
            "<Enter>",
            self._ne_digitos_ini.mostrar
        )
        self._elemento_entrada_rango_inicio.entrada.bind(
            "<Leave>",
            self._ne_digitos_ini.ocultar
        )
        # Nota emergente rango fin
        self._ne_digitos_fin = NotaEmergente(
            self._elemento_entrada_rango_fin.entrada,
            leng.tex['ne_digitos']
        )
        self._elemento_entrada_rango_fin.entrada.bind(
            "<Enter>",
            self._ne_digitos_fin.mostrar
        )
        self._elemento_entrada_rango_fin.entrada.bind(
            "<Leave>",
            self._ne_digitos_fin.ocultar
        )
        # Lista con tipos numéricos
        self._opc_tipo_base = [leng.tex['opc_num_int'], leng.tex['opc_num_float']]
        self._elemento_opcion_tipo = EntradaOpciones(
            self.marco_modulo,
            leng.tex['selecc_tipo_num'],
            self._opc_tipo_base,
            self._rastrear_tipo_num
        )
        self._elemento_entrada_redondeo = EntradaTexto(
            self.marco_modulo,
            leng.tex['redondear'],
            "2", # Opción por defecto
            lambda event=None: self._confirmar_rango()
        )
        self._ne_redondeo = NotaEmergente(
            self._elemento_entrada_redondeo.entrada,
            leng.tex['ne_redondeo']
        )
        self._elemento_entrada_redondeo.entrada.bind(
            "<Enter>",
            self._ne_redondeo.mostrar
        )
        self._elemento_entrada_redondeo.entrada.bind(
            "<Leave>",
            self._ne_redondeo.ocultar
        )
        self._contenedor_boton_campo_numerico = tk.Frame(
            self.marco_modulo,
            **gb.ESTILO_MARCO_MOD
        )
        self._contenedor_boton_campo_numerico.pack(**gb.PACK_MARCO_BTN)

        self._boton_confirmar_rango = Boton(
            self._contenedor_boton_campo_numerico,
            leng.tex['btn_ok'],
            self._confirmar_rango,
            gb.ESTILO_BTN_OK,
            lambda event=None: self._confirmar_rango(),
            gb.fuente_boton
        )
        # Lista con campos de ejemplo
        self._opc_elegir_campo_base = [leng.tex['campo_def_0'],
                                       leng.tex['campo_def_1'],
                                       leng.tex['campo_def_2'],
                                       leng.tex['campo_def_3']]
        
        self._elemento_elegir_campo = EntradaOpciones(
            self.marco_modulo,
            leng.tex['selecc_campo_num'],
            self._opc_elegir_campo_base,
            lambda *args: None,
            gb.ESTILO_BTN_OPC,
            gb.PACK_MARCO_ENT_BOOL
        )         
        # Oculta la entrada de redondeo al inicio 
        self._rastrear_tipo_num()

    def limpiar_entrada(self):
        """
        Ver Ruta.limpiar_entrada()
        """     
        self._elemento_entrada_rango_inicio.borrar_valor()
        self._elemento_entrada_rango_fin.borrar_valor()

    def enfocar(self):
        """
        Ver Ruta.enfocar()
        """     
        self._elemento_entrada_rango_inicio.enfocar_entrada()

    def actualizar_opciones_campo(self):
        """
        Ver CampoBooleano.actualizar_opciones_campo()       
        """
        nuevos_campos:list = self.gestor.ver_campos_sin_definir()
        if len(nuevos_campos) == 0:
            nuevos_campos = [leng.tex['opc_vacio']]
        self._elemento_elegir_campo.actualizar_opciones(nuevos_campos)
    
    def actualizar_opciones_numero(self, opciones:list):
        """
        Actualiza la opción de tipo numérico según el modo de aleatoriedad.

        :param opciones: Opciones de tipo numérico (entero o decimal)
        :type opciones: list
        :return: None
        """
        self._elemento_opcion_tipo.actualizar_opciones(opciones)

    def _confirmar_rango(self):
        """
        Ver CampoBooleano._confirmar_campo_booleano()
        """   
        mensaje:list = []
        mensaje.append(self._elemento_elegir_campo.obtener_valor())
        mensaje.append(self._elemento_entrada_rango_inicio.obtener_valor())
        mensaje.append(self._elemento_entrada_rango_fin.obtener_valor())
        mensaje.append(self._elemento_opcion_tipo.obtener_valor())
        mensaje.append(self._elemento_entrada_redondeo.obtener_valor())
        respuesta:bool = self.gestor.recibir("m_campo_numerico", mensaje)
        if respuesta:
            self.gestor.actualizar_opciones()
            self.interface.modulo_exportar.enfocar()

    def _rastrear_tipo_num(self, *args):
        """
        Rastrea el tipo numérico seleccionado. Si es 'decimal', habilita
        la entrada que permite ingresar en cuántos dígitos redondear.
        
        :param args: Señal de cambio en la opción de tipo numérico.
        :return: None
        """
        tipo:str = self._elemento_opcion_tipo.obtener_valor()
        if tipo == leng.tex['opc_num_float']:
            self._elemento_entrada_redondeo.establecer_valor("2")
            self._elemento_entrada_redondeo.mostrar_elemento()
        else:
            self._elemento_entrada_redondeo.establecer_valor("0")
            self._elemento_entrada_redondeo.ocultar_elemento()


class BorrarCampo:
    """
    Clase encargada de gestionar la eliminación de los valores de los campos y
    la opción de restablecer la tabla.
    """

    def __init__(self,ubicacion, gestor):
        """
        Constructor de la clase BorrarCampo. Permite vaciar un campo
        o todos los valores ingresados y las opciones seleccionadas.

        :param ubicacion: Marco donde se anidará el módulo.
        :type ubicacion: tk.Frame
        :param gestor: Instancia que comunica componentes, tabla y generador.
        :type gestor: Gestor
        """
        self.gestor = gestor        
        
        # Almacena la opción activa del campo a vaciar
        self._campo_a_vaciar:str = ""

        self.marco_modulo = tk.Frame(ubicacion, **gb.ESTILO_MARCO_MOD)
        self.marco_modulo.pack(**gb.PACK_MARCO_MODULO)

        self._contenedor_boton_restablecer = tk.Frame(
            self.marco_modulo,
            **gb.ESTILO_MARCO_MOD
        )
        self._contenedor_boton_restablecer.pack(**gb.PACK_MARCO_BTN)

        self._boton_reestablecer_tabla = Boton(
            self._contenedor_boton_restablecer,
            leng.tex['btn_vaciar_tabla'],
            self._restablecer_todo,
            gb.ESTILO_BTN_NO_OK,
            lambda event=None: self._restablecer_todo(),
            gb.fuente_boton
        )
        self._ne_restablecer = NotaEmergente(
            self._boton_reestablecer_tabla.boton,
            leng.tex['ne_btn_restablecer']
        )
        self._boton_reestablecer_tabla.boton.bind(
            "<Enter>",
            self._ne_restablecer.mostrar
        )
        self._boton_reestablecer_tabla.boton.bind(
            "<Leave>",
            self._ne_restablecer.ocultar
        )
        self._contenedor_boton_borrar_campo = tk.Frame(
            self.marco_modulo,
            **gb.ESTILO_MARCO_MOD
        )
        self._contenedor_boton_borrar_campo.pack(
            **gb.PACK_MARCO_BTN
        )
        self._boton_borrar_campo = Boton(
            self._contenedor_boton_borrar_campo,
            leng.tex['btn_vaciar_campo'],
            self._eliminar_valores,
            gb.ESTILO_BTN_NO_OK,
            lambda event=None: self._eliminar_valores(),
            gb.fuente_boton
        )
        # Lista con campos de ejemplo
        self._opc_campos = [
            leng.tex['campo_def_0'],
            leng.tex['campo_def_1'],
            leng.tex['campo_def_2'],
            leng.tex['campo_def_3']
        ]
        self._elemento_borrar_campo = EntradaOpciones(
            self.marco_modulo,
            leng.tex['campo_a_borrar'],
            self._opc_campos,
            self._campo_borrable,
            gb.ESTILO_ALERT,
            gb.PACK_MARCO_ENT_BOOL
        )

    def actualizar_opciones_borrado(self):
        """
        Actualiza la opción de campo a elegir con campos definidos.

        :param args: Señal de cambio en la opción del campo a borrar.
        :return: None        
        """
        nuevos_campos:list = self.gestor.ver_campos_definidos()
        if len(nuevos_campos) == 0:
            nuevos_campos = [leng.tex['opc_vacio']]
        self._elemento_borrar_campo.actualizar_opciones(nuevos_campos)

    def _campo_borrable(self, *args):
        """
        Establece el campo a vaciar.

        :param args: Señal de cambio en la opción del campo a borrar.
        :return: None
        """
        self._campo_a_vaciar = self._elemento_borrar_campo.obtener_valor()

    def _eliminar_valores(self):
        """
        Vacía los valores del campo seleccionado y actualiza la vista.

        :return: None
        """
        self.gestor.vaciar_campo(self._campo_a_vaciar)
        self.gestor.actualizar_opciones()

    def _restablecer_todo(self):
        """
        Vacía todos los valores ingresados y actualiza la vista.

        :return: None
        """
        self.gestor.vaciar_tabla()
        self.gestor.restablecer_aplicacion()    


class Exportar:
    """
    Clase encargada de inciar el proceso de exportar.
    """

    def __init__(self,ubicacion, gestor, interface):
        """
        Constructor de la clase Exportar. Permite establecer
        la cantidad de registros a crear.

        :param ubicacion: Marco donde se anidará el módulo.
        :type ubicacion: tk.Frame
        :param gestor: Instancia que comunica componentes, tabla y generador.
        :type gestor: Gestor
        :param interface: Instancia que contiene a los componentes.
        :type interface: Interface
        """
        self.gestor = gestor
        self.interface = interface
        
        self.marco_modulo = tk.Frame(ubicacion, **gb.ESTILO_MARCO_MOD)
        self.marco_modulo.pack(**gb.PACK_MARCO_MODULO)

        self._elemento_entrada_num_filas = EntradaTexto(
            self.marco_modulo,
            leng.tex['num_filas'],
            "1000",
            lambda event=None: self._exportar(),
            gb.PACK_ENT_TEX_FILA,
            gb.PACK_ETIQ_ENT_FILA
        )
        self._ne_filas = NotaEmergente(
            self._elemento_entrada_num_filas.entrada,
            leng.tex['ne_filas']
        )
        self._elemento_entrada_num_filas.entrada.bind(
            "<Enter>",
            self._ne_filas.mostrar
        )
        self._elemento_entrada_num_filas.entrada.bind(
            "<Leave>",
            self._ne_filas.ocultar
        )
        self._contenedor_botones_exportar = tk.Frame(
            self.marco_modulo,
            **gb.ESTILO_MARCO_MOD
        )
        self._contenedor_botones_exportar.pack(**gb.PACK_MARCO_BTN)

        self._boton_exportar = Boton(
            self._contenedor_botones_exportar,
            leng.tex['btn_exportar'],
            self._exportar,
            gb.ESTILO_BTN_OK,
            lambda event=None: self._exportar(),
            gb.fuente_boton
        )

    def limpiar_entrada(self):
        """
        Ver Ruta.limpiar_entrada()
        """     
        self._elemento_entrada_num_filas.borrar_valor()

    def enfocar(self):
        """
        Ver Ruta.enfocar()
        """     
        self._elemento_entrada_num_filas.enfocar_entrada()

    def _exportar(self):
        """
        Confirma e inicia el proceso de exportar. Si fue exitoso,
        establece el enfoque del teclado en el widget principal
        del módulo ruta.

        return: None
        """
        confirmacion = messagebox.askyesno(
            leng.tex['vt_expo_sn'],
            leng.tex['vt_expo_sn_mensaje']
        )
        if confirmacion:            
            respuesta:bool = self.gestor.recibir(
                "m_exportar",
                self._elemento_entrada_num_filas.obtener_valor()
            )
            if respuesta:
                self.interface.modulo_ruta.enfocar()

