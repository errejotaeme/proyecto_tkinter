
"""
🞑 ESTRUCTURA DEL ARCHIVO

• Bloque de importaciones

• Diccionarios con variables de texto para alternar el idioma
• Diccionarios que definen la ubicación de los objetos
• Diccionarios que defienen el aspecto visual de los objetos

• Clases:
    · InterfaceUsuario
    · ModuloVerDatos
    · ModuloRuta
    · ModuloEncabezados
    · ModuloOpcionesTabla
    · ModuloCampoBooleano
    · ModuloCampoTexto
    · ModuloCampoNumerico
    · ModuloBorrarCampo
    · ModuloExportar
    · Gestor
    · Tabla
    · Generador
    · SubmoduloEntradaTexto
    · SubmoduloEntradaOpciones
    · Boton
    · BotonEspecial

• Bloque de ejecución principal
    · Instancia y configuración de raiz
    · Diccionarios que defienen estilos de fuente
    · Instancia de InterfaceUsuario(), Gestor(), Tabla(), Generador()
    · Inicio del bucle de la aplicación



🞑 ORGANIZACIÓN GENERAL

-----------------------------------------------------------------------------------------
| gestor                                                                                |
| tabla                                                                                 |
| generador                                                                             |
| raiz                                                                                  |
|   ⊦−− interface_usuario                                                               |
|                      ⊦−−−− modulo_ajustes                                             |
|                      |                ⊦−−−−− modulo_ruta                              |
|                      |                ⊦−−−−− modulo_encabezados                       |
|                      |                ⊦−−−−− modulo_opciones_tabla                    |
|                      |                ⊦−−−−− modulo_campo_booleano                    |
|                      |                ⊦−−−−− modulo_campo_texto                       |
|                      |                ⊦−−−−− modulo_campo_numerico                    |
|                      |                ⊦−−−−− modulo_borrar_campo                      |
|                      |                ⊦−−−−− modulo_exportar                          |
|                      |                                                                |
|                      ⊦−−−− modulo_vista                                               |
|                                     ⊦−−−−− modulo_ver_datos                           |
|                                                                                       |
-----------------------------------------------------------------------------------------



🞑 DESCRIPCIÓN GENERAL

• interface_usuario: contiene a los modulos.

• modulo_ruta: recibe el ingreso de la ruta de salida.

• modulo_encabezados: recibe los distintos encabezados de la tabla.

• modulo_opciones_tabla: recibe las opciones de la tabla (delimitador, orden).

• modulo_campo_booleano: define valores booleanos.

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


import time
import csv, random, secrets
import tkinter as tk
from tkinter import filedialog, font
from pathlib import Path



# Dicionario que permite alternar el idioma
tex = dict()

# Idioma por defecto: castellano
# Contiene los valores de texto para poder cambiar el idioma
# Es auxiliar al diccionario siguiente y contiene las frases largas partidas
TEX_AUX:dict = { "_acl_1" : "Los encabezados designados como campos calculados ",
                 "_acl_2" : "no requieren valores ni asignación de tipos de datos.\n\n",
                 "_err_enc_1" : "Por favor introduzca los encabezados de ",
                 "_err_enc_2" : "su tabla separados por comas.",
                 "_err_criterio_1" : "La tabla no se pudo ordenar según el campo especificado. ",
                 "_err_criterio_2" : "Por favor, revise su elección.",
                 "_err_no_val_1" : "El campo seleccionado no recibió ningún ",
                 "_err_no_val_2" : "valor. Por favor, ingreso los datos y vuelva a intentarlo.",
                 "_err_campo_inex_1" : "Solo se puede definir valores de un campo existente. ",
                 "_err_campo_inex_2" : "Por favor revise los campos de la tabla.",
                 "_err_campo_repe_1" : "El campo elegido tiene valores definidos. ",
                 "_err_campo_repe_2" : "Para reemplazarlos, borre el campo.",
                 "_err_ruta_ingreso_1" : "El archivo no se puede abrir porque ",
                 "_err_ruta_ingreso_2" : "la ruta especificada no existe.",
                 "_err_secrets_1" : "El modulo secrets no genera números de coma flotante.\n",
                 "_err_secrets_2" : 'Si necesita campos de números con decimales, puede seleccionar "random"'}               
                                 
# Valores de texto para cambiar el idioma
TEX:dict = { "titulo_gui" : "GENERADOR DE TABLAS CON DATOS (PSEUDO)ALEATORIOS",
             "btn_salir" : "Salir",
             # Modulo vista
             "aclaracion" : TEX_AUX["_acl_1"] + TEX_AUX["_acl_2"],
             # Modulo ruta
             "ruta" : "Ruta de salida",
             "ruta_def" : "/ruta_a_archivo.csv",
             "btn_ruta" : "Elegir ubicación",
             # Modulo encabezados
             "campos_def" : "Campo_1, Campo_2, ..., Campo_n", # Se repite
             "encabezado" : "Campos de la tabla",
             "btn_encabezado" : "Borrar encabezado",
             # Modulo opciones tabla
             "delimitador" : "Delimitador",
             "orden" : "Orden",
             "criterio" : "Criterio",
             "modo" : "Aleatoriedad",
             "semilla" : "Semilla",
             "orden_opc_0" : "Ascendente",
             "orden_opc_1" : "Descendente",
             "orden_opc_2" : "Ninguno",
             "criterio_opc_base" : "Campo_n",
             "semilla_def" : "Sin semilla",
             "opc_vacio" : "Vacío", # Se repite
             # Modulo campo booleano
             "selecc_campo_bool" : "Definir como booleano",
             "logica" : "Valores",
             "campo_def_0" : "Campo_1", #
             "campo_def_1" : "Campo_2", #
             "campo_def_2" : "...",     #
             "campo_def_3" : "Campo_n", # Se repiten
             # Modulo campo texto
             "valores_texto" : "Alternativas de texto",
             "selecc_campo" : "Definir como texto",
             "valores_tex_def" : "valor_1, valor_2, ..., valor_n",
             "btn_borrar_tex" : "Borrar valores",
             # Modulo campo numerico
             "selecc_campo_num" : "Definir como numérico",
             "rango_desde" : "Desde",
             "rango_hasta" : "Hasta",
             "selecc_tipo_num" : "Tipo numérico",
             "opc_num_int" : "Enteros",  #
             "opc_num_float" : "Decimales", # Se repiten
             # Modulo campo borrar
             "campo_a_borrar" : "Campo a borrar",
             "btn_vaciar_campo" : "Eliminar datos ingresados",
             "btn_vaciar_tabla" : "Borrar todo",
             # Modulo exportar
             "num_filas" : "Número de filas",
             "btn_exportar" : "Exportar tabla",
             # Gestion ruta
             "err_ruta_invalida" : "Por favor introduzca una ruta válida",
             "err_vt_ruta_invalida" : "Error de ruta de salida",
             "ruta_archivo" : "tabla_datos_pseudoaleatorios.csv",
             # Gestion encabezados
             "err_encabezados" : TEX_AUX['_err_enc_1'] + TEX_AUX['_err_enc_2'],
             "err_vt_encabezados" : "Error: campos no ingresados",
             # Gestion opciones tabla
             "err_delimitador" : "Solo se permite un único carácter como delimitador.",
             "err_vt_delimitador" : "Error: delimitador no válido",
             "err_criterio" : TEX_AUX['_err_criterio_1'] + TEX_AUX['_err_criterio_2'],
             "err_vt_criterio" : "Error: campo de ordenación",
             # Gestion campo texto
             "err_no_valores_tex" : TEX_AUX["_err_no_val_1"] + TEX_AUX["_err_no_val_2"],
             "err_vt_no_valores_tex" : "Error: valores no ingresados",
             # Gestion condiciones basicas
             "err_campo_def" : "Por favor seleccione un campo que no haya sido definido.",
             "err_vt_campo_def" : "Error de asignación de tipo de campo",
             "err_campo_inexistente" : TEX_AUX["_err_campo_inex_1"] + TEX_AUX["_err_campo_inex_2"],
             "err_vt_campo_inex" : "Error: campo inexistente",
             "err_campo_repetido" : TEX_AUX["_err_campo_repe_1"] + TEX_AUX["_err_campo_repe_2"],
             "err_vt_campo_repe" : "Error: campo repetido",
             # Gestion campo numerico
             "err_rango_invalido" : "Por favor ingrese un rango válido",
             "err_vt_rango_invalido" : "Error: rango no válido",
             "err_rango_menor" : "El rango de inicio debe ser menor que el final",
             "err_vt_rango_menor" : "Error: rango inconsistente",
             # Gestion exportar
             "err_ruta_ingresada" : TEX_AUX["_err_ruta_ingreso_1"] + TEX_AUX["_err_ruta_ingreso_2"],
             "err_vt_ruta_ingresada" : "Error: ruta de salida",
             "err_escritura" : "No posee permisos de escritura en la ruta especificada.",
             "vt_err_escritura" : "Error: permisos de escritura",
             "err_ruta_inesperado" : "Ocurrió un error inesperado: ",
             "err_vt_ruta_inesperado" : "Error: inesperado",
             "err_secrets" : TEX_AUX["_err_secrets_1"] + TEX_AUX["_err_secrets_2"],
             "err_vt_secrets" : "Error: modo de aleatoriedad",
             "err_filas" : "Por favor ingrese un número de filas válido",
             "err_vt_filas" : "Error: número de filas no válido",
             "ok_tabla" : "¡La tabla se generó correctamente!",
             "vt_ok_tabla" : "Operación exitosa",
             # Tabla
             "ruta_clave" : " • Ruta: ",
             "encabezado_clave" : "\n • Encabezado de la tabla: ",
             "delimitador_clave" : "\n • Delimitador: ",
             "orden_clave" : "\n • Tipo de orden: ",
             "criterio_campo" : "\n • Registros ordenados según el campo: ",
             "clave_modo" : "\n • Módulo de aleatoriedad: ",
             "clave_semilla" : "\n • Semilla: ",
             "clave_bool" : "\n • Campos con valores booleanos: ",
             "clave_tex" : "\n • Campos con valores de texto: ",
             "clave_int" : "\n • Campos con números enteros: ",
             "clave_float" : "\n • Campos con números reales: "}


# Auxiliar al diccionario siguiente
# Contiene las frases largas en inglés partidas
TEX_EN_AUX:dict = { "_acl_1" : "Los encabezados designados como campos calculados ",
                    "_acl_2" : "no requieren valores ni asignación de tipos de datos.\n\n",
                    "_err_enc_1" : "Por favor introduzca los encabezados de ",
                    "_err_enc_2" : "su tabla separados por comas.",
                    "_err_criterio_1" : "La tabla no se pudo ordenar según el campo especificado. ",
                    "_err_criterio_2" : "Por favor, revise su elección.",
                    "_err_no_val_1" : "El campo seleccionado no recibió ningún ",
                    "_err_no_val_2" : "valor. Por favor, ingreso los datos y vuelva a intentarlo.",
                    "_err_campo_inex_1" : "Solo se puede definir valores de un campo existente. ",
                    "_err_campo_inex_2" : "Por favor revise los campos de la tabla.",
                    "_err_campo_repe_1" : "El campo elegido tiene valores definidos. ",
                    "_err_campo_repe_2" : "Para reemplazarlos, borre el campo.",
                    "_err_ruta_ingreso_1" : "El archivo no se puede abrir porque ",
                    "_err_ruta_ingreso_2" : "la ruta especificada no existe.",
                    "_err_secrets_1" : "El modulo secrets no genera números de coma flotante.\n",
                    "_err_secrets_2" : 'Si necesita campos de números con decimales, puede seleccionar "random"'}               
                                 
TEX_EN:dict = { "titulo_gui" : "PSEUDO-RANDOM DATA TABLE GENERATOR",
                "btn_salir" : "Exit",
                # Modulo vista
                "aclaracion" : TEX_EN_AUX["_acl_1"] + TEX_EN_AUX["_acl_2"],
                # Modulo ruta
                "ruta" : "Output path or file location",
                "ruta_def" : "/path_to_file.csv",
                "btn_ruta" : "Choose location",
                # Modulo encabezados
                "campos_def" : "Field_1, Field_2, ..., Field_n", # Se repite
                "encabezado" : "Table Fields",
                "btn_encabezado" : "Remove Header",
                # Modulo opciones tabla
                "delimitador" : "Delimiter",
                "orden" : "Sort",
                "criterio" : "Criterion",
                "modo" : "Randomness",
                "semilla" : "Seed",
                "orden_opc_0" : "Ascending",
                "orden_opc_1" : "Descending",
                "orden_opc_2" : "None",
                "criterio_opc_base" : "Field_n",
                "semilla_def" : "No seed",
                "opc_vacio" : "Empty", # Se repite
                # Modulo campo booleano
                "selecc_campo_bool" : "Set field as boolean",
                "logica" : "Values",
                "campo_def_0" : "Field_1", #
                "campo_def_1" : "Field_2", #
                "campo_def_2" : "...",     #
                "campo_def_3" : "Field_n", # Se repiten
                # Modulo campo texto
                "valores_texto" : "Text Alternatives",
                "selecc_campo" : "Set as text field",
                "valores_tex_def" : "value_1, value_2, ..., value_n",
                "btn_borrar_tex" : "Clear values",
                # Modulo campo numerico
                "selecc_campo_num" : "Set as numeric field",
                "rango_desde" : "From",
                "rango_hasta" : "To",
                "selecc_tipo_num" : "Number type",
                "opc_num_int" : "Integer",  #
                "opc_num_float" : "Float", # Se repiten
                # Modulo campo borrar
                "campo_a_borrar" : "Field to delete",
                "btn_vaciar_campo" : "Remove entered data",
                "btn_vaciar_tabla" : "Clear all",
                # Modulo exportar
                "num_filas" : "Número de filas",
                "btn_exportar" : "Exportar tabla",
                # Gestion ruta
                "err_ruta_invalida" : "Por favor introduzca una ruta válida",
                "err_vt_ruta_invalida" : "Error de ruta de salida",
                "ruta_archivo" : "tabla_datos_pseudoaleatorios.csv",
                # Gestion encabezados
                "err_encabezados" : TEX_EN_AUX['_err_enc_1'] + TEX_EN_AUX['_err_enc_2'],
                "err_vt_encabezados" : "Error: campos no ingresados",
                # Gestion opciones tabla
                "err_delimitador" : "Solo se permite un único carácter como delimitador.",
                "err_vt_delimitador" : "Error: delimitador no válido",
                "err_criterio" : TEX_EN_AUX['_err_criterio_1'] + TEX_EN_AUX['_err_criterio_2'],
                "err_vt_criterio" : "Error: campo de ordenación",
                # Gestion campo texto
                "err_no_valores_tex" : TEX_EN_AUX["_err_no_val_1"] + TEX_EN_AUX["_err_no_val_2"],
                "err_vt_no_valores_tex" : "Error: valores no ingresados",
                # Gestion condiciones basicas
                "err_campo_def" : "Por favor seleccione un campo que no haya sido definido.",
                "err_vt_campo_def" : "Error de asignación de tipo de campo",
                "err_campo_inexistente" : TEX_EN_AUX["_err_campo_inex_1"] + TEX_EN_AUX["_err_campo_inex_2"],
                "err_vt_campo_inex" : "Error: campo inexistente",
                "err_campo_repetido" : TEX_EN_AUX["_err_campo_repe_1"] + TEX_EN_AUX["_err_campo_repe_2"],
                "err_vt_campo_repe" : "Error: campo repetido",
                # Gestion campo numerico
                "err_rango_invalido" : "Por favor ingrese un rango válido",
                "err_vt_rango_invalido" : "Error: rango no válido",
                "err_rango_menor" : "El rango de inicio debe ser menor que el final",
                "err_vt_rango_menor" : "Error: rango inconsistente",
                # Gestion exportar
                "err_ruta_ingresada" : TEX_EN_AUX["_err_ruta_ingreso_1"] + TEX_EN_AUX["_err_ruta_ingreso_2"],
                "err_vt_ruta_ingresada" : "Error: ruta de salida",
                "err_escritura" : "No posee permisos de escritura en la ruta especificada.",
                "vt_err_escritura" : "Error: permisos de escritura",
                "err_ruta_inesperado" : "Ocurrió un error inesperado: ",
                "err_vt_ruta_inesperado" : "Error: inesperado",
                "err_secrets" : TEX_EN_AUX["_err_secrets_1"] + TEX_EN_AUX["_err_secrets_2"],
                "err_vt_secrets" : "Error: modo de aleatoriedad",
                "err_filas" : "Por favor ingrese un número de filas válido",
                "err_vt_filas" : "Error: número de filas no válido",
                "ok_tabla" : "¡La tabla se generó correctamente!",
                "vt_ok_tabla" : "Operación exitosa",
                # Tabla
                "ruta_clave" : " • Ruta: ",
                "encabezado_clave" : "\n • Encabezado de la tabla: ",
                "delimitador_clave" : "\n • Delimitador: ",
                "orden_clave" : "\n • Tipo de orden: ",
                "criterio_campo" : "\n • Registros ordenados según el campo: ",
                "clave_modo" : "\n • Módulo de aleatoriedad: ",
                "clave_semilla" : "\n • Semilla: ",
                "clave_bool" : "\n • Campos con valores booleanos: ",
                "clave_tex" : "\n • Campos con valores de texto: ",
                "clave_int" : "\n • Campos con números enteros: ",
                "clave_float" : "\n • Campos con números reales: "}

# Define el texto por defecto en castellano            
tex = TEX


# Diccionarios que definen la ubicación de los objetos
PACK_MARCO_MODULO:dict = {'side':'top',
                          'fill': 'x',
                          'anchor':'n',
                          'expand': True,
                          'padx': 2,
                          'pady': 2}

PACK_CONTENEDOR_INGRESO:dict = {'side':'left',
                                'anchor':'w',
                                'fill': 'x',
                                'expand': True,
                                'padx': 5,
                                'pady': 10}

PACK_CONTENEDOR_INGRESO_BOOLEANEO:dict = {'side':'left',
                                         'anchor':'w',
                                         'expand': False,
                                         'padx': 5,
                                         'pady': 10}

PACK_ETI_INGRESO:dict = {'side':'top',
                         'anchor':'n',
                         'expand': True,
                         'padx': 5,
                         'pady': 2}

PACK_ETI_INGRESO_FILA:dict = {'side':'top',
                              'anchor':'ne',
                              'padx': 25,
                              'pady': 5}

PACK_ETI_TITULO:dict = {'side':'top',
                        'anchor':'s',
                        'expand': True,
                        'padx': 5,
                        'pady': 10}

PACK_ETI_ERROR:dict = {'side':'top',
                         'anchor':'s',
                         'fill': 'x',
                         'expand': True,
                         'padx': 5,
                         'pady': 30}

PACK_ENTRADA_TEXTO:dict = {'side':'top',
                           'fill': 'x',
                           'expand': True,
                           'pady':2}

PACK_ENTRADA_TEXTO_FILA:dict = {'side':'top',
                                'anchor':'ne',
                                'expand': False,
                                'pady':2,
                                'padx':2,
                                'ipadx':10}

PACK_ENTRADA_OPCION:dict = {'side':'bottom',
                            'anchor':'s',
                            'expand': False}

PACK_CONTENEDOR_BOTON:dict = {'side':'right',
                              'fill': 'both',
                              'expand': False,
                              'padx': 5,
                              'pady': 5}

PACK_CONTENEDOR_BOTON_BORRADO:dict = {'side':'left',
                                      'fill': 'both',
                                      'expand': False,
                                      'padx': 5,
                                      'pady': 0}

PACK_BOTON:dict = {'side':'left',
                   'anchor': 's',
                   'padx': 5,
                   'pady': 5}

PACK_VACIAR_CAMPO:dict = {'side':'right',
                          'anchor': 's',
                          'padx': 5,
                          'pady': 5}

PACK_BOTON_SALIR:dict = {'side':'right',
                   'anchor': 's',
                   'padx': 5,
                   'pady': 5}

# Diccionarios que defienen aspectos visuales de los objetos
ESTILO_RAIZ = {'bg':'black'}
ESTILO_CONTENEDORES_EXTERNOS = {'bg':'purple'}
ESTILO_MARCO_MODULO = {'bg':'#a34cb4'}  # predominante
ESTILO_CONTENEDOR_INGRESO = {'bg':'#a34cb4'}
ESTILO_TEXTO_VISTA = { 'bg':'black'}

ESTILO_BOTON_OK:dict = {'bg':'#15ffbd',
                        'activebackground':'#0a8c5c',
                        'activeforeground':'#15ffbd',
                        'highlightthickness':2,
                        'borderwidth':5,
                        'height':1}

ESTILO_BOTON_OPCION:dict = {'bg':'#b915ff',
                            'activebackground':'#4d096a',
                            'activeforeground':'#b915ff',
                            'borderwidth':3,
                            'height':1,
                            'width':13}

ESTILO_BOTON_NO_OK:dict = {'bg':'#ff3a2c',
                           'activebackground':'#8c2018',
                           'activeforeground':'#ff3a2c',
                           'highlightthickness':2,
                           'borderwidth':5}

ESTILO_ALERTA:dict = {'bg':'#e36b02',
                      'activebackground':'#713501',
                      'activeforeground':'#e36b02',
                      'borderwidth':5,
                      'width':15}

ESTILO_ETIQUETA:dict = {'bg':'#000000', 'fg':'white'}
ESTILO_CONTENEDOR_BOTON:dict = {'bg':'#a34cb4'}
ESTILO_PANEL = {'bg': 'yellow'}



idioma_actual = 'ES'
def idioma(raiz,idioma:str):
    global tex
    if idioma == "EN":
        tex = TEX_EN
        print('ingles')
        raiz.destroy()
        main()    
    else:
        tex = TEX
        print('castellano')
        raiz.destroy()
        main()
        
    
    

class InterfaceUsuario:
    def __init__(self,raiz,gestor,tabla,generador):    

        self.raiz = raiz
        self.gestor = gestor
        self.tabla = tabla
        self.generador = generador

        # Marco raiz, contiene a todos loS widgets
        self.marco_raiz = tk.PanedWindow(self.raiz,
                                         orient=tk.VERTICAL,
                                         **ESTILO_PANEL)

        # Modulo Salir
        self.modulo_salir = tk.Frame(self.marco_raiz,
                                     **ESTILO_MARCO_MODULO)
        # Boton Salir
        self._boton_salir = BotonEspecial(self.modulo_salir,
                                          tex['btn_salir'],
                                          self.raiz.destroy,
                                          ESTILO_ALERTA,
                                          FUENTE_BOTON_SALIR,
                                          PACK_BOTON_SALIR,
                                          lambda event=None: self.raiz.destroy())
        # Boton idioma
        self._boton_idioma = BotonEspecial(self.modulo_salir,
                                          'ES | EN',
                                          self.cambiar_idioma,
                                          ESTILO_BOTON_OPCION,
                                          FUENTE_BOTON_SALIR,
                                          PACK_BOTON,
                                          lambda event=None: cambiar_idioma())

        # Etiqueta del modulo OpcionesTabla
        self._eti_titulo = tk.Label(self.modulo_salir,
                                    text=tex['titulo_gui'],
                                    **ESTILO_ETIQUETA)
        self._eti_titulo.configure(font=FUENTE_TITULO)
        self._eti_titulo.pack(**PACK_ETI_TITULO)

        # Contenedor de modulos Ajustes y Datos
        self.contenedor_ajustes_datos = tk.Frame(self.marco_raiz,
                                                 **ESTILO_CONTENEDORES_EXTERNOS)
        # Agrega los modulos a la ventana panelizada
        self.marco_raiz.add(self.modulo_salir)
        self.marco_raiz.add(self.contenedor_ajustes_datos)
        self.marco_raiz.pack(fill='both', expand=True)
        self.seccion_ajustes_datos = tk.PanedWindow(self.contenedor_ajustes_datos,
                                                    orient=tk.HORIZONTAL)

        # Modulo ajustes
        self.modulo_ajustes = tk.Frame(self.seccion_ajustes_datos,
                                       **ESTILO_CONTENEDORES_EXTERNOS)
        self.seccion_modulos = tk.PanedWindow(self.modulo_ajustes,
                                              orient=tk.VERTICAL,
                                              **ESTILO_PANEL)
        # Modulo Rutas
        self.modulo_ruta = ModuloRuta(self.modulo_ajustes)
        self.modulo_ruta.enfocar()

        # Modulo Encabezados
        self.modulo_encabezados = ModuloEncabezados(self.modulo_ajustes)

        # Modulo Opciones tabla
        self.modulo_opciones_tabla = ModuloOpcionesTabla(self.modulo_ajustes)

        # Modulo Campo
        self.modulo_campo_booleano = ModuloCampoBooleano(self.modulo_ajustes)

        # Modulo Campo Texto
        self.modulo_campo_texto = ModuloCampoTexto(self.modulo_ajustes)

        # Modulo Campo Numerico
        self.modulo_campo_numerico = ModuloCampoNumerico(self.modulo_ajustes)

        # Modulo Borrar campo (trabaja junto con modulo_campo_booleano)
        self.modulo_borrar_campo = ModuloBorrarCampo(self.modulo_ajustes)

        self.seccion_exportar = tk.Frame(self.modulo_ajustes, **ESTILO_PANEL)
        self.seccion_exportar.pack(side='top', padx=0, pady=0)
        # Modulo Exportar
        self.modulo_exportar = ModuloExportar(self.seccion_exportar)

        # Agrega los modulos a la ventana panelizada
        self.seccion_modulos.add(self.modulo_ruta.marco_modulo)
        self.seccion_modulos.add(self.modulo_encabezados.marco_modulo)
        self.seccion_modulos.add(self.modulo_opciones_tabla.marco_modulo)
        self.seccion_modulos.add(self.modulo_campo_booleano.marco_modulo)
        self.seccion_modulos.add(self.modulo_campo_texto.marco_modulo)
        self.seccion_modulos.add(self.modulo_campo_numerico.marco_modulo)
        self.seccion_modulos.add(self.modulo_borrar_campo.marco_modulo)

        #self.seccion_modulos.add(self.modulo_exportar.marco_modulo)
        self.seccion_modulos.add(self.seccion_exportar)
        self.seccion_modulos.pack(fill='both', expand=True)

        # Modulo Vista
        self.modulo_vista = tk.Frame(self.seccion_ajustes_datos,
                                     **ESTILO_CONTENEDORES_EXTERNOS)
        # Modulo ver datos
        self.modulo_ver_datos = ModuloVerDatos(self.modulo_vista, self.raiz)

        # Agrega los modulos a la ventana panelizada
        self.seccion_ajustes_datos.add(self.modulo_ajustes)
        self.seccion_ajustes_datos.add(self.modulo_vista)
        self.seccion_ajustes_datos.pack(fill='both', expand=True)

    def ejecutar(self):
        self.raiz.mainloop()

    def cambiar_idioma(self):
        global idioma_actual
        if idioma_actual == "ES":
            idioma_actual = "EN"
            idioma(self.raiz,"EN")            
        else:
            idioma_actual = "ES"
            idioma(self.raiz,"ES")
            
        
        



class ModuloVerDatos:

    def __init__(self,ubicacion, m_raiz):

        # Marco de todo el módulo Vista
        self.marco_modulo = tk.Frame(ubicacion, **ESTILO_MARCO_MODULO)
        self.marco_modulo.pack(side="left", fill="both", expand=True)

        # Barra de desplazamiento vertical
        self._b_vertical = tk.Scrollbar(self.marco_modulo,
                                        command=self.desplazar)
        self._b_vertical.pack(side="right", fill="y")

        # Cuadro texto donde se verán los datos ingresados
        self._contenedor_texto = tk.Text(self.marco_modulo,
                                         wrap="word",
                                         yscrollcommand=self._b_vertical.set,
                                         width=70,
                                         height=40)
        self._contenedor_texto.pack(side="left", fill="both", expand=True)
        self._contenedor_texto.configure(**ESTILO_TEXTO_VISTA)

        # Define los distintos colores del texto insertado
        self._contenedor_texto.tag_config("clave",
                                          foreground="#b53dff",
                                          font="Monospace 8 bold")
        self._contenedor_texto.tag_config("valor",
                                          foreground="#ff7700",
                                          font="Monospace 8 normal")

        # Previene que se oculte la barra de desplazamiento
        m_raiz.bind("<Configure>", self.barra_visible)

    # Muestra al usuario los datos que se van ingresando
    def insertar_datos(self, datos):
        self._contenedor_texto.configure(state='normal')
        self._contenedor_texto.delete("1.0", "end")
        self._contenedor_texto.insert("1.0", tex['aclaracion'], "clave")
        for indice, item in enumerate(datos):
            if indice%2 == 0:
                self._contenedor_texto.insert("end", item, "clave")
            else:
                self._contenedor_texto.insert("end", item, "valor")
        self._contenedor_texto.configure(state='disabled')

    def desplazar(self, *args):
        self._contenedor_texto.yview(*args)

    def barra_visible(self, event):
        # Permite que sete visible la barra aunque cambien las dimensiones
        self._contenedor_texto.pack_configure(side="left", fill="both", expand=True)


class ModuloRuta:

    def __init__(self,ubicacion):

        # Marco de todo el módulo Ruta
        self.marco_modulo = tk.Frame(ubicacion, **ESTILO_MARCO_MODULO)
        self.marco_modulo.pack(**PACK_MARCO_MODULO)

        # Submodulo entrada de la Ruta
        self._submodulo_entrada_ruta = SubmoduloEntradaTexto(
            self.marco_modulo,
            tex['ruta'],
            tex['ruta_def'],
            lambda event=None: self._confirmar_ruta()
        )
        # Contenedor boton modulo Ruta
        self._contenedor_boton_ruta = tk.Frame(self.marco_modulo,
                                               **ESTILO_CONTENEDOR_BOTON)
        self._contenedor_boton_ruta.pack(**PACK_CONTENEDOR_BOTON)

        # Boton Seleccionar Ruta
        self._boton_seleccionar_ruta = Boton(self._contenedor_boton_ruta,
                                             tex['btn_ruta'],
                                             self._seleccionar_ruta,
                                             ESTILO_BOTON_OK,
                                             lambda event=None: self._seleccionar_ruta())
        # Boton Confirmar Ruta
        self._boton_confirmar_ruta = Boton(self._contenedor_boton_ruta, "OK",
                                           self._confirmar_ruta, ESTILO_BOTON_OK,
                                           lambda event=None: self._confirmar_ruta())

    def _seleccionar_ruta(self):
        ruta_elegida = filedialog.askdirectory()
        self._submodulo_entrada_ruta.establecer_valor(ruta_elegida)
        return None

    def _confirmar_ruta(self):
        respuesta = gestor.recibir("m_ruta", self._submodulo_entrada_ruta.obtener_valor())
        if respuesta:
            interface_usuario.modulo_encabezados.enfocar()
        return None

    # Vacía el texto del widget de entrada
    def limpiar_entrada(self):
        self._submodulo_entrada_ruta.borrar_valor()

    def enfocar(self):
        self._submodulo_entrada_ruta.enfocar_entrada()



class ModuloEncabezados:

    def __init__(self,ubicacion):

        # Marco de todo el módulo Encabezados
        self.marco_modulo = tk.Frame(ubicacion, **ESTILO_MARCO_MODULO)
        self.marco_modulo.pack(**PACK_MARCO_MODULO)

        # Submodulo entrada de los Encabezados
        self._submodulo_entrada_encabezados = SubmoduloEntradaTexto(self.marco_modulo,
                                                                    tex['encabezado'],
                                                                    tex['campos_def'],
                                                                    lambda event=None: self._confirmar_encabezados())
        # Contenedor botones modulo Encabezados
        self._contenedor_botones_encabezados = tk.Frame(self.marco_modulo,
                                                        **ESTILO_CONTENEDOR_BOTON)
        self._contenedor_botones_encabezados.pack(**PACK_CONTENEDOR_BOTON)

        # Boton borrar Encabezados
        self._boton_borrar_encabezados = Boton(self._contenedor_botones_encabezados,
                                               tex['btn_encabezado'],
                                               self._borrar_encabezados_ingresados,
                                               ESTILO_BOTON_NO_OK,
                                               lambda event=None: self._borrar_encabezados_ingresados())
        # Boton confirmar Encabezados
        self._boton_confirmar_encabezados = Boton(self._contenedor_botones_encabezados,
                                                  "OK",
                                                  self._confirmar_encabezados,
                                                  ESTILO_BOTON_OK,
                                                  lambda event=None: self._confirmar_encabezados())

    def _confirmar_encabezados(self):
        respuesta = gestor.recibir("m_encabezados",
                                   self._submodulo_entrada_encabezados.obtener_valor())
        if respuesta:
            gestor.actualizar_opciones()
            interface_usuario.modulo_opciones_tabla.enfocar()
        return

    # Vacia el widget de entrada y actualiza los encabezados
    def _borrar_encabezados_ingresados(self):
        self.limpiar_entrada()
        gestor.borrar_encabezados()

    # Vacía el texto del widget de entrada
    def limpiar_entrada(self):
        self._submodulo_entrada_encabezados.borrar_valor()

    def enfocar(self):
        self._submodulo_entrada_encabezados.enfocar_entrada()



class ModuloOpcionesTabla:

    def __init__(self,ubicacion):

        # Marco de todo el módulo OpcionesTabla
        self.marco_modulo = tk.Frame(ubicacion, **ESTILO_MARCO_MODULO)
        self.marco_modulo.pack(**PACK_MARCO_MODULO)

        # Submodulo entrada del Delimitador
        self._submodulo_entrada_delimitador = SubmoduloEntradaTexto(self.marco_modulo,
                                                                    tex['delimitador'],
                                                                    ",",
                                                                    lambda event=None: self._confirmar_opciones())
        # Submodulo opciones Orden
        self._opc_orden_base = [tex['orden_opc_0'], tex['orden_opc_1'], tex['orden_opc_2']]
        self._submodulo_opcion_orden = SubmoduloEntradaOpciones(self.marco_modulo,
                                                                tex['orden'],
                                                                self._opc_orden_base)
        # Submodulo opciones criterio
        self._opc_criterio_base = [tex['criterio_opc_base']]
        self._submodulo_opcion_criterio = SubmoduloEntradaOpciones(self.marco_modulo,
                                                                tex['criterio'],
                                                                self._opc_criterio_base)
        # Submodulo opciones Modo
        self._opc_modo_base = ["random", "secrets"]
        self._submodulo_opcion_modo = SubmoduloEntradaOpciones(self.marco_modulo,
                                                               tex['modo'],
                                                               self._opc_modo_base,
                                                               self._rastrear_opcion_aleatoriedad)
        # Submodulo entrada semilla
        self._submodulo_entrada_semilla = SubmoduloEntradaTexto(self.marco_modulo,
                                                                    tex['semilla'],
                                                                    tex['semilla_def'],
                                                                    lambda event=None: self._confirmar_opciones())
        # Contenedor boton modulo OpcionesTabla
        self._contenedor_boton_opciones_tabla = tk.Frame(self.marco_modulo,
                                                         **ESTILO_CONTENEDOR_BOTON)
        self._contenedor_boton_opciones_tabla.pack(**PACK_CONTENEDOR_BOTON)

        # Boton confirmar OpcionesTabla
        self._boton_confirmar_opciones = Boton(self._contenedor_boton_opciones_tabla,
                                               "OK",
                                               self._confirmar_opciones,
                                               ESTILO_BOTON_OK,
                                               lambda event=None: self._confirmar_opciones())


    def _rastrear_opcion_aleatoriedad(self, *args):
        modo = self._submodulo_opcion_modo.obtener_valor()
        if modo == "random":
            self._submodulo_entrada_semilla.mostrar_submodulo()
            interface_usuario.modulo_campo_numerico.actualizar_opciones_numero(
                [tex['opc_num_int'], tex['opc_num_float']]
            )
        else:
            self._submodulo_entrada_semilla.ocultar_submodulo()
            self._submodulo_entrada_semilla.establecer_valor(tex['semilla_def'])
            interface_usuario.modulo_campo_numerico.actualizar_opciones_numero([tex['opc_num_int']])
        return None

    def _confirmar_opciones(self):
        aux_opc:list = []
        aux_opc.append(self._submodulo_entrada_delimitador.obtener_valor())
        aux_opc.append(self._submodulo_opcion_orden.obtener_valor())
        aux_opc.append(self._submodulo_opcion_criterio.obtener_valor())
        aux_opc.append(self._submodulo_opcion_modo.obtener_valor())
        aux_opc.append(self._submodulo_entrada_semilla.obtener_valor())
        respuesta = gestor.recibir("m_opciones_tabla", aux_opc)
        if respuesta:
            interface_usuario.modulo_campo_booleano.enfocar()
        return

    # Vacía el texto del widget de entrada
    def limpiar_entrada(self):
        self._submodulo_entrada_delimitador.borrar_valor()

    def enfocar(self):
        self._submodulo_entrada_delimitador.enfocar_entrada()

    # Actualiza las opciones de campos con los encabezados existentes
    def actualizar_opciones_criterio(self, *args):
        nuevos_campos:list = gestor.ver_encabezados()
        if len(nuevos_campos) == 0:
            nuevos_campos = [tex['opc_vacio']]
        self._submodulo_opcion_criterio.actualizar_opciones(nuevos_campos)
        return None



class ModuloCampoBooleano:

    def __init__(self, ubicacion):

        # Marco de todo el módulo Campos
        self.marco_modulo = tk.Frame(ubicacion, **ESTILO_MARCO_MODULO)
        self.marco_modulo.pack(**PACK_MARCO_MODULO)
        
        # Contenedor opciones fijas Campo
        self._contenedor_opciones_campo = tk.Frame(self.marco_modulo, **ESTILO_MARCO_MODULO)
        self._contenedor_opciones_campo.pack(**PACK_MARCO_MODULO)
        
        # Submodulo elegir Campo
        self._opc_elegir_campo_base = [tex['campo_def_0'],
                                       tex['campo_def_1'],
                                       tex['campo_def_2'],
                                       tex['campo_def_3']]
        
        self._submodulo_elegir_campo = SubmoduloEntradaOpciones(self._contenedor_opciones_campo,
                                                                tex['selecc_campo_bool'],
                                                                self._opc_elegir_campo_base,
                                                                lambda *args: None,
                                                                ESTILO_BOTON_OPCION,
                                                                PACK_CONTENEDOR_INGRESO_BOOLEANEO)
        # Submodulo elegir Logica
        self._opc_logica_base = ["True, False", "True, False, None"]
        self._submodulo_elegir_logica = SubmoduloEntradaOpciones(self._contenedor_opciones_campo,
                                                                 tex['logica'],
                                                                 self._opc_logica_base,
                                                                 lambda *args: None,
                                                                 ESTILO_BOTON_OPCION,
                                                                 PACK_CONTENEDOR_INGRESO_BOOLEANEO)
        # Contenedor del boton confirmar Campo booleano
        self._contenedor_boton_definir_campo_booleano = tk.Frame(self._contenedor_opciones_campo,
                                                                 **ESTILO_CONTENEDOR_BOTON)
        self._contenedor_boton_definir_campo_booleano.pack(**PACK_CONTENEDOR_BOTON)
        # Boton confirmar Campo booleano
        self._boton_confirmar_campo_booleano = Boton(self._contenedor_boton_definir_campo_booleano,
                                                     "OK",
                                                     self._confirmar_campo_booleano,
                                                     ESTILO_BOTON_OK,
                                                     lambda event=None: self._confirmar_campo_booleano())

    def _confirmar_campo_booleano(self):
        mensaje:list = []
        mensaje.append(self._submodulo_elegir_campo.obtener_valor())
        mensaje.append(self._submodulo_elegir_logica.obtener_valor())
        respuesta = gestor.recibir("m_campo_booleano", mensaje)
        if respuesta:
            gestor.actualizar_opciones()
            interface_usuario.modulo_exportar.enfocar()
        return None

    def enfocar(self):
        self._boton_confirmar_campo_booleano.enfocar_boton()

    # Actualiza las opciones de campos con los encabezados existentes
    def actualizar_opciones_campo(self):
        nuevos_campos:list = gestor.ver_campos_sin_definir()
        if len(nuevos_campos) == 0:
            nuevos_campos = [tex['opc_vacio']]
        self._submodulo_elegir_campo.actualizar_opciones(nuevos_campos)
        return



class ModuloCampoTexto:

    def __init__(self,ubicacion):

        # Marco de todo el módulo CampoTexto
        self.marco_modulo = tk.Frame(ubicacion,
                                     **ESTILO_MARCO_MODULO)
        self.marco_modulo.pack(**PACK_MARCO_MODULO)

        # Submodulo elegir Campo
        self._opc_elegir_campo_base = [tex['campo_def_0'],
                                       tex['campo_def_1'],
                                       tex['campo_def_2'],
                                       tex['campo_def_3']]
        self._submodulo_elegir_campo = SubmoduloEntradaOpciones(
            self.marco_modulo,
            tex['selecc_campo'],
            self._opc_elegir_campo_base
        )

        # Submodulo entrada de valores CampoTexto
        self._submodulo_entrada_valores_texto = SubmoduloEntradaTexto(
            self.marco_modulo,
            tex['valores_texto'],
            tex['valores_tex_def'],
            lambda event=None: self._confirmar_campo_texto()
        )

        # Contenedor boton modulo CampoTexto
        self._contenedor_boton_texto = tk.Frame(self.marco_modulo,
                                                **ESTILO_CONTENEDOR_BOTON)
        self._contenedor_boton_texto.pack(**PACK_CONTENEDOR_BOTON)

        # Boton borrar valores ingresados
        self._boton_borrar_valores_texto = Boton(
            self._contenedor_boton_texto,
            tex['btn_borrar_tex'],
            self.limpiar_entrada,
            ESTILO_BOTON_NO_OK,
            lambda event=None: self.limpiar_entrada()
        )

        # Boton Confirmar valores texto
        self._boton_confirmar_texto = Boton(
            self._contenedor_boton_texto, "OK",
            self._confirmar_campo_texto,
            ESTILO_BOTON_OK,
            lambda event=None: self._confirmar_campo_texto()
        )

    # Actualiza las opciones de campos con los encabezados existentes
    def actualizar_opciones_campo(self, *args):
        nuevos_campos:list = gestor.ver_campos_sin_definir()
        if len(nuevos_campos) == 0:
            nuevos_campos = [tex['opc_vacio']]
        self._submodulo_elegir_campo.actualizar_opciones(nuevos_campos)
        return

    def _confirmar_campo_texto(self):
        mensaje:list = []
        mensaje.append(self._submodulo_elegir_campo.obtener_valor())
        mensaje.append(self._submodulo_entrada_valores_texto.obtener_valor())
        respuesta = gestor.recibir("m_campo_texto", mensaje)
        if respuesta:
            gestor.actualizar_opciones()
            interface_usuario.modulo_exportar.enfocar()
        return

    # Vacía el texto del widget de entrada
    def limpiar_entrada(self):
        self._submodulo_entrada_valores_texto.borrar_valor()

    def enfocar(self):
        self._submodulo_entrada_valores_texto.enfocar_entrada()



class ModuloCampoNumerico:

    def __init__(self,ubicacion):

        # Marco de todo el módulo Campo numerico
        self.marco_modulo = tk.Frame(ubicacion,
                                      **ESTILO_MARCO_MODULO)
        self.marco_modulo.pack(**PACK_MARCO_MODULO)

        # Submodulo elegir Campo
        self._opc_elegir_campo_base = [tex['campo_def_0'],
                                       tex['campo_def_1'],
                                       tex['campo_def_2'],
                                       tex['campo_def_3']]
        
        self._submodulo_elegir_campo = SubmoduloEntradaOpciones(self.marco_modulo,
                                                                tex['selecc_campo_num'],
                                                                self._opc_elegir_campo_base)
        # Submodulo entrada rango incio
        self._submodulo_entrada_rango_inicio = SubmoduloEntradaTexto(self.marco_modulo,
                                                                     tex['rango_desde'],
                                                                     "0",
                                                                     lambda event=None: self._confirmar_rango())
        # Submodulo entrada rango fin
        self._submodulo_entrada_rango_fin = SubmoduloEntradaTexto(self.marco_modulo,
                                                                  tex['rango_hasta'],
                                                                  "100",
                                                                  lambda event=None: self._confirmar_rango())
        # Submodulo opciones tipo numerico
        self._opc_tipo_base = [tex['opc_num_int'], tex['opc_num_float']]
        self._submodulo_opcion_tipo = SubmoduloEntradaOpciones(self.marco_modulo,
                                                               tex['selecc_tipo_num'],
                                                               self._opc_tipo_base)
        # Contenedor boton modulo Campo numerico
        self._contenedor_boton_campo_numerico = tk.Frame(self.marco_modulo,
                                                         **ESTILO_CONTENEDOR_BOTON)
        self._contenedor_boton_campo_numerico.pack(**PACK_CONTENEDOR_BOTON)
        # Boton confirmar rango
        self._boton_confirmar_rango = Boton(self._contenedor_boton_campo_numerico,
                                            "OK",
                                            self._confirmar_rango,
                                            ESTILO_BOTON_OK,
                                            lambda event=None: self._confirmar_rango())

    # Actualiza las opciones de campos con los encabezados existentes
    def actualizar_opciones_campo(self, *args):
        nuevos_campos:list = gestor.ver_campos_sin_definir()
        if len(nuevos_campos) == 0:
            nuevos_campos = [tex['opc_vacio']]
        self._submodulo_elegir_campo.actualizar_opciones(nuevos_campos)
        return
    
    # Actualiza las opciones de tipo numerico segun el modo de aleatoriedad
    def actualizar_opciones_numero(self, opciones):
        self._submodulo_opcion_tipo.actualizar_opciones(opciones)
        return None

    def _confirmar_rango(self):
        mensaje:list = []
        mensaje.append(self._submodulo_elegir_campo.obtener_valor())
        mensaje.append(self._submodulo_entrada_rango_inicio.obtener_valor())
        mensaje.append(self._submodulo_entrada_rango_fin.obtener_valor())
        mensaje.append(self._submodulo_opcion_tipo.obtener_valor())
        respuesta = gestor.recibir("m_campo_numerico", mensaje)
        if respuesta:
            gestor.actualizar_opciones()
            interface_usuario.modulo_exportar.enfocar()
        return

    # Vacía el texto los widgets de entrada
    def limpiar_entrada(self):
        self._submodulo_entrada_rango_inicio.borrar_valor()
        self._submodulo_entrada_rango_fin.borrar_valor()

    def enfocar(self):
        self._submodulo_entrada_rango_inicio.enfocar_entrada()



class ModuloBorrarCampo:
    # Permite borrar los campos definidos y restablecer la tabla

    def __init__(self,ubicacion):

        self._campo_a_eliminar:str = ""

        # Marco de todo el módulo Borrar campos
        self.marco_modulo = tk.Frame(ubicacion,
                                      **ESTILO_MARCO_MODULO)
        self.marco_modulo.pack(**PACK_MARCO_MODULO)

        # Submodulo borrar campo
        self._opc_campos = [tex['campo_def_0'],
                            tex['campo_def_1'],
                            tex['campo_def_2'],
                            tex['campo_def_3']]
        self._submodulo_borrar_campo = SubmoduloEntradaOpciones(
            self.marco_modulo,
            tex['campo_a_borrar'],
            self._opc_campos,
            self._campo_borrable,
            ESTILO_ALERTA
        )

        # Contenedor boton restablecer
        self._contenedor_boton_restablecer = tk.Frame(
            self.marco_modulo,
            **ESTILO_CONTENEDOR_BOTON
        )
        self._contenedor_boton_restablecer.pack(**PACK_CONTENEDOR_BOTON)

        # Boton restablecer la tabla
        self._boton_reestablecer_tabla = Boton(
            self._contenedor_boton_restablecer,
            tex['btn_vaciar_tabla'],
            self._restablecer_todo,
            ESTILO_BOTON_NO_OK,
            lambda event=None: self._restablecer_todo()
        )

        # Contenedor boton para vaciar datos de campo
        self._contenedor_boton_borrar_campo = tk.Frame(
            self.marco_modulo,
            **ESTILO_CONTENEDOR_BOTON
        )
        self._contenedor_boton_borrar_campo.pack(
            **PACK_CONTENEDOR_BOTON
        )

        # Boton vaciar datos de campo
        self._boton_borrar_campo = Boton(
            self._contenedor_boton_borrar_campo,
            tex['btn_vaciar_campo'],
            self._eliminar_valores,
            ESTILO_BOTON_NO_OK,
            lambda event=None: self._eliminar_valores()
        )


    def _eliminar_valores(self):
        gestor.borrar_campo(self._campo_a_eliminar)
        gestor.actualizar_opciones()
        return None


    # Restablece los valores de Tabla
    def _restablecer_todo(self):
        gestor.vaciar_tabla()
        gestor.restablecer_aplicacion()
        return None

    def _campo_borrable(self, *args):
        self._campo_a_eliminar = self._submodulo_borrar_campo.obtener_valor()
        return None

    def actualizar_opciones_borrado(self, *args):
        nuevos_campos:list = gestor.ver_campos_definidos()
        if len(nuevos_campos) == 0:
            nuevos_campos = [tex['opc_vacio']]
        self._submodulo_borrar_campo.actualizar_opciones(nuevos_campos)
        return None

        


class ModuloExportar:

    def __init__(self,ubicacion):

        # Marco de todo el módulo Encabezados
        self.marco_modulo = tk.Frame(ubicacion,
                                     **ESTILO_MARCO_MODULO)
        self.marco_modulo.pack(**PACK_MARCO_MODULO)

        # Submodulo entrada numero de filas
        self._submodulo_entrada_num_filas = SubmoduloEntradaTexto(
            self.marco_modulo,
            tex['num_filas'], "100",
            lambda event=None: self._exportar(),
            PACK_ENTRADA_TEXTO_FILA,
            PACK_ETI_INGRESO_FILA
        )

        # Contenedor botones modulo Exportar
        self._contenedor_botones_exportar = tk.Frame(self.marco_modulo,
                                                     **ESTILO_CONTENEDOR_BOTON)
        self._contenedor_botones_exportar.pack(**PACK_CONTENEDOR_BOTON)

        # Boton confirmar Exportar
        self._boton_exportar = Boton(
            self._contenedor_botones_exportar,
            tex['btn_exportar'],
            self._exportar,
            ESTILO_BOTON_OK,
            lambda event=None: self._exportar()
        )

    def _exportar(self):
        respuesta = gestor.recibir(
            "m_exportar",
            self._submodulo_entrada_num_filas.obtener_valor()
        )
        if respuesta:
            interface_usuario.modulo_ruta.enfocar()
        return None

    # Vacía el texto del widget de entrada
    def limpiar_entrada(self):
        self._submodulo_entrada_num_filas.borrar_valor()
        return None

    def enfocar(self):
        self._submodulo_entrada_num_filas.enfocar_entrada()
        return None




class Gestor:
# Gestiona la comunicación entre los módulos

    def __init__(self):
        pass

    # Enruta los mensajes recibidos
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
        
        if gestion:
            self.actualizar_vista()

        return gestion

    # Actualiza la vista de los datos ingresados
    def actualizar_vista(self):
        interface_usuario.modulo_ver_datos.insertar_datos(tabla.obtener_datos())
        return None

    # Devuelve los encabezados registrados en la tabla
    def ver_encabezados(self) -> list:
        return tabla.obtener_encabezados()

    # Vuelve a cero la lista de encabezados
    # y las opciones que los utilizan
    def borrar_encabezados(self):
        tabla.borrar_encabezados()
        tabla.borrar_todos_los_campos()
        self.actualizar_opciones()
        gestor.actualizar_vista()

    def actualizar_opciones(self):
        interface_usuario.modulo_opciones_tabla.actualizar_opciones_criterio()
        interface_usuario.modulo_campo_booleano.actualizar_opciones_campo()
        interface_usuario.modulo_campo_texto.actualizar_opciones_campo()
        interface_usuario.modulo_campo_numerico.actualizar_opciones_campo()
        interface_usuario.modulo_borrar_campo.actualizar_opciones_borrado()
        return None


    # Devuelve los campos definidos en la tabla
    def ver_campos_definidos(self) -> str:
        return tabla.campos_definidos()

    def ver_campos_sin_definir(self) -> list:
        a = set(self.ver_encabezados())
        b = set(self.ver_campos_definidos())
        return list(a - b)

    def restablecer_aplicacion(self):
        # Limpia las entradas
        interface_usuario.modulo_ruta.limpiar_entrada()
        interface_usuario.modulo_encabezados.limpiar_entrada()
        interface_usuario.modulo_campo_texto.limpiar_entrada()
        interface_usuario.modulo_campo_numerico.limpiar_entrada()
        interface_usuario.modulo_opciones_tabla.limpiar_entrada()
        self.actualizar_opciones()
        # Establece el foco en el cuadro de entrada de la ruta de salida
        interface_usuario.modulo_ruta.enfocar()
        return None

    # Devuelve todos los datos de la tabla
    def ver_datos_tabla(self) -> str:
        return tabla.obtener_datos()

    # Vacia todos los datos ingresados a la tabla
    def vaciar_tabla(self):
        tabla.restablecer_tabla()


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
        return None

    # Gestion mensajes de módulo Ruta
    def _gestion_modulo_ruta(self, mensaje:str) -> bool:
        res:bool = False
        if self._es_ruta_valida(mensaje):
            res = True
        else:
            self._mostrar_error(tex['err_ruta_invalida'],
                                tex['err_vt_ruta_invalida'])
        return res

    # Valida la ruta ingresada y actuliza el dato en Tabla
    def _es_ruta_valida(self, ruta) -> bool:
        res:bool = False
        ruta_final = Path(ruta)
        if ruta.endswith(".csv") and ruta_final.parent.is_dir():
            res = True
        elif ruta_final.is_dir():
            ruta_final = ruta_final / tex['ruta_archivo'] 
            res = True
        if res:
            tabla.establecer_ruta(ruta_final)
        return res

    # Gestion mensajes de módulo Encabezados
    def _gestion_modulo_encabezados(self, mensaje:str) -> bool:
        res:bool = False
        lista_encabezados:list = []
        if len(mensaje) < 1:
            self._mostrar_error(tex['err_encabezados'], tex['err_vt_encabezados'])
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

        # Actualiza las opciones de campos
        interface_usuario.modulo_campo_booleano.actualizar_opciones_campo()
        interface_usuario.modulo_campo_texto.actualizar_opciones_campo()
        interface_usuario.modulo_campo_numerico.actualizar_opciones_campo()
        interface_usuario.modulo_borrar_campo.actualizar_opciones_borrado()
        return res

    def _limpiar_lista(self, cadena:str) -> list:
        lista_salida:list = cadena.split(',')
        lista_salida = [item.strip() for item in lista_salida]
        lista_salida = [item for item in lista_salida if item != " "]
        lista_aux:list = []
        [lista_aux.append(e) for e in lista_salida if e not in lista_aux]
        lista_salida = lista_aux
        return lista_salida

    # Gestion mensajes de módulo Opciones tabla
    def _gestion_modulo_opciones_tabla(self, mensaje:list) -> bool:
        res:bool = False
        delimitador = mensaje[0]
        orden = mensaje[1]
        criterio_campo = mensaje[2]
        modo = mensaje[3]
        semilla = mensaje[4]
        if modo == "secrets":
            tabla.borrar_campos_reales()
        if len(delimitador) != 1:
            self._mostrar_error(tex['err_delimitador'], tex['err_vt_delimitador'])
        elif (not criterio_campo in tabla.obtener_encabezados() and
              orden != tex['orden_opc_2']):
            self._mostrar_error(tex['err_criterio'], tex['err_vt_criterio'])
        else:
            tabla.establecer_delimitador(delimitador)
            tabla.establecer_orden(orden)
            tabla.establecer_criterio(criterio_campo)
            tabla.establecer_modo(modo)
            if semilla == "":
                tabla.establecer_semilla(tex['semilla_def'])
            else:
                tabla.establecer_semilla(semilla)
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
                self._mostrar_error(tex['err_no_valores_tex'],
                                    tex['err_vt_no_valores_tex'])
        return res

    def _condiciones_basicas(self, nombre_campo:str) -> bool:
        res:bool = False
        campos_definidos:list = tabla.campos_definidos()
        if nombre_campo == "":
            self._mostrar_error(tex['err_campo_def'] , tex['err_vt_campo_def'])
        elif nombre_campo not in tabla.obtener_encabezados():
            self._mostrar_error(tex['err_campo_inexistente'], tex['err_vt_campo_inex'])
        elif nombre_campo in campos_definidos:
            self._mostrar_error(tex['err_campo_repetido'], tex['err_vt_campo_repe'])
        else:
            res = True
        return res

    def _gestion_modulo_campo_numerico(self, mensaje):
        res:bool = False
        nombre_campo:str = mensaje[0]
        rango_inicio:str = mensaje[1].strip()
        rango_fin:str = mensaje[2].strip()
        tipo_numerico:str = mensaje[3]
        condiciones_ok:bool = self._condiciones_basicas(nombre_campo)
        if rango_inicio == '' or rango_fin == '':
            self._mostrar_error(tex['err_rango_invalido'], tex['err_vt_rango_invalido'])
            return res
        if condiciones_ok:
            rango_inicio:int = self._preservar_signo(rango_inicio)
            rango_fin:int = self._preservar_signo(rango_fin)
            if type(rango_inicio) is int and type(rango_fin) is int:
                if rango_inicio > rango_fin:
                    self._mostrar_error(tex['err_rango_menor'], tex['err_vt_rango_menor'])
                elif rango_inicio < rango_fin:
                    rango:tuple = (rango_inicio, rango_fin)
                    if tipo_numerico == tex['opc_num_int']: # Entero
                        tabla.establecer_campo_entero(nombre_campo, rango)
                        res = True
                    elif tipo_numerico == tex['opc_num_float']: # Flotante
                        tabla.establecer_campo_real(nombre_campo, rango)
                        res = True
                elif rango_inicio == rango_fin:
                    self._mostrar_error(tex['err_rango_invalido'], tex['err_vt_rango_invalido'])         
            else:
                self._mostrar_error(tex['err_rango_invalido'], tex['err_vt_rango_invalido'])
        return res

    # Preseva el signo de los numeros negativos
    def _preservar_signo(self, numero:str):
        res:int = 0
        if ((not numero.isdigit() and
             numero[0] == '-' and
             numero[1:].isdigit()) or
             numero.isdigit()):
            res = int(numero)
        else:
            res = numero
        return res

    # Envia los datos al generador para que produzca la tabla
    def _gestion_modulo_exportar(self, mensaje):
        res:bool = False
        try:
            # Verifica la validez de la ruta y los permisos de escritura
            with open(tabla.obtener_ruta(), "w", newline="", encoding="utf-8"):
                pass # Sigue si todo ok
        except FileNotFoundError:
            self._mostrar_error(tex['err_ruta_ingresada'], tex['err_vt_ruta_ingresada'])
            return res
        except PermissionError:
            self._mostrar_error(tex['err_escritura'], tex['vt_err_escritura'])
            return res
        except Exception as e:
            self._mostrar_error(f'{tex["err_ruta_inesperado"]} {e}', tex['err_vt_ruta_inesperado'])
            return res

        # Chequea que no haya inconsistencias en las opciones
        if tabla.obtener_orden() != tex['orden_opc_2']:
            if tabla.obtener_criterio() not in tabla.campos_definidos():
                self._mostrar_error(tex['err_criterio'], tex['err_vt_criterio'])
                return res
        # Previene que se intente generar decimales con secrets
        if tabla.obtener_modo() == "secrets":
            if tabla.obtener_campos_reales():
                self._mostrar_error(tex['err_secrets'], tex['err_vt_secrets'])
                return res
        # Envia los datos al generador
        num_filas:int = mensaje
        if num_filas.isdigit():
            d_aux = vars(tabla)
            d_aux["_filas"] = int(num_filas)
            res = generador.crear_tabla(d_aux)
        else:
            self._mostrar_error(tex['err_filas'], tex['err_vt_filas'])
        # Respuesta de tabla generada ok    
        if res:
            self._mostrar_error(
                tex['ok_tabla'],
                tex['vt_ok_tabla'],
                ESTILO_BOTON_OK,"OK"
            )
        else:
            self._mostrar_error(tex['err_ruta_inesperado'], tex['err_vt_ruta_inesperado'])
        return res


    # Genera la ventana que muestra el aviso de error
    def _mostrar_error(self,
                       mensaje_error,
                       titulo_ventana,
                       estilo_boton=ESTILO_BOTON_NO_OK,
                       texto_boton="Cerrar"):
        
        self._ventana_error = tk.Toplevel(raiz, **ESTILO_RAIZ)
        self._ventana_error.title(titulo_ventana)
        self._ventana_error.minsize(600,100)
        
        self._etiqueta_mensaje = tk.Label(self._ventana_error,
                                  text=mensaje_error,
                                  **ESTILO_ETIQUETA)
        
        self._etiqueta_mensaje.config(font=FUENTE_ETIQUETA)
        self._etiqueta_mensaje.pack(**PACK_ETI_ERROR)

        self._boton_cerrar = tk.Button(self._ventana_error,
                                       text=texto_boton,
                                       command=self._ventana_error.destroy,
                                       **estilo_boton)
        
        self._boton_cerrar.pack(side='top', pady=20)
        self._boton_cerrar.focus_set()
        # Llama a establecer_opciones cada vez que el usuario
        # presione enter dentro del delimitador
        self._boton_cerrar.bind(
            "<Return>",
            lambda event=None: self._ventana_error.destroy()
        )


#Almacen de datos
class Tabla:

    def __init__(self):
        self._ruta_salida_csv:str = ""
        self._encabezados_tabla:list = []
        self._delimitador:str = ""
        self._orden:str = ""
        self._criterio:str = ""
        self._modo:str = ""
        self._semilla:str = ""
        self._campos_booleanos:dict = dict()
        self._campos_texto:dict = dict()
        self._campos_enteros:dict = dict()
        self._campos_reales:dict = dict()

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

    # MÉTODOS CRITERIO
    def establecer_criterio(self, criterio:str):
        self._criterio = criterio

    def obtener_criterio(self) -> str:
        return self._criterio

    # MÉTODOS MODO
    def establecer_modo(self, modo:str):
        self._modo = modo

    def obtener_modo(self) -> str:
        return self._modo

    # MÉTODOS SEMILLA
    def establecer_semilla(self, semilla:str):
        self._semilla = semilla

    def obtener_semilla(self) -> str:
        return self._semilla

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

    def borrar_campos_reales(self):
        self._campos_reales.clear()
        return None

    def obtener_campos_reales(self) -> dict:
        return self._campos_reales


    # MÉTODOS GENERALES
    def campos_definidos(self) -> list:
        lista_aux:list = list(self._campos_booleanos.keys())
        lista_aux += list(self._campos_texto.keys())
        lista_aux += list(self._campos_enteros.keys())
        lista_aux += list(self._campos_reales.keys())
        return lista_aux

    def borrar_todos_los_campos(self):
        self._campos_booleanos.clear()
        self._campos_texto.clear()
        self._campos_enteros.clear()
        self._campos_reales.clear()
        self._criterio:str = ""
        gestor.actualizar_vista()

    def obtener_datos(self) -> list:
        l_aux:list = []
        l_aux.append(tex['ruta_clave'])
        l_aux.append(f'{self.obtener_ruta()}\n')
        l_aux.append(tex['encabezado_clave'])
        l_aux.append(f'{self.obtener_encabezados()}\n')
        l_aux.append(tex['delimitador_clave'])
        l_aux.append(f'"{self.obtener_delimitador()}"\n')
        l_aux.append(tex['orden_clave'])
        l_aux.append(f'{self.obtener_orden()}\n')
        l_aux.append(tex['criterio_campo'])
        l_aux.append(f'{self.obtener_criterio()}\n')
        l_aux.append(tex['clave_modo'])
        l_aux.append(f'{self.obtener_modo()}\n')
        l_aux.append(tex['clave_semilla'])
        l_aux.append(f'"{self.obtener_semilla()}"\n')
        l_aux.append(tex['clave_bool'])
        l_aux.append(f'{self.obtener_campos_booleanos()}\n')
        l_aux.append(tex['clave_tex'])
        l_aux.append(f'{self.obtener_campos_texto()}\n')
        l_aux.append(tex['clave_int'])
        l_aux.append(f'{self.obtener_campos_enteros()}\n')
        l_aux.append(tex['clave_float'])
        l_aux.append(f'{self.obtener_campos_reales()}\n')
        return l_aux

    def restablecer_tabla(self):
        self._ruta_salida_csv = ""
        self._encabezados_tabla = []
        self._delimitador = ""
        self._orden = ""
        self._criterio = ""
        self._modo = ""
        self._semilla = ""
        self._campos_booleanos.clear()
        self._campos_texto.clear()
        self._campos_enteros.clear()
        self._campos_reales.clear()
        gestor.actualizar_vista()
        return None


class Generador:
    
    _ruta_salida_csv:str = ""
    _encabezados_tabla = []
    _delimitador:str = ""
    _orden:str = ""
    _criterio:str = ""
    _modo:str = ""
    _semilla:str = ""
    _campos_booleanos:dict = dict()
    _campos_texto:dict = dict()
    _campos_enteros:dict = dict()
    _campos_reales:dict = dict()
    _filas:int= 0

    def crear_tabla(self, datos:dict) -> bool:
        res:bool = False
        registros:list = []
        # Asigna valores automáticamente a las variables de clase
        for clave, valor in datos.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)
        # Utiliza la libreria indicada para producir los datos        
        if self._modo == "random":
            registros = self._registros_random()
        elif self._modo == "secrets":
            registros = self._registros_secrets()
        res = self._grabar_datos(registros)
        return res

    def _registros_random(self) -> list:
        # Estado inicial para generar datos pseudoaleatorios
        if self._semilla == tex['semilla_def']:
            random.seed()
        else:
            random.seed(self._semilla)           
        # Crea los registros
        filas:int = self._filas
        booleanos = [True,False,"None"]
        registros_transpuestos:list = []
        for campo in self._encabezados_tabla:
            columna:list = []
            # Booleanos
            if campo in self._campos_booleanos:
                if self._campos_booleanos[campo] == "True, False":
                    for _ in range(filas):
                        columna.append(booleanos[random.randint(0, 1)])
                    registros_transpuestos.append(columna)
                else:
                    for _ in range(filas):
                        columna.append(booleanos[random.randint(0, 2)])
                    registros_transpuestos.append(columna)
            # Texto
            elif campo in self._campos_texto:
                variantes_de_texto:list = self._campos_texto[campo]
                n_items = len(variantes_de_texto)
                for _ in range(filas):
                    columna.append(
                        variantes_de_texto[random.randint(0, n_items - 1)]
                    )
                registros_transpuestos.append(columna)
            # Enteros
            elif campo in self._campos_enteros:
                rango = self._campos_enteros[campo]
                for _ in range(filas):
                    columna.append(random.randint(rango[0], rango[1]))
                registros_transpuestos.append(columna)
            # Reales
            elif campo in self._campos_reales:
                rango = self._campos_reales[campo]
                for _ in range(filas):
                    columna.append(random.uniform(rango[0], rango[1]))
                registros_transpuestos.append(columna)
            # Campos sin definir    
            else:
                for _ in range(filas):
                    columna.append("")
                registros_transpuestos.append(columna)
        # Transpone la lista de lista para que coincida con el formato de tabla        
        registros = list(zip(*registros_transpuestos))
        # Se aplica el orden definido
        if self._orden != tex['orden_opc_2']: # Ninguno
            indice_orden:int = self._encabezados_tabla.index(self._criterio)
            if self._orden == tex['orden_opc_0']: # Ascendente
                registros = sorted(registros, key=lambda x: x[indice_orden])
            elif self._orden == tex['orden_opc_1']: # Descendente
                registros = sorted(registros,
                                   key=lambda x: x[indice_orden],
                                   reverse=True)
        return registros

    def _registros_secrets(self) -> list:
        # Crea los registros
        filas:int = self._filas
        booleanos = [True,False,"None"]
        registros_transpuestos:list = []
        for campo in self._encabezados_tabla:
            columna:list = []
            # Booleanos
            if campo in self._campos_booleanos:
                if self._campos_booleanos[campo] == "True, False":
                    for _ in range(filas):
                        columna.append(booleanos[secrets.randbelow(2)])
                    registros_transpuestos.append(columna)
                else:
                    for _ in range(filas):
                        columna.append(booleanos[secrets.randbelow(3)])
                    registros_transpuestos.append(columna)
            # Texto
            elif campo in self._campos_texto:
                variantes_de_texto:list = self._campos_texto[campo]
                n_items = len(variantes_de_texto)
                for _ in range(filas):
                    columna.append(
                        variantes_de_texto[secrets.randbelow(n_items)]
                    )
                registros_transpuestos.append(columna)
            # Enteros
            elif campo in self._campos_enteros:
                rango = self._campos_enteros[campo]
                intervalo:int = rango[1] - rango[0] + 1
                piso:int = rango[0] 
                for _ in range(filas):
                    columna.append(secrets.randbelow(intervalo) + piso)
                registros_transpuestos.append(columna)
            # Reales
            elif campo in self._campos_reales:
                for _ in range(filas):
                    columna.append("")
                registros_transpuestos.append(columna)
            # Campos sin definir    
            else:
                for _ in range(filas):
                    columna.append("")
                registros_transpuestos.append(columna)
        # Transpone la lista de lista para que coincida con el formato de tabla        
        registros = list(zip(*registros_transpuestos))
        # Se aplica el orden definido
        if self._orden != tex['orden_opc_2']:
            indice_orden:int = self._encabezados_tabla.index(self._criterio)
            if self._orden == tex['orden_opc_0']:
                registros = sorted(registros, key=lambda x: x[indice_orden])
            elif self._orden == tex['orden_opc_1']:
                registros = sorted(registros,
                                   key=lambda x: x[indice_orden],
                                   reverse=True)
        return registros


    def _grabar_datos(self, registros:list) -> bool:
        res:bool = False
        try:
            with open(self._ruta_salida_csv, "w", newline="", encoding="utf-8") as archivo:
                tabla_final = csv.writer(archivo, delimiter=self._delimitador)
                tabla_final.writerow(self._encabezados_tabla)
                tabla_final.writerows(registros)
                res = True
        except:
            res = False
        return res



class SubmoduloEntradaTexto:

    def __init__(self,
                 ubicacion,
                 texto_etiqueta:str,
                 texto_base_entrada:str="",
                 evento_enter = lambda event=None: lambda *args: None,
                 pack_entrada=PACK_ENTRADA_TEXTO,
                 pack_etiqueta=PACK_ETI_INGRESO):

        # Configuración pack
        self.pack_eti_base = pack_etiqueta
        self.pack_entrada_base = pack_entrada

        # Contenedor ingreso
        self._contenedor_ingreso = tk.Frame(ubicacion,
                                            **ESTILO_CONTENEDOR_INGRESO)
        self._contenedor_ingreso.pack(**PACK_CONTENEDOR_INGRESO)

        # Etiqueta
        self._eti_ingreso = tk.Label(self._contenedor_ingreso,
                                     text=texto_etiqueta,
                                     **ESTILO_ETIQUETA)
        self._eti_ingreso.config(font=FUENTE_ETIQUETA)
        self._eti_ingreso.pack(**self.pack_eti_base)

        # Entrada
        # Almacena el valor registrado
        self._valor_ingresado = tk.StringVar()        
        self._entrada = tk.Entry(self._contenedor_ingreso,
                                 textvariable=self._valor_ingresado)
        self._entrada.config(font=FUENTE_ENTRADA)
        self._entrada.insert(0, texto_base_entrada)
        self._entrada.pack(**self.pack_entrada_base)
        self._entrada.bind("<Return>", evento_enter)

    def borrar_valor(self):
        self._entrada.delete(0, "end")
        return None

    def obtener_valor(self) -> str:
        return self._valor_ingresado.get()

    def establecer_valor(self, valor:str):
        self._valor_ingresado.set(valor)

    def enfocar_entrada(self):
        self._entrada.focus_set()

    def mostrar_submodulo(self):
        self._contenedor_ingreso.pack(**PACK_CONTENEDOR_INGRESO)
        self._eti_ingreso.pack(**self.pack_eti_base)
        self._entrada.pack(**self.pack_entrada_base)
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
                 estilo_opc=ESTILO_BOTON_OPCION,
                 pack_cont_ingreso=PACK_CONTENEDOR_INGRESO):
        # Contenedor ingreso
        self._contenedor_ingreso = tk.Frame(ubicacion,
                                            **ESTILO_CONTENEDOR_INGRESO)
        self._contenedor_ingreso.pack(**pack_cont_ingreso)

        # Etiqueta
        self._eti_ingreso = tk.Label(self._contenedor_ingreso,
                                     text=texto_etiqueta,
                                     **ESTILO_ETIQUETA)
        self._eti_ingreso.config(font=FUENTE_ETIQUETA)
        self._eti_ingreso.pack(**PACK_ETI_INGRESO)

        # Entrada
        ancho_maximo = 13
        self._opciones = opciones_base
        # Almacena el valor registrado
        self._valor_ingresado = tk.StringVar()
        self._valor_ingresado.set(self._opciones[0])
        self._entrada_opciones = tk.OptionMenu(self._contenedor_ingreso,
                                               self._valor_ingresado,
                                               *self._opciones)
        self._entrada_opciones.config(font=FUENTE_BOTON,
                                      **estilo_opc)
        self._entrada_opciones.pack(**PACK_ENTRADA_OPCION)
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
        self._contenedor_ingreso.pack(**pack_cont_ingreso)
        self._eti_ingreso.pack(**PACK_ETI_INGRESO)
        self._entrada_opciones.pack(**PACK_ENTRADA_OPCION)
        return None

    def ocultar_submodulo(self):
        self._contenedor_ingreso.pack_forget()
        self._eti_ingreso.pack_forget()
        self._entrada_opciones.pack_forget()
        return None



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
        self._boton.pack(**PACK_BOTON)
        self._boton.bind("<Return>", evento_enter)

    def enfocar_boton(self):
        self._boton.focus_set()



class BotonEspecial:
    def __init__(self, ubicacion,
                 texto_boton:str,
                 funcion_comando,
                 estilo_boton,
                 fuente_boton,
                 pack_variable=PACK_BOTON,
                 evento_enter = lambda event=None: lambda *args: None):
        self._boton = tk.Button(ubicacion,
                                text=texto_boton,
                                command=funcion_comando,
                                **estilo_boton)
        self._boton.config(font=fuente_boton)
        self._boton.pack(**pack_variable)
        self._boton.bind("<Return>", evento_enter)
        





def main():
    # Ventana principal
    global raiz
    raiz = tk.Tk()
    #raiz.attributes('-zoomed', True)
    raiz.geometry("1100x675")
    raiz.resizable(True,True)
    x_pantalla = raiz.winfo_screenwidth()
    y_pantalla = raiz.winfo_screenheight()
    raiz.maxsize(x_pantalla,y_pantalla)
    raiz.configure(**ESTILO_RAIZ)
    raiz.title(' ')

    # Diccionarios que defienen estilos de fuente
    global FUENTE_PRINCIPAL
    FUENTE_PRINCIPAL = tk.font.Font(family="Monospace",
                                   size=9,
                                   weight="bold",
                                   slant="roman")
    global FUENTE_TITULO
    FUENTE_TITULO = tk.font.Font(family="Monospace",
                                 size=8,
                                 weight="bold",
                                 slant="roman")
    global FUENTE_ETIQUETA 
    FUENTE_ETIQUETA = tk.font.Font(family="Monospace",
                                   size=8,
                                   weight="bold",
                                   slant="roman")
    global FUENTE_ENTRADA
    FUENTE_ENTRADA = tk.font.Font(family="Monospace",
                                  size=8,
                                  weight="normal",
                                  slant="italic")
    global FUENTE_BOTON 
    FUENTE_BOTON = tk.font.Font(family="Monospace",
                                size=7,
                                weight="normal",
                                slant="roman")
    global FUENTE_BOTON_SALIR
    FUENTE_BOTON_SALIR = tk.font.Font(family="Monospace",
                                      size=7,
                                      weight="normal",
                                      slant="roman")

    # Instancias de las clases principales
    global gestor
    gestor = Gestor()
    global tabla
    tabla = Tabla()
    global generador
    generador = Generador()
    global interface_usuario
    interface_usuario = InterfaceUsuario(raiz, gestor, tabla, generador)
    # Inicio del bucle de la aplicación
    interface_usuario.ejecutar()

# Bloque principal     
if __name__ == "__main__":
    main()




    
