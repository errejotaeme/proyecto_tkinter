
"""
🟪 ESTRUCTURA DEL ARCHIVO

• Descripción básica del programa
• Bloque de importaciones
• Instancia: raiz
• Clase principales: InterfaceUsuario, ModuloRuta, ModuloEncabezados,
                      ModuloOpcionesTabla, ModuloCampo, ModuloCampoTexto,
                      ModuloCampoNumerico, ModuloBorrarCampo, ModuloVista,
                      ModuloExportar, Gestor, Tabla, Generador.
                      
• Clases secundarias: SubmoduloEntradaTexto, SubmoduloEntradaOpciones, Boton
                      BotonEspecial.         
• Diccionarios que definen la ubicación de los objetos
• Diccionarios que defienen el aspecto visual de los objetos
• Diccionarios que defienen estilos de fuente
• Constantes de titulos y etiquetas
• Instancias: InterfaceUsuario(), Gestor(), Tabla(), Generador()
• Inicio del bucle de la apliación
• Tareas pendientes


🟪 ORGANIZACIÓN GENERAL

        Existen otros marcos no detallados que ayudan a organizar los elementos. 
-----------------------------------------------------------------------------------------
| raiz                                                                                  |
|   ⊦−− interface_usuario                                                               |
|                      ⊦−−−− modulo_ajustes                                             |
|                      |                ⊦−−−−− modulo_ruta                              |
|                      |                ⊦−−−−− modulo_encabezados                       |
|                      |                ⊦−−−−− modulo_opciones_tabla                    |
|                      |                ⊦−−−−− modulo_campo                             |
|                      |                               ⊦−−−−− modulo_campo_texto        |
|                      |                               ⊦−−−−− modulo_campo_numerico     |
|                      ⊦−−−− modulo_borrar_campo                                        |
|                      ⊦−−−− modulo_vista                                               |
|                                     ⊦−−−−− modulo_ver_datos                           |
|                                     ⊦−−−−− modulo_exportar                            |
| gestor                                                                                |
| tabla                                                                                 |
| generador                                                                             |
-----------------------------------------------------------------------------------------


🟪 FUNCIONES GENERALES

• interface_usuario: contiene a los modulos.

• modulo_ruta: recibe el ingreso de la ruta de salida.

• modulo_encabezados: recibe los distintos encabezados de la tabla.

• modulo_opciones_tabla: recibe las opciones de la tabla (delimitador, orden).

• modulo_campo: refine valores booleanos y habilita a los modulos de texto y numéricos.

• modulo_campo_texto: recibe distintas cadenas de caracteres para generar los registros
                      del campo especificado.

• modulo_campo_numerico: recibe la configuración de cada campo  y su tipo numérico.

• modulo_borrar_campo: permite eliminar los campos ingresados.

• modulo_ver_datos: muestra la configuración definida por el usuario.

• modulo_exportar: confirma la configuración y exporta la tabla.

• gestor: comunica los modulos con la tabla, la tabla con el generador y
          a los modulos que no trabajan juntos, entre sí.

• tabla: almacena los datos que ingresa el usuario

• generador: produce la tabla con datos (pseudo)aleatorios de acuerdo a
             la configuración ingresada por el usuario
"""


import tkinter as tk
from tkinter import filedialog, font
from pathlib import Path
import random, secrets



# DICCIONARIOS QUE DEFINEN LA UBICACIÓN DE LOS OBJETOS
pack_marco_salir:dict = {'side':'top',
                         'fill': 'x',
                         'anchor':'n',
                         'expand': False,
                         'padx': 5,
                         'pady': 5}

pack_modulo_ajustes:dict = {'side':'left',
                            'fill': 'x',
                            'anchor':'ne',
                            'expand': True,
                            'padx': 5,
                            'pady': 5}

pack_modulo_vista:dict = {'side':'right',
                          'fill': 'x',
                          'anchor':'nw',
                          'expand': True,
                          'padx': 5,
                          'pady': 5}

pack_marco_modulo:dict = {'side':'top',
                          'fill': 'both',
                          'anchor':'n',
                          'expand': True,
                          'padx': 5,
                          'pady': 5}

pack_contenedor_ingreso:dict = {'side':'left',
                                'anchor':'w',
                                'fill': 'x',
                                'expand': True,
                                'padx': 5,
                                'pady': 5}

pack_eti_ingreso:dict = {'side':'top',
                         'anchor':'s',
                         'fill': 'x',
                         'expand': True,
                         'padx': 5,
                         'pady': 5}
pack_eti_error:dict = {'side':'top',
                         'anchor':'s',
                         'fill': 'x',
                         'expand': True,
                         'padx': 5,
                         'pady': 30}

pack_entrada_texto:dict = {'side':'top',
                           'fill': 'x',
                           'expand': True,
                           'pady':2}

pack_entrada_opcion:dict = {'side':'bottom',
                            'anchor':'s',
                           'expand': False,}

pack_contenedor_boton:dict = {'side':'right',
                              'fill': 'both',
                              'expand': False,
                              'padx': 5,
                              'pady': 0}
pack_contenedor_boton_borrado:dict = {'side':'left',
                              'fill': 'both',
                              'expand': False,
                              'padx': 5,
                              'pady': 0}

pack_boton:dict = {'side':'left',
                   'anchor': 's',
                   'padx': 5,
                   'pady': 5}
pack_boton_salir:dict = {'side':'right',
                   'anchor': 's',
                   'padx': 5,
                   'pady': 5} 

# DICCIONARIOS QUE DEFIENEN EL ASPECTO VISUAL DE LOS OBJETOS
estilo_raiz = {'bg':'black'}
estilo_contenedores_externos = {'bg':'purple'}
estilo_marco_modulo = {'bg':'#a34cb4'}
estilo_contenedor_ingreso = {'bg':'#e04cb4'}
estilo_vista_datos = { 'bg':'white', 'bd':2}
estilo_boton_ok:dict = {'bg':'#15ffbd',
                        'activebackground':'#0a8c5c',
                        'activeforeground':'#15ffbd',
                        'highlightthickness':2,
                        'borderwidth':5,
                        'height':1}
estilo_boton_opcion:dict = {'bg':'#b915ff',
                            'activebackground':'#4d096a',
                            'activeforeground':'#b915ff',
                            'borderwidth':3,
                            'height':1}
estilo_boton_ruido_ok:dict = {'bg':'#b915ff',
                            'activebackground':'#4d096a',
                            'activeforeground':'#b915ff',
                            'borderwidth':3,
                            'height':1}

estilo_boton_ruido_no_ok:dict = {'bg':'#ff3a2c',
                           'activebackground':'#8c2018',
                           'activeforeground':'#ff3a2c',
                            'borderwidth':3,
                            'height':1}
estilo_boton_no_ok:dict = {'bg':'#ff3a2c',
                           'activebackground':'#8c2018',
                           'activeforeground':'#ff3a2c',
                           'highlightthickness':2,
                           'borderwidth':5}
estilo_alerta:dict = {'bg':'#e36b02',
                         'activebackground':'#713501',
                         'activeforeground':'#e36b02',
                         'borderwidth':5}
estilo_:dict = {'bg':'#e36b02',
                         'activebackground':'#713501',
                         'activeforeground':'#e36b02',
                         'borderwidth':5}

estilo_etiqueta:dict = {'bg':'#000000', 'fg':'white'}
estilo_contenedor_boton:dict = {'bg':'#4a4a4a'}


#VENTANA PRINCIPAL
raiz = tk.Tk() 
raiz.attributes('-zoomed', True)
raiz.resizable(width=True,height=True)
raiz.configure(**estilo_raiz)
raiz.title('Generador')
#self.raiz.iconbitmap("") ICONO APLICACION
#self.raiz.minsize(700, 500)
x_pantalla = raiz.winfo_screenwidth()
y_pantalla = raiz.winfo_screenheight()
raiz.maxsize(x_pantalla,y_pantalla)
raiz.minsize(1248,632)

