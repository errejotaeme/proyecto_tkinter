import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from app.comunes.globales import gb
from app.comunes.idioma import leng


class Gestor:
    """
    Clase encargada de coordinar los componentes y facilitar la comunicación
    entre la tabla, los componentes y el generador.
    """

    def __init__(self):
        """
        Constructor de la clase Gestor. Contiene los componentes principales
        de la aplicación y coordina sus tareas.
        """
        self.raiz = None
        self.tabla = None
        self.generador = None
        self.interface = None
        
    def enlazar_raiz(self, raiz_activa):
        """
        Almacena la instancia de la ventana raiz.

        :param raiz: Ventana principal de la aplicación.
        :type raiz: Tk
        :return: None
        """
        self.raiz = raiz_activa

    def enlazar_tabla(self, tabla_activa):
        """
        Almacena la instancia de la tabla.

        :param tabla: Componente que almacena los datos ingresados.
        :type tabla: Tabla
        :return: None
        """
        self.tabla = tabla_activa
        
    def enlazar_generador(self, generador_activo):
        """
        Almacena la instancia del generador.

        :param generador_activo: Componente que produce y exporta la tabla.
        :type generador_activo: Generador
        :return: None
        """
        self.generador = generador_activo
        
    def enlazar_interface(self, interface_activa):
        """
        Almacena la instancia de la interface.

        :param interface_activa: Componente que contiene los widgets de ingreso de datos.
        :type interface_activa: Interface
        :return: None
        """
        self.interface = interface_activa
                
        

    def recibir(self, origen:str, mensaje) -> bool:
        """
        Enruta los mensajes al método correspondiente. Si la gestión fue exitosa
        (se logró almacenar los datos en la tabla), actualiza la vista.

        :param origen: Módulo que efectúa la llamada.
        :type origen: str
        :param mensaje: Contenido a gestionar.
        :type mensaje: str, list
        :return gestion: True si fue exitosa, False en caso contrario.
        :rtype gestion: bool
        """
        gestion:bool = False

        if origen == "m_ruta":
            gestion = self._gestion_ruta(mensaje) # str

        elif origen == "m_encabezado":
            gestion = self._gestion_encabezado(mensaje) # str

        elif origen == "m_opciones_tabla":
            gestion = self._gestion_opciones_tabla(mensaje) # list

        elif origen == "m_campo_booleano":
            gestion = self._gestion_campo_booleano(mensaje) # list

        elif origen == "m_campo_texto":
            gestion = self._gestion_campo_texto(mensaje) # list

        elif origen == "m_campo_numerico":
            gestion = self._gestion_campo_numerico(mensaje) # list

        elif origen == "m_exportar":
            gestion = self._gestion_exportar(mensaje) # str
        
        if gestion:
            self.actualizar_vista()
        return gestion


    def actualizar_vista(self):
        """
        Envía a la vista los datos almacenados en la tabla.

        :return: None
        """
        self.interface.modulo_ver_datos.insertar_datos(self.tabla.obtener_datos())

    def ver_encabezado(self) -> list:
        """
        Retorna los campos almacenados en la tabla.

        :return encabezado: Campos ingresados.
        :rtype encabezado: list
        """
        encabezado:list = self.tabla.obtener_encabezado()
        return encabezado

    def borrar_encabezado(self):
        """
        Vacía la lista de campos, las opciones que la utilizan y luego
        actualiza la vista.

        :return: None
        """
        self.tabla.borrar_encabezado()
        self.tabla.borrar_todos_los_campos()
        self.actualizar_opciones()
        self.actualizar_vista()

    def actualizar_opciones(self):
        """
        Actualiza todos los componentes que utilizan los campos ingresados
        en la tabla.
        
        :return: None
        """
        self.interface.modulo_opciones_tabla.actualizar_opciones_criterio()
        self.interface.modulo_campo_booleano.actualizar_opciones_campo()
        self.interface.modulo_campo_texto.actualizar_opciones_campo()
        self.interface.modulo_campo_numerico.actualizar_opciones_campo()
        self.interface.modulo_borrar_campo.actualizar_opciones_borrado()

    def ver_campos_definidos(self) -> list:
        """
        Retorna una lista con los nombres de los campos almacenados en la tabla.

        :return: Lista de los nombres de los campos almacenados.
        :rtype: list
        """
        return self.tabla.campos_definidos()

    def ver_campos_sin_definir(self) -> list:
        """
        Retorna una lista con los nombres de los campos sin definir.

        :return: Lista de los nombres de los campos sin definir.
        :rtype: list
        """
        a = set(self.ver_encabezado())
        b = set(self.ver_campos_definidos())
        return list(a - b)

    def restablecer_aplicacion(self):
        """
        Limpia el texto de las entradas, actualiza las opciones y
        establece el enfoque del teclado en el widget principal
        del módulo ruta.

        :return: None
        """
        self.interface.modulo_ruta.limpiar_entrada()
        self.interface.modulo_encabezado.limpiar_entrada()
        self.interface.modulo_campo_texto.limpiar_entrada()
        self.interface.modulo_campo_numerico.limpiar_entrada()
        self.interface.modulo_opciones_tabla.limpiar_entrada()
        self.interface.modulo_exportar.limpiar_entrada()
        self.actualizar_opciones()
        self.interface.modulo_ruta.enfocar()

    def vaciar_tabla(self):
        """
        Vacia todos los datos ingresados a la tabla.
        
        :return: None
        """
        self.tabla.restablecer_tabla()

    def vaciar_campo(self, nombre_campo:str):
        """
        Borra los valores registrados en la tabla del campo especificado.
        
        :param nombre_campo: Campo especificado.
        :type nombre_campo: str
        :return: None        
        """
        if nombre_campo in self.tabla.obtener_campos_booleanos():
            self.tabla.borrar_campo_booleano(nombre_campo)
        elif nombre_campo in self.tabla.obtener_campos_texto():
            self.tabla.borrar_campo_texto(nombre_campo)
        elif nombre_campo in self.tabla.obtener_campos_enteros():
            self.tabla.borrar_campo_entero(nombre_campo)
        elif nombre_campo in self.tabla.obtener_campos_decimales():
            self.tabla.borrar_campo_real(nombre_campo)

    def _gestion_ruta(self, mensaje:str) -> bool:
        """
        Gestiona la validación de la ruta ingresada. Si fue exitosa
        retorna True, caso contrario notifica el error y retorna False.
        
        :param mensaje: Ruta de salida ingresada.
        :type mensaje: str
        :return res: True si la gestión fue exitosa, de lo contrario False.
        :rtype res: bool 
        """       
        res:bool = False
        if self._es_ruta_valida(mensaje):
            res = True
        else:
            self._ventana_dialogo(
                leng.tex['err_ruta_invalida'],
                leng.tex['err_vt_ruta_invalida']
            )
        return res

    def _es_ruta_valida(self, ruta:str) -> bool:
        """
        Verifica la validez de la ruta ingresada o la existencia
        del directorio de salida. Si la verificación es positiva,
        registra la ruta en la tabla.

        :param ruta: Ruta de salida ingresada.
        :type ruta: str
        :return res: True si la verificación fue exitosa, de lo contrario False.
        :rtype res: bool
        """
        res:bool = False
        ruta_final = Path(ruta)
        if ruta.endswith(".csv") and ruta_final.parent.is_dir():
            res = True
        elif ruta_final.is_dir():
            ruta_final = ruta_final / leng.tex['ruta_archivo'] 
            res = True
        if res:
            self.tabla.establecer_ruta(ruta_final)
        return res

    def _gestion_encabezado(self, mensaje:str) -> bool:
        """
        Notifica si el encabezado ingresado está vacío. Si no lo está,
        lo procesa y registra en la tabla. Elimina aquellos campos
        definidos que no estén en el nuevo encabezado y actualiza
        las opciones de los componentes correspondientes.

        :param mensaje: Encabezado ingresado.
        :type mensaje: str
        :return res: True si la gestión fue exitosa, de lo contrario False.
        :rtype res: bool        
        """
        res:bool = False
        lista_encabezado:list = []
        if len(mensaje) < 1:
            self._ventana_dialogo(
                leng.tex['err_encabezado'],
                leng.tex['err_vt_encabezado']
            )
            return res
        else:
            lista_encabezado = self._limpiar_lista(mensaje)
            # Limita el maximo de caracteres de un campo 
            for campo in lista_encabezado:
                if len(campo) > 100: # Umbral
                    self._ventana_dialogo(
                        leng.tex['err_long_encabezado'],
                        leng.tex['err_vt_long_encabezado']
                    )
                    return res
            self.tabla.establecer_encabezado(lista_encabezado)
            res = True
            
        for campo in list(self.tabla.obtener_campos_booleanos()):
            if campo not in lista_encabezado:
                self.tabla.borrar_campo_booleano(campo)
        for campo in list(self.tabla.obtener_campos_texto()):
            if campo not in lista_encabezado:
                self.tabla.borrar_campo_texto(campo)
        for campo in list(self.tabla.obtener_campos_enteros()):
            if campo not in lista_encabezado:
                self.tabla.borrar_campo_entero(campo)
        for campo in list(self.tabla.obtener_campos_decimales()):
            if campo not in lista_encabezado:
                self.tabla.borrar_campo_real(campo)

        self.interface.modulo_campo_booleano.actualizar_opciones_campo()
        self.interface.modulo_campo_texto.actualizar_opciones_campo()
        self.interface.modulo_campo_numerico.actualizar_opciones_campo()
        self.interface.modulo_borrar_campo.actualizar_opciones_borrado()
        return res

    def _limpiar_lista(self, cadena:str) -> list:
        """
        Produce una lista de items únicos y no vacíos a partir de una cadena.

        :param cadena: Cadena con valores separados por coma.
        :param cadena: str
        :return lista_salida: Lista de items únicos.
        :rtype lista_salida: list
        """
        lista_salida:list = cadena.split(',')
        lista_salida = [item.strip() for item in lista_salida]
        lista_salida = [item for item in lista_salida if item != " "]
        lista_aux:list = []
        [lista_aux.append(e) for e in lista_salida if e not in lista_aux]
        lista_salida = lista_aux
        return lista_salida

    def _gestion_opciones_tabla(self, mensaje:list) -> bool:
        """
        Valida los valores definidos. Si la validación es exitosa
        los registra en la tabla; caso contrario, notifica el error.

        :param mensaje: Opciones seleccionadas.
        :type mensaje: list
        :return res: True si la gestión fue exitosa, de lo contrario False.
        :rtype res: bool 
        """
        res:bool = False
        delimitador:str = mensaje[0]
        orden:str = mensaje[1]
        criterio_campo:str = mensaje[2]
        modo:str = mensaje[3]
        semilla:str = mensaje[4]
        encabezado:list = self.tabla.obtener_encabezado()
        if "pandas" in orden:
            try:
                import pandas
            except Exception as e:
                m_error:str = leng.tex['err_import_1'] + f"\n{e}\n" + leng.tex['err_import_2']
                m_error += leng.tex['err_import_3']
                self._ventana_dialogo(m_error, leng.tex['err_vt_import'])
                return res

        if modo == "secrets":
            self.tabla.borrar_campos_decimales()

        if len(delimitador) != 1:
            self._ventana_dialogo(
                leng.tex['err_delimitador'],
                leng.tex['err_vt_delimitador']
            )
            return res
        
        elif (not criterio_campo in encabezado and
              orden != leng.tex['orden_opc_2']):
            self._ventana_dialogo(
                leng.tex['err_criterio'],
                leng.tex['err_vt_criterio']
            )
            return res

        else:
            self.tabla.establecer_delimitador(delimitador)
            self.tabla.establecer_orden(orden)
            self.tabla.establecer_criterio(criterio_campo)
            self.tabla.establecer_modo(modo)
            if len(semilla) > 100: # Umbral
                self._ventana_dialogo(
                    leng.tex['err_semilla'],
                    leng.tex['err_vt_semilla']
                )
                return res
            if semilla == "":
                self.tabla.establecer_semilla(leng.tex['semilla_def'])
            else:
                self.tabla.establecer_semilla(semilla)
            res = True
        return res

    def _gestion_campo_booleano(self, mensaje:list) -> bool:
        """
        Verifica las condiciones mínimas para registrar el campo.
        Si la validación es exitosa lo registra en la tabla;
        caso contrario, notifica el error.

        :param mensaje: Campo y opción seleccionada.
        :type mensaje: list
        :return res: True si la gestión fue exitosa, de lo contrario False.
        :rtype res: bool 
        """
        res:bool = False
        nombre_campo = mensaje[0]
        valores_bool = mensaje[1]
        condiciones:bool = self._condiciones_basicas(nombre_campo)
        if condiciones:
            self.tabla.establecer_campo_booleano(nombre_campo, valores_bool)
            res = True
        return res

    def _gestion_campo_texto(self, mensaje:list) -> bool:
        """
        Verifica las condiciones mínimas para registrar el campo y procesa
        las alternativas de texto ingresadas. Si la operación es exitosa
        lo registra en la tabla; caso contrario, notifica el error.

        :param mensaje: Campo y alternativas de texto.
        :type mensaje: list
        :return res: True si la gestión fue exitosa, de lo contrario False.
        :rtype res: bool 
        """
        res:bool = False
        nombre_campo:str = mensaje[0]
        valores_posibles:str = mensaje[1]
        condiciones:bool = self._condiciones_basicas(nombre_campo)
        if condiciones:
            valores:list = self._limpiar_lista(valores_posibles)
            valores = [item for item in valores if item != ""]
            for alternativa in valores:
                if len(alternativa) > 500: # Umbral
                    self._ventana_dialogo(
                        leng.tex['err_long_alter_tex'],
                        leng.tex['err_vt_long_alter_tex']
                    )
                    return res                 
            if any(valor != "" for valor in valores):
                self.tabla.establecer_campo_texto(nombre_campo, valores)
                res = True
            else:
                self._ventana_dialogo(
                    leng.tex['err_no_valores_tex'],
                    leng.tex['err_vt_no_valores_tex']
                )
        return res

    def _condiciones_basicas(self, nombre_campo:str) -> bool:
        """
        Verifica las condiciones mínimas que debe cumplir un campo
        para ser registrado en la tabla.

        :param nombre_campo: Campo a evaluar.
        :type nombre_campo: str
        :return res: True si la verificación fue exitosa, de lo contrario False.
        :rtype res: bool"
        """
        res:bool = False
        campos_definidos:list = self.tabla.campos_definidos()
        if nombre_campo == "":
            self._ventana_dialogo(
                leng.tex['err_campo_def'],
                leng.tex['err_vt_campo_def']
            )
            return res
        elif nombre_campo not in self.tabla.obtener_encabezado():
            self._ventana_dialogo(
                leng.tex['err_campo_inexistente'],
                leng.tex['err_vt_campo_inex']
            )
            return res
        elif nombre_campo in campos_definidos:
            self._ventana_dialogo(
                leng.tex['err_campo_repetido'],
                leng.tex['err_vt_campo_repe']
            )
            return res
        else:
            res = True
        return res

    def _gestion_campo_numerico(self, mensaje:list) -> bool:
        """
        Verifica las condiciones mínimas para registrar el campo y valida
        el rango y el valor de redondeo. Si la operación es exitosa
        lo registra en la tabla; caso contrario, notifica el error.

        :param mensaje: Campo, rango, tipo numérico y valor de redondeo.
        :type mensaje: list
        :return res: True si la gestión fue exitosa, de lo contrario False.
        :rtype res: bool 
        """
        res:bool = False
        nombre_campo:str = mensaje[0]
        rango_inicio:str = mensaje[1].strip()        
        rango_fin:str = mensaje[2].strip()        
        tipo_numerico:str = mensaje[3]
        redondeo: str = mensaje[4]
        digitos_inicio:int = len(rango_inicio)
        digitos_fin:int = len(rango_fin)
        redondear:int = 0
        if not redondeo.isdigit():
            self._ventana_dialogo(
                leng.tex['err_redondeo'],
                leng.tex['err_vt_redondeo']
            )
            return res
        if (redondeo.isdigit() and
            int(redondeo) >= 0 and
            int(redondeo) < 16): # Umbral
            redondear = int(redondeo)
        else:
            self._ventana_dialogo(
                leng.tex['err_redondeo'],
                leng.tex['err_vt_redondeo']
            )
            return res
        if rango_inicio == '' or rango_fin == '':
            self._ventana_dialogo(
                leng.tex['err_rango_invalido'],
                leng.tex['err_vt_rango_invalido']
            )
            return res
        condiciones_ok:bool = self._condiciones_basicas(nombre_campo)
        if not condiciones_ok:
            return res
        else:
            rango_i:int = self._preservar_signo(rango_inicio)
            rango_f:int = self._preservar_signo(rango_fin)
            if type(rango_i) is int and type(rango_f) is int:
                if rango_i > rango_f:
                    self._ventana_dialogo(
                        leng.tex['err_rango_menor'],
                        leng.tex['err_vt_rango_menor']
                    )
                    return res
                elif (rango_i < rango_f and
                      digitos_inicio <= 100 and
                      digitos_fin <= 100): # Umbral
                    rango:tuple = (rango_i, rango_f, redondear)
                    if tipo_numerico == leng.tex['opc_num_int']: # Entero
                        self.tabla.establecer_campo_entero(nombre_campo, rango)
                        res = True
                    elif tipo_numerico == leng.tex['opc_num_float']: # Flotante
                        self.tabla.establecer_campo_decimal(nombre_campo, rango)
                        res = True
                elif rango_i == rango_f:
                    self._ventana_dialogo(
                        leng.tex['err_rango_invalido'],
                        leng.tex['err_vt_rango_invalido']
                    )
                    return res
                else:
                    self._ventana_dialogo(
                    leng.tex['err_rango_invalido'],
                    leng.tex['err_vt_rango_invalido']
                    )
                    return res
            else:
                self._ventana_dialogo(
                    leng.tex['err_rango_invalido'],
                    leng.tex['err_vt_rango_invalido']
                )         
        return res

    def _preservar_signo(self, numero:str):
        """
        Evalúa y convierte una cadena a entero si es un número válido;
        de lo contrario, retorna la cadena original.

        :param numero: Cadena a evaluar.
        :type numero: str
        :return res: Resultado de la operación.
        :rtype res: int, str
        """
        res:int = 0
        if ((not numero.isdigit() and
             numero[0] == '-' and
             numero[1:].isdigit()) or
             numero.isdigit()):
            res = int(numero)
        else:
            res = numero
        return res

    def _gestion_exportar(self, mensaje:str) -> bool:
        """
        Envía al generador los datos registrados en la tabla si se cumplen
        las condiciones de exportación. Notifica si la operación fue existosa.
        En caso de que alguna condición no se cumpla, notifica el error.

        :param mensaje: Número de filas ingresado.
        :type mensaje: str
        :return res: True si la gestión fue exitosa, de lo contrario False.
        :rtype res: bool 
        """
        res:bool = False
        num_filas:int = 0
        if mensaje.isdigit():
            num_filas = int(mensaje)
        else:
            self._ventana_dialogo(leng.tex['err_filas'], leng.tex['err_vt_filas'])
            return res         
        if num_filas > 1000000: # Umbral
            self._ventana_dialogo(
                leng.tex['err_umbral_filas'],
                leng.tex['err_vt_umbral_filas']
            )
            return res
        try:
            # Verifica la validez de la ruta y los permisos de escritura
            with open(self.tabla.obtener_ruta(), "w", newline="", encoding="utf-8"):
                pass # Si no hay error sigue
        except FileNotFoundError:
            self._ventana_dialogo(
                leng.tex['err_ruta_ingresada'],
                leng.tex['err_vt_ruta_ingresada']
            )
            return res
        except PermissionError:
            self._ventana_dialogo(
                leng.tex['err_escritura'],
                leng.tex['vt_err_escritura']
            )
            return res
        except Exception as e:
            self._ventana_dialogo(
                f'{leng.tex["err_ruta_inesperado"]}: {e}',
                leng.tex['err_vt_ruta_inesperado']
            )
            return res
        # Chequea que no haya inconsistencias en el tipo de orden
        if self.tabla.obtener_orden() != leng.tex['orden_opc_2']:
            if self.tabla.obtener_criterio() not in self.tabla.campos_definidos():
                self._ventana_dialogo(
                    leng.tex['err_criterio'],
                    leng.tex['err_vt_criterio']
                )
                return res
        # Previene que se intente generar decimales con secrets
        if self.tabla.obtener_modo() == "secrets":
            if self.tabla.obtener_campos_decimales():
                self._ventana_dialogo(
                    leng.tex['err_secrets'],
                    leng.tex['err_vt_secrets']
                )
                return res
        # Envia los datos al generador      
        if num_filas:
            d_aux:dict = vars(self.tabla)
            d_aux["_filas"] = num_filas
            res = self.generador.crear_tabla(d_aux)   
        else:
            self._ventana_dialogo(
                leng.tex['err_filas'],
                leng.tex['err_vt_filas']
            )
        # Respuesta de tabla generada ok    
        if res:
            self._ventana_dialogo(
                leng.tex['ok_tabla'],
                leng.tex['vt_ok_tabla'],
                gb.ESTILO_BTN_OK
            )
        else:
            self._ventana_dialogo(
                leng.tex['err_ruta_inesperado'],
                leng.tex['err_vt_ruta_inesperado']
            )
        return res

    def _ventana_dialogo(
        self,
        notificacion,
        titulo_ventana,
        estilo_boton=gb.ESTILO_BTN_NO_OK):
        """
        Produce la ventana de notificación.

        :param notificacion: Mensaje a notificar.
        :type notificacion: str
        :param titulo_ventana: Título de la ventana.
        :type titulo_ventana: str
        :param estilo_boton: Aspecto visual del boton.
        :type estilo_boton: dict
        :return: None
        """        
        self._ventana_error = tk.Toplevel(self.raiz, **gb.ESTILO_MARCO_MOD)
        self._ventana_error.title(titulo_ventana)
        self._ventana_error.minsize(600,100)
        
        self._etiqueta_mensaje = tk.Label(self._ventana_error,
                                  text=notificacion,
                                  **gb.ESTILO_ETIQ)
        
        self._etiqueta_mensaje.config(font=gb.fuente_etiqueta)
        self._etiqueta_mensaje.pack(**gb.PACK_ETI_ERROR)

        self._boton_cerrar = tk.Button(
            self._ventana_error,
            text=leng.tex['btn_vt_cerrar'],
            command=self._ventana_error.destroy,
            **estilo_boton
        )
        self._boton_cerrar.pack(side='top', pady=20)
        self._boton_cerrar.focus_set()

        self._boton_cerrar.bind(
            "<Return>",
            lambda event=None: self._ventana_error.destroy()
        )

