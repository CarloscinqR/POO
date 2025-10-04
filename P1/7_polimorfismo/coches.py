class Coches():
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas


    #metodos set y get
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca=marca
 
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,col):
        self._color=col

    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self,mod):
        self._modelo=mod

    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self,vel):
        self._velocidad=vel

    @property
    def caballaje(self):
        return self._caballaje
    @caballaje.setter
    def caballaje(self,cab):
        self._caballaje=cab

    @property
    def plazas(self):
        return self._plazas
    @plazas.setter
    def plazas(self,plaz):
        self._plazas=plaz  
    
    def acelerar(self):
        return "Estoy acelerando el coche"

    def frenar(self):
        return "Estoy frenando el coche"

class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

    @property
    def eje(self):
        return self.__eje
    @eje.setter
    def eje(self,eje):
        self.__eje=eje
        
    @property
    def capacidadCarga(self):
        return self.__capacidadCarga
    @capacidadCarga.setter
    def capacidadCarga(self,capacidad):
        self.__capacidadCarga=capacidad
    
    def cargar(self,tipo_carga):
        self.__tipo_carga=tipo_carga
        return self.__tipo_carga

    def acelerar(self):
        return "Estoy acelerando el camion"
    def frenar(self):
        return "Estoy frenando el camion"

class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion=traccion
        self.__cerrada=cerrada

    @property
    def traccion(self):
        return self.__traccion
    @traccion.setter
    def traccion(self,trac):
        self.__traccion=trac

    @property
    def cerrada(self):
        return self.__cerrada
    @cerrada.setter
    def cerrada(self,cerr):
        self.__cerrada=cerr

    def transportar(self,num_pas):
        self.__num_pas=num_pas
        return self.__num_pas

    def acelerar(self):
        return "Estoy acelerando la camioneta"
    def frenar(self):
        return "Estoy frenando la camioneta"