class InterfaceUsuario:
    def __init__(self):        
      
        # Marco raiz, contiene a todos loS widgets
        self.marco_raiz = tk.Frame(raiz, **estilo_marco_modulo)
        self.marco_raiz.pack(**pack_marco_modulo)

        # Modulo Salir
        self.modulo_salir = tk.Frame(self.marco_raiz,
                                     **estilo_marco_modulo)
        self.modulo_salir.pack(**pack_marco_salir)
        
        # Boton Salir
        self._boton_salir = BotonEspecial(self.modulo_salir,
                                          "Salir",
                                          raiz.destroy,
                                          estilo_alerta,
                                          FUENTE_BOTON_SALIR,
                                          pack_boton_salir,
                                          lambda event=None: raiz.destroy())
 
        # Etiqueta titulo de aplicacion
        self._eti_titulo_apliacion = tk.Label(self.modulo_salir,
                                               text=TX_TITULO,
                                               **estilo_etiqueta)
        self._eti_titulo_apliacion.config(font=FUENTE_PRINCIPAL)
        self._eti_titulo_apliacion.pack(**pack_eti_ingreso)

        # Contenedor de modulos Ajustes y Datos
        self.contenedor_ajustes_datos = tk.Frame(self.marco_raiz,
                                                 **estilo_contenedores_externos)
        self.contenedor_ajustes_datos.pack(**pack_marco_modulo)
        
        # Modulo ajustes
        self.modulo_ajustes = tk.Frame(self.contenedor_ajustes_datos,
                                       **estilo_contenedores_externos)
        self.modulo_ajustes.pack(**pack_modulo_ajustes)
        
        # Modulo Rutas
        self.modulo_ruta = ModuloRuta(self.modulo_ajustes)
        self.modulo_ruta.enfocar()

        # Modulo Encabezados
        self.modulo_encabezados = ModuloEncabezados(self.modulo_ajustes)

        # Modulo Opciones tabla
        self.modulo_opciones_tabla = ModuloOpcionesTabla(self.modulo_ajustes)

        # Modulo Campo
        self.modulo_campo = ModuloCampo(self.modulo_ajustes)

        # Modulo Borrar campo (trabaja junto con modulo_campo)
        self.modulo_borrar_campo = ModuloBorrarCampo(self.modulo_ajustes)

        # Modulo Campo Texto        
        self.modulo_campo_texto = ModuloCampoTexto(self.modulo_campo.marco_modulo)

        # Modulo Campo Numerico       
        self.modulo_campo_numerico = ModuloCampoNumerico(self.modulo_campo.marco_modulo)
       
        # Modulo Vista
        self.modulo_vista = tk.Frame(self.contenedor_ajustes_datos,
                                     **estilo_contenedores_externos)
        self.modulo_vista.pack(**pack_modulo_vista)
        self.modulo_ver_datos = ModuloVerDatos(self.modulo_vista)

        # Modulo Exportar
        self.modulo_exportar = ModuloExportar(self.modulo_vista)
        #aca tmb va el modulo_exportar_datos =  Modulo...()



class ModuloVerDatos:
    
    def __init__(self,ubicacion):

        # Marco de todo el módulo Vista
        self.marco_modulo = tk.Frame(ubicacion,
                                      **estilo_marco_modulo)
        self.marco_modulo.pack(**pack_marco_modulo)
        # Etiqueta modulo Vista
        self._eti_datos_ingresados = tk.Label(self.marco_modulo,
                                              text='DATOS INGRESADOS', #hacerlo constante
                                              **estilo_etiqueta)
        self._eti_datos_ingresados.config(font=FUENTE_ETIQUETA)
        self._eti_datos_ingresados.pack(**pack_eti_ingreso)
        
        # Cuadro texto donde se verán los datos ingresados
        self._contenedor_texto = tk.Text(self.marco_modulo,
                                         **estilo_vista_datos) 
        self._contenedor_texto.pack(**pack_marco_modulo)

## ACA DEBE IR UN SCROLL PARA LA VISTA CUANDO ESTE LLENO EL CUADRO
                
    # Muestra al usuario los datos que se van ingresando  
    def insertar_datos(self, datos):
        # Aca probar con el color del texto
        self._contenedor_texto.config(state=tk.NORMAL)
        self._contenedor_texto.delete("1.0", "end")
        self._contenedor_texto.insert("1.0", datos)
        self._contenedor_texto.config(state=tk.DISABLED)

       


   
class ModuloRuta:
        
    def __init__(self,ubicacion):
             
        # Marco de todo el módulo Ruta
        self.marco_modulo = tk.Frame(ubicacion,
                                      **estilo_marco_modulo)
        self.marco_modulo.pack(**pack_marco_modulo)

        # Submodulo entrada de la Ruta
        self._submodulo_entrada_ruta = SubmoduloEntradaTexto(self.marco_modulo,
                                                             TX_RUTA,
                                                             "/ruta_a_archivo.csv",
                                                             lambda event=None: self._confirmar_ruta())#hacerlo constante
        # Contenedor boton modulo Ruta
        self._contenedor_boton_ruta = tk.Frame(self.marco_modulo,
                                               **estilo_contenedor_boton)
        self._contenedor_boton_ruta.pack(**pack_contenedor_boton)

        # Boton Seleccionar Ruta
        self._boton_seleccionar_ruta = Boton(self._contenedor_boton_ruta,
                                             "Elegir ubicación",
                                             self._seleccionar_ruta,
                                             estilo_boton_ok,
                                             lambda event=None: self._seleccionar_ruta())
        # Boton Confirmar Ruta
        self._boton_confirmar_ruta = Boton(self._contenedor_boton_ruta,
                                           "Confirmar",
                                           self._confirmar_ruta,
                                           estilo_boton_ok,
                                           lambda event=None: self._confirmar_ruta())

    def _seleccionar_ruta(self):
        ruta_elegida = filedialog.askdirectory()
        self._submodulo_entrada_ruta.establecer_valor(ruta_elegida)
        return

    def _confirmar_ruta(self):
        respuesta = gestor.recibir("m_ruta",
                                   self._submodulo_entrada_ruta.obtener_valor())
        if respuesta:
            interface_usuario.modulo_encabezados.enfocar()
        return

    # Vacía el texto del widget de entrada
    def limpiar_entrada(self):
        self._submodulo_entrada_ruta.borrar_valor()

    def enfocar(self):
        self._submodulo_entrada_ruta.enfocar_entrada()
        
      


class ModuloEncabezados:

    # Se utiliza para gestionar la visibilidad del módulo
    _estado_modulo:bool = False
       
    def __init__(self,ubicacion):

        # Marco de todo el módulo Encabezados
        self.marco_modulo = tk.Frame(ubicacion,
                                     **estilo_marco_modulo)

        # Etiqueta del modulo OpcionesTabla
        self._eti_modulo_opciones = tk.Label(self.marco_modulo,
                                             text=TX_OPCIONES_TABLA,#hacerlo constante
                                             **estilo_etiqueta)
        self._eti_modulo_opciones.config(font=FUENTE_TITULO)
        self._eti_modulo_opciones.pack(**pack_eti_ingreso)        
        
        # Submodulo entrada de los Encabezados
        self._submodulo_entrada_encabezados = SubmoduloEntradaTexto(self.marco_modulo,
                                                                    TX_ENCABEZADOS,
                                                                    "Columna_1, ..., Columna_n",
                                                                    lambda event=None: self._confirmar_encabezados())      
        # Contenedor botones modulo Encabezados
        self._contenedor_botones_encabezados = tk.Frame(self.marco_modulo,
                                                        **estilo_contenedor_boton)
        self._contenedor_botones_encabezados.pack(**pack_contenedor_boton)

        # Boton borrar Encabezados
        self._boton_borrar_encabezados = Boton(self._contenedor_botones_encabezados,
                                               "Borrar encabezados",
                                               self._borrar_encabezados_ingresados,
                                               estilo_boton_no_ok,
                                               lambda event=None: self._borrar_encabezados_ingresados())
        # Boton confirmar Encabezados
        self._boton_confirmar_encabezados = Boton(self._contenedor_botones_encabezados,
                                                  "Confirmar",
                                                  self._confirmar_encabezados,
                                                  estilo_boton_ok,
                                                  lambda event=None: self._confirmar_encabezados())
        # Oculta el modulo al inicio
        self.cambiar_estado_modulo(False)

    def _confirmar_encabezados(self):
        respuesta = gestor.recibir("m_encabezados",
                                   self._submodulo_entrada_encabezados.obtener_valor())
        if respuesta:
            interface_usuario.modulo_opciones_tabla.enfocar()
        return
    
    # Vacia el widget de entrada y llama al Gestor
    # para que actulize los encabezados y se preserve
    # la consistencia de la tabla final
    def _borrar_encabezados_ingresados(self):
        self.limpiar_entrada()
        gestor.recibir("m_encabezados","actualizar_encabezados")

    # Vacía el texto del widget de entrada
    def limpiar_entrada(self):
        self._submodulo_entrada_encabezados.borrar_valor()

    def enfocar(self):
        self._submodulo_entrada_encabezados.enfocar_entrada()
        
    # Métodos de comunicacion con el Gestor
    def ver_estado_modulo(self):
        return self._estado_modulo
    
    def cambiar_estado_modulo(self, estado_modulo:bool):
        self._estado_modulo = estado_modulo
        if not estado_modulo:
            self.marco_modulo.pack_forget()            
        else:
            self.marco_modulo.pack(**pack_marco_modulo)

            

