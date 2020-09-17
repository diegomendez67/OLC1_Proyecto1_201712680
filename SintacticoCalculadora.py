tablaSimbolos = {
    'E': {'PARA': "eT", 'NUMERO': "eT", 'IDENTIFICADOR': "eT"},
    'e': {'SIGNO MAS': "eT+", 'SIGNO MENOS': "eT-", 'PARENTESIS CERRADO': None, '$': None},
    'T': {'PARA': "tF", 'NUMERO': "tF", 'IDENTIFICADOR': "tF"},
    't': {'SIGNO MULTIPLICACION': "tF*", 'SIGNO DIVISION': "tF/", 'SIGNO MAS': None, 'SIGNO MENOS': None,
          'PARENTESIS CERRADO': None, '$': None},
    'F': {'PARA': ")E(", 'NUMERO': "i", 'IDENTIFICADOR': "d"}
}
# variables para erroes y look ahead
pilaAnilisis = ['$', 'E']
Errores = []
recorrido =0

class Sintactico:


    def recorrido(produccion, token):
        global tablaSimbolos,pilaAnilisis,Errores
        try:
            return tablaSimbolos[produccion][token]
        except:
            print("ERROR SINTACTICO")
            return "ERROR DE SINTAXIS"

    def insertar_Pila(producciones):
        entradas = list(producciones)
        for e in entradas:
            if e is "(":
                pilaAnilisis.append('PARENTESISABIERTO')
            elif l == ")":
                pilaAnilisis.append('PARENTESISCERRADO')
            elif l == "i":
                pilaAnilisis.append('NUMERO')
            elif l == "d":
                pilaAnilisis.append('IDENTIFICADOR')
            elif l == "+":
                pilaAnilisis.append('SIGNOMAS')
            elif l == "-":
                pilaAnilisis.append('SIGNOMENOS')
            elif l == "*":
                pilaAnilisisa.ppend('SIGNO MULTIPLICACION')
            elif l == "/":
                pilaAnilisis.append('SIGNO DIVISION')
            else:
                pilaAnilisis.append(l)
                
    def TipoToken(entrada):
        tipos = ['PARENTESIS ABIERTO','PARENTESIS CERRADO','NUMERO','IDENTIFICADOR','SIGNO MAS','SIGNO MENOS','SIGNO MULTIPLICACION','SIGNO DIVISION']
        for t in tipos:
            if entrada == t:
                return True
            else: 
                return False
                
    def parser (tokens):
        global pilaAnilisis,recorrido
        tokens.append(['$',0,0,0])
        while len(pilaAnilisis)-1>=0:
            recorrido = len(pilaAnilisis)-1
            t1 = pilaAnilisis[recorrido]
            t2 = tokens[0][0]
            
            if t1==t2:
                if var1 is '$':
                    return True
                elif Sintactico.TipoToken(t1):
                    pilaAnilisis.pop()
                    del tokens[0]
            else:
                pilaAnilisis.pop()
                val = Sintactico.recorrido(t1,t2)

                if val == "ERROR DE SINTAXIS":
                    return False
                elif val != None:
                    Sintactico.insertar_Pila(val)
                    
                
            

