

class Persona:


    def __init__(self, n,e,cp,cpe,co,ed):
        self.Nombre = n
        self.Estatura = e
        self.ColorPiel = cp
        self.ColorPelo = cpe
        self.ColorOjos = co
        self.Edad = ed

    def ImprmirNombre(self):
        print (self.Nombre)

    def ImprmirEstatura(self):
        print (self.Estatura)

    def ImprmirColorPiel(self):
        print (self.ColorPiel)

    def ImprmirColorPelo(self):
        print (self.ColorPelo)

    def ImprmirColorOjos(self):
        print (self.ColorOjos)

    def ImprmirEdad(self):
        print (self.Edad)


Diego = Persona('Diego Mendez',1.71,'Moreno','Castaño','cafes',21)
Fer =  Persona('Fernando Carrera',1.70,'Moreno','Negro','CafeObscuro',23)
Jose = Persona('Jose silvestre',1.60,'Moreno','Negro','Verdes',20)

Diego.ImprmirNombre()
Fer.ImprmirNombre()
Jose.ImprmirNombre()

