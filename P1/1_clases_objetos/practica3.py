import os
os.system("cls")


class Alumnos():
    def __init__(self,nombre,edad,matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula

    def inscribirse():
        pass

    def estudiar():
        pass

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,edad):
        self.__edad=edad

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def color(self,matricula):
        self.__matricula=matricula

alumno_1=Alumnos("Carlos",19,"3141240128")
alumno_2=Alumnos("Miguel",19,"3141240112")

print(alumno_1.nombre,alumno_1.edad,alumno_1.matricula)


class Profesores():
    def __init__(self,nombre,experiencia,num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor

    def impartir():
        pass

    def evaluar():
        pass

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def experiencia(self):
        return self.__experiencia
    @experiencia.setter
    def edad(self,ex):
        self.__experiencia=ex

    @property
    def num(self):
        return self.__num_profesor
    @num.setter
    def color(self,num):
        self.__num_profesor=num

profesor_1=Profesores("Dagoberto",14,349812098)
profesor_2=Profesores("Juan Pablo",3,2398980230)

print(profesor_1.nombre,profesor_1.experiencia,profesor_1.num)


class Cursos():
    def __init__(self,nombre,codigo,creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos

    def asignar():
        pass

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def edad(self,cod):
        self.__codigo=cod

    @property
    def creditos(self):
        return self.__creditos
    @creditos.setter
    def color(self,cred):
        self.__creditos=cred

curso_1=Cursos("Topicos", "67soi0", 90)
curso_2=Cursos("POO","34bnh4",100)

print(curso_1.nombre,curso_1.codigo,curso_1.creditos)

