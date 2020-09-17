import re
linea = 0
columna = 0
contador = 0
Error = []
reservadas = ["color","background-color","background-image","border","border-top","content","Opacity","background","text-align","margin-top","font-family","font-style","font-weight","font-size","font","padding-left","padding-right","padding-bottom","padding-topp","padding","display","line-height","width","height","margin-top","margin-right","margin-bottom","margin-left","margin","padding","border-style","display","position","bottom","top","right","left","float","clear","max-width","min-width","max-height","min-height"]
Tokens= []
Entrada_Corregida =''
consola =''
retorno =''


class analizadorCSS:
    #variable para control de estados
    estado = 0
    
    # variables para contadores de tokens
    


    def leerLetras(char):
        x = ord(char)
        if (x >= 65 and x <= 90) or (x >= 97 and x <= 122):
            return True
        else:
            return False

    def signoSelector(char):
        signos= [':','.','#','*',',']
        for s in signos:
            if char == s:
                #print(char,s)
                return True
        for s in signos:
            if char != s:
                #print(char,s)
                return False

    def signoPropiedad(char):
        signos= ['-','.','(',')','#','%','=','_','\"',' ',',','\'','\\',':']
        for s in signos:
            if char == s:
                #print(char,s)
                return True
        for s in signos:
            if char != s:
                #print(char,s)
                return False

    def Mandar_Nuevo():
        global Entrada_Corregida
        print(Entrada_Corregida)
        return Entrada_Corregida

    def consola():
        global consola
        return consola

    def ReporteErrores():
        global Error
        f = open("ReporteCSS.html", 'w')
        f.write("<html lang=\"es\">\n")
        f.write("<head><title>Reporte de Errores</title></head>\n")
        f.write("<body>\n")
        f.write("<p><h1>" + "ERRORES" + "</h1><p>\n")

        if len(Error) > 0:
            f.write("<table border=\"1\">\n")
            f.write("<td>Error</td><td>Fila</td><td>Columna</td>")

            for i in Error:
                f.write("<tr>")

                for j in i:
                    f.write("<td>" + str(j) + "</td>")
                f.write("</td>\n")
            f.write("</table>\n")

        else:
            f.write("<p><h3>No hay errores</h3><p>\n")

        f.write("</body>\n")
        f.write("</html>\n")

    # DEFINICION DE ESTADOS DEL AUTOMATA

    def analizador(texto):
        global linea, columna, counter, Errores, Entrada_Corregida, Error,consola,retorno
        listaTokens = []
        entrada = texto
        lexema = ""
        consola = ""
        Entrada_Corregida =""
        columna = 1
        fila = 1
        estado = 0
        i = 0
        id = 1

        while i < len(entrada):
            cadena = entrada[i]
            if estado is 0:
                consola += 'entradando a estado 0 con lexema: '+lexema+'\n'
                if analizadorCSS.leerLetras(entrada[i]):
                    estado =0
                    lexema = lexema+ entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]

                    columna += 1
                elif entrada[i].isdigit():
                    estado = 0
                    lexema = lexema + entrada[i]
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif analizadorCSS.signoSelector(entrada[i]):
                    estado =0
                    lexema = lexema+ entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    columna += 1
                elif entrada[i] is '{':
                    estado = 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    listaTokens.append(["Selector: " + lexema, fila, columna])
                    consola += 'TOKEN ' + lexema+'= Selector: encontrado con estado 0\n'
                    #analizadorCSS.textarea.tag_config('BOOL', foreground="blue")
                    listaTokens.append(["Llave Abierta: " + '{', fila, columna])
                    consola += 'TOKEN { = Llave Abierta: encontrado con estado 0\n'
                    columna += 1
                    lexema = ""
                elif entrada[i] is '/':
                    estado = 4
                    retorno ='A'
                    columna += 1
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] == '\t' or entrada[i] ==' ':
                    estado = 0
                    columna += 1
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] =='\n':
                    estado = 0
                    fila += 1
                    columna =0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    #Error.append(["Salto de linea no esperado: " + entrada[i], fila, columna])
                else:
                    estado = 0
                    fila += 1
                    Error.append(["Caracter no valido: " + entrada[i], fila, columna])
                    consola += 'ERROR Caracter no valido' + entrada[i] + 'encontrado EN estado 0\n'

            elif estado is 1:
                consola += 'entradando a estado 1 con lexema: '+lexema+'\n'
                if analizadorCSS.leerLetras(entrada[i]):
                    estado =1
                    lexema = lexema+ entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    columna += 1
                elif entrada[i] is '-':
                    estado = 1
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    columna += 1
                elif entrada[i] is ':':
                    estado = 3;
                    #lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    for token in reservadas:
                        if lexema == token:
                            listaTokens.append(["Propiedad: " + lexema, fila, columna])
                            consola += 'TOKEN ' + lexema + '= Propiedad: encontrado con estado 1\n'
                            lexema = ""
                            estado = 2
                    for token in reservadas:
                        if lexema != token and lexema != '':
                            estado = 2
                            Error.append(["Propiedad inexistente: " + lexema, fila, columna])
                            consola += 'ERROR ' + lexema + '= Propiedad inexistente: encontrado con estado 1\n'
                            lexema = ""
                    columna += 1
                elif entrada[i] == '\t' or entrada[i] ==' ':
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    #Error.append(["Espacio no esperado: " + entrada[i], fila, columna])
                elif entrada[i] =='\n':
                    fila += 1
                    columna =0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    #Error.append(["Salto de linea no esperado: " + entrada[i], fila, columna])

                else:
                    estado = 1
                    fila += 1
                    Error.append(["Caracter no valido: " + entrada[i], fila, columna])
                    consola += 'ERROR Caracter no valido' + entrada[i] + 'encontrado EN estado 1\n'

            elif estado is 2:
                consola += 'entradando a estado 2 con lexema: '+lexema+'\n'
                if entrada[i] is '}':
                    estado = 0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + ''
                    listaTokens.append(["Propiedades: " + lexema, fila, columna])
                    consola += 'TOKEN ' + lexema + '= Propiedad: encontrado con estado 2\n'
                    listaTokens.append(["Llave Cerrada: " + '}', fila, columna])
                    consola += 'TOKEN } = Llave Cerrada: encontrado con estado 0\n'
                    columna += 1
                    lexema = ""
                elif analizadorCSS.leerLetras(entrada[i]):
                    estado =2
                    lexema = lexema+ entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    columna += 2
                elif entrada[i].isdigit():
                    estado = 2
                    lexema = lexema + entrada[i]
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif analizadorCSS.signoPropiedad(entrada[i]):
                    estado = 2
                    columna += 1
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] is ';':
                    estado = 2
                    retorno = 'B'
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    listaTokens.append(["Propiedades: " + lexema, fila, columna])
                    consola += 'TOKEN ' + lexema + '= Propiedad: encontrado con estado 2\n'
                    columna += 1
                    lexema = ""
                elif entrada[i] is '/':
                    estado = 3
                    retorno = 'B'
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    listaTokens.append(["Propiedades: " + lexema, fila, columna])
                    consola += 'TOKEN ' + lexema + '= Propiedad: encontrado con estado 2\n'
                    columna += 1

                elif entrada[i] == '\t' or entrada[i] ==' ':
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    #Error.append(["Espacio no esperado: " + entrada[i], fila, columna])
                elif entrada[i] =='\n':
                    fila += 1
                    columna = 0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    #Error.append(["Salto de linea no esperado: " + entrada[i], fila, columna])

                else:
                    estado = 2
                    fila += 1
                    Error.append(["Caracter no valido: " + entrada[i], fila, columna])
                    consola += 'ERROR Caracter no valido' + entrada[i] + 'encontrado EN estado 1\n'

            elif estado is 3:
                consola += 'entradando a estado 3 con lexema: ' + lexema + '\n'

                if entrada[i] is '*':
                    estado = 4
                    columna += 1
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] == '\t' or entrada[i] ==' ':
                    columna += 1
                    estado = 3
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    lexema = lexema + entrada[i]
                    #Error.append(["Espacio no esperado: " + entrada[i], fila, columna])
                elif entrada[i] =='\n':
                    fila += 1
                    columna = 0
                    estado = 3
                    lexema = lexema + entrada[i]
                    #Entrada_Corregida = Entrada_Corregida + entrada[i]
                    #Error.append(["Salto de linea no esperado: " + entrada[i], fila, columna])

                else:
                    estado = 2
                    fila += 1

            elif estado is 4:
                consola += 'entradando a estado 4 con lexema: ' + lexema + '\n'
                if entrada[i] is '*':
                    estado = 5
                    columna += 1
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] == '\t' or entrada[i] == ' ':
                    columna += 1
                    #lexema = lexema + entrada[i]
                    #Entrada_Corregida = Entrada_Corregida + entrada[i]
                    # Error.append(["Espacio no esperado: " + entrada[i], fila, columna])
                elif entrada[i] == '\n':
                    fila += 1
                    columna = 0
                    #lexema = lexema + entrada[i]
                    #Entrada_Corregida = Entrada_Corregida + entrada[i]
                    # Error.append(["Salto de linea no esperado: " + entrada[i], fila, columna])

                else:
                    estado = 5
                    fila += 1

            elif estado is 5:
                consola += 'entradando a estado 5 con lexema: ' + lexema + '\n'
                if entrada[i] is '*':
                    estado =6
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] == '\t' or entrada[i] == ' ':
                    columna += 1
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    # Error.append(["Espacio no esperado: " + entrada[i], fila, columna])
                elif entrada[i] == '\n':
                    fila += 1
                    columna = 0
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    # Error.append(["Salto de linea no esperado: " + entrada[i], fila, columna])
                else:
                    estado = 5
                    fila += 1
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]

            elif estado is 6:
                consola += 'entradando a estado 6 con lexema: ' + lexema + '\n'
                if entrada[i] is '/':
                    if retorno is 'A':
                        estado = 0
                    elif retorno is 'B':
                        estado = 1
                    columna += 1
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    listaTokens.append(["Cometario: " + lexema, fila, columna])
                    consola += 'Comentario ' + lexema + ': encontrado con estado 6\n'
                    lexema = ""
                elif entrada[i] == '\t' or entrada[i] == ' ':
                    columna += 1
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    # Error.append(["Espacio no esperado: " + entrada[i], fila, columna])
                elif entrada[i] == '\n':
                    fila += 1
                    columna = 0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    lexema = lexema + entrada[i]
                    # Error.append(["Salto de linea no esperado: " + entrada[i], fila, columna])
                else:
                    estado = 5
                    fila += 1
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]

            i+=1
        consola += "-------------IMPRIMIENDO ENTRADA SIN ERRORES--------------\n"
        consola += "---------------------GENERANDO REPORTE--------------------\n"
            



