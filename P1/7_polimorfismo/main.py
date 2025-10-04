import os
#Instanciar los objetos para posteriormente implementarlos
from coches import *
'''
coche=Coches("Vw","Blanco","2020",220,180,5)
print(coche.marca, coche.acelerar())
camioneta=Camionetas("Toyota","Blanco","2010",200,240,6,"trasera",True)
print(camioneta.marca, camioneta.acelerar())
camion=Camiones("Volvo","Rojo","2023",180,200,4,2,3000)
print(camion.marca, camion.acelerar())
'''
def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\n\t...Oprima una tecla para continuar...")

def datos_autos(tipo):
    borrarPantalla()
    print(f"\n\t...Ingresar los datos del vehiculo tipo {tipo}...")
    marca=input("Marca ").upper()
    color=input("Color ").upper()
    modelo=input("Modelo ").upper()
    velocidad=int(input("Velocidad "))
    caballaje=int(input("Caballaje "))
    plazas=int(input("Plazas "))
    return marca,color,modelo,velocidad,caballaje,plazas

def imprimir(marca,color,modelo,velocidad,caballaje,plazas):
    print(f"\nMarca: {marca}\nColor: {color}\nModelo: {modelo}\nVelocidad: {velocidad}\nCaballaje: {caballaje}\nPlazas: {plazas}")


def autos():
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("carro")
    coche=Coches(marca,color,modelo,velocidad,caballaje,plazas)
    imprimir(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    

def camiones():
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("camion")
    eje=int(input("Ingrese el eje "))
    capacidad=int(input("Ingresa la capacidad de carga "))

    coche=Camiones(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad)

    imprimir(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"Eje del coche: {coche.eje}\nCapacidad de carga: {coche.capacidadCarga}")

def camionetas():
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("camioneta")
    traccion=input("Ingresa la traccion ").upper()
    cerrada=input("Ingresa si es cerrada o no ").upper()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False
    
    coche=Camionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
    imprimir(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"Traccion: {coche.traccion}\nEs cerrada?: {coche.cerrada}")



def main():
    os.system("cls")
    opcion=True
    while opcion:
        borrarPantalla()
        opcion=input("\n\t\t...Menu principal...\n1.-Autos\n2.-Camionetas\n3.-Camiones\n4.-Salir\nElige una opcion: ").lower().strip()
        match opcion:
            case "1":
                borrarPantalla()
                print("Autos")
                autos()
                esperarTecla()
            case "2":
                borrarPantalla()
                print("Camionetas")
                camionetas()
                esperarTecla()
            case "3":
                borrarPantalla()
                print("Camiones")
                camiones()
                esperarTecla()
            case "4":
                borrarPantalla()
                os.system("cls")
                print("Gracias por utilizar el software")
                opcion=False
            case _:
                borrarPantalla()
                print("Opcion no valida, vuelva a intentarlo")
                esperarTecla()
                opcion=True

if __name__=="__main__":
    main()