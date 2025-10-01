"""
class Coches:
    __marca=""
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0
            
    def acelerar(self,velocidad,incremento):
        self.__velocidad=velocidad+incremento
        return self.__velocidad
    
    def frenar(self, velocidad, decremento):
        self.__velocidad=velocidad-decremento
        return self.__velocidad
    
coche1=Coches()
coche1.__marca="VW"
coche1.__color="Blanco"
coche1.__modelo="2022"
coche1.__velocidad=220
coche1.__caballaje=150
coche1.__plazas=5
print(coche1.__marca,coche1.__color,coche1.__modelo,coche1.__velocidad,coche1.__caballaje,coche1.__plazas)
print(f"El coche 1 acelero de {coche1.__velocidad} a {coche1.acelerar(coche1.__velocidad,50)}")

coche2=Coches()
coche2.__marca="Nissan"
coche2.__color="Azul"
coche2.__modelo="2020"
coche2.__velocidad=180
coche2.__caballaje=150
coche2.__plazas=6
print(coche2.__marca,coche2.__color,coche2.__modelo,coche2.__velocidad,coche2.__caballaje,coche2.__plazas)
print(f"El coche 2 desacelero de {coche2.__velocidad} a {coche1.frenar(coche2.__velocidad,80)}")
"""

class Coches:
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0

    def acelerar(self):
        pass

    def frenar(self):
        pass

coche1=Coches()
coche1.marca="VW"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5
print(coche1.marca,coche1.color,coche1.modelo,coche1.velocidad,coche1.caballaje,coche1.plazas)

coche2=Coches()
coche2.marca="Nissan"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6
print(coche2.marca,coche2.color,coche2.modelo,coche2.velocidad,coche2.caballaje,coche2.plazas)