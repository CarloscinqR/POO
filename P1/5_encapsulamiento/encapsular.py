"""
Es un pilar de la po que permite indicar cyal es la manera de como poder utilizar los atributos y metodos de una clase a la hora de usar en 
objetos o en herenciad
"""
import os
os.system("cls")

class Clase():
    atributo_publico = "Soy un atributo publico"
    _atributo_protegido = "Soy un atributo protegido"
    __atributo_privado = "Soy un atributo privado"

    def __init__(self,color,size):
        self.__color=color
        self.__size=size

    def getAtributoPrivado(self):
        return self.__atributo_privado
    def setAtributoPrivado(self,nuevo):
        self.__atributo_privado=nuevo
    
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,color):
        self.__color=color

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self,size):
        self.__size=size

    @property
    def publico(self):
        return self.atributo_publico
    @publico.setter
    def publico(self,atributo_publico):
        self.__size=atributo_publico

    @property
    def protegido(self):
        return self._atributo_protegido
    @protegido.setter
    def protegido(self,_atributo_protegido):
        self._atributo_protegido=_atributo_protegido

    @property
    def privado(self):
        return self.__atributo_privado
    @privado.setter
    def privado(self,__atributo_privado):
        self.__atributo_privado=__atributo_privado

objeto=Clase("Rojo","Grande")

#print(objeto.atributo_publico)
#print(objeto._atributo_protegido) No es buena practica acceder a los valores directamente 
print(objeto.privado)
print(objeto.publico)
print(objeto.protegido)
objeto.color="amarillo"
print(objeto.color,objeto.size)