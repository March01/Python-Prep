#1) Crear una variable que contenga un elemento del conjunto de números enteros y 
  # luego imprimir por pantalla si es mayor o menor a cero



print("(#01)")
var1 = -5
if (var1 > 0):
    print('var1 es mayor a cero')
elif (var1 < 0):
    print('var1 es menor que cero')
else:
    print("var1 es igual a cero")

#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
print("(#02)")
var2 = '5'
var3 = 5
if (type(var2) == type(var3)):
    print("mismos datos")
else:
    print("datos distintos")
#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
print("(#03)")
for i in range(1,21):
    if(i%2 == 0):
        print(i,"es par")
    else:
        print(i,"es impar")

#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo
#  a la potencia igual a 3
print("(#04)")
for i in range(0,6):
    print(i**3)

#5) Crear una variable que contenga un número entero y realizar un ciclo for la 
  # misma cantidad de ciclos
print("(#05)")
var4 =10
for i in range(0,var4 ):
    print(i+1)
#6) Utilizar un ciclo while para realizar el factorial de un número guardado 
  # en una variable, sólo si la variable contiene un número entero mayor a 0
print("(#06)")
var5 = 10
var6 = var5
i =1
while (True):
    if (var5 <0):
        print("valor menor que cero")
        break
    if (var5 == 0):
        print("el factorial de ",0,"es",1)
        break
    if (var5 > 0 ):
        var6 = var6*i
        i += 1
    if(i >= var5):
        print("el factorial de ",var5,"es",var6)
        break




#7) Crear un ciclo for dentro de un ciclo while
print("(#07)")
i=0
while (i <10):
    i += 1
 
    print(i)
print("acabo ciclo")

#8) Crear un ciclo while dentro de un ciclo for
print("(#08)")
i=0;
for i in range(1,100):
    if(i>10):
        break
    print("hola",i)
    i += 1
    continue

#9) Imprimir los números primos existentes entre 0 y 30
print("(#09)")
i=0
for x in range(2,31):#0 y 1 no son primos
    for y in range(2,x):#solo es  primo si es divible por el mismo y la unidad
        if(x%y == 0):
            i += 1
            break
    if(i == 0):# no se encontro que sea divisible a parte del 0 y 1
        print(x)
    i = 0


#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
print("(#10)")
print("ya use break en el punto 9")
#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. 
   # ¿Es posible saber en qué medida se optimizó?
print("(#11)")

#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
print("(#12)")

#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12,
  #   dentro del rango de números de 100 a 300
print("(#13)")
i = 100
while (i < 300+1):
    if (i%12 == 0):
        print(i)
    i += 1
#14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar 
   # números primos y dar la opción al usario de buscar el siguiente
print("(#14)")

while (True):
    print ("Buscar numeros primos desde 0 a : ")
    d = input()
    if (d == "esc"):
        break
    for x in range(2,int(d)+1):#0 y 1 no son primos
        for y in range(2,x):#solo es  primo si es divible por el mismo y la unidad
            if(x%y == 0):
                i += 1
                break
        if(i == 0):# no se encontro que sea divisible a parte del 0 y 1
            print(x)
        i = 0
    
#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible 
  # por 3 y además múltiplo de 6
print("(#15)")
i = 100
while (i < 300+1):
    if (i%3 == 0 & i%6 == 0):
        print(i)
        break
    i += 1
    