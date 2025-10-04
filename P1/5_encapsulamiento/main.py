#Instanciar los objetos para posteriormente implementarlos
from coches import Coches
num_coches=int(input("Cuantos coches deseas?"))
for i in range(0,num_coches):
    print(f"\n\t...Datos del coche {i+1} ...")
    marca=input("Ingresa la marca ").upper()
    color=input("Ingresa el color ").upper()
    modelo=input("Ingresa el modelo ").upper()
    velocidad=int(input("Ingresa la velocidad "))
    caballaje=int(input("Ingresa el caballaje "))
    plazas=int(input("Ingresa las plazas "))

    coche1=Coches(marca,color,modelo,velocidad,caballaje,plazas)
    print(coche1.marca,coche1.getColor(),coche1.getModelo(),coche1.getVelocidad(),coche1.getCaballaje(),coche1.getPlazas())

    print(f"\n\n\n {coche1.acelerar()}")

"""
coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,0)
"""



#print(coche2.getMarca(),coche2.getColor(),coche2.getModelo(),coche2.getVelocidad(),coche2.getCaballaje(),coche2.getPlazas())