class ModuloOpcionesTabla:
    
    # Se utiliza para gestionar la visibilidad del módulo    
    _estado_modulo:bool = False
    
    def __init__(self,ubicacion):
     
        # Marco de todo el módulo OpcionesTabla
        self.marco_modulo = tk.Frame(ubicacion,
                                     **estilo_marco_modulo)

        # Submodulo entrada del Delimitador
        self._submodulo_entrada_delimitador = SubmoduloEntradaTexto(self.marco_modulo,
                                                                    TX_DELIMITADOR,
                                                                    ",",
                                                                    lambda event=None: self._confirmar_opciones())
        # Submodulo opciones Orden
        self._opc_orden_base = ["Ascendente", "Descendente", "Ninguno"]
        self._submodulo_opcion_orden = SubmoduloEntradaOpciones(self.marco_modulo,
                                                                TX_ORDEN,
                                                                self._opc_orden_base)
        # Submodulo opciones Segun
        self._opc_segun_base = ["columna_n"]
        self._submodulo_opcion_segun = SubmoduloEntradaOpciones(self.marco_modulo,
                                                                TX_SEGUN,
                                                                self._opc_segun_base)
        # Submodulo opciones Modo
        self._opc_modo_base = ["random", "secrets"]
        self._submodulo_opcion_modo = SubmoduloEntradaOpciones(self.marco_modulo,
                                                               TX_MODO,
                                                               self._opc_modo_base)
        # Contenedor boton modulo OpcionesTabla
        self._contenedor_boton_opciones_tabla = tk.Frame(self.marco_modulo,
                                                         **estilo_contenedor_boton)
        self._contenedor_boton_opciones_tabla.pack(**pack_contenedor_boton)
        
        # Boton confirmar OpcionesTabla
        self._boton_confirmar_opciones = Boton(self._contenedor_boton_opciones_tabla,
                                               "Confirmar opciones",
                                               self._confirmar_opciones,
                                               estilo_boton_ok,
                                               lambda event=None: self._confirmar_opciones())
        # Oculta el modulo al inicio
        self.cambiar_estado_modulo(False) 
        
    def _confirmar_opciones(self):
        aux_opc:list = []
        aux_opc.append(self._submodulo_entrada_delimitador.obtener_valor())
        aux_opc.append(self._submodulo_opcion_orden.obtener_valor())
        aux_opc.append(self._submodulo_opcion_segun.obtener_valor())
        aux_opc.append(self._submodulo_opcion_modo.obtener_valor())
        respuesta = gestor.recibir("m_opciones_tabla", aux_opc)
        if respuesta:
            interface_usuario.modulo_campo.enfocar()
        return

    # Vacía el texto del widget de entrada
    def limpiar_entrada(self):
        self._submodulo_entrada_delimitador.borrar_valor()
    
    def enfocar(self):
        self._submodulo_entrada_delimitador.enfocar_entrada()
        
    def ver_estado_modulo(self):
        return self._estado_modulo

    def actualizar_opciones_segun(self):
        self._submodulo_opcion_segun.actualizar_opciones(gestor.ver_encabezados())
        return None
    
    # Solo cuando se reinicia recibe un False
    def cambiar_estado_modulo(self, estado_modulo:bool): 
        self._estado_modulo = estado_modulo
        if not estado_modulo:
            self.marco_modulo.pack_forget()            
        else:
            # Actuliza la lista con la opción por defecto
            self._submodulo_opcion_segun.actualizar_opciones(gestor.ver_encabezados())           
            self.marco_modulo.pack(**pack_marco_modulo)


class ModuloCampo:
    
    # Se utiliza para gestionar la visibilidad del módulo
    _estado_modulo:bool = False
    _tipo_de_dato_activado: str = ""

    def __init__(self, ubicacion):

        # Marco de todo el módulo Campos
        self.marco_modulo = tk.Frame(ubicacion,
                                      **estilo_marco_modulo)
        # Etiqueta modulo Campos
        self._eti_modulo_campo = tk.Label(self.marco_modulo,
                                          text=TX_VALORES_CAMPO,
                                          **estilo_etiqueta)
        self._eti_modulo_campo.config(font=FUENTE_TITULO)
        self._eti_modulo_campo.pack(**pack_eti_ingreso)
        
        # Contenedor opciones fijas Campo
        self._contenedor_opciones_campo = tk.Frame(self.marco_modulo,
                                                   **estilo_marco_modulo)
        self._contenedor_opciones_campo.pack(**pack_marco_modulo)

        # Submodulo elegir Campo
        self._opc_elegir_campo_base = ["Encabezado_1","Encabezado_2"]
        self._submodulo_elegir_campo = SubmoduloEntradaOpciones(self._contenedor_opciones_campo,
                                                                TX_SELECC_CAMPO,
                                                                self._opc_elegir_campo_base,
                                                                self._rastrear_campo_elegido)
        # Submodulo Tipo de campo
        self._opc_tipo_campo_base = ["Booleano","Numérico", "Texto"]
        self._submodulo_tipo_campo = SubmoduloEntradaOpciones(self._contenedor_opciones_campo,
                                                              TX_TIPO_CAMPO,
                                                              self._opc_tipo_campo_base,
                                                              self._rastrear_opcion_tipo_de_dato)
        # Submodulo elegir Logica
        self._opc_logica_base = ["True|False", "True|False|None"]
        self._submodulo_elegir_logica = SubmoduloEntradaOpciones(self._contenedor_opciones_campo,
                                                                 TX_LOGICA,
                                                                 self._opc_logica_base)
        # Contenedor del boton confirmar Campo booleano
        self._contenedor_boton_definir_campo_booleano = tk.Frame(self._contenedor_opciones_campo,
                                                                 **estilo_contenedor_boton)
        self._contenedor_boton_definir_campo_booleano.pack(**pack_contenedor_boton)
        
        # Boton confirmar Campo booleano
        self._boton_confirmar_campo_booleano = Boton(self._contenedor_boton_definir_campo_booleano,
                                                     "Confirmar campo booleano",
                                                     self._confirmar_campo_booleano,
                                                     estilo_boton_ok,
                                                     lambda event=None: self._confirmar_campo_booleano())
        # Oculta el modulo al inicio
        self.cambiar_estado_modulo(False)
        
    def _rastrear_campo_elegido(self, *args):
        campo_actual = self._submodulo_elegir_campo.obtener_valor()
        if self._tipo_de_dato_activado == "Texto":
            interface_usuario.modulo_campo_texto.activar_campo(campo_actual)
        elif self._tipo_de_dato_activado == "Numérico":
            interface_usuario.modulo_campo_numerico.activar_campo(campo_actual)
        return None

    # Cada vez que se cambia el campo seleccionado
    # define el actual como campo activo (si corresponde)
    def _rastrear_opcion_tipo_de_dato(self, *args):
        self._tipo_de_dato_activado = self._submodulo_tipo_campo.obtener_valor()
        campo_actual = self._submodulo_elegir_campo.obtener_valor()     
        if self._tipo_de_dato_activado == "Texto":
            # Oculta el boton de confirmar campo booleano
            self._contenedor_boton_definir_campo_booleano.pack_forget()
            self._submodulo_elegir_logica.ocultar_submodulo()
            # Activa el campo actual en Campo texto
            interface_usuario.modulo_campo_texto.activar_campo(campo_actual)
            # Vuelve visible el modulo para definir los posibles valores del campo actual
            gestor.ocultar_modulo("campo_numerico")
            gestor.mostrar_modulo("campo_texto")
            interface_usuario.modulo_campo_texto.enfocar()
            
        elif self._tipo_de_dato_activado == "Numérico":
            self._contenedor_boton_definir_campo_booleano.pack_forget()
            self._submodulo_elegir_logica.ocultar_submodulo()
            interface_usuario.modulo_campo_numerico.activar_campo(campo_actual)
            gestor.ocultar_modulo("campo_texto")
            gestor.mostrar_modulo("campo_numerico")
            interface_usuario.modulo_campo_numerico.enfocar()

        elif self._tipo_de_dato_activado == "Booleano":
            # Desactiva el campo actual para que no haya contradicciones
            # con los campos de texto y numéricos
            self._tipo_de_dato_activado = ""
            interface_usuario.modulo_campo_texto.desactivar_campo()
            interface_usuario.modulo_campo_numerico.desactivar_campo() 
            # Hace visible el boton definir campo booleano y tipo de logica
            self._contenedor_boton_definir_campo_booleano.pack(**pack_contenedor_boton)
            self._submodulo_elegir_logica.mostrar_submodulo()
            # Oculta los módulos que no estan en uso
            gestor.ocultar_modulo("campo_texto")
            gestor.ocultar_modulo("campo_numerico")
        return None

    def _confirmar_campo_booleano(self):
        mensaje:list = []
        mensaje.append(self._submodulo_elegir_campo.obtener_valor())
        mensaje.append(self._submodulo_elegir_logica.obtener_valor())
        respuesta = gestor.recibir("m_campo_booleano", mensaje)
        if respuesta:
            gestor.mostrar_modulo("exportar")
            gestor.mostrar_modulo("borrar_campo")
            interface_usuario.modulo_borrar_campo.actualizar_campos_definidos()
            interface_usuario.modulo_exportar.enfocar()
        return None
    
    def reiniciar_tipo_de_campo(self):
        self._submodulo_tipo_campo.reiniciar_opciones()

    def enfocar(self):
        self._boton_confirmar_campo_booleano.enfocar_boton()
    
    def ver_estado_modulo(self):
        return self._estado_modulo

    # Actualiza las opciones de campos con los encabezados existentes
    def actualizar_opciones_campo(self):
        self._submodulo_elegir_campo.actualizar_opciones(gestor.ver_encabezados())
        return

    def ver_estado_modulo(self):
        return self._estado_modulo
    
    # Solo cuando se reinicia recibe un False
    def cambiar_estado_modulo(self, estado_modulo:bool): 
        self._estado_modulo = estado_modulo
        if not estado_modulo:
            self.marco_modulo.pack_forget()            
        else:
            # Actuliza la lista con las opciones por defecto
            self._submodulo_elegir_campo.actualizar_opciones(gestor.ver_encabezados())           
            self.marco_modulo.pack(**pack_marco_modulo)
        return
    


