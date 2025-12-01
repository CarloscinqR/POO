from tkinter import *
from controller import funciones
from model import operaciones

class Vistas():
    def __init__(self,ventana):
        ventana.geometry("600x450")
        ventana.title("Calculadora")
        Vistas.interfaz(ventana)
    
    @staticmethod
    def menuPrincipal(ventana):
        Vistas.borrarPantalla(ventana)
        mnBar=Menu(ventana)
        ventana.config(menu=mnBar)

        operacionMenu=Menu(mnBar,tearoff=FALSE)
        mnBar.add_cascade(label="Archivo",menu=operacionMenu)
        operacionMenu.add_command(label="Agregar",command=lambda: Vistas.interfaz(ventana))
        operacionMenu.add_command(label="Consultar",command=lambda: Vistas.interfazConsultar(ventana))
        operacionMenu.add_command(label="Modificar",command=lambda: Vistas.interfazModificar(ventana))
        operacionMenu.add_command(label="Borrar",command=lambda: Vistas.intrfaz_buscar_eliminar(ventana))
        operacionMenu.add_separator()
        operacionMenu.add_command(label="Salir",command=ventana.quit)
   
    @staticmethod
    def interfaz(ventana):
        Vistas.menuPrincipal(ventana)
        num1=IntVar()
        txtNum1=Entry(ventana,textvariable=num1,justify=CENTER,width=10)
        txtNum1.pack()
        txtNum1.focus()
        num2=IntVar()
        txtNum2=Entry(ventana,textvariable=num2,justify=CENTER,width=10)
        txtNum2.pack(pady=20)

        btnSuma=Button(ventana,command=lambda: funciones.Controladores.operacion(num1.get(),num2.get(),"suma","+"),text="+ SUMA",border=4,relief=RIDGE)
        btnSuma.pack()

        btnResta=Button(ventana,command=lambda: funciones.Controladores.operacion(num1.get(),num2.get(),"resta","-"),text="- RESTA",border=4,relief=RIDGE)
        btnResta.pack()

        btnMulti=Button(ventana,command=lambda: funciones.Controladores.operacion(num1.get(),num2.get(),"multiplicacion","X"),text="* MULTIPLICACION",border=4,relief=RIDGE)
        btnMulti.pack()

        btnDivision=Button(ventana,command=lambda: funciones.Controladores.operacion(num1.get(),num2.get(),"division","/"),text="/ DIVISION",border=4,relief=RIDGE)
        btnDivision.pack()

        btnSalir=Button(ventana,command=ventana.quit,text="Salir",border=4,relief=RIDGE,background="#FF0000",activebackground="#810404")
        btnSalir.pack(pady=30)
   
    @staticmethod
    def intrfaz_buscar_eliminar(ventana):
        Vistas.borrarPantalla(ventana)
        Vistas.menuPrincipal(ventana)

        lblTitulo=Label(ventana,text=f".:Buscar una operacion:.")
        lblTitulo.pack(pady=10)

        lblId=Label(ventana,text=f"ID de la Operacion:")
        lblId.pack(pady=10)

        id=IntVar()
        txtId=Entry(ventana,textvariable=id)
        txtId.pack(pady=10)
        txtId.focus()

        btnEliminar=Button(ventana,text=f"Buscar",command=lambda: funciones.Controladores.buscarId(ventana,id.get()))
        btnEliminar.pack(pady=10)

        btnVolver=Button(ventana,text=f"Volver",command=lambda: Vistas.interfaz(ventana),border=4,relief=RIDGE,background="#0400FF",activebackground="#060481")
        btnVolver.pack(pady=10)

    @staticmethod
    def interfazEliminar(ventana,opid):
        Vistas.borrarPantalla(ventana)
        Vistas.menuPrincipal(ventana)

        lblTitulo=Label(ventana,text=f".:Borrar una operacion:.")
        lblTitulo.pack(pady=10)

        lblId=Label(ventana,text=f"ID de la Operacion:")
        lblId.pack(pady=10)

        id=IntVar()
        txtId=Entry(ventana,textvariable=id)
        txtId.delete(0,END)
        txtId.insert(0,opid)
        txtId.config(state="readonly")
        txtId.pack(pady=10)
        txtId.focus()

        btnEliminar=Button(ventana,text=f"Eliminar",command=lambda: funciones.Controladores.respuesta_sql("Eliminar registro",operaciones.Operaciones.eliminar(id.get())))
        btnEliminar.pack(pady=10)

        btnVolver=Button(ventana,text=f"Volver",command=lambda: Vistas.interfaz(ventana),border=4,relief=RIDGE,background="#0400FF",activebackground="#060481")
        btnVolver.pack(pady=10)
    
    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
    
    @staticmethod
    def interfazConsultar(ventana):
        Vistas.borrarPantalla(ventana)
        Vistas.menuPrincipal(ventana)
    
        lblTitulo=Label(ventana,text="Listado de Operaciones")
        lblTitulo.pack(pady=10)

        lblTabla=Label(ventana,text=funciones.Controladores.mostrar(),width=400)
        lblTabla.pack(pady=10)

        btnVolver=Button(ventana,text=f"Volver",command=lambda: Vistas.interfaz(ventana),border=4,relief=RIDGE,background="#0400FF",activebackground="#060481")
        btnVolver.pack(pady=10)

    @staticmethod
    def interfazModificar(ventana):
        Vistas.borrarPantalla(ventana)
        Vistas.menuPrincipal(ventana)
    
        lblTitulo=Label(ventana,text="Cambiar una operacion")
        lblTitulo.pack(pady=10)

        lblId=Label(ventana,text="Id de la operacion")
        lblId.pack(pady=5)
        id=IntVar()
        txtId=Entry(ventana,textvariable=id)
        txtId.pack(pady=5)

        lblNumero1=Label(ventana,text="Numero 1")
        lblNumero1.pack(pady=5)
        num1=IntVar()
        txtNumero1=Entry(ventana,textvariable=num1)
        txtNumero1.pack(pady=5)

        lblNumero2=Label(ventana,text="Numero 2")
        lblNumero2.pack(pady=5)
        num2=IntVar()
        txtNumero2=Entry(ventana,textvariable=num2)
        txtNumero2.pack(pady=5)

        lblSigno=Label(ventana,text="Signo")
        lblSigno.pack(pady=5)
        signo=StringVar()
        txtSigno=Entry(ventana,textvariable=signo)
        txtSigno.pack(pady=5)

        lblResultado=Label(ventana,text="Nuevo resultado")
        lblResultado.pack(pady=5)
        resul=DoubleVar()
        txtResultado=Entry(ventana,textvariable=resul)
        txtResultado.pack(pady=5)

        btnGuardar=Button(ventana,text="Guardar",command=lambda: funciones.Controladores.respuesta_sql("Modificar Registro",operaciones.Operaciones.actualizar(num1.get(),num2.get(),signo.get(),resul.get(),id.get())))
        btnGuardar.pack(pady=5)
        btnVolver=Button(ventana,text=f"Volver",command=lambda: Vistas.interfaz(ventana),border=4,relief=RIDGE,background="#0400FF",activebackground="#060481")
        btnVolver.pack(pady=5)