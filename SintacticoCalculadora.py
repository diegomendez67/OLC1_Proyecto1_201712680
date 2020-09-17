tabla = {
    'E' : { 'PARA' : "XT", 'NUMERIC' : "XT",'ID' : "XT" }, 
    'X' : { 'MAS' : "XT+", 'MEN' : "XT-",'PARC' : None, '$' : None }, 
    'T' : { 'PARA' : "ZF", 'NUMERIC' : "ZF" ,'ID' : "ZF"},
    'Z' : { 'POR' : "ZF*", 'DIV' : "ZF/",'MAS' : None, 'MEN' : None,'PARC' : None, '$' : None }, 
    'F' : { 'PARA' : ")E(", 'NUMERIC' : "i",'ID' : "d" } 
    }
# variables para erroes y look ahead
pila = ['$', 'E']
Errores = []
recorrido =0

class Sintactico:


    def obtenerMatrix(produccion, token):
        global tabla,pila,Errores
        try:
            return tabla[produccion][token]
        except:
            print("ERROR SINTACTICO")
            return "MALO"

    def pushear(producciones):
        lista = list(producciones)
        for l in lista:
            if l == "(":
                pila.append('PARA')
            elif l == ")":
                pila.append('PARC')
            elif l == "i":
                pila.append('NUMERIC')
            elif l == "d":
                pila.append('ID')
            elif l == "+":
                pila.append('MAS')
            elif l == "-":
                pila.append('MEN')
            elif l == "*":
                pila.append('POR')
            elif l == "/":
                pila.append('DIV')
            else:
                pila.append(l)
                
    def TipoToken(entrada):
        tipos = ['PARENTESIS ABIERTO','PARENTESIS CERRADO','NUMERO','IDENTIFICADOR','SIGNO MAS','SIGNO MENOS','SIGNO MULTIPLICACION','SIGNO DIVISION']
        for t in tipos:
            if entrada == t:
                return True
            else: 
                return False
                
    def parse (tokens):
        global pila
        tokens.append([0,0,'$',0])
        while len(pila)-1>=0:
            counter = len(pila)-1
            var1 = pila[counter]
            var2 = tokens[0][2]

            if var1 == var2:
                if var1 == "$":
                    return True
                elif var1 == "NUMERIC" or var1 == "ID" or var1 == "PARA" or var1 == "PARC" or var1 == "MAS" or var1 == "MEN" or var1 == "POR" or var1 == "DIV":
                    pila.pop()
                    del tokens[0]
                    
            else:
                pila.pop()
                val = Sintactico.obtenerMatrix(var1, var2)

                if val == "MALO":
                    return False
                elif val != None:
                    Sintactico.pushear(val)
                    
                
            