# Permite borrar los campos definidos y restablecer la tabla
class ModuloBorrarCampo:

    # Se utiliza para gestionar la visibilidad del módulo
    _estado_modulo:bool = False  
    
    def __init__(self,ubicacion):

        # Marco de todo el módulo Borrar campos
        self.marco_modulo = tk.Frame(ubicacion,
                                      **estilo_marco_modulo)
        # Contenedor boton borrar campo
        self._contenedor_boton_borrar_campo = tk.Frame(self.marco_modulo,
                                                      **estilo_contenedor_boton)
        self._contenedor_boton_borrar_campo.pack(**pack_contenedor_boton_borrado)

        # Submodulo borrar campo
        self._opc_campos = ['campo_1', '...', 'campo_n']
        self._submodulo_borrar_campo = SubmoduloEntradaOpciones(self._contenedor_boton_borrar_campo,
                                                                TX_CAMPO_BORRAR,
                                                                self._opc_campos,
                                                                self.actualizar_campos_definidos,
                                                                estilo_alerta)
        # Boton borrar campoa seleccionado
        self._boton_borrar_campo = Boton(self._contenedor_boton_borrar_campo,
                                               "Eliminar datos del campo",
                                               self._eliminar_valores,
                                               estilo_boton_no_ok,
                                               lambda event=None: self._eliminar_valores())
        
        # Contenedor boton restablecer
        self._contenedor_boton_restablecer = tk.Frame(self.marco_modulo,
                                                      **estilo_contenedor_boton)
        self._contenedor_boton_restablecer.pack(**pack_contenedor_boton)

        # Boton restablecer la tabla
        self._boton_reestablecer_tabla = Boton(self._contenedor_boton_restablecer,
                                               "Borrar todo",
                                               self._restablecer_todo,
                                               estilo_boton_no_ok,
                                               lambda event=None: self._restablecer_todo())
        # Oculta el modulo al iniciar
        self.cambiar_estado_modulo(False)

    def _eliminar_valores(self):
        campo_a_eliminar = self._submodulo_borrar_campo.obtener_valor()
        gestor.borrar_campo(campo_a_eliminar)
        self.actualizar_campos_definidos()
        
    # Restablece los valores de Tabla
    def _restablecer_todo(self):
        gestor.vaciar_tabla()
        gestor.restablecer_aplicacion()

    def actualizar_campos_definidos(self, *args):
        nuevos_campos:list = gestor.ver_campos_definidos()
        if len(nuevos_campos) == 0:
            nuevos_campos = ['No hay campos definidos']
            gestor.ocultar_modulo("exportar")
        self._submodulo_borrar_campo.actualizar_opciones(nuevos_campos)
    
    # Comunicacion con Gestor
    def ver_estado_modulo(self):
        return self._estado_modulo
    
    def cambiar_estado_modulo(self, estado_modulo:bool):
        self._estado_modulo = estado_modulo
        if not estado_modulo:
            self.marco_modulo.pack_forget()
        else:
            self.actualizar_campos_definidos()
            self.marco_modulo.pack(**pack_marco_modulo)

class ModuloCampoTexto:
    _estado_modulo:bool = False
    _campo_activo:str = ""
        
    def __init__(self,ubicacion):
             
        # Marco de todo el módulo CampoTexto
        self.marco_modulo = tk.Frame(ubicacion,
                                      **estilo_marco_modulo)
        # Submodulo entrada de valores CampoTexto
        self._submodulo_entrada_valores_texto = SubmoduloEntradaTexto(self.marco_modulo,
                                                                      TX_VALORES_TEXTO,
                                                                      "valor_1, ..., valor_n",
                                                                      lambda event=None: self._confirmar_campo_texto())
        # Contenedor boton modulo CampoTexto
        self._contenedor_boton_texto = tk.Frame(self.marco_modulo,
                                               **estilo_contenedor_boton)
        self._contenedor_boton_texto.pack(**pack_contenedor_boton)
        # Boton borrar valores ingresados
        self._boton_borrar_valores_texto = Boton(self._contenedor_boton_texto,
                                                 "Borrar valores",
                                                 self.limpiar_entrada,
                                                 estilo_boton_no_ok,
                                                 lambda event=None: self.limpiar_entrada())
        # Boton Confirmar valores texto
        self._boton_confirmar_texto = Boton(self._contenedor_boton_texto,
                                            "Confirmar campo de texto",
                                            self._confirmar_campo_texto,
                                            estilo_boton_ok,
                                            lambda event=None: self._confirmar_campo_texto())
        # Oculta el modulo al iniciar
        self.cambiar_estado_modulo(False)        
                
    def _confirmar_campo_texto(self):
        mensaje:list = []
        mensaje.append(self._campo_activo)
        mensaje.append(self._submodulo_entrada_valores_texto.obtener_valor())
        respuesta = gestor.recibir("m_campo_texto", mensaje)
        if respuesta:
            gestor.mostrar_modulo("exportar")
            gestor.mostrar_modulo("borrar_campo")
            interface_usuario.modulo_borrar_campo.actualizar_campos_definidos()
            interface_usuario.modulo_exportar.enfocar()
        return 

    # Vacía el texto del widget de entrada
    def limpiar_entrada(self):
        self._submodulo_entrada_valores_texto.borrar_valor()

    def enfocar(self):
        self._submodulo_entrada_valores_texto.enfocar_entrada()

    # Métodos para indicarle a los módulos sobre cual campo
    # deben registrar los valores que reciban
    def activar_campo(self, campo:str):
        self._campo_activo = campo

    def desactivar_campo(self):
        self._campo_activo = "" 

    def cambiar_estado_modulo(self, estado_modulo:bool):
        self._estado_modulo = estado_modulo
        if not estado_modulo:
            self.marco_modulo.pack_forget()
        else:
            self.marco_modulo.pack(**pack_marco_modulo)



