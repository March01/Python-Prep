import math
#1)Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
print("(#1)")
var1 = 10
print(var1)
#2) Imprimir el tipo de dato de la constante 8.5
print("(#2)")
var2 = 8.5
print(type(var2))
#3) Imprimir el tipo de dato de la variable creada en el punto 1
print("(#3)")
print(type(var1))
#4) Crear una variable que contenga tu nombre
print("(#4)")
nombre = 'Daukan'
print(nombre)
#5) Crear una variable que contenga un número complejo
print("(#5)")
complejo = 5 + 2j
print(complejo)
#6) Mostrar el tipo de dato de la variable crada en el punto 5
print("(#6)")
print(type(complejo))
#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
print("(#7)") 
var3 = round(math.pi,4)
print(var3)
#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
print("(#8)") 
var4 = 'True'
var5 = True
print("no es lo mismo el tipo de dato de uno es string y el otro bool")
#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print("(#9)") 
print(type(var4))
print(type(var5))
#10) Asignar a una variable, la suma de un número entero y otro decimal
print("(#10)") 
var6 = 5 +5.5
print(var6 )
#11) Realizar una operación de suma de números complejos
print("(#11)") 
var7 = 1 + 2j
var8 = 1 + 3j
print(var7+var8)
#12) Realizar una operación de suma de un número real y otro complejo
print("(#12)") 
var9 = 10
var10 = 1 + 2j
print(var9 + var10)
#13) Realizar una operación de multiplicación
print("(#13)") 
var11 = 7
var12 = 6
print(var11*var12)
#14) Mostrar el resultado de elevar 2 a la octava potencia
print("(#14)") 
var13 = 2**8
print(var13)
#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
print("(#15)") 
var14 = 27/4
print(var14)
#16) De la división anterior solamente mostrar la parte entera
print("(#16)") 
var15 = 27//4
print(var15)
#17) De la división de 27 entre 4 mostrar solamente el resto
print("(#17)") 
var16 = 27%4
print(var16)
#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. 
   # Obtener 27 como resultado
print("(#18)") 
print(var15*4+var16)
#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print("(#19)") 
x = "hola"
y = "Daukan"
print(x+y)
#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print("(#20)") 
print("2" == 2)
print("no son el mismo tipo de dato")
#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print("(#21)") 
print("2" == str(2))
#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
print("(#22)") 
#a = float('3,8')
#print(a)
print("porque , el string tiene coma en vez de punto")
#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
print("(#23)") 
var17 = 3
var17 -= 2
print(var17)
#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print("(#24)") 
print(1<<2)# 0001 << 2 =0100
print("por que desplaza segun el segundo operando dos bits hacia la izquierda al primer operando")
#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo,
  #  siempre arrojaría el mismo resultado?
print("(#25)") 
#print(2 + '2')
print("por que no son mismo tipo de valor, si son el mismo tipo siempre seria el mismo resultado")
#26) Realizar una operación válida entre valores de tipo entero y string
print("(#26)") 
a = "naci en 1"
b = "9"

print(a + b*2 + str(5))