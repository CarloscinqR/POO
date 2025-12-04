from tkinter import *
from tkinter import messagebox
class InterfacesMenu():
    def __init__(self,ventana):
        ventana.geometry("800x600")
        ventana.title("Coches system")
        self.menu_principal(ventana)

    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def menu_principal(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Menu principal")
        lblTitulo.pack(pady=5)
        btnCoches=Button(ventana,text="1.-Coches",command=lambda : self.menu_acciones(ventana,"coches"))
        btnCoches.pack(pady=5)
        btnCamiones=Button(ventana,text="2.-Camiones",command=lambda: self.menu_acciones(ventana,"camiones"))
        btnCamiones.pack(pady=5)
        btnCamionetas=Button(ventana,text="3.-Camionetas",command=lambda: self.menu_acciones(ventana,"camionetas"))
        btnCamionetas.pack(pady=5)
        btnSalir=Button(ventana,text="4.-Salir",command=ventana.quit)
        btnSalir.pack(pady=5)

    def menu_acciones(self,ventana,vehiculo):
        global tipo
        tipo=vehiculo
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Menu de {tipo}")
        lblTitulo.pack(pady=5)
        if tipo=="coches":
            btnAgregar=Button(ventana,text="1.-Agregar",command=lambda: self.coches_agregar(ventana))
            btnAgregar.pack(pady=5)
            btnMostrar=Button(ventana,text="2.-Mostrar",command=lambda: self.coches_mostrar(ventana))
            btnMostrar.pack(pady=5)
        elif tipo=="camionetas":
            btnAgregar=Button(ventana,text="1.-Agregar",command=lambda: self.camionetas_agregar(ventana))
            btnAgregar.pack(pady=5)
            btnMostrar=Button(ventana,text="2.-Mostrar",command=lambda: self.camionetas_mostrar(ventana))
            btnMostrar.pack(pady=5)
        elif tipo=="camiones":
            btnAgregar=Button(ventana,text="1.-Agregar",command=lambda: self.camiones_agregar(ventana))
            btnAgregar.pack(pady=5)
            btnMostrar=Button(ventana,text="2.-Mostrar",command=lambda: self.camiones_mostrar(ventana))
            btnMostrar.pack(pady=5)

        btnCambiar=Button(ventana,text="3.-Cambiar",command=lambda: self.intrfaz_buscar_cambiar(ventana))
        btnCambiar.pack(pady=5)
        btnEliminar=Button(ventana,text="4.-Eliminar",command=lambda: self.intrfaz_buscar_eliminar(ventana))
        btnEliminar.pack(pady=5)
        btnSalir=Button(ventana,text="5.-Volver",command=lambda: self.menu_principal(ventana))
        btnSalir.pack(pady=5)


#Parte de coche
    def coches_agregar(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Agregar coches")
        lblTitulo.pack(pady=5)
        lblMarca=Label(ventana,text="Inserte la marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblPotencia=Label(ventana,text="Inserte la potencia")
        lblPotencia.pack()
        txtPotencia=Entry(ventana)
        txtPotencia.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        btnAgregar=Button(ventana,text="Agregar",command= lambda: "")
        btnAgregar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def coches_mostrar(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Coches agregados")
        lblTitulo.pack(pady=5)
        filas=""
        registros=[("1","Subaru","Azul","2020","160","400","4"),("2","Amg","Rojo","2021","250","400","2")]
        if len(registros)>0:
            num_autos=1
            for fila in registros:
                filas=filas+f"\nAuto #{num_autos} con ID: {fila[0]} \nMarca: {fila[1]} Color: {fila[2]} Modelo: {fila[3]} Velocidad: {fila[4]} Potencia: {fila[5]} Plazas: {fila[6]}"
                num_autos+=1
        else:
            messagebox.showinfo(message="No existen coches en el sistema")

        lblNote=Label(ventana,text=filas)
        lblNote.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command=lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def coches_cambiar(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Cambiar coche")
        lblTitulo.pack(pady=5)

        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()

        lblMarca=Label(ventana,text="Inserte la marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblPotencia=Label(ventana,text="Inserte la potencia")
        lblPotencia.pack()
        txtPotencia=Entry(ventana)
        txtPotencia.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        btnGuardar=Button(ventana,text="Guardar",command= lambda: "")
        btnGuardar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def coches_eliminar(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Eliminar un coche")
        lblTitulo.pack(pady=5)
        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()
        btnEliminar=Button(ventana,text="Eliminar",command= lambda:"")
        btnEliminar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)


#Parte de camiones
    def camiones_agregar(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Agregar {tipo}")
        lblTitulo.pack(pady=5)
        lblMarca=Label(ventana,text="Inserte la marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblPotencia=Label(ventana,text="Inserte la potencia")
        lblPotencia.pack()
        txtPotencia=Entry(ventana)
        txtPotencia.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        lblEje=Label(ventana,text="Ingrese el eje")
        lblEje.pack(pady=5)
        txtEje=Entry(ventana)
        txtEje.pack()

        lblCapacidad=Label(ventana,text="Ingrese la capacidad")
        lblCapacidad.pack(pady=5)
        txtCapacidad=Entry(ventana)
        txtCapacidad.pack()

        btnAgregar=Button(ventana,text="Agregar",command= lambda: "")
        btnAgregar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def camiones_mostrar(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Mostrar {tipo}")
        lblTitulo.pack(pady=5)
        filas=""
        registros=registros=[("1","Subaru","Azul","2020","160","400","4","6","2"),("2","Amg","Rojo","2021","250","400","2","10",4)]
        if len(registros)>0:
            num_camion=1
            for fila in registros:
                filas=filas+f"\nCamion #{num_camion} con ID: {fila[0]} \nMarca: {fila[1]} Color: {fila[2]} Modelo: {fila[3]} Velocidad: {fila[4]} Potencia: {fila[5]} Plazas: {fila[6]} Eje: {fila[7]} Capacidad: {fila[8]}"
                num_camion+=1
        else:
            messagebox.showinfo(message="No existen camiones en el sistema")

        lblNote=Label(ventana,text=filas)
        lblNote.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def camiones_cambiar(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Modificar {tipo}")
        lblTitulo.pack(pady=5)
        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()
        lblMarca=Label(ventana,text="Inserte la marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblPotencia=Label(ventana,text="Inserte la potencia")
        lblPotencia.pack()
        txtPotencia=Entry(ventana)
        txtPotencia.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        lblEje=Label(ventana,text="Ingrese el eje")
        lblEje.pack(pady=5)
        txtEje=Entry(ventana)
        txtEje.pack()

        lblCapacidad=Label(ventana,text="Ingrese la capacidad")
        lblCapacidad.pack(pady=5)
        txtCapacidad=Entry(ventana)
        txtCapacidad.pack()

        btnGuardar=Button(ventana,text="Guardar",command= lambda: "")
        btnGuardar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def camiones_eliminar(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Eliminar un {tipo}")
        lblTitulo.pack(pady=5)
        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()
        btnEliminar=Button(ventana,text="Eliminar",command= lambda: "")
        btnEliminar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)


#Parte de camionetas
    def camionetas_agregar(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Agregar {tipo}")
        lblTitulo.pack(pady=5)
        lblMarca=Label(ventana,text="Inserte la marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblPotencia=Label(ventana,text="Inserte la potencia")
        lblPotencia.pack()
        txtPotencia=Entry(ventana)
        txtPotencia.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        lblTraccion=Label(ventana,text="Ingrese la traccion")
        lblTraccion.pack(pady=5)
        lbxTraccion=Listbox(ventana,width=10,height=3,selectmode="single",exportselection=False)
        traccion=["Trasera","Delantera","Total"]
        for i in traccion:
            lbxTraccion.insert(END,i)
        lbxTraccion.pack()

        lblCerrada=Label(ventana,text="Es cerrada?")
        lblCerrada.pack(pady=5)
        lbxCerrada=Listbox(ventana,width=10,height=2,selectmode="single",exportselection=False)
        eleccion=["Si","No"]
        for i in eleccion:
            lbxCerrada.insert(END,i)
        lbxCerrada.pack()

        btnAgregar=Button(ventana,text="Agregar",command= lambda: "")
        btnAgregar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def camionetas_mostrar(self,ventana):

        
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Mostrar {tipo}")
        lblTitulo.pack(pady=5)
        filas=""
        registros=""
        if len(registros)>0:
            num_camion=1
            for fila in registros:
                filas=filas+f"\nAuto #{num_camion} con ID: {fila[0]} \nMarca: {fila[1]} Color: {fila[2]} Modelo: {fila[3]} Velocidad: {fila[4]} Potencia: {fila[5]} Plazas: {fila[6]} Traccion: {fila[7]} Cerrada: {fila[8]}"
                num_camion+=1
        else:
            messagebox.showinfo(message=f"No existen {tipo} en el sistema")

        lblNote=Label(ventana,text=filas)
        lblNote.pack(pady=5)

        btnVolver=Button(ventana,text="Volver",command=lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def camionetas_cambiar(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Modificar {tipo}")
        lblTitulo.pack(pady=5)
        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()
        lblMarca=Label(ventana,text="Inserte la marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblPotencia=Label(ventana,text="Inserte la potencia")
        lblPotencia.pack()
        txtPotencia=Entry(ventana)
        txtPotencia.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        lblTraccion=Label(ventana,text="Ingrese la traccion")
        lblTraccion.pack(pady=5)
        lbxTraccion=Listbox(ventana,width=10,height=3,selectmode="single",exportselection=False)
        traccion=["Trasera","Delantera","Total"]
        for i in traccion:
            lbxTraccion.insert(END,i)
        lbxTraccion.pack()

        lblCerrada=Label(ventana,text="Es cerrada?")
        lblCerrada.pack(pady=5)
        lbxCerrada=Listbox(ventana,width=10,height=2,selectmode="single",exportselection=False)
        eleccion=["Si","No"]
        for i in eleccion:
            lbxCerrada.insert(END,i)
        lbxCerrada.pack()

        btnGuardar=Button(ventana,text="Guardar",command= lambda: "")
        btnGuardar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def camionetas_eliminar(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Eliminar una {tipo}")
        lblTitulo.pack(pady=5)
        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()
        btnEliminar=Button(ventana,text="Eliminar",command= lambda: "")
        btnEliminar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)



    def intrfaz_buscar_cambiar(self,ventana):
        self.borrarPantalla(ventana)
       
        lblTitulo=Label(ventana,text=f".:Buscar una vehiculo:.")
        lblTitulo.pack(pady=10)

        lblId=Label(ventana,text=f"ID del vehiculo:")
        lblId.pack(pady=10)

        id=IntVar()
        txtId=Entry(ventana,textvariable=id)
        txtId.pack(pady=10)
        txtId.focus()
        if tipo=="coches":
            btnCambiar=Button(ventana,text=f"Buscar",command=lambda: self.coches_cambiar(ventana))
            btnCambiar.pack(pady=10)
        elif tipo=="camiones":
            btnCambiar=Button(ventana,text=f"Buscar",command=lambda: self.camiones_cambiar(ventana))
            btnCambiar.pack(pady=10)
        elif tipo=="camionetas":
            btnCambiar=Button(ventana,text=f"Buscar",command=lambda: self.camionetas_cambiar(ventana))
            btnCambiar.pack(pady=10)
        btnVolver=Button(ventana,text=f"Volver",command=lambda:self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=10)

    def intrfaz_buscar_eliminar(self,ventana):
        self.borrarPantalla(ventana)
       
        lblTitulo=Label(ventana,text=f".:Buscar una vehiculo:.")
        lblTitulo.pack(pady=10)

        lblId=Label(ventana,text=f"ID del vehiculo:")
        lblId.pack(pady=10)

        id=IntVar()
        txtId=Entry(ventana,textvariable=id)
        txtId.pack(pady=10)
        txtId.focus()
        if tipo=="coches":
            btnEliminar=Button(ventana,text=f"Buscar",command=lambda: self.coches_eliminar(ventana))
            btnEliminar.pack(pady=10)
        elif tipo=="camiones":
            btnEliminar=Button(ventana,text=f"Buscar",command=lambda: self.camiones_eliminar(ventana))
            btnEliminar.pack(pady=10)
        elif tipo=="camionetas":
            btnEliminar=Button(ventana,text=f"Buscar",command=lambda: self.camionetas_eliminar(ventana))
            btnEliminar.pack(pady=10)


        btnVolver=Button(ventana,text=f"Volver",command=lambda:self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=10)
