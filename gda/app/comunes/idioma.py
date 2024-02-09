import tkinter as tk

# Diccionarios que reunen el texto en español y en inglés.
# Los dos diccionarios con sufijo "_AUX" contiene las frases largas
# del idioma correspondiente, separadas en cadenas más pequeñas.
# Los comentarios indican el módulo o función a la que pertenecen
# o en la cual se utilizan por primera vez.
TEX_ES_AUX:dict = { 
    "_acl_0" : "\n DATOS INGRESADOS\n\n",
    "_acl_1" : "Para los campos que se prevean como calculados, ",
    "_acl_2" : "no se requiere asignar valores ni tipos de datos.\n\n",
    "_err_enc_1" : "Por favor, ingrese los campos de ",
    "_err_enc_2" : "su tabla separados por comas.",
    "_err_long_enc_1" : "El máximo es de 100 caracteres por cada campo. ",
    "_err_long_enc_2" : "Por favor, revise el encabezado ingresado",
    "_err_criterio_1" : "La tabla no pudo ser ordenada según el campo especificado. ",
    "_err_criterio_2" : "Por favor, verifique su selección.",
    "_err_no_val_1" : "El campo seleccionado no ha recibido ningún valor. ",
    "_err_no_val_2" : "Por favor, ingrese los datos y vuelva a intentarlo.",
    "_err_campo_inex_1" : "Solamente se pueden definir valores para un campo existente. ",
    "_err_campo_inex_2" : "Por favor, revise los campos de la tabla.",
    "_err_campo_repe_1" : "El campo seleccionado ya tiene valores definidos. ",
    "_err_campo_repe_2" : "Para reemplazarlos, elimine los valores existentes del campo.",
    "_err_ruta_ent_1" : "El archivo no se puede abrir porque ",
    "_err_ruta_ent_2" : "la ruta especificada no existe.",
    "_err_secrets_1" : "El módulo 'secrets' no genera números de coma flotante.\n",
    "_err_secrets_2" : "Si necesita valores con decimales, puede seleccionar 'random'."
}                                       
TEX_ES:dict = {
    # Módulo interface
    "vt_principal" : "GDA",
    "titulo_app" : "GENERADOR DE TABLAS CON DATOS PSEUDO-ALEATORIOS",
    "btn_salir" : "Salir",
    "btn_idioma" : "EN",
    "ne_btn_idioma" : "Se reiniciará la aplicación y se perderán los datos ingresados",
    "vt_salida" : "Confirmar Salir",
    "vt_salida_mensaje" : "¿Confirma que desea salir?",
    "titulo_generar" : " CONFIGURACION DE LA TABLA ",
    # Modulo vista
    "aclaracion" : TEX_ES_AUX["_acl_0"] + TEX_ES_AUX["_acl_1"] + TEX_ES_AUX["_acl_2"],
    "titulo_convertir" : " CSV A JSON ",
    # Modulo ruta
    "ruta" : "Ruta de salida",
    "ruta_def" : "/ruta_a_archivo_vacío.csv",
    "btn_ubicacion" : "Elegir ubicación",
    "btn_ok" : "Aceptar",
    # Modulo encabezado
    "campos_def" : "Campo_1, Campo_2, ..., Campo_n",
    "encabezado" : "Campos de la tabla",
    "btn_encabezado" : "Borrar encabezado",
    # Modulo opciones tabla
    "delimitador" : "Delimitador",
    "orden" : "Orden",
    "ne_opc_orden" : "Las tablas pequeñas no requieren librerías externas",
    "criterio" : "Criterio",
    "modo" : "Aleatoriedad",
    "semilla" : "Semilla",
    "orden_opc_0" : "Ascendente",
    "orden_opc_1" : "Descendente",
    "orden_opc_2" : "Ninguno",
    "orden_opc_3" : "Ascendente - pandas",
    "orden_opc_4" : "Descendente - pandas",
    "criterio_opc_base" : "Campo_n",
    "semilla_def" : "Sin semilla",
    "opc_vacio" : "Vacío",
    # Modulo campo booleano
    "selecc_campo_bool" : "Definir como booleano",
    "logica" : "Valores",
    "campo_def_0" : "Campo_1", 
    "campo_def_1" : "Campo_2", 
    "campo_def_2" : "...",     
    "campo_def_3" : "Campo_n", 
    # Modulo campo texto
    "valores_texto" : "Alternativas de texto",
    "selecc_campo" : "Definir como texto",
    "valores_tex_def" : "valor_1, valor_2, ..., valor_n",
    "btn_borrar_tex" : "Borrar valores",
    # Modulo campo numerico
    "selecc_campo_num" : "Definir como numérico",
    "rango_desde" : "Desde",
    "rango_hasta" : "Hasta",
    "ne_digitos" : "Máximo: 100 dígitos",
    "selecc_tipo_num" : "Tipo numérico",
    "opc_num_int" : "Enteros",     
    "opc_num_float" : "Decimales",
    "redondear" : "Redondear",
    "ne_redondeo" : "Máximo: 15",
    # Modulo campo a borrar
    "campo_a_borrar" : "Campo a borrar",
    "btn_vaciar_campo" : "Eliminar datos ingresados",
    "btn_vaciar_tabla" : "Borrar todo",
    'ne_btn_restablecer' : "Todos los datos ingresados serán eliminados",
    # Modulo exportar
    "num_filas" : "Número de filas",
    "ne_filas" : "Máximo: 1000000 filas",
    "btn_exportar" : "Exportar tabla",
    "vt_expo_sn" : "Confirmar exportar",
    "vt_expo_sn_mensaje" : "¿Confirma que desea exportar?", 
    # Gestion ruta
    "err_ruta_invalida" : "Por favor introduzca una ruta válida",
    "err_vt_ruta_invalida" : "Error: ruta de salida",
    "ruta_archivo" : "tabla_datos_pseudoaleatorios.csv",
    # Gestion encabezado
    "err_encabezado" : TEX_ES_AUX['_err_enc_1'] + TEX_ES_AUX['_err_enc_2'],
    "err_vt_encabezado" : "Error: campos no ingresados",
    "err_long_encabezado" : TEX_ES_AUX['_err_long_enc_1'] + TEX_ES_AUX['_err_long_enc_2'],
    "err_vt_long_encabezado" : "Error: nombres de campos",
    # Gestion opciones tabla
    "err_delimitador" : "Solo se permite un único carácter como delimitador.",
    "err_vt_delimitador" : "Error: delimitador no válido",
    "err_import_1" : "Ocurrió un error al importar 'pandas': ",
    "err_import_2" : "Si la tabla es pequeña, puedes volver a ",
    "err_import_3" : "intentarlo sin importar librerías externas.",
    "err_vt_import" : "Error: importación de librería",
    "err_criterio" : TEX_ES_AUX['_err_criterio_1'] + TEX_ES_AUX['_err_criterio_2'],
    "err_vt_criterio" : "Error: campo de ordenación",
    # Gestion campo texto
    "err_no_valores_tex" : TEX_ES_AUX["_err_no_val_1"] + TEX_ES_AUX["_err_no_val_2"],
    "err_vt_no_valores_tex" : "Error: valores no ingresados",
    # Gestion condiciones basicas
    "err_campo_def" : "Por favor seleccione un campo que no haya sido definido.",
    "err_vt_campo_def" : "Error: campo ya definido",
    "err_campo_inexistente" : TEX_ES_AUX["_err_campo_inex_1"] + TEX_ES_AUX["_err_campo_inex_2"],
    "err_vt_campo_inex" : "Error: campo inexistente",
    "err_campo_repetido" : TEX_ES_AUX["_err_campo_repe_1"] + TEX_ES_AUX["_err_campo_repe_2"],
    "err_vt_campo_repe" : "Error: campo repetido",
    # Gestion campo numerico
    "err_rango_invalido" : "Por favor ingrese un rango válido.",
    "err_vt_rango_invalido" : "Error: rango no válido",
    "err_rango_menor" : "El inicio del rango debe ser menor que el final.",
    "err_vt_rango_menor" : "Error: rango inconsistente",
    "err_redondeo" : "Por favor ingrese un entero entre 0 y 15.",
    "err_vt_redondeo" : "Error: valor de redondeo no válido",
    # Gestion exportar
    "err_ruta_ingresada" : TEX_ES_AUX["_err_ruta_ent_1"] + TEX_ES_AUX["_err_ruta_ent_2"],
    "err_vt_ruta_ingresada" : "Error: ruta de salida",
    "err_escritura" : "No posee permisos de escritura en la ruta especificada.",
    "vt_err_escritura" : "Error: permisos de escritura",
    "err_ruta_inesperado" : "Ocurrió un error inesperado: ",
    "err_vt_ruta_inesperado" : "Error: inesperado",
    "err_secrets" : TEX_ES_AUX["_err_secrets_1"] + TEX_ES_AUX["_err_secrets_2"],
    "err_vt_secrets" : "Error: modo de aleatoriedad",
    "err_umbral_filas" : "El número de filas ingresado excede el umbral establecido.",
    "err_vt_umbral_filas" : "Error: umbral de número de filas",
    "err_filas" : "Por favor ingrese un número de filas válido",
    "err_vt_filas" : "Error: número de filas no válido",
    "ok_tabla" : "¡La tabla se generó correctamente!",
    "vt_ok_tabla" : "Operación exitosa",
    # Mostrar ventana
    "btn_vt_cerrar" : "Cerrar",
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
    "clave_float" : "\n • Campos con números decimales: "
}
TEX_EN_AUX:dict = {
    "_acl_0" : "\n ENTERED DATA\n\n",
    "_acl_1" : "For fields envisioned as calculated, ",
    "_acl_2" : "assigning values or data types is not required.\n\n",
    "_err_long_enc_1" : "The maximum is 100 characters per field. ",
    "_err_long_enc_2" : "Please review the entered header.",
    "_err_criterio_1" : "The table could not be sorted according ",
    "_err_criterio_2" : "to the specified field. Please review your choice.",
    "_err_no_val_1" : "The selected field has not received any value. ",
    "_err_no_val_2" : "Please enter the data and try again.",
    "_err_campo_inex_1" : "Values can only be defined for an existing field. ",
    "_err_campo_inex_2" : "Please review the table fields.",
    "_err_campo_repe_1" : "The selected field already has defined values. To ",
    "_err_campo_repe_2" : "replace them, remove the existing values from the field.",
    "_err_ruta_ent_1" : "The file cannot be opened because ",
    "_err_ruta_ent_2" : "the specified path does not exist.",
    "_err_secrets_1" : "The 'secrets' module does not generate floating-point numbers.\n",
    "_err_secrets_2" : "If you need decimal values, you can choose 'random'."
}                        
TEX_EN:dict = {
    # Módulo interface
    "vt_principal" : "GDA",
    "titulo_app" : "PSEUDO-RANDOM DATA TABLE GENERATOR",
    "btn_salir" : "Exit",
    "btn_idioma" : "ES",
    "ne_btn_idioma" : "The application will restart, and any entered data will be lost",
    "vt_salida" : "Confirm Exit",
    "vt_salida_mensaje" : "Confirm that you want to exit?",
    "titulo_generar" : " TABLE SETTINGS ",
    # Modulo vista
    "aclaracion" : TEX_EN_AUX["_acl_0"] + TEX_EN_AUX["_acl_1"] + TEX_EN_AUX["_acl_2"],
    "titulo_convertir" : " CSV TO JSON ",
    # Modulo ruta
    "ruta" : "Output path or file location",
    "ruta_def" : "/path_to_empty_file.csv",
    "btn_ubicacion" : "Choose location",
    "btn_ok" : "OK",
    # Modulo encabezado
    "campos_def" : "Field_1, Field_2, ..., Field_n", 
    "encabezado" : "Table Fields",
    "btn_encabezado" : "Remove Header",
    # Modulo opciones tabla
    "delimitador" : "Delimiter",
    "orden" : "Sort",
    "ne_opc_orden" : "Small tables do not require external libraries",
    "criterio" : "Criterion",
    "modo" : "Randomness",
    "semilla" : "Seed",
    "orden_opc_0" : "Ascending",
    "orden_opc_1" : "Descending",
    "orden_opc_2" : "None",
    "orden_opc_3" : "Ascending - pandas",
    "orden_opc_4" : "Descending - pandas",
    "criterio_opc_base" : "Field_n",
    "semilla_def" : "No seed",
    "opc_vacio" : "Empty", 
    # Modulo campo booleano
    "selecc_campo_bool" : "Set as boolean field",
    "logica" : "Values",
    "campo_def_0" : "Field_1", 
    "campo_def_1" : "Field_2", 
    "campo_def_2" : "...",     
    "campo_def_3" : "Field_n", 
    # Modulo campo texto
    "valores_texto" : "Text Alternatives",
    "selecc_campo" : "Set as text field",
    "valores_tex_def" : "value_1, value_2, ..., value_n",
    "btn_borrar_tex" : "Clear values",
    # Modulo campo numerico
    "selecc_campo_num" : "Set as numeric field",
    "rango_desde" : "From",
    "rango_hasta" : "To",
    "ne_digitos" : "Max: 100 digits",
    "selecc_tipo_num" : "Number type",
    "opc_num_int" : "Integer",  
    "opc_num_float" : "Float",
    "redondear" : "Round",
    "ne_redondeo" : "Max: 15",
    # Modulo campo a borrar
    "campo_a_borrar" : "Field to delete",
    "btn_vaciar_campo" : "Remove entered data",
    "btn_vaciar_tabla" : "Clear all",
    "ne_btn_restablecer" : "All entered data will be deleted",
    # Modulo exportar
    "num_filas" : "Number of rows",
    "ne_filas" : "Max: 1000000 rows",
    "btn_exportar" : "Export table",
    "vt_expo_sn" : "Confirm export",
    "vt_expo_sn_mensaje" : "Confirm that you want to export?",
    # Gestion ruta
    "err_ruta_invalida" : "Please enter a valid path.",
    "err_vt_ruta_invalida" : "Output path error",
    "ruta_archivo" : "pseudo_random_data_table.csv",
    # Gestion encabezado
    "err_encabezado" : "Please enter your table headers separated by commas.",
    "err_vt_encabezado" : "Error: Unentered fields",
    "err_long_encabezado" : TEX_EN_AUX['_err_long_enc_1'] + TEX_EN_AUX['_err_long_enc_2'],
    "err_vt_long_encabezado" : "Error: fields names",
    # Gestion opciones tabla
    "err_delimitador" : "Only a single character is allowed as a delimiter.",
    "err_vt_delimitador" : "Error: Invalid delimiter",
    "err_import_1" : "An error occurred while importing 'pandas': ",
    "err_import_2" : "If the table is small, you can try again ",
    "err_import_3" : "without importing external libraries.",
    "err_vt_import" : "Error: library import",
    "err_criterio" : TEX_EN_AUX['_err_criterio_1'] + TEX_EN_AUX['_err_criterio_2'],
    "err_vt_criterio" : "Error: Sorting field",
    # Gestion campo texto
    "err_no_valores_tex" : TEX_EN_AUX["_err_no_val_1"] + TEX_EN_AUX["_err_no_val_2"],
    "err_vt_no_valores_tex" : "Error: Unentered values",
    # Gestion condiciones basicas
    "err_campo_def" : "Please select a field that has not been defined.",
    "err_vt_campo_def" : "Error: Field already defined.",
    "err_campo_inexistente" : TEX_EN_AUX["_err_campo_inex_1"] + TEX_EN_AUX["_err_campo_inex_2"],
    "err_vt_campo_inex" : "Error: Field does not exist",
    "err_campo_repetido" : TEX_EN_AUX["_err_campo_repe_1"] + TEX_EN_AUX["_err_campo_repe_2"],
    "err_vt_campo_repe" : "Error: Duplicate field",
    # Gestion campo numerico
    "err_rango_invalido" : "Please enter a valid range.",
    "err_vt_rango_invalido" : "Error: Invalid range",
    "err_rango_menor" : "The start of the range must be less than the end.",
    "err_vt_rango_menor" : "Error: Inconsistent range",
    "err_redondeo" : "Please enter an integer between 0 and 15.",
    "err_vt_redondeo" : "Error: Invalid rounding value",
    # Gestion exportar
    "err_ruta_ingresada" : TEX_EN_AUX["_err_ruta_ent_1"] + TEX_EN_AUX["_err_ruta_ent_2"],
    "err_vt_ruta_ingresada" : "Error: Output path",
    "err_escritura" : "No write permissions for the specified path.",
    "vt_err_escritura" : "Error: write permission",
    "err_ruta_inesperado" : "An unexpected error occurred: ",
    "err_vt_ruta_inesperado" : "Error: unexpected",
    "err_secrets" : TEX_EN_AUX["_err_secrets_1"] + TEX_EN_AUX["_err_secrets_2"],
    "err_vt_secrets" : "Error: randomness mode",
    "err_umbral_filas" : "The number of entered rows exceeds the established threshold.",
    "err_vt_umbral_filas" : "Error: threshold for number of rows",
    "err_filas" : "Please enter a valid number of rows.",
    "err_vt_filas" : "Error: invalid number of rows",
    "ok_tabla" : "The table was generated successfully!",
    "vt_ok_tabla" : "Successful operation",
    # Mostrar ventana
    "btn_vt_cerrar" : "Close",
    # Tabla
    "ruta_clave" : " • Path: ",
    "encabezado_clave" : "\n • Table header: ",
    "delimitador_clave" : "\n • Delimiter: ",
    "orden_clave" : "\n • Sorting type: ",
    "criterio_campo" : "\n • Records sorted by the field: ",
    "clave_modo" : "\n • Randomization module: ",
    "clave_semilla" : "\n • Seed: ",
    "clave_bool" : "\n • Fields with boolean values ",
    "clave_tex" : "\n • Fields with text values: ",
    "clave_int" : "\n • Fields with integer values: ",
    "clave_float" : "\n • Fields with float numbers: "
}

class Idioma:
    """
    Clase que genera el diccionario que permite alternar el idioma
    entre inglés y español.
    """
    tex:dict = dict()

leng = Idioma()
# Inicia en español
leng.tex = TEX_ES

def alternar(raiz, reseteador):
    """
    Administra el cambio de idioma mediante la actualización del diccionario
    de texto y la posterior reinicialización de la aplicación.

    :param raiz: Instancia de la ventana principal.
    :type raiz: Tk
    :param reseteador: Instancia que permite el reinicio de la aplicación.
    :type reseteador: Reseteador
    :return: None
    """ 
    if leng.tex == TEX_ES:
        leng.tex = TEX_EN
        raiz.destroy()
        reseteador.reiniciar()   
    else:
        leng.tex = TEX_ES
        raiz.destroy()
        reseteador.reiniciar()
