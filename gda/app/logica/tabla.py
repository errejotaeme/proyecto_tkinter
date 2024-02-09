from app.comunes.idioma import leng


class Tabla:
    """
    Clase encargada de almacenar los datos y opciones ingresadas.
    """

    def __init__(self):
        """
        Constructor de la clase Tabla.
        """
        self.gestor = None
        
        self._ruta_salida_csv:str = ""
        self._encabezado_tabla:list = []
        self._delimitador:str = ""
        self._orden:str = ""
        self._criterio:str = ""
        self._modo:str = ""
        self._semilla:str = ""
        self._campos_booleanos:dict = dict()
        self._campos_texto:dict = dict()
        self._campos_enteros:dict = dict()
        self._campos_decimales:dict = dict()

    def enlazar_gestor(self, gestor):
        """
        Almacena la instancia del gestor.
        
        :param gestor: Componente que coordina y comunica los módulos.
        :type gestor: Gestor
        :return: None
        """
        self.gestor = gestor
        
    # Ruta
    def establecer_ruta(self, ruta:str):
        """
        Establece la ruta de salida.

        :param ruta: Ruta de salida.
        :type ruta: str
        :return: None
        """
        self._ruta_salida_csv = ruta

    def obtener_ruta(self) -> str:
        """
        Obtiene y retorna el valor del atributo.

        :return: Valor del atributo.
        """
        return self._ruta_salida_csv

    # Encabezado
    def establecer_encabezado(self, encabezado:list):
        """
        Establece los campos de la tabla.

        :param encabezado: Campos de la tabla.
        :type encabezado: list
        :return: None
        """        
        encabezado = [e for e in encabezado if e != ""]
        self._encabezado_tabla = encabezado

    def obtener_encabezado(self) -> list:
        """
        Ver Tabla.obtener_ruta()
        """
        return self._encabezado_tabla

    def borrar_encabezado(self):
        """
        Vacía el encabezado de la tabla y actualiza la vista

        :return: None
        """
        self._encabezado_tabla = []
        self.gestor.actualizar_vista()

    # Delimitador
    def establecer_delimitador(self, delimitador:str):
        """
        Establece el delimitador de las columnas.

        :param delimitador: Delimitador de la tabla.
        :type delimitador: str
        :return: None
        """
        self._delimitador = delimitador

    def obtener_delimitador(self) -> str:
        """
        Ver Tabla.obtener_ruta()
        """
        return self._delimitador

    # Orden
    def establecer_orden(self, orden:str):
        """
        Establece el orden de la tabla.

        :param orden: Forma de ordenar la tabla.
        :type orden: str
        :return: None
        """
        self._orden = orden

    def obtener_orden(self) -> str:
        """
        Ver Tabla.obtener_ruta()
        """
        return self._orden

    # Criterio
    def establecer_criterio(self, criterio:str):
        """
        Establece el campo de referencia para ordenar la tabla.

        :param criterio: Campo de referencia.
        :type criterio: str
        :return: None
        """
        self._criterio = criterio

    def obtener_criterio(self) -> str:
        """
        Ver Tabla.obtener_ruta()
        """
        return self._criterio

    # Modo
    def establecer_modo(self, modo:str):
        """
        Establece el modo de aleatoriedad.

        :param modo: Librería a utilizar.
        :type modo: str
        :return: None
        """
        self._modo = modo

    def obtener_modo(self) -> str:
        """
        Ver Tabla.obtener_ruta()
        """
        return self._modo

    # Semilla
    def establecer_semilla(self, semilla:str):
        """
        Establece el estado incial para 'random'.

        :param semilla: Valor de 'seed'.
        :type semilla: str
        :return: None
        """
        self._semilla = semilla

    def obtener_semilla(self) -> str:
        """
        Ver Tabla.obtener_ruta()
        """
        return self._semilla

    # Campos booleanos
    def establecer_campo_booleano(self, nombre_campo:str, valores_bool:str):
        """
        Establece un campo como booleano.

        :param nombre_campo: Nombre del campo.
        :type nombre_campo: str
        :param valores_bool: Posibles valores (True, False, None).
        :type valores_bool: str
        :return: None
        """
        self._campos_booleanos[nombre_campo] = valores_bool

    def borrar_campo_booleano(self, nombre_campo:str):
        """
        Si está registrado en la tabla, elimina el campo recibido y
        actualiza la vista.

        :param nombre_campo: Nombre del campo recibido.
        :type nombre_campo: str
        :return: None        
        """
        self._campos_booleanos.pop(nombre_campo, None)
        self.gestor.actualizar_vista()

    def obtener_campos_booleanos(self) -> dict:
        """
        Ver Tabla.obtener_ruta()
        """
        return self._campos_booleanos

    # Campos de texto
    def establecer_campo_texto(self, nombre_campo:str, valores:list):
        """
        Establece un campo como de texto.

        :param nombre_campo: Nombre del campo.
        :type nombre_campo: str
        :param valores: Alternativas de texto para el campo.
        :type valores: list
        :return: None
        """
        self._campos_texto[nombre_campo] = valores

    def borrar_campo_texto(self, nombre_campo:str):
        """
        Ver Tabla.borrar_campo_booleano()
        """
        self._campos_texto.pop(nombre_campo, None)
        self.gestor.actualizar_vista()

    def obtener_campos_texto(self) -> dict:
        """
        Ver Tabla.obtener_ruta()
        """
        return self._campos_texto

    # Campos enteros
    def establecer_campo_entero(self, campo:str, rango:tuple):
        """
        Establece un campo como de enteros.

        :param campo: Nombre del campo.
        :type campo: str
        :param rango: Rango de posibles valores.
        :type rango: tuple
        :return: None
        """
        self._campos_enteros[campo] = rango

    def borrar_campo_entero(self, campo:str):
        """
        Ver Tabla.borrar_campo_booleano()
        """
        self._campos_enteros.pop(campo, None)
        self.gestor.actualizar_vista()

    def obtener_campos_enteros(self) -> dict:
        """
        Ver Tabla.obtener_ruta()
        """
        return self._campos_enteros

    # Campos decimales
    def establecer_campo_decimal(self, campo:str, rango:tuple):
        """
        Establece un campo como de decimales.

        :param campo: Nombre del campo.
        :type campo: str
        :param rango: Rango de posibles valores.
        :type rango: tuple
        :return: None
        """
        self._campos_decimales[campo] = rango

    def borrar_campo_real(self, campo:str):
        """
        Ver Tabla.borrar_campo_booleano()
        """
        self._campos_decimales.pop(campo, None)
        self.gestor.actualizar_vista()

    def borrar_campos_decimales(self):
        """
        Elimina los campos definidos como decimales cuando se elige
        el modo de aleatoriedad 'secrets'.

        :return: None
        """
        self._campos_decimales.clear()

    def obtener_campos_decimales(self) -> dict:
        """
        Ver Tabla.obtener_ruta()
        """
        return self._campos_decimales


    # Métodos generales
    def campos_definidos(self) -> list:
        """
        Retorna una lista con los campos definidos.

        :return: Lista con los campos definidos.
        :rtype: list
        """
        lista_aux:list = list(self._campos_booleanos.keys())
        lista_aux += list(self._campos_texto.keys())
        lista_aux += list(self._campos_enteros.keys())
        lista_aux += list(self._campos_decimales.keys())
        return lista_aux

    def borrar_todos_los_campos(self):
        """
        Elimina todos los campos registrados en la tabla y actualiza la vista.

        :return: None
        """
        self._campos_booleanos.clear()
        self._campos_texto.clear()
        self._campos_enteros.clear()
        self._campos_decimales.clear()
        self._criterio:str = ""
        self.gestor.actualizar_vista()

    def obtener_datos(self) -> list:
        """
        Produce y retorna una lista con todos los datos ingresados
        praparados para que se puedan insertar en la vista.

        :return: Lista con los datos.
        :rtype: list
        """
        l_aux:list = []
        l_aux.append(leng.tex['ruta_clave'])
        l_aux.append(f'{self.obtener_ruta()}\n')
        l_aux.append(leng.tex['encabezado_clave'])
        l_aux.append(f'{self.obtener_encabezado()}\n')
        l_aux.append(leng.tex['delimitador_clave'])
        l_aux.append(f'"{self.obtener_delimitador()}"\n')
        l_aux.append(leng.tex['orden_clave'])
        l_aux.append(f'{self.obtener_orden()}\n')
        l_aux.append(leng.tex['criterio_campo'])
        l_aux.append(f'{self.obtener_criterio()}\n')
        l_aux.append(leng.tex['clave_modo'])
        l_aux.append(f'{self.obtener_modo()}\n')
        l_aux.append(leng.tex['clave_semilla'])
        l_aux.append(f'"{self.obtener_semilla()}"\n')
        l_aux.append(leng.tex['clave_bool'])
        l_aux.append(f'{self.obtener_campos_booleanos()}\n')
        l_aux.append(leng.tex['clave_tex'])
        l_aux.append(f'{self.obtener_campos_texto()}\n')
        l_aux.append(leng.tex['clave_int'])
        l_aux.append(f'{self.obtener_campos_enteros()}\n')
        l_aux.append(leng.tex['clave_float'])
        l_aux.append(f'{self.obtener_campos_decimales()}\n')
        return l_aux

    def restablecer_tabla(self):
        """
        Vacía todos los datos registrados y actualiza la vista.

        :return: None
        """
        self._ruta_salida_csv = ""
        self._encabezado_tabla = []
        self._delimitador = ""
        self._orden = ""
        self._criterio = ""
        self._modo = ""
        self._semilla = ""
        self._campos_booleanos.clear()
        self._campos_texto.clear()
        self._campos_enteros.clear()
        self._campos_decimales.clear()
        self.gestor.actualizar_vista()
        
