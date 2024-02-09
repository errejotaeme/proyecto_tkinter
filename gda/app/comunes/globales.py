class Globales:
    """
    Clase encargada de contener variables y constantes globales.
    """
    
    # Diccionarios que definen la organización espacial.
    PACK_MARCO_MODULO:dict = {
        'side' : 'top',        # Ubicación
        'fill' : 'x',          # Expansión horizontal
        'anchor' : 'n',        # Anclaje
        'expand' : False,      # Habilita la expensaión
        'padx' : 2,            # Relleno horizontal
        'pady' : 2             # Relleno Vertical
    }
    PACK_MARCO_ENT:dict = {
        'side' : 'left',
        'anchor' : 'w',
        'fill' : 'x',
        'expand' : True,
        'padx' : 5,
        'pady' : 10
    }
    PACK_MARCO_ENT_BOOL:dict = {
        'side' : 'right',
        'anchor' : 'w',
        'expand' : False,
        'padx' : 5,
        'pady' : 10
    }
    PACK_MARCO_BTN:dict = {
        'side' : 'right',
        'fill' : 'both',
        'expand' : False,
        'padx' : 5,
        'pady' : 5
    }
    PACK_ETIQ_ENT:dict = {
        'side' : 'top',
        'anchor' : 'n',
        'expand' : True,
        'padx' : 5,
        'pady' : 2
    }
    PACK_ETIQ_ENT_FILA:dict = {
        'side' : 'top',
        'anchor' : 'ne',
        'padx' : 25,
        'pady' : 5
    }
    PACK_ETIQ_APP:dict = {
        'side' : 'bottom',
        'anchor' : 's',
        'expand' : False,
        'padx' : 5,
        'pady' : 12
    }
    PACK_ETI_ERROR:dict = {
        'side' : 'top',
        'anchor' : 's',
        'fill' : 'x',
        'expand' : True,
        'padx' : 5,
        'pady' : 30
    }
    PACK_ENT_TEX:dict = {
        'side' : 'top',
        'fill' : 'x',
        'expand' : True,
        'pady' : 2,
        'ipady' : 3
    }
    PACK_ENT_TEX_FILA:dict = {
        'side' : 'top',
        'anchor' : 'ne',
        'expand' : False,
        'pady' : 2,
        'padx' : 2,
        'ipadx' : 10,
        'ipady' : 3
    }
    PACK_ENT_OPC:dict = {
        'side' : 'bottom',
        'anchor' : 's',
        'expand' : False
    }
    PACK_BTN:dict = {
        'side' : 'left',
        'anchor' : 's',
        'padx' : 5,
        'pady' : 5
    }
    PACK_BTN_SALIR:dict = {
        'side' : 'right',
        'anchor' : 's',
        'padx' : 5,
        'pady' : 5
    }
    
    # Diccionarios que defienen el aspecto visual.
    ESTILO_MARCO_MOD:dict = {
        'background' : '#0d0d0d'           # color predominante
    }   
    ESTILO_TX_VISTA:dict = {
        'background' : '#272727',          # color vista de datos
        'highlightthickness': 2,
        'highlightbackground' : '#0d0d0d', # color predominante
        'highlightcolor' : '#08d698',
    }
    ESTILO_TX_ENTRADA:dict = {
        'background' : '#272727',   
        'foreground' : '#08d698',   # texto de los datos ingresados tabla
        'bd' : 0,
        'highlightthickness': 1,
        'highlightbackground' : '#0d0d0d', # color predominante
        'highlightcolor' : '#a5a5a5',
    }

    ESTILO_TX_CLAVE:dict = {        # texto de la aplicación en vista
        'foreground' : "#e7e7eb",
        'font' : "Monospace 8 bold"
    }
    ESTILO_TX_VALOR:dict = {        # texto de los datos ingresados en vista
        'foreground' : '#08d698',
        'font' : 'Monospace 8 normal italic'
    }
    ESTILO_BTN_OK:dict = {
        'background' : '#06b180',
        'activebackground' : '#01120d',
        'activeforeground' : '#06b180',
        'bd' : 2,
        'highlightthickness': 2,
        'highlightbackground' : '#0d0d0d', # color predominante
        'highlightcolor' : '#08d698',
        'height' : 1
    }
    ESTILO_BTN_OPC:dict = {
        'background' : '#7306b1',
        'activebackground' : '#08000c',
        'activeforeground' : '#7306b1',
        'bd' : 2,
        'highlightthickness': 0,
        'height' : 1,
        'width' : 13
    }
    ESTILO_BTN_LENG:dict = {
        'background' : '#0800ff',
        'activebackground' : '#00000c',
        'activeforeground' : '#0800ff',
        'bd' : 2,
        'highlightthickness': 2,
        'highlightbackground' : '#0d0d0d', # color predominante
        'highlightcolor' : '#0703ff',
        'height' : 1
    }
    ESTILO_BTN_SALIR:dict = {
        'background' : '#dda823',
        'activebackground' : '#0b0802',
        'activeforeground' : '#dda823',
        'bd' : 2,
        'highlightthickness': 2,
        'highlightbackground' : '#0d0d0d', # color predominante
        'highlightcolor' : '#ffbf28',
        'height' : 1,
        'width' : 5
    }
    ESTILO_BTN_NO_OK:dict = {
        'background' : '#d52b2b',
        'activebackground' : '#100303',
        'activeforeground' : '#d52b2b',
        'bd' : 2,
        'highlightthickness': 2,
        'highlightbackground' : '#0d0d0d', # color predominante
        'highlightcolor' : '#ff3333',
    }
    ESTILO_ALERT:dict = {
        'background' : '#dda823',
        'activebackground' : '#0b0802',
        'activeforeground' : '#dda823',
        'bd' : 2,
        'highlightthickness': 0,
        'highlightbackground' : '#0d0d0d', # color predominante
        'highlightcolor' : '#ffbf28',
        'width' : 15
    }
    ESTILO_ETIQ:dict = {
        'background' : '#0d0d0d',
        'foreground' : '#e7e7eb'  # texto de etiquetas
    }
    ESTILO_ETIQ_TITULO:dict = {
        'background' : '#d9d9d9',
        'foreground' : '#0d0d0d' # texto de etiquetas (color predominante)
    }

    # Formatos de fuente (serán instancias de tk.Font)
    fuente_principal = None
    fuente_titulo = None
    fuente_etiqueta = None
    fuente_entrada = None
    fuente_boton = None
    fuente_boton_salir = None
 

gb = Globales()
