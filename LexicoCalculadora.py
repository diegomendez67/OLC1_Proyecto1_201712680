import re
texto=""
confirmacion =[]
error = ""
token = []
parent = ""
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


    def analizador(entrada):

        global texto, confirmacion, error, token, parent
        entrada = entrada+ "\n "
        lexema = ""
        columna = 1
        fila = 1
        estado = 0
        i = 0
        id = 1
        idE = 1

        while i <len(entrada):

            char = entrada[i]
            if estado is 0:
                # print("entro a 0")
                if char == '(':
                    estado = 0
                    confirmacion.append([columna, fila, 'PARA', char])
                    columna += 1
                elif char == ')':
                    estado = 0
                    confirmacion.append([columna, fila, 'PARC', char])
                    columna+=1
                elif char == '-':
                    estado = 0
                    confirmacion.append([columna, fila, 'MEN', char])
                    columna+=1
                elif char == '+':
                    estado = 0
                    confirmacion.append([columna, fila, 'MAS', char])
                    columna+=1
                elif char == '/':
                    estado = 0
                    confirmacion.append([columna, fila, 'DIV', char])
                    columna+=1
                elif char == '*':
                    estado = 0
                    confirmacion.append([columna, fila, 'POR', char])
                    columna+=1
                elif char.isdigit():
                    estado  = 1
                    lexema+=char
                elif analizadorCalculadora.leerLetras(char):
                    estado = 2
                    lexema+=char
                elif char == '\t' or char ==' ':
                    estado = 0
                    columna+=1
                elif char == '\n':
                    estado = 0
                    expresion = ""
                    for tokens in confirmacion:
                        expresion += str(tokens[3])
                    parser = Sintactico
                    if len(confirmacion) != 0:
                        parseoCorrecto = parser.parse(confirmacion)
                        if parseoCorrecto:
                            print("Analisis Sintactico Correcto.")
                            token.append([idE,fila,expresion,"True"])
                        else:
                            token.append([idE,fila,expresion,"False"])
                    confirmacion = []
                    id = 1
                    fila += 1
                    idE += 1
                #agregar parse aqui

                else:
                    error.append([idE,lexema,fila, columna])
                    idE+=1
            elif estado is 1:
                if char.isdigit():
                    lexema+=char
                    estado = 1
                elif char =='.':
                    lexema+=char
                    estado = 3
                else:
                    confirmacion.append([columna, fila, 'NUMERIC', lexema])
                    columna+=1
                    estado = 0
                    lexema=""
                    i-=1
            elif estado is 2:
                if char.isdigit() or analizadorCalculadora.leerLetras(char):
                    lexema+=char
                    estado = 2
                else:
                    confirmacion.append([columna, fila, 'ID', lexema])
                    columna+=1
                    estado = 0
                    lexema=""
                    i-=1
            elif estado is 3:
                if char.isdigit():
                    lexema += char
                    estado = 1
                else:
                    confirmacion.append([columna, fila, 'NUMERIC', lexema])
                    columna += 1
                    estado = 0
                    lexema = ""
                    i -= 1






            i+= 1



