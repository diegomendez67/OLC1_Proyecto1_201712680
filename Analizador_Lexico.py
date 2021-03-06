'''
EXPRESIONES REGULARES PARA IMPLEMENTACIÓN DE ANÁLISIS LÉXICO
'''


import re
linea = 0
columna = 0
counter = 0
Errores = []
reservadas = ['int', 'String', 'Char', 'Boolean','Type','if','console','log', 'else','var']
signos = {"PUNTO Y COMA": ';', "LLAVE ABIERTA": '{', "LLAVE CERRADA": '}', "PARENTESIS ABIERTO": '\(', "PARENTESIS CERRADO": '\)', "IGUAL": '=', "DIAGONAL": '/', "MENOR O IGUAL": '=', "MENOR QUE": '<',"MAYOR QUE": '>', "PUNTO": '.', "COMA": ',',"COMILLAS": '/"'}
class analizador:

    def inic(text):
        global linea, columna, counter, Errores
        linea = 1
        columna = 1
        listaTokens = []

        while counter < len(text):
            if re.search(r"[A-Za-z]", text[counter]):  # IDENTIFICADOR
                listaTokens.append(analizador.StateIdentifier(linea, columna, text, text[counter]))
            elif re.search(r"[0-9]", text[counter]):  # NUMERO
                listaTokens.append(analizador.StateNumber(linea, columna, text, text[counter]))
            elif re.search(r"[\n]", text[counter]):  # SALTO DE LINEA
                counter += 1
                linea += 1
                columna = 1
            elif re.search(r"[ \t]", text[counter]):  # ESPACIOS Y TABULACIONES
                counter += 1
                columna += 1
            else:
                # SIGNOS
                isSign = False
                for clave in signos:
                    valor = signos[clave]
                    if re.search(valor, text[counter]):
                        listaTokens.append([linea, columna, clave, valor.replace('\\', '')])
                        counter += 1
                        columna += 1
                        isSign = True
                        break
                if not isSign:
                    columna += 1
                    Errores.append([linea, columna, text[counter]])
                    counter += 1
        return listaTokens

    # [linea, columna, tipo, valor]

    def StateIdentifier(line, column, text, word):
        global counter, columna
        counter += 1
        columna += 1
        if counter < len(text):
            if re.search(r"[a-zA-Z_0-9]",text[counter]):  # IDENTIFICADOR
                return analizador.StateIdentifier(line, column, text, word + text[counter])
            else:
                return [line, column, 'identificador', word]
                # agregar automata de identificador en el arbol, con el valor
        else:
            return [line, column, 'identificador', word]

    def StateNumber(line, column, text, word):
        global counter, columna
        counter += 1
        columna += 1
        if counter < len(text):
            if re.search(r"[0-9]", text[counter]):  # ENTERO
                return analizador.StateNumber(line, column, text, word + text[counter])
            elif re.search(r"\.", text[counter]):  # DECIMAL
                return analizador.StateDecimal(line, column, text, word + text[counter])
            else:
                return [line, column, 'integer', word]
                # agregar automata de numero en el arbol, con el valor
        else:
            return [line, column, 'integer', word]

    def StateDecimal(line, column, text, word):
        global counter, columna
        counter += 1
        columna += 1
        if counter < len(text):
            if re.search(r"[0-9]", text[counter]):  # DECIMAL
                return analizador.StateDecimal(line, column, text, word + text[counter])
            else:
                return [line, column, 'decimal', word]
                # agregar automata de decimal en el arbol, con el valor
        else:
            return [line, column, 'decimal', word]

    def Reserved(TokenList):
        for token in TokenList:
            if token[2] == 'identificador':
                for reservada in reservadas:
                    palabra = r"^" + reservada + "$"
                    if re.match(palabra, token[3], re.IGNORECASE):
                        token[2] = 'reservada'
                        break

    def my_function(fname):
        print(fname)
        tokens = analizador.inic(fname)
        analizador.Reserved(tokens)
        for token in tokens:
            print(token)

        print('ERRORES')
        for error in Errores:
            print(error)



