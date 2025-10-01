class Coches:
    __marca=""
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0
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
        pass

    def frenar(self):
        pass

coche1=Coches()
coche2=Coches()
coche3=Coches()

coche1.marca="VW"
coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)
coche1.num_serie="239tgyweffoig9723"
print(coche1.marca,coche1.getColor(),coche1.getModelo(),coche1.getVelocidad(),coche1.getCaballaje(),coche1.getPlazas())


coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)
print(coche2.getMarca(),coche2.getColor(),coche2.getModelo(),coche2.getVelocidad(),coche2.getCaballaje(),coche2.getPlazas())

coche3.marca="Honda"
print(coche3.marca)