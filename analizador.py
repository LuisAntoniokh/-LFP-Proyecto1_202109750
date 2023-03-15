from Instrucciones.aritmeticas import *
from Instrucciones.trigonometricas import *
from Abstracto.lexema import *
from Abstracto.numeros import *
#Patron: forma que se entregaba
#Lexema: dato que ingresa.
#Token: nombre que se le asigna al lexema

#Todos los valores de las palabras reservadas, es todo el Lexico, si no esta
#algo es un error Lexico
palabras_reservadas = {
    'Reser_OPERACION':      'Operacion',
    'Reser_Valor1':         'Valor1',
    'Reser_Valor2':         'Valor2'   ,
    'Reser_Suma':           'Suma',
    'Reser_Resta':          'Resta',
    'Reser_Multiplicacion': 'Multiplicacion',
    'Reser_Division':       'Division',
    'Reser_Potencia':       'Potencia',
    'Reser_Raiz':           'Raiz',
    'Reser_Inverso':        'Inverso',
    'Reser_Seno':           'Seno',
    'Reser_Coseno':         'Coseno',
    'Reser_Tangente':       'Tangente',
    'Reser_Modulo':         'Mod',  
    'Reser_Texto':          'Texto',
    'Reser_ColFondoNodo':   'Color-Fondo-Nodo',
    'Reser_ColFuenteNodo':  'Color-Fuente-Nodo',
    'Reser_NodeShape':      'Forma-Nodo',
    'Coma':                 ',',
    'Punto':                '.',
    'DosPuntos':            ':',
    'CorcheteIzquierdo':    '[',
    'CorcheteDerecho':      ']',
    'LlaveIzquierda':       '{',
    'LlaveDerecha':         '}',
}

#Contiene la lista de las palabras reservadas
lexemas = list(palabras_reservadas.values())

global  n_linea
global  n_columna
global  instrucciones
global  lista_lexemas

n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []

def instruccion(cadena):
    global  n_linea
    global  n_columna
    global  lista_lexemas

    lexema = ''
    pointer = 0

    while cadena:
        char = cadena[pointer]
        pointer += 1

        if char == '\"':
            lexema, cadena = armar_lexema(cadena[pointer:])
            if lexema and cadena:
                n_columna +=1
                #Lexema como clase
                l = Lexema(lexema, n_linea, n_columna)
                #Lexema a la lista de lexemaslista_lexemas.append(lexema)
                lista_lexemas.append(l)
                n_columna += len(lexema)+1
                pointer = 0

        elif char.isdigit():
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n_columna +=1
                #Lexema como clase
                n = Numero(token, n_linea, n_columna) 
                #Lexema a la lista de lexemaslista_lexemas.append(lexema)
                lista_lexemas.append(n)
                n_columna += len(str(token)) +1
                pointer = 0

        elif char == '[' or char == ']':
            #Lexema como clase
            c = Lexema(char, n_linea, n_columna)
            #Lexema a la lista de lexemas
            lista_lexemas.append(c)
            cadena = cadena[1:]
            pointer = 0
            n_columna +=1

        elif char == '\t':
            n_columna +=4
            cadena = cadena[4:]
            pointer = 0

        elif char == '\n':
            cadena = cadena[1:]
            pointer = 0
            n_linea += 1
            n_columna = 1
        
        else:
            cadena = cadena[1:]
            pointer = 0
            n_columna += 1
    
    for lexema in lista_lexemas:
        print(lexema)

    #return lista_lexemas

def armar_lexema(cadena):
    global  n_linea
    global  n_columna
    global  lista_lexemas

    lexema = ''
    pointer = ''

    for char in cadena:
        pointer += char
        if char == '\"':
            return lexema, cadena[len(pointer):]
        else:
            lexema += char
    return None, None

def armar_numero(cadena):
    numero = ''
    pointer = ''
    is_decimal = False

    for char in cadena:
        pointer += char
        if char == '.':
            is_decimal = True
        if char == '"' or char == ' ' or char == '\n' or char == '\t':
            if is_decimal:
                return float(numero), cadena[len(pointer)-1:]
            else:
                return int(numero), cadena[len(pointer)-1:]
        else:
            numero += char
    return None, None

def operar():
    global  instrucciones
    global  lista_lexemas

    operacion = ''
    n1 = ''
    n2 = ''

    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        if lexema.operar(None) == 'Operacion':
            operacion = lista_lexemas.pop(0)
        elif lexema.operar(None) == 'Valor1':
            n1 = lista_lexemas.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()
        elif lexema.operar(None) == 'Valor2':
            n2 = lista_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()
        
        if operacion and n1 and n2:
            return Aritmetica(n1, n2, operacion,
                              f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', 
                              f'Fin: {n2.getFila()}:{n2.getColumna()}')
        
        elif operacion and n1 and operacion.operar(None) == ('Seno' or 'Coseno' or 'Tangente'):
            return Trigonometricas(n1, operacion, 
                                   f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', 
                                   f'Fin: {n1.getFila()}:{n1.getColumna()}')
    return None

def operar_():
    global instrucciones
    while True:
        operacion = operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break

    for instruccion in instrucciones:
        print(instruccion.operar(None))

    return instrucciones

entrada= '''{
	{
        "Operacion":"Suma"
		"Valor1" : 4.5
		"Valor2" : 5.32
	},
	{
		"Operacion":"Resta"
		"Valor1":4.5
		"Valor2": [
			"Operacion":"Potencia"
			"Valor1":10
			"Valor2":3
	]},
	{
		"Operacion":"Suma"
		"Valor1":[
			"Operacion":"Seno"
			"Valor1":90
	]
		"Valor2":5.32
	}

	"Texto":"Realizacion de Operaciones"
	"Color-Fondo-Nodo":"Amarillo"
	"Color-Fuente-Nodo":"Rojo"
	"Forma-Nodo":"Circulo"
}'''

instruccion(entrada)
operar_()