class ModuloCampoNumerico:
    
    # Se utiliza para gestionar la visibilidad del módulo    
    _estado_modulo:bool = False
    _campo_activo:str = ""
    
    def __init__(self,ubicacion):
     
        # Marco de todo el módulo Campo numerico
        self.marco_modulo = tk.Frame(ubicacion,
                                      **estilo_marco_modulo)
                
        # Submodulo entrada rango incio
        self._submodulo_entrada_rango_inicio = SubmoduloEntradaTexto(self.marco_modulo,
                                                                     TX_R_DESDE,
                                                                     "0",
                                                                     lambda event=None: self._confirmar_rango())
        # Submodulo entrada rango fin
        self._submodulo_entrada_rango_fin = SubmoduloEntradaTexto(self.marco_modulo,
                                                                  TX_R_HASTA,
                                                                  "100",
                                                                  lambda event=None: self._confirmar_rango())
        # Submodulo opciones tipo numerico
        self._opc_tipo_base = ["Enteros", "Reales", "Complejos"]
        self._submodulo_opcion_tipo = SubmoduloEntradaOpciones(self.marco_modulo,
                                                               TX_R_CONJUNTO,
                                                               self._opc_tipo_base)
        # Contenedor boton modulo Campo numerico
        self._contenedor_boton_campo_numerico = tk.Frame(self.marco_modulo,
                                                         **estilo_contenedor_boton)
        self._contenedor_boton_campo_numerico.pack(**pack_contenedor_boton)   
        # Boton confirmar rango
        self._boton_confirmar_rango = Boton(self._contenedor_boton_campo_numerico,
                                            "Caonfirmar campo numérico",
                                            self._confirmar_rango,
                                            estilo_boton_ok,
                                            lambda event=None: self._confirmar_rango())
        # Oculta el modulo al inicio
        self.cambiar_estado_modulo(False) 
           
    def _confirmar_rango(self):
        mensaje:list = []
        mensaje.append(self._campo_activo)
        mensaje.append(self._submodulo_entrada_rango_inicio.obtener_valor())
        mensaje.append(self._submodulo_entrada_rango_fin.obtener_valor())
        mensaje.append(self._submodulo_opcion_tipo.obtener_valor())
        respuesta = gestor.recibir("m_campo_numerico", mensaje)
        if respuesta:
            gestor.mostrar_modulo("exportar")
            gestor.mostrar_modulo("borrar_campo")
            interface_usuario.modulo_borrar_campo.actualizar_campos_definidos()
            interface_usuario.modulo_exportar.enfocar()
        return    

    # Vacía el texto los widgets de entrada
    def limpiar_entrada(self):
        self._submodulo_entrada_rango_inicio.borrar_valor()
        self._submodulo_entrada_rango_fin.borrar_valor()
        
    def enfocar(self):
        self._submodulo_entrada_rango_inicio.enfocar_entrada()
    
    # Métodos para indicarle a los módulos sobre cual campo
    # deben registrar los valores que reciban
    def activar_campo(self, campo:str):
        self._campo_activo = campo

    def desactivar_campo(self):
        self._campo_activo = "" 

    def cambiar_estado_modulo(self, estado_modulo:bool):
        self._estado_modulo = estado_modulo
        if not estado_modulo:
            self.marco_modulo.pack_forget()
        else:
            self.marco_modulo.pack(**pack_marco_modulo)


class ModuloExportar:

    # Se utiliza para gestionar la visibilidad del módulo
    _estado_modulo:bool = False
    _contador_ruido:int = 0
       
    def __init__(self,ubicacion):

        # Marco de todo el módulo Encabezados
        self.marco_modulo = tk.Frame(ubicacion,
                                      **estilo_marco_modulo)     
        # Submodulo entrada numero de filar
        self._submodulo_entrada_num_filas = SubmoduloEntradaTexto(self.marco_modulo,
                                                                  TX_NUM_FILAS,
                                                                  "100",
                                                                  lambda event=None: self._confirmar_exportar())      
        # Contenedor botones modulo Exportar
        self._contenedor_botones_exportar = tk.Frame(self.marco_modulo,
                                                     **estilo_contenedor_boton)
        self._contenedor_botones_exportar.pack(**pack_contenedor_boton)
        
        # Boton agregar ruido
        self._boton_agregar_ruido = Boton(self._contenedor_botones_exportar,
                                                  "Agregar ruido",
                                                  self._agregar_ruido,
                                                  estilo_boton_ruido_ok,
                                                  lambda event=None: self._agregar_ruido())      
        
        # Boton eliminar ruido
        self._boton_eliminar_ruido = Boton(self._contenedor_botones_exportar,
                                           "Eliminar ruido",
                                           self._eliminar_ruido,
                                           estilo_boton_ruido_no_ok,
                                           lambda event=None: self._eliminar_ruido())       
        # Boton confirmar Exportar
        self._boton_exportar = Boton(self._contenedor_botones_exportar,
                                     "Exportar tabla",
                                     self._exportar,
                                     estilo_boton_ok,
                                     lambda event=None: self._exportar())
        # Oculta el modulo al inicio
        self.cambiar_estado_modulo(False)

    def _exportar(self):
        t_aux:tuple = (self._submodulo_entrada_num_filas.obtener_valor(),
                       self._contador_ruido)
        respuesta = gestor.recibir("m_exportar", t_aux)
        if respuesta:
            interface_usuario.modulo_ruta.enfocar()
        return None
    
    #5% de errores en los ingresos
    def _agregar_ruido(self):
        if self._contador_ruido < 20:
            self._contador_ruido += 1
        return None
        
    def _eliminar_ruido(self):
        self._contador_ruido = 0
        return None

    # Vacía el texto del widget de entrada
    def limpiar_entrada(self):
        self._submodulo_entrada_num_filas.borrar_valor()
        self._eliminar_ruido()
        return None

    def enfocar(self):
        self._submodulo_entrada_num_filas.enfocar_entrada()
        return None
        
    # Métodos de comunicacion con el Gestor
    def ver_estado_modulo(self):
        return self._estado_modulo
    
    def cambiar_estado_modulo(self, estado_modulo:bool):
        self._estado_modulo = estado_modulo
        if not estado_modulo:
            self.limpiar_entrada()
            self._eliminar_ruido()
            self.marco_modulo.pack_forget()            
        else:
            self.marco_modulo.pack(**pack_marco_modulo)
        return None
     


