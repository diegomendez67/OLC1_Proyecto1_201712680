import re
linea = 0
columna = 0
contador = 0
Error = []
reservadas = ['<HTML>', '</HTML>', '<HEAD>', '</HEAD>','<TITLE>','</TITLE>','<BODY>','</BODY>','<P>','</P>','<H1>','<H2>','<H3>','<H4>','<H5>','<H6>','</H1>','</H2>','</H3>','</H4>','</H5>','</H5>','</UL>','</LI>','<UL>','<LI>','<TABLE>','<TH>','<TR>','<TD>','<CAPTION>','<COLGROUP>','<COL>','<THEAD>','<TOBODY>','<TFOOT>','</TABLE>','</TH>','</TR>','</TD>','</CAPTION>','</COLGROUP>','</COL>','</THEAD>','</TBODY>','</TFOOT>']
Tokens = []
Entrada_Corregida =''

class analizador:
    #variable para control de estados
    estado = 0
    # variables para contadores de tokens
    

    



    def analizador(texto):
        global linea, columna, counter, Errores,Entrada_Corregida,Error
        listaTokens=[]
        entrada = texto.upper()
        lexema = ""
        Entrada_Corregida =""
        columna = 1
        fila = 1
        estado = 0
        i = 0
        id = 1



        while i < len(entrada):

            cadena = entrada[i]
            if estado is 0:
                if entrada[i] is '<':
                    estado = 0;
                    lexema = lexema+ entrada[i]
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida+entrada[i]

                elif analizador.leerLetras(entrada[i]):
                    estado =1
                    lexema = lexema+ entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    columna += 1
                elif entrada[i] is '/':
                    estado = 1;
                    lexema = lexema+ entrada[i]
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] == '\t' or entrada[i] ==' ':
                    estado = 0
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] =='\n':
                    estado = 0
                    fila += 1
                    columna =0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                else:
                    estado = 0
                    fila += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    Error.append(["Caracter no valido: "+entrada[i],fila,columna])

            elif estado  is 1:
                if analizador.leerLetras(entrada[i]):
                    estado = 1;
                    lexema = lexema+ entrada[i]
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] is '=':
                    estado = 2;
                    lexema = lexema+ entrada[i]
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] is '>':
                    estado = 3;
                    lexema = lexema+ entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    columna += 1
                    #print(entrada[i])

                    for token in reservadas:
                        if lexema == token:
                            #print(entrada)
                            #print("Etiqueta: ",lexema," Fila: ",fila," Columna: ",columna)
                            listaTokens.append(["Etiqueta: "+lexema,fila,columna])
                            lexema = ""
                            estado = 3
                    for token in reservadas:
                        if lexema != token and lexema != '':
                            estado = 3
                            Error.append(["Etiqueta inexistente: " + lexema, fila, columna])
                            lexema = ""


                elif entrada[i] == '\t' or entrada[i] ==' ':
                    estado = 0
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] =='\n':
                    estado = 0
                    fila += 1
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                else:
                    estado = 1
                    fila += 1
                    Error.append(["Caracter no valido: " + entrada[i], fila, columna])

            elif estado is 2:
                if analizador.leerLetras(entrada[i]):
                    estado = 2;
                    lexema = lexema + entrada[i]
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i].isdigit():
                    estado = 2
                    lexema = lexema + entrada[i]
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif analizador.signo(entrada[i]):
                    estado = 2
                    lexema = lexema + entrada[i]
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] is '>':
                    estado = 3;
                    lexema = lexema + entrada[i]
                    columna += 1
                    #print("Instruccion Especial: ", lexema, " Fila: ", fila, " Columna: ", columna)
                    listaTokens.append(["Instruccion Especial: " + lexema, fila, columna])
                    lexema = ""
                    estado = 3
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] == '\t' or entrada[i] == ' ':
                    estado = 2
                    columna += 1
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] == '\n':
                    estado = 2
                    fila += 1
                    columna =0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                else:
                    estado = 2
                    fila += 1
                    Error.append(["Caracter no valido: "+entrada[i],fila,columna])



            elif estado is 3:
                if analizador.leerLetras(entrada[i]):
                    estado = 3;
                    lexema = lexema + entrada[i]
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]

                elif entrada[i].isdigit():
                    estado = 3
                    lexema = lexema + entrada[i]
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] == '.'or entrada[i] == ':'or entrada[i] == ';'or entrada[i] == '='or entrada[i] == '/'or entrada[i] == '.'or entrada[i] == '-'or entrada[i] == '_'or entrada[i] == '\"':
                    estado = 3
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    lexema = lexema + entrada[i]
                elif entrada[i] is '<':
                    estado = 0;
                    if lexema != "":
                        #print("Texto Plano: ", lexema, " Fila: ", fila, " Columna: ", columna)
                        listaTokens.append(["Texto Plano: " + lexema, fila, columna])
                    lexema = ""
                    lexema = lexema + entrada[i]
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                elif entrada[i] == '\t' or entrada[i] == ' ':
                    estado = 3
                    columna += 1
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                    #lexema = lexema + entrada[i]
                elif entrada[i] == '\n':
                    estado = 3
                    fila += 1
                    columna =0
                    Entrada_Corregida = Entrada_Corregida + entrada[i]
                else:
                    estado = 3
                    fila += 1
                    Error.append(["Caracter no valido: "+entrada[i],fila,columna])

            i+=1

        for token in listaTokens:
            print(token)

        for error in Error:
            print(error)


    def leerLetras(char):
        x = ord(char)
        if (x >= 65 and x <= 90) or (x >= 97 and x <= 122):
            return True
        else:
            return False

    def signo(char):
        signos= [':',';','=','/','.','-','_','\"',' ','']
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
    
    def ReporteErrores():
        global Error
        f=open("ReporteHTML.html",'w')
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