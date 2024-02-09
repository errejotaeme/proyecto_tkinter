import csv
import random
import secrets
import os
from pathlib import Path
from app.comunes.idioma import leng


class Generador:
    """
    Clase encargada de producir y exportar la tabla.
    """    
    _ruta_salida_csv:str = ""
    _encabezado_tabla = []
    _delimitador:str = ""
    _orden:str = ""
    _criterio:str = ""
    _modo:str = ""
    _semilla:str = ""
    _campos_booleanos:dict = dict()
    _campos_texto:dict = dict()
    _campos_enteros:dict = dict()
    _campos_decimales:dict = dict()
    _filas:int= 0

    def __init__(self):
        """
        Constructor de la clase Generador.
        """
        pass

    def crear_tabla(self, datos:dict) -> bool:
        """
        Procesa los datos de la tabla utilizando el método correspondiente
        según el tipo de orden.
        
        :param datos: Datos regitrados en la tabla.
        :type datos: dict
        :return res: True si la operación fue exitosa, de lo contrario False.
        :rtype res: bool
        """
        res:bool = False
        registros:list = []
        # Registra los valores de la tabla en las variables de clase
        for clave, valor in datos.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)                
        orden:str = self._orden
        if orden == leng.tex['orden_opc_2'] or "pandas" in orden: 
            res = self._registros_incremental() # Ninguno, pandas
        else: 
            registros:list = self._registros_no_incremental() # Ascendente, Descendente
            # Escribe los registros en la ruta de salida.
            res = self._grabar_datos(registros) 
        return res


    def _registros_no_incremental(self) -> list:
        """
        Produce y retorna un lista de registros en el orden indicado,
        que luego se exporta en bloque en la ruta de salida.
        Se ordena con este método cuando no está instalada la librería 'pandas'.
        Genera los datos por columna y después los transpone.
        Las tablas con orden 'Asecendente' o 'Descendente' se producen con este método.

        :return: Lista de listas con los registros ordenados.
        :rtype: list 
        """        
        modo:str = self._modo
        # Estado inicial para random
        if self._semilla == leng.tex['semilla_def']:
            random.seed()
        else:
            random.seed(self._semilla)           

        # Crea los registros     
        filas:int = self._filas
        booleanos = [True,False,"None"]
        registros_transpuestos:list = []
        for campo in self._encabezado_tabla:
            columna:list = []

            # Booleanos
            if campo in self._campos_booleanos:
                if self._campos_booleanos[campo] == "True, False":
                    if modo == "random":
                        for _ in range(filas):
                            columna.append(booleanos[random.randint(0, 1)])
                        registros_transpuestos.append(columna)
                    else: # secrets
                        for _ in range(filas):
                            columna.append(booleanos[secrets.randbelow(2)])
                        registros_transpuestos.append(columna)
                else:
                    if modo == "random":
                        for _ in range(filas):
                            columna.append(booleanos[random.randint(0, 2)])
                        registros_transpuestos.append(columna)
                    else: # secrets
                        for _ in range(filas):
                            columna.append(booleanos[secrets.randbelow(3)])
                        registros_transpuestos.append(columna)                       

            # Texto
            elif campo in self._campos_texto:
                vars_texto:list = self._campos_texto[campo]
                n_items = len(vars_texto)
                if modo == "random":
                    for _ in range(filas):
                        columna.append(vars_texto[random.randint(0, n_items - 1)])
                    registros_transpuestos.append(columna)
                else: # secrets
                    for _ in range(filas):
                        columna.append(vars_texto[secrets.randbelow(n_items)])
                    registros_transpuestos.append(columna)                 

            # Enteros
            elif campo in self._campos_enteros:
                rango = self._campos_enteros[campo]
                if modo == "random":
                    for _ in range(filas):
                        columna.append(random.randint(rango[0], rango[1]))
                    registros_transpuestos.append(columna)
                else: # secrets
                    intervalo:int = rango[1] - rango[0] + 1
                    piso:int = rango[0] 
                    for _ in range(filas):
                        columna.append(secrets.randbelow(intervalo) + piso)
                    registros_transpuestos.append(columna)                  

            # Decimales
            elif campo in self._campos_decimales:
                if modo == "random":
                    rango = self._campos_decimales[campo]
                    redondeo = rango[2]
                    for _ in range(filas):
                        columna.append(
                            round(random.uniform(rango[0], rango[1]),
                                  redondeo
                            )
                        )
                    registros_transpuestos.append(columna)
                else: # secrets
                    for _ in range(filas):
                        columna.append("")
                    registros_transpuestos.append(columna)                    

            # Campos sin definir    
            else:
                for _ in range(filas):
                    columna.append("")
                registros_transpuestos.append(columna)

        # Transpone la lista de listas para darle formato de tabla        
        registros = list(zip(*registros_transpuestos))

        # Aplica el orden definido
        indice:int = self._encabezado_tabla.index(self._criterio)
        if self._orden == leng.tex['orden_opc_0']: # Ascendente
            registros = sorted(registros, key=lambda x: x[indice])
        elif self._orden == leng.tex['orden_opc_1']: # Descendente
            registros = sorted(registros, key=lambda x: x[indice], reverse=True)
        return registros


    def _registros_incremental(self) -> bool:
        """
        Produce y exporta un lista de registros en el orden indicado.
        Se ordena con este método cuando está instalada la librería 'pandas'.
        Genera los datos por fila y los escribe en el archivo de salida con el
        método writerow a medida que son creados. Luego los ordena si es necesario.
        Las tablas con orden 'Ninguno' o '(...) - pandas' se producen con este método.
        """      
        res: bool = False
        modo:str = self._modo
        with open(
            self._ruta_salida_csv,
            "w", newline="",
            encoding="utf-8") as archivo:
            
            tabla_final = csv.writer(archivo, delimiter=self._delimitador)
            tabla_final.writerow(self._encabezado_tabla)          

            # Estado inicial para random
            if self._semilla == leng.tex['semilla_def']:
                random.seed()
            else:
                random.seed(self._semilla)            

            # Crea los registros
            filas:int = self._filas
            booleanos = [True,False,"None"]
            for i in range(filas):
                registro:list = []
                for campo in self._encabezado_tabla:     

                    # Booleanos
                    if campo in self._campos_booleanos:
                        if self._campos_booleanos[campo] == "True, False":
                            if modo == "random":
                                registro.append(booleanos[random.randint(0, 1)])
                            else: # secrets
                                registro.append(booleanos[secrets.randbelow(2)])
                        else:
                            if modo == "random":
                                registro.append(booleanos[random.randint(0, 2)])
                            else: # secrets
                                registro.append(booleanos[secrets.randbelow(3)])              

                    # Texto
                    elif campo in self._campos_texto:
                        vars_texto:list = self._campos_texto[campo]
                        n_items = len(vars_texto)
                        if modo == "random":
                            registro.append(vars_texto[random.randint(0, n_items-1)])
                        else: # secrets
                            registro.append(vars_texto[secrets.randbelow(n_items)])            

                    # Enteros
                    elif campo in self._campos_enteros:
                        rango = self._campos_enteros[campo]
                        if modo == "random":
                            registro.append(random.randint(rango[0], rango[1]))
                        else: # secrets
                            intervalo:int = rango[1] - rango[0] + 1
                            piso:int = rango[0]
                            registro.append(secrets.randbelow(intervalo) + piso)        

                    # Decimales
                    elif campo in self._campos_decimales:
                        if modo == "random":
                            rango = self._campos_decimales[campo]
                            redondeo = rango[2]
                            registro.append(
                                round(random.uniform(rango[0], rango[1]),
                                      redondeo
                                )
                            )
                        else: # secrets
                            registro.append("")

                    # Campos sin definir    
                    else:                        
                        registro.append("")
                tabla_final.writerow(registro) 

        # Ordena si corresponde
        if self._orden != leng.tex['orden_opc_2']: # Ninguno
            import pandas as pd
            orden:str = str(self._orden)
            criterio:str = str(self._criterio)
            nueva_ruta:str = f"{str(self._ruta_salida_csv)[:-4]}"
            nueva_ruta += f"_{orden[:-9]}.csv"           

            # Lee el archivo generado y lo ordena
            tabla = pd.read_csv(self._ruta_salida_csv)          
            if orden == leng.tex['orden_opc_3']: # Ascendente
                tabla_ordenada = tabla.sort_values(by=criterio)
            elif orden == leng.tex['orden_opc_4']: # Descendente
                tabla_ordenada = tabla.sort_values(by=criterio, ascending=False)
            else:
                res = False  
            tabla_ordenada.to_csv(nueva_ruta, index=False)
            os.remove(self._ruta_salida_csv)
            res = True

        else: # Ninguno
            res = True
        return res

    
    def _grabar_datos(self, registros:list) -> bool:
        """
        Utiliza el método writerows para escribir todos los registros
        simultáneamente como un bloque en el archivo de salida.
        Es auxiliar al método no incremental.

        :param registros: Lista de listas con los registros.
        :type registros: list
        :return res: True si la operación fue exitosa, de lo contrario False
        :rtype res: bool        
        """
        res:bool = False
        try:
            with open(
                self._ruta_salida_csv,
                "w",
                newline="",
                encoding="utf-8") as archivo:
                
                tabla_final = csv.writer(archivo, delimiter=self._delimitador)
                tabla_final.writerow(self._encabezado_tabla)
                tabla_final.writerows(registros)
                res = True
        except:
            res = False
        return res
