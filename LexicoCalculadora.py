import re
linea = 0
columna = 0
contador = 0
Error = []
Tokens= []
Entrada_Corregida =''
consola =''
retorno =''
from SintacticoCalculadora import Sintactico
class analizadorCalculadora:
    # variable para control de estados
    estado = 0

    # variables para contadores de tokens

    def leerLetras(char):
        x = ord(char)
        if (x >= 65 and x <= 90) or (x >= 97 and x <= 122):
            return True
        else:
            return False

    def consola():
        global consola
        return consola

    def analizador(texto):
        global linea, columna, counter, Errores, Entrada_Corregida, Error, consola, retorno
        listaTokens = []
        entrada = texto
        lexema = ""
        consola = ""
        Entrada_Corregida = ""
        columna = 1
        fila = 1
        estado = 0
        i = 0
        portador = 0


        while i < len(entrada):
            if estado is 0:
                if entrada[i] is '(':
                    estado = 0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    listaTokens.append(['PARENTESIS ABIERTO',   entrada[i], fila, columna])
                    columna+=1
                elif entrada[i] is ')':
                    estado = 0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    listaTokens.append(['PARENTESIS CERRADO',   entrada[i], fila, columna])
                    columna+=1
                elif entrada[i] is '-':
                    estado = 0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    listaTokens.append(['SIGNO MENOS',   entrada[i], fila, columna])
                    columna+=1
                elif entrada[i] is '+':
                    estado = 0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    listaTokens.append(['SIGNO MAS',   entrada[i], fila, columna])
                    columna+=1
                elif entrada[i] is '*':
                    estado = 0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    listaTokens.append(['SIGNO MULTIPLICACION',   entrada[i], fila, columna])
                    columna+=1
                elif entrada[i] is '/':
                    estado = 0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    listaTokens.append(['SIGNO DIVISION',   entrada[i], fila, columna])
                    columna+=1
                elif entrada.isdigit():
                    estado  = 1
                    lexema+=char
                elif analizadorCalculadora.leerLetras(entrada[i]):
                    estado = 2
                    lexema= lexema + entrada[i]
                elif entrada[i] == '\t' or entrada[i] ==' ':
                    estado = 0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    columna+=1
                elif entrada[i] =='\n':
                    estado = 0
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    OperacionCompleta=""

                    for token in listaTokens:
                        OperacionCompleta += str(token[0])
                    #comienza analisis con lookahead
                    if len(listaTokens)!=0:
                        
                         
                        if Sintactico.parser(listaTokens):
                            print("ANALISIS SINTACTICO CORRECTO")
                            Tokens.append([portador,fila,OperacionCompleta,"TRUE"])
                        else:
                            Tokens.append([portador, fila, OperacionCompleta, "TRUE"])
                        OperacionCompleta = ""
                        listaTokens = []
                        id=1
                        fila += 1
                        portador += 1

                    '''
                        aca vamos a poner el analizador sintacitco como llamada
                    '''
                else:
                    portador += 1
                    Error.append([lexema,fila,columna])

            elif estado is 1:
                if entrada[i].isdigit():
                    estado = 1
                    lexema= lexema + entrada[i]
                elif entrada[i] is '.':
                    estado = 3
                    lexema = lexema + entrada[i]
                else:
                    estado = 0
                    listaTokens.append(['NUMERO', lexema, fila, columna])
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    columna += 1
                    lexema = ""
                    i -= 1
            elif estado is 2:
                if entrada[i].isdigit() or analizadorCalculadora.leerLetras(entrada[i]):
                    estado = 2
                    lexema = lexema + entrada[i]
                else:
                    columna+=1
                    estado = 0
                    i-=1
                    listaTokens.append(['IDENTIFICADOR',lexema,fila,columna])
                    lexema =''
            elif estado is 3:
                if entrada[i].isdigit():
                    estado = 1
                    lexema+=char
                else:
                    columna +=1
                    estado = 0
                    lexema = ''
                    i-=1
                    listaTokens.append(['NUMERO', lexema, fila, columna])

            i+= 1