# Gestiona la comunicación entre los módulos
class Gestor:
    
    def __init__(self):
        pass

    # Recibe un mensaje y el módulo de origen
    # y lo envía al método correspondiente
    def recibir(self, origen, mensaje) -> None:
        gestion:bool = False
        
        if origen == "m_ruta":
            gestion = self._gestion_modulo_ruta(mensaje)
            
        elif origen == "m_encabezados":
            gestion = self._gestion_modulo_encabezados(mensaje)

        elif origen == "m_opciones_tabla":
            gestion = self._gestion_modulo_opciones_tabla(mensaje)
            
        elif origen == "m_campo_booleano":
            gestion = self._gestion_modulo_campo_booleano(mensaje)
            
        elif origen == "m_campo_texto":
            gestion = self._gestion_modulo_campo_texto(mensaje)
        
        elif origen == "m_campo_numerico":
            gestion = self._gestion_modulo_campo_numerico(mensaje)

        elif origen == "m_exportar":
            gestion = self._gestion_modulo_exportar(mensaje)                 
        # Cada vez que el mensaje se gestionó bien
        # actualiza la vista de Datos Ingresados
        if gestion:
            self.actualizar_vista()
            
        return gestion
    
    # Actualiza la vista de Datos Ingresados
    def actualizar_vista(self):
        interface_usuario.modulo_ver_datos.insertar_datos(tabla.obtener_datos())
        return None

    # Devuelve los encabezados registrados en la tabla
    def ver_encabezados(self) -> str:
        return tabla.obtener_encabezados()
    
    # Devuelve los campos definidos en la tabla
    def ver_campos_definidos(self) -> str:
        return tabla.campos_definidos()

    def restablecer_aplicacion(self):
        # Limpia las entradas
        interface_usuario.modulo_ruta.limpiar_entrada()
        interface_usuario.modulo_encabezados.limpiar_entrada()
        interface_usuario.modulo_campo_texto.limpiar_entrada()
        interface_usuario.modulo_campo_numerico.limpiar_entrada()
        interface_usuario.modulo_opciones_tabla.limpiar_entrada()
        # Oculta todos los modulos excepto Ruta
        modulos_a_ocultar = ["exportar","borrar_campo", "campo_texto", "campo_numerico",
                             "campo", "opciones_tabla", "encabezados"]
        for modulo in modulos_a_ocultar:
            self.ocultar_modulo(modulo)  
        # Establecer el tipo de campo en Booleano
        interface_usuario.modulo_campo.reiniciar_tipo_de_campo()
        # Establece el foco en el cuadro de entrada de la ruta de salida        
        interface_usuario.modulo_ruta.enfocar()
        return None
    # Devuelve todos los datos de la tabla
    def ver_datos_tabla(self) -> str:
        return tabla.obtener_datos()

    # Vacia todos los datos ingresados a la tabla
    def vaciar_tabla(self):
        tabla.restablecer_tabla()


    # Metodos auxiliares a la gestion de estados de los módulos
    # Pueden ser llamados directamente para resolver casos puntuales
    # Reciben el nombre del modulo a tratar, sin el prefijo "_modulo"          
    def ocultar_modulo(self, modulo:str):
        modulo_objetivo = getattr(interface_usuario, f"modulo_{modulo.lower()}")
        modulo_objetivo.cambiar_estado_modulo(False)

    def mostrar_modulo(self, modulo:str):
        modulo_objetivo = getattr(interface_usuario, f"modulo_{modulo.lower()}")
        modulo_objetivo.cambiar_estado_modulo(True)

    # Borra campos los valores ingresados a la tabla
    # del campo que se le especifique
    def borrar_campo(self, nombre_campo):
        if nombre_campo in tabla.obtener_campos_booleanos():
            tabla.borrar_campo_booleano(nombre_campo)
        elif nombre_campo in tabla.obtener_campos_texto():
            tabla.borrar_campo_texto(nombre_campo)      
        elif nombre_campo in tabla.obtener_campos_enteros():
            tabla.borrar_campo_entero(nombre_campo)
        elif nombre_campo in tabla.obtener_campos_reales():
            tabla.borrar_campo_real(nombre_campo)
        elif nombre_campo in tabla.obtener_campos_complejos():
            tabla.borrar_campo_complejo(nombre_campo)
        return None


    # Gestion mensajes de módulo Ruta
    def _gestion_modulo_ruta(self, mensaje:str) -> bool:
        res:bool = False
        if self._es_ruta_valida(mensaje):
            res = True
        else:
            self._mostrar_error("Por favor introduzca una ruta válida",
                                "Error de ubicación")
        # Gestión de estados del modulos: habilita encabezados
        if res:
            estado_modulo:bool = interface_usuario.modulo_encabezados.ver_estado_modulo()
            if estado_modulo==False and len(str(tabla.obtener_ruta()))>4:
                self.mostrar_modulo("encabezados")
            elif estado_modulo==True and len(str(tabla.obtener_ruta()))<=4:
                self.ocultar_modulo("encabezados")
            else:
                self.mostrar_modulo("encabezados")
        return res                             

    # Valida la ruta ingresada y actuliza el dato en Tabla
    def _es_ruta_valida(self, ruta) -> bool: 
        res:bool = False
        ruta_final = Path(ruta)
        if ruta.endswith(".csv") and ruta_final.parent.is_dir():
            res = True
        elif ruta_final.is_dir():
            ruta_final = ruta_final / "tabla_datos_pseudoaleatorios.csv"
            res = True
        if res:
            tabla.establecer_ruta(ruta_final)        
        return res

    # Gestion mensajes de módulo Encabezados
    def _gestion_modulo_encabezados(self, mensaje:str) -> bool:
        res:bool = False
        lista_encabezados:list = []
        if mensaje == "actualizar_encabezados":
            self._actualizar_encabezados()
            return            
        if len(mensaje) < 1:
            self._mostrar_error("Por favor introduzca los encabezados de su tabla separados por comas.",
                                "Error al ingresar los encabezados")
        else:
            lista_encabezados = self._limpiar_lista(mensaje)
            tabla.establecer_encabezados(lista_encabezados)
            res = True         
        # Si algún Campo definido no está en Encabezados lo borra
        for campo in list(tabla.obtener_campos_booleanos()):
            if campo not in lista_encabezados:
                tabla.borrar_campo_booleano(campo)
        for campo in list(tabla.obtener_campos_texto()):
            if campo not in lista_encabezados:
                tabla.borrar_campo_texto(campo)
        for campo in list(tabla.obtener_campos_enteros()):
            if campo not in lista_encabezados:
                tabla.borrar_campo_entero(campo)
        for campo in list(tabla.obtener_campos_reales()):
            if campo not in lista_encabezados:
                tabla.borrar_campo_real(campo)
        for campo in list(tabla.obtener_campos_complejos()):
            if campo not in lista_encabezados:
                tabla.borrar_campo_complejo(campo)
                
        # Actualiza las opciones de campos a borrar
        interface_usuario.modulo_borrar_campo.actualizar_campos_definidos()
        # Gestión de estados del modulos: habilita opciones de tabla
        if res:
            self.mostrar_modulo("opciones_tabla")
        # Manda los nuevos valores para que esten disponibles en modulo Campo
        interface_usuario.modulo_campo.actualizar_opciones_campo() 
        return res

    def _limpiar_lista(self, cadena:str) -> list:
        lista_salida:list = cadena.split(',')
        lista_salida = [item.strip() for item in lista_salida]
        lista_salida = [item for item in lista_salida if item != " "]
        lista_aux:list = []
        [lista_aux.append(e) for e in lista_salida if e not in lista_aux]
        lista_salida = lista_aux
        return lista_salida

    # Vuelve a cero la lista de encabezados
    # y las opciones que los utilizan
    def _actualizar_encabezados(self):
        tabla.borrar_encabezados()        
        tabla.borrar_todos_los_campos()
        interface_usuario.modulo_borrar_campo.actualizar_campos_definidos()
        interface_usuario.modulo_opciones_tabla.actualizar_opciones_segun()
        interface_usuario.modulo_campo.actualizar_opciones_campo()
        gestor.actualizar_vista()

    # Gestion mensajes de módulo Opciones tabla
    def _gestion_modulo_opciones_tabla(self, mensaje:list) -> bool:
        res:bool = False
        if len(mensaje[0]) != 1:
            self._mostrar_error("Solo se permite un único carácter como delimitador.",
                                "Error de delimitador")
        elif (not mensaje[2] in tabla.obtener_encabezados() and
                  mensaje[1] != "Ninguno"):
            self._mostrar_error("Por favor verifique los encabezados ingresados y seleccione alguno de ellos.",
                                "Error en opción: SEGÚN")
        else:
            tabla.establecer_delimitador(mensaje[0])
            tabla.establecer_orden(mensaje[1])
            tabla.establecer_segun(mensaje[2])
            tabla.establecer_modo(mensaje[3])
            # Gestión de estados del modulos: habilita opciones de tabla
            self.mostrar_modulo("campo")
            res = True           
        return res

    # Gestion mensajes de módulo Campo
    # Si todo ok lo registra en la tabla
    def _gestion_modulo_campo_booleano(self, mensaje:list) -> bool:
        res:bool = False
        nombre_campo = mensaje[0]
        tipo_logica = mensaje[1]
        condiciones:bool = self._condiciones_basicas(nombre_campo)            
        if condiciones:
            tabla.establecer_campo_booleano(nombre_campo, tipo_logica)
            res = True
        return res

    def _gestion_modulo_campo_texto(self, mensaje):
        res:bool = False
        nombre_campo:str = mensaje[0]
        valores_posibles:str = mensaje[1]
        condiciones:bool = self._condiciones_basicas(nombre_campo)        
        if condiciones:
            valores:list = self._limpiar_lista(valores_posibles)
            valores = [item for item in valores if item != ""]
            if any(valor != "" for valor in valores):
                tabla.establecer_campo_texto(nombre_campo, valores)
                res = True
            else:
                m_error = f'El campo "{nombre_campo}" no recibió ningún valor posible.\n'
                self._mostrar_error(m_error, "Error de valores ingresados")        
        return res

    def _condiciones_basicas(self, nombre_campo:str) -> bool:
        res:bool = False
        campos_definidos:list = tabla.campos_definidos()
        if nombre_campo == "":
            m_error:str = "Por favor seleccione un campo que no haya sido definido."                
            self._mostrar_error(m_error, "Error de asignación de tipo de campo") 
        elif nombre_campo not in tabla.obtener_encabezados():
            m_error:str = "Solo se puede definir valores de un campo existente. Por favor revise los encabezados."                
            self._mostrar_error(m_error, "Error de campo inexistente")     
        elif nombre_campo in campos_definidos:
            m_error = f'El campo "{nombre_campo}" ya tiene definidos sus posibles valores.\n'
            m_error += f'Para reemplazarlos borre "{nombre_campo}" presionando el botón correspondiente.'
            self._mostrar_error(m_error, "Error de campo repetido")
        else:
            res = True
        return res
        
    
    def _gestion_modulo_campo_numerico(self, mensaje):
        res:bool = False
        nombre_campo:str = mensaje[0]
        rango_inicio = mensaje[1].strip()
        rango_fin = mensaje[2].strip()
        tipo_numerico = mensaje[3]
        condiciones:bool = self._condiciones_basicas(nombre_campo)
        if rango_inicio == '' or rango_fin == '':
            m_error:str = "Por favor ingrese un rango válido"
            self._mostrar_error(m_error, "Error de rango")
            return res
        if condiciones:
            rango_inicio = self._preservar_signo(rango_inicio)
            rango_fin = self._preservar_signo(rango_fin)
            if type(rango_inicio) is int and type(rango_fin) is int:
                if rango_inicio > rango_fin:
                    m_error:str = "El rango de inicio debe ser menor que el final"
                    self._mostrar_error(m_error, "Error de rango")
                if rango_inicio < rango_fin:
                    rango:range = range(rango_inicio, rango_fin)
                    if tipo_numerico == "Enteros":
                        tabla.establecer_campo_entero(nombre_campo, rango)
                        res = True
                    elif tipo_numerico == "Reales":
                        tabla.establecer_campo_real(nombre_campo, rango)
                        res = True
                    elif tipo_numerico == "Complejos":
                        tabla.establecer_campo_complejo(nombre_campo, rango)
                        res = True
            else:
                m_error:str = "Por favor ingrese un rango válido"
                self._mostrar_error(m_error, "Error de rango")
        return res

    # Permite ingresar números negativos como rango (ver de mejorarla un poco)
    def _preservar_signo(self, numero:str):
        res:int = 0
        if (not numero.isdigit() and numero[0] == '-' and numero[1:].isdigit()) or numero.isdigit():
            res = int(numero)
        else:
            res = numero
        return res

    def _gestion_modulo_exportar(self, mensaje):
        res:bool = False
        num_filas:int = mensaje[0]
        cant_ruido:int = mensaje[1]
        if num_filas.isdigit():
            print('Se activa el generador')
            pass
            res = True
        else:
            m_error:str = "Por favor ingrese un número de filas válido"
            self._mostrar_error(m_error, "Error de número de filas")
        return res


    # Genera la ventana que muestra el aviso de error
    def _mostrar_error(self, mensaje_error, titulo_ventana):
        #agregar icnono ventana
        self._ventana_error = tk.Toplevel(raiz, **estilo_raiz)
        self._ventana_error.title(titulo_ventana)
        self._ventana_error.minsize(600,100)
        self._etiqueta_mensaje = tk.Label(self._ventana_error,
                                  text=mensaje_error,
                                  **estilo_etiqueta)
        self._etiqueta_mensaje.config(font=FUENTE_ETIQUETA)
        self._etiqueta_mensaje.pack(**pack_eti_error)

        self._boton_cerrar = tk.Button(self._ventana_error,
                                       text="Cerrar",
                                       command=self._ventana_error.destroy,
                                       **estilo_boton_no_ok)
        self._boton_cerrar.pack(side='top', pady=20)
        self._boton_cerrar.focus_set()
        
        # Llama a establecer_opciones cada vez que el usuario
        # presione enter dentro del delimitador
        self._boton_cerrar.bind("<Return>",
                                lambda event=None: self._ventana_error.destroy())


