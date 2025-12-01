from tkinter import *
from controller import funciones
ventana=Tk()
ventana.geometry("600x400")
ventana.title("Calculadora")
def interfaz():
    num1=IntVar()
    txtNum1=Entry(ventana,textvariable=num1,justify=CENTER,width=10)
    txtNum1.pack()
    num2=IntVar()
    txtNum2=Entry(ventana,textvariable=num2,justify=CENTER,width=10)
    txtNum2.pack(pady=20)

    btnSuma=Button(ventana,command=lambda: funciones.operacion(num1.get(),num2.get(),"suma","+"),text="+ SUMA",border=4,relief=RIDGE)
    btnSuma.pack()

    btnResta=Button(ventana,command=lambda: funciones.operacion(num1.get(),num2.get(),"resta","-"),text="- RESTA",border=4,relief=RIDGE)
    btnResta.pack()

    btnMulti=Button(ventana,command=lambda: funciones.operacion(num1.get(),num2.get(),"multiplicacion","X"),text="* MULTIPLICACION",border=4,relief=RIDGE)
    btnMulti.pack()

    btnDivision=Button(ventana,command=lambda: funciones.operacion(num1.get(),num2.get(),"division","/"),text="/ DIVISION",border=4,relief=RIDGE)
    btnDivision.pack()

    btnSalir=Button(ventana,command=ventana.quit,text="Salir",border=4,relief=RIDGE,background="#FF0000",activebackground="#810404")
    btnSalir.pack(pady=30)


    ventana.mainloop()