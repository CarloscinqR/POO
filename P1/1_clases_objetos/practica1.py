import os
"""
Practica #1 Implementar paradigma estructurado Vs Orientado a objetos
Crear un programa que obtenga el area de un rectangulo
"""
"#1.- Estructurado"
base=5
altura=3

def calcArea(base,altura):
    area=base*altura
    return area

resultado=calcArea(base,altura)
print(resultado)

os.system("cls")
"#2.- Orientada a objetos"
class AreaRectangulo:
    def calcArea(self,base,altura):
        area=base*altura
        return area
    
rectangulo=AreaRectangulo() #Instanciar un objeto de la clase AreaRectangulo
#El constructor inicializa los valores del objeto
print(f"El area del rectangulo es: {rectangulo.calcArea(5,3)}")

"Con atributos"
class AreaRectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def calcArea(self):
        area=self.base*self.altura
        return area
    
rectangulo=AreaRectangulo(5,3) #Instanciar un objeto de la clase AreaRectangulo
#El constructor inicializa los valores del objeto
print(f"El area del rectangulo es: {rectangulo.calcArea()}")