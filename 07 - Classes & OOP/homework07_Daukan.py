## Clases y Programación Orientada a Objetos

#1) Crear la clase vehículo que contenga los atributos:
#Color
#Si es moto, auto, camioneta ó camión
#Cilindrada del motor
#print("(#01)")
from cgitb import handler
from msilib import PID_LASTSAVE_DTM


class vehiculo:
    def __init__(self,color,tipo,cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
#2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:
#Acelerar
#Frenar
#Doblar
#print("(#02)")
class vehiculo:
    def __init__(self,color,tipo,cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0
    def Acelerar(self,vel):
        self.velocidad += vel
    def Frenar(self,vel):
        self.velocidad -= vel
    def Doblar(self,grados):
        self.direccion += grados
  
    
    # segun punto #4
    def estado(self):
        print("su velocidad es ",self.velocidad," y su direccion es de ",self.direccion)
    def caracteristicas(self):
        print('mi vehiculo es de color ', self.color, ' es una ', self.tipo, ' y de cilindrada',self.cilindrada)

#3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado
print("(#03)")
p1 = vehiculo('amarillo','auto','100')
p2 = vehiculo('rojo','moto','200')
p3 = vehiculo('negro','camioneta','300')

p1.Acelerar(10)
p2.Acelerar(20)
p3.Acelerar(30)
p1.Frenar(-20)
p2.Doblar(-10)
p1.Doblar(20)


#4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad
   #se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada
print("(#04)")
p1 = vehiculo('amarillo','auto','100')
p1.caracteristicas()
p1.estado()
p1.Acelerar(20)
p1.estado()
p1.Acelerar(20)
p1.estado()
p1.Doblar(-20)
p1.estado()
p1.Doblar(20)
p1.estado()

#5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6
  #Verificar Primo
  #Valor modal
  #Conversión grados
  #Factorial
print("(#05)")
class herramientas:
    def __define__(self) -> None:
        pass
    #########################################  Verificar Primo
    def comprobar_primo(self,x):
        ok=True
        if (type(x) == int):
            if (x > 0 and x != 1):
                for i in range (2,x):
                    if (x%i == 0):
                        ok = False
                        return ok
            else:
                ok=False
            return ok
        else:
            return not(ok)
########################################  Valor modal
    def repetido1(self,lista):
        cuenta2 = 0
        dato_list=[]
        for i in lista:#primero creamos lista con numeros sin repeticiones
            if i not in dato_list:
                dato_list.append(i)
        for i in range (0,len(dato_list)):#luego buscamos dichos numeros las veces q se repiten
            cuenta1=lista.count(dato_list[i])
            if cuenta1 > cuenta2 :
                dato = dato_list[i]
                cuenta2 = cuenta1
        return dato,cuenta2
##########################################   Conversión grados
    def temp(self,t,m1,m2):
        conv = 0
        if (m1== "C" and m2== "F"):
            conv=(t*(9/5))+32
            return round(conv,2)
        if (m1== "C" and m2== "K"):
            conv=t+273.15
            return round(conv,2)
        if (m1== "F" and m2== "C"):
            conv=((t-32)/9)*5
            return round(conv,2)
        if (m1== "F" and m2== "K"):
            conv=(((t-32)*5)/9)+273.15
            return round(conv,2)
        if (m1== "K" and m2== "C"):
            conv=t-273.15
            return round(conv,2)
        if (m1== "K" and m2== "F"):
            conv=((t-273.15)*(9/5))+32
            return round(conv,2)
    ##########################################    Factorial
    def fact(self,n):
        if type(n) != int:
            return "error_no es entero"
        if n < 0:
            return "error_valor negativo"
        
        if n==0:
            return 1
        else:
            return n*self.fact(n-1)#agregar el self.

#6) Probar las funciones incorporadas en la clase del punto 5
print("(#06)")
h=herramientas()
print(h.comprobar_primo(10))
lista = [1,1,2,2,2,5,5,5,5,8,2,1,3,3]
print(h.repetido1(lista))
print(h.temp(22,"K","C"))
print(h.fact(6))
#7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual 
  # se aplquen las funciones incorporadas
print("(#07)")
class herramientas:
    def __init__(self,lista_num):
        self.lista = lista_num
    ########################################  Valor modal  > solo la lista aqui no necesitara otro metodo
    def repetido1(self):
        cuenta2 = 0
        dato_list=[]
        for i in self.lista:#primero creamos lista con numeros sin repeticiones  agregar self.
            if i not in dato_list:
                dato_list.append(i)
        for i in range (0,len(dato_list)):#luego buscamos dichos numeros las veces q se repiten
            cuenta1=self.lista.count(dato_list[i]) #agregar self.
            if cuenta1 > cuenta2 :
                dato = dato_list[i]
                cuenta2 = cuenta1
        return dato,cuenta2
     #******************************************************   
    def comprobar_primo(self):
        for i in self.lista:
            if(self.__comprobar_primo(i) ==True):
                print(i,"es primo")
            else:
                print(i,"no es primo")

    def temp(self,tipo1,tipo2):
        for i in self.lista:
            print(i,"grados",tipo1," son: ",self.__temp(i,tipo1,tipo2),"grados",tipo2)

    def fact(self):
        for i in self.lista:
            print("el factorial de ",i," es ",self.__fact(i))  
    #*******************************************************

    #########################################  Verificar Primo
    def __comprobar_primo(self,x):
        ok=True
        if (type(x) == int):
            if (x > 0 and x != 1):
                for i in range (2,x):
                    if (x%i == 0):
                        ok = False
                        return ok
            else:
                ok=False
            return ok
        else:
            return not(ok)

##########################################   Conversión grados
    def __temp(self,t,m1,m2):
        conv = 0
        if (m1== "C" and m2== "F"):
            conv=(t*(9/5))+32
            return round(conv,2)
        if (m1== "C" and m2== "K"):
            conv=t+273.15
            return round(conv,2)
        if (m1== "F" and m2== "C"):
            conv=((t-32)/9)*5
            return round(conv,2)
        if (m1== "F" and m2== "K"):
            conv=(((t-32)*5)/9)+273.15
            return round(conv,2)
        if (m1== "K" and m2== "C"):
            conv=t-273.15
            return round(conv,2)
        if (m1== "K" and m2== "F"):
            conv=((t-273.15)*(9/5))+32
            return round(conv,2)
    ##########################################    Factorial
    def __fact(self,n):
        if type(n) != int:
            return "error_no es entero"
        if n < 0:
            return "error_valor negativo"
        
        if n==0:
            return 1
        else:
            return n*self.__fact(n-1)#agregar el self.

h = herramientas([1,1,2,5,8,8,9,11,15,16,16,16,18,20])
h.comprobar_primo()
x,y=h.repetido1()
print("el numero: ",x," se repite",y,"veces")
h.temp("K","C")
h.fact()
#8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. 
  # Luego realizar la importación del módulo y probar alguna de sus funciones
print("(#08)")

from modulo_homework.herramientas_Daukan import *


x= herramientasx([1,1,2,5,8,8,9,11,15,16,16,16,18,20])
x.comprobar_primo()
