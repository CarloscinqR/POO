#Instanciar los objetos para posteriormente implementarlos
from coches import *
coche=Coches("Vw","Blanco","2020",220,180,5)
print(coche.marca, coche.acelerar())

camioneta=Camionetas("Toyota","Blanco","2010",200,240,6,"trasera",True)
print(camioneta.marca, camioneta.acelerar())

camion=Camiones("Volvo","Rojo","2023",180,200,4,2,3000)
print(camion.marca, camion.acelerar())



#print(coche2.getMarca(),coche2.getColor(),coche2.getModelo(),coche2.getVelocidad(),coche2.getCaballaje(),coche2.getPlazas())