#Almacen de datos
class Tabla:
    _ruta_salida_csv:str = ""
    _encabezados_tabla:list = []
    _delimitador:str = ""
    _orden:str = ""
    _segun:str = ""
    _modo:str = ""
    _campos_booleanos:dict = dict()
    _campos_texto:dict = dict()
    _campos_enteros:dict = dict()
    _campos_reales:dict = dict()
    _campos_complejos:dict = dict()
    
    def __init__(self):
        pass
    
    # MÉTODOS RUTA    
    def establecer_ruta(self, ruta:str):
        self._ruta_salida_csv = ruta

    def obtener_ruta(self):
        return self._ruta_salida_csv
    
    # MÉTODOS ENCABEZADOS
    def establecer_encabezados(self, encabezados:list):
        encabezados = [e for e in encabezados if e != ""] 
        self._encabezados_tabla = encabezados
        return None

    def obtener_encabezados(self) -> list:
        return self._encabezados_tabla

    def borrar_encabezados(self):
        self._encabezados_tabla = []
        gestor.actualizar_vista()

    # MÉTODOS DELIMITADOR    
    def establecer_delimitador(self, delimitador:str):
        self._delimitador = delimitador

    def obtener_delimitador(self) -> str:
        return self._delimitador    

    # MÉTODOS ORDEN
    def establecer_orden(self, orden:str):
        self._orden = orden

    def obtener_orden(self) -> str:
        return self._orden

    # MÉTODOS SEGÚN
    def establecer_segun(self, segun:str):
        self._segun = segun

    def obtener_segun(self) -> str:
        return self._segun

    # MÉTODOS MODO
    def establecer_modo(self, modo:str):
        self._modo = modo

    def obtener_modo(self) -> str:
        return self._modo
    
    # MÉTODOS CAMPOS BOOLEANOS
    def establecer_campo_booleano(self, nombre_campo:str, tipo_logica:str):
        self._campos_booleanos[nombre_campo] = tipo_logica
            
    def borrar_campo_booleano(self, nombre_campo:str):
        self._campos_booleanos.pop(nombre_campo, None)
        gestor.actualizar_vista()

    def obtener_campos_booleanos(self) -> dict:
        return self._campos_booleanos

    # MÉTODOS CAMPOS DE TEXTO
    def establecer_campo_texto(self, nombre_campo:str, valores:list):
        self._campos_texto[nombre_campo] = valores
    
    def borrar_campo_texto(self, nombre_campo:str):
        self._campos_texto.pop(nombre_campo, None)
        gestor.actualizar_vista()
        
    def obtener_campos_texto(self) -> dict:
        return self._campos_texto

    # MÉTODOS CAMPOS ENTEROS
    def establecer_campo_entero(self, campo:str, rango:range):
        self._campos_enteros[campo] = rango

    def borrar_campo_entero(self, campo:str):
        self._campos_enteros.pop(campo, None)
        gestor.actualizar_vista()
        
    def obtener_campos_enteros(self) -> dict:
        return self._campos_enteros

    # MÉTODOS CAMPOS REALES
    def establecer_campo_real(self, campo:str, rango:range):
        self._campos_reales[campo] = rango

    def borrar_campo_real(self, campo:str):
        self._campos_reales.pop(campo, None)
        gestor.actualizar_vista()
        
    def obtener_campos_reales(self) -> dict:
        return self._campos_reales

    # MÉTODOS CAMPOS COMPLEJOS
    def establecer_campo_complejo(self, campo:str, rango:range):
        self._campos_complejos[campo] = rango

    def borrar_campo_complejo(self, campo:str):
        self._campos_complejos.pop(campo, None)
        gestor.actualizar_vista()
        
    def obtener_campos_complejos(self) -> dict:
        return self._campos_complejos


    # MÉTODOS GENERALES

    def campos_definidos(self) -> list:
        lista_aux:list = list(self._campos_booleanos.keys())
        lista_aux += list(self._campos_texto.keys())
        lista_aux += list(self._campos_enteros.keys())
        lista_aux += list(self._campos_reales.keys())
        lista_aux += list(self._campos_complejos.keys())
        return lista_aux
               
    def borrar_todos_los_campos(self):
        self._campos_booleanos.clear()
        self._campos_texto.clear()
        self._campos_enteros.clear()
        self._campos_reales.clear()
        self._campos_complejos.clear()
        self._segun:str = ""
        gestor.actualizar_vista()
        
    def obtener_datos(self) -> str:
        cadena_aux:str = "\n-------------------------------------------------------------------------------------\n"
        cadena_aux += "  Los futuros campos calculados no reciben valores ni se les asigna un tipo de dato\n"
        cadena_aux += "-------------------------------------------------------------------------------------\n\n"
        cadena_aux += f'🟪 RUTA: {self.obtener_ruta()}\n'
        cadena_aux += f'\n🟪 Encabezados de la tabla: {self.obtener_encabezados()}\n'
        cadena_aux += f'\n🟪 Delimitador: "{self.obtener_delimitador()}"\n'
        cadena_aux += f'\n🟪 Tipo de orden: {self.obtener_orden()}\n'
        cadena_aux += f'\n🟪 Registros ordenados según el campo: {self.obtener_segun()}\n'
        cadena_aux += f'\n🟪 Módulo de aleatoriedad: {self.obtener_modo()}\n'
        cadena_aux += f'\n🟪 Campos con valores booleanos: {self.obtener_campos_booleanos()}\n'
        cadena_aux += f'\n🟪 Campos con valores de texto: {self.obtener_campos_texto()}\n'
        cadena_aux += f'\n🟪 Campos con números enteros: {self.obtener_campos_enteros()}\n'
        cadena_aux += f'\n🟪 Campos con números reales: {self.obtener_campos_reales()}\n'
        cadena_aux += f'\n🟪 Campos con números complejos: {self.obtener_campos_complejos()}\n'
        return cadena_aux
    
    def restablecer_tabla(self):
        self._ruta_salida_csv:str = ""
        self._encabezados_tabla:list = []
        self._delimitador:str = ""
        self._orden:str = ""
        self._segun:str = ""
        self._modo:str = ""
        self._campos_booleanos.clear()
        self._campos_texto.clear()
        self._campos_enteros.clear()
        self._campos_reales.clear()
        self._campos_complejos.clear()
        gestor.actualizar_vista()
        return None


