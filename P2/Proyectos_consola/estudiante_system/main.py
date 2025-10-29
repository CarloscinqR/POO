from estudiante import estudiante
import os
class Menu():

    @staticmethod
    def esperarTecla():
        input("Pulse una tecla para continuar: ")

    @staticmethod
    def borrarPantalla():
        os.system("cls")

    @staticmethod
    def crear_registro():
        Menu.borrarPantalla()
        nombre=input("Inserte el nombre del alumno: ")
        nota=input("Inserte la nota del alumno: ")
        return nombre,nota
    
    @staticmethod
    def confirmar(resp):
        if resp:
            return f"Accion realizada con exito"
        else:
            return f"Hubo un problema al realizar la accion"

    @staticmethod
    def menu_acciones(tipo):
        Menu.borrarPantalla()
        opcion=input(f"\tSistema de Gestion de {tipo}\n\t\t1.-Insertar\n\t\t2.-Mostrar\n\t\t3.-Cambiar\n\t\t4.-Eliminar\n\t\t5.-Salir\nElegir opcion: ")
        return opcion
    
    @staticmethod
    def menu_estudiante():
        while True:
            opcion=Menu.menu_acciones("Estudiante")
            if opcion=="1":
                nombre,nota=Menu.crear_registro()
                respuesta=estudiante.Estudiante.insertar(nombre,nota)
                print(Menu.confirmar(respuesta))
                Menu.esperarTecla()
            elif opcion=="2":
                Menu.borrarPantalla()
                registros=estudiante.Estudiante.mostrar()
                if len(registros)>0:
                    print(f"{"Id":<10}{"Nombre":<20}{"Nota":<10}")
                    for lineas in registros:
                        print(f"{lineas[0]:<10}{lineas[1]:<20}{lineas[2]:<10}")
                else:
                    print("No hay ningun registro ingresado")
                Menu.esperarTecla()
            elif opcion=="3":
                Menu.borrarPantalla()
                id=input("Introduzca el id del alumno a actualizar: ")
                nombre,nota=Menu.crear_registro()
                respuesta=estudiante.Estudiante.actualizar(id,nombre,nota)
                print(Menu.confirmar(respuesta))
                Menu.esperarTecla()
            elif opcion=="4":
                Menu.borrarPantalla()
                id=input("Introduzca el id del alumno a eliminar: ")
                respuesta=estudiante.Estudiante.eliminar(id)
                print(Menu.confirmar(respuesta))
                Menu.esperarTecla()
            elif opcion=="5":
                print("Gracias por usar el programa")
                break
            else:
                print("Opcion incorrecta")
                Menu.esperarTecla()

    @staticmethod
    def menuPrincipal():
        while True:
            Menu.borrarPantalla()
            opcion=input(f"\tMenu Principal\n\t\t1.-Estudiante\n\t\t2.-Salir\nElegir opcion: ")
            if opcion=="1":
                Menu.menu_estudiante()
            elif opcion=="2":
                print("Gracias por usar el programa")
                break
            else:
                print("Opcion incorrecta")
                Menu.esperarTecla()
    





if __name__ == "__main__":
  Menu.menuPrincipal()