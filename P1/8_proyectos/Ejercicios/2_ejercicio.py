"""
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el metodo __init__. Calcular
despues la suma, resta, multiplicacion y divisio. Utilzar un metodo para cada una e imprimi los resultados obtenidos.
Llamar a la clase Calculadora.

class Calculadora():
    def __init__(self,val_1,val_2):
        self._val_1=int(val_1)
        self._val_2=int(val_2)

    def suma(self,num1,num2):
        res_suma=num1+num2
        return res_suma
    
    def resta(self,num1,num2):
        res_resta=num1-num2
        return res_resta

    def multiplicacion(self,num1,num2):
        res_mult=num1*num2
        return res_mult
    
    def division(self,num1,num2):
        res_div=num1/num2
        return res_div
    
    @property
    def val_1(self):
        return self._val_1
    @val_1.setter
    def val_1(self,num):
        self._val_1=num

    @property
    def val_2(self):
        return self._val_2
    @val_2.setter
    def val_2(self,num):
        self._val_2=num


op=Calculadora(5,10)
sum=op.suma(op.val_1,op.val_2)
rest=op.resta(op.val_1,op.val_2)
mult=op.multiplicacion(op.val_1,op.val_2)
div=op.division(op.val_1,op.val_2)
print(sum,rest,mult,div)
"""


class Calculadora():
    def __init__(self):
        self._numero1=int(input("Numero 1: "))
        self._numero2=int(input("Numero 2: "))

    def sumar(self):
        return self._numero1+self._numero2
    
    def restar(self):
        return self._numero1-self._numero2
    
    def multiplicar(self):
        return self._numero1*self._numero2
    
    def dividir(self):
        return self._numero1/self._numero2
    
    @property
    def numero1(self):
        return self._numero1
    @numero1.setter
    def numero1(self,num):
        self._numero1=num

    @property
    def numero2(self):
        return self._numero2
    @numero2.setter
    def numero2(self,num):
        self._numero2=num
    
op=Calculadora()
print(f"{op.numero1} + {op.numero2} = {op.sumar()}")
print(f"{op.numero1} - {op.numero2} = {op.restar()}")
print(f"{op.numero1} * {op.numero2} = {op.multiplicar()}")
print(f"{op.numero1} / {op.numero2} = {op.dividir()}")
