from tkinter import messagebox
def operacion(a,b,op,caracter):
    match op:
        case "suma":
            opera=a+b
        case "resta":
            opera=a-b
        case "multiplicacion":
            opera=a*b
        case "division":
            opera=a/b
    messagebox.showinfo(message=f"El resultado de {a} {caracter} {b} es: {opera}",title=op)