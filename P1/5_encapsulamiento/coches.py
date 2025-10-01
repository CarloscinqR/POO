class Coches:

    #Metodo constructor.- Con este metodo se inicializa un objeto cuando es creado con valores
    """
    def __init__(self):
        __marca=""
        __color=""
        __modelo=""
        __velocidad=0
        __caballaje=0
        __plazas=0
    """

    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas

#Crear los metodos getter y stters estos metodos son importantes y necesarios en todas las clases para que el programador
#interactue con los valores de los atributps a traves de estos metodos, digamos que es la manera mas adecuada y recomendada para 
#solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto

#En teoria se deberia de crear un metodo getters y setters por cada atributo que contenga la clase

#Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return 

# Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor de atributo o propiedad en cuestion 

    def getMarca(self):
        return self.__marca
    
    def setMarca(self,marca):
        self.__marca=marca

    #2da forma de crear set y get
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,marca):
        self.__marca=marca
    #Aqui termina

    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color=color

    def getModelo(self):
        return self.__modelo
    
    def setModelo(self,modelo):
        self.__modelo=modelo

    def getVelocidad(self):
        return self.__velocidad
    
    def setVelocidad(self,velocidad):
        self.__velocidad=velocidad

    def getCaballaje(self):
        return self.__caballaje
    
    def setCaballaje(self,caballaje):
        self.__caballaje=caballaje

    def getPlazas(self):
        return self.__plazas
    
    def setPlazas(self,plazas):
        self.__plazas=plazas    
    
    def acelerar(self):
        return "Estoy acelerando el coche"

    def frenar(self):
        return "Estoy frenando el coche"

coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,0)


print(coche1.marca,coche1.getColor(),coche1.getModelo(),coche1.getVelocidad(),coche1.getCaballaje(),coche1.getPlazas())

print(coche2.getMarca(),coche2.getColor(),coche2.getModelo(),coche2.getVelocidad(),coche2.getCaballaje(),coche2.getPlazas())

print(coche3.marca)