class Generador:
    pass


# Clases de submodulos
class SubmoduloEntradaTexto:   
    
    def __init__(self,
                 ubicacion,
                 texto_etiqueta:str,
                 texto_base_entrada:str="",
                 evento_enter = lambda event=None: lambda *args: None):
        # Contenedor ingreso
        self._contenedor_ingreso = tk.Frame(ubicacion,
                                            **estilo_contenedor_ingreso)
        self._contenedor_ingreso.pack(**pack_contenedor_ingreso)

        # Etiqueta
        self._eti_ingreso = tk.Label(self._contenedor_ingreso,
                                     text=texto_etiqueta,
                                     **estilo_etiqueta)
        self._eti_ingreso.config(font=FUENTE_ETIQUETA)
        self._eti_ingreso.pack(**pack_eti_ingreso)

        # Entrada
        self._valor_ingresado = tk.StringVar()
        # Almacena el valor registrado en cada instancia
        self._entrada = tk.Entry(self._contenedor_ingreso,
                                 textvariable=self._valor_ingresado)
        self._entrada.config(font=FUENTE_ENTRADA)
        self._entrada.insert(0, texto_base_entrada)
        self._entrada.pack(**pack_entrada_texto)
        self._entrada.bind("<Return>", evento_enter)

    def borrar_valor(self):
        self._entrada.delete(0, "end")

    def obtener_valor(self) -> str:
        return self._valor_ingresado.get()
    
    def establecer_valor(self, valor:str):
        self._valor_ingresado.set(valor)

    def enfocar_entrada(self):
        self._entrada.focus_set()

    def mostrar_submodulo(self):
        self._contenedor_ingreso.pack(**pack_contenedor_ingreso)
        self._eti_ingreso.pack(**pack_eti_ingreso)
        self._entrada.pack(**pack_entrada_texto)
        return None

    def ocultar_submodulo(self):
        self._contenedor_ingreso.pack_forget()
        self._eti_ingreso.pack_forget()
        self._entrada.pack_forget()
        return None

        
class SubmoduloEntradaOpciones:   
    
    def __init__(self,
                 ubicacion,
                 texto_etiqueta:str,
                 opciones_base:list=[],
                 funcion_rastrear_opciones=lambda *args: None,
                 estilo_opc=estilo_boton_opcion):
        # Contenedor ingreso
        self._contenedor_ingreso = tk.Frame(ubicacion,
                                            **estilo_contenedor_ingreso)
        self._contenedor_ingreso.pack(**pack_contenedor_ingreso)

        # Etiqueta
        self._eti_ingreso = tk.Label(self._contenedor_ingreso,
                                     text=texto_etiqueta,
                                     **estilo_etiqueta)
        self._eti_ingreso.config(font=FUENTE_ETIQUETA)
        self._eti_ingreso.pack(**pack_eti_ingreso)

        # Entrada
        self._opciones = opciones_base
        # Almacena el valor registrado en cada instancia
        self._valor_ingresado = tk.StringVar()
        self._valor_ingresado.set(self._opciones[0])
        self._entrada_opciones = tk.OptionMenu(self._contenedor_ingreso,
                                               self._valor_ingresado,
                                               *self._opciones)
        self._entrada_opciones.config(font=FUENTE_BOTON,
                                      **estilo_opc)
        self._entrada_opciones.pack(**pack_entrada_opcion)
        self._valor_ingresado.trace("w", funcion_rastrear_opciones)

    def obtener_valor(self) -> str:
        return self._valor_ingresado.get()
         
    def actualizar_opciones(self, nuevas_opciones:list):
        if nuevas_opciones:            
            menu = self._entrada_opciones["menu"]
            menu.delete(0, "end")
            for opcion in nuevas_opciones:
                menu.add_command(label=opcion,
                                 command=lambda opc=opcion: self._valor_ingresado.set(opc))
            self._valor_ingresado.set(nuevas_opciones[0])

    def reiniciar_opciones(self):
        self._valor_ingresado.set(self._opciones[0])

    def mostrar_submodulo(self):
        self._contenedor_ingreso.pack(**pack_contenedor_ingreso)
        self._eti_ingreso.pack(**pack_eti_ingreso)
        self._entrada_opciones.pack(**pack_entrada_opcion)
        return None


    def ocultar_submodulo(self):
        self._contenedor_ingreso.pack_forget()
        self._eti_ingreso.pack_forget()
        self._entrada_opciones.pack_forget()
        return None

            
# Clases de botones
class Boton:
    def __init__(self, ubicacion,
                 texto_boton:str,
                 funcion_comando,
                 estilo_boton,
                 evento_enter = lambda event=None: lambda *args: None):
        
        self._boton = tk.Button(ubicacion,
                                text=texto_boton,
                                command=funcion_comando,
                                **estilo_boton)
        self._boton.config(font=FUENTE_BOTON)
        self._boton.pack(**pack_boton)
        self._boton.bind("<Return>", evento_enter)

    def enfocar_boton(self):
        self._boton.focus_set()
        

class BotonEspecial:
    def __init__(self, ubicacion,
                 texto_boton:str,
                 funcion_comando,
                 estilo_boton,
                 fuente_boton,
                 pack_variable,
                 evento_enter = lambda event=None: lambda *args: None):  
        self._boton = tk.Button(ubicacion,
                                text=texto_boton,
                                command=funcion_comando,
                                **estilo_boton)
        self._boton.config(font=fuente_boton)
        self._boton.pack(**pack_variable)
        self._boton.bind("<Return>", evento_enter)



# DICCIONARIOS QUE DEFIENEN ESTILOS DE FUENTE
FUENTE_PRINCIPAL = tk.font.Font(family="Monospace",
                               size=9,
                               weight="bold",
                               slant="roman")
FUENTE_TITULO = tk.font.Font(family="Monospace",
                             size=7,
                             weight="bold",
                             slant="roman")
FUENTE_ETIQUETA = tk.font.Font(family="Monospace",
                               size=8,
                               weight="bold",
                               slant="roman")
FUENTE_ENTRADA = tk.font.Font(family="Monospace",
                              size=8,
                              weight="normal",
                              slant="italic")
FUENTE_BOTON = tk.font.Font(family="Monospace",
                            size=7,
                            weight="normal",
                            slant="roman")
FUENTE_BOTON_SALIR = tk.font.Font(family="Monospace",
                                  size=7,
                                  weight="normal",
                                  slant="roman")

# CONSTANTES Y TITULOS DE ETIQUETAS
TX_TITULO = "CONFIGURACIÓN DE LA TABLA"
TX_RUTA = "Ruta de salida"
TX_ENCABEZADOS = "Encabezados"
TX_OPCIONES_TABLA = "FORMATO DE TABLA"
TX_DELIMITADOR = "Delimitador"
TX_ORDEN = "Orden"
TX_SEGUN = "Según"
TX_MODO = "Aleatoriedad"
TX_VALORES_CAMPO = "OPCIONES DE CAMPO"
TX_SELECC_CAMPO = "Nombre"
TX_TIPO_CAMPO = "Tipo de campo"
TX_LOGICA = "Valores de verdad"
TX_CAMPO_BORRAR = "Vaciar campo"
TX_VALORES_TEXTO = "Variantes de texto"
TX_RANGO = "DEFINIR RANGO"
TX_R_DESDE = "Desde"
TX_R_HASTA = "Hasta"
TX_R_CONJUNTO = "Números"
TX_NUM_FILAS = "Número de filas"


# CONTIENE A TODOS LOS MODULOS
interface_usuario = InterfaceUsuario()

# CONTROLA EL COMPORTAMIENTO GENERAL DE LA APLICACIÓN
# Comunica los modulos con la tabla
gestor = Gestor()

# ALMACENA LOS DATOS INGRESADOS Y LOS MÉTODOS PARA OPERARLOS
tabla = Tabla()

# CONSTRUYE Y EXPORTA LA TABLA CON DATOS (PSEUDO)ALEATORIOS
generador = Generador()


raiz.mainloop()
##def main():
##    aplicacion = Aplicacion()
##    return 0

##if __name__ == '__main__':
##    main()




# COSAS POR HACER
#------------------
# Sumar el generador
# Chequear que no hayan cosas borradas dando vueltas
# Revisar el ciclo de la aplicacion
# Modificar el estilo


