from conexionBD import *
class Estudiante():
    def __init__(self,nombre,nota):
        self._nombre=nombre
        self._nota=nota
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nomb):
        self._nombre=nomb

    @property
    def nota(self):
        return self._nota
    @nota.setter
    def nota(self,nota):
        self._nota=nota

    def imprimir(self):
        print(f"El nombre del alumno es {self.nombre} y su nota es {self.nota}")

    def calificar(self):
        if self.nota>=7:
            return f"El alumno ha aprobado con un {self.nota}"
        else:
            return f"El alumno ha reprobado con un {self.nota} "


    @staticmethod
    def insertar(nombre,nota):
        try:
            cursor.execute(
                "insert into estudiantes values(null,%s,%s)",
                (nombre,nota)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def mostrar():
            try:
                cursor.execute("select * from estudiantes")
                return cursor.fetchall()
            except:    
                return []

    @staticmethod
    def actualizar(id,nombre,nota):
        try:
            cursor.execute("update estudiantes set nombre=%s,nota=%s where id=%s",(nombre,nota,id))
            conexion.commit()
            return True
        except: 
            return False
    
    @staticmethod
    def eliminar(id):
            try:
                cursor.execute(
                    "delete from estudiantes where id=%s",
                    (id,)
                ) 
                conexion.commit() 
                return True  
            except:    
                return False
            
        
'''
alumno=Estudiante("Carlos",9)
alumno.imprimir()
print(alumno.calificar())
'''
    