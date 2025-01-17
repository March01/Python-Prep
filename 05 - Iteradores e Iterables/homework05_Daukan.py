
#1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1



print("(#01)")
i = 15
list_num = []
while (i >= 1):
    list_num.append(i*(-1))
    i -= 1
print(list_num)

#2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
print("(#02)")
i=0
while (i< len(list_num)):
    if (list_num[i]%2 == 0):
        print(list_num[i])
    i += 1


#3) Resolver el punto anterior sin utilizar un ciclo while
print("(#03)")
pares = [i for i in list_num if list_num[i]%2 == 0]
print(pares)
#4) Utilizar el iterable para recorrer sólo los primeros 3 elementos
print("(#04)")
marcador = iter(list_num)
print(next(marcador))
print(next(marcador))
print(next(marcador))
#5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento
print("(#05)")
for i , d in enumerate(list_num):
    print(i,d)
#6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]
print("(#06)")
lista = [1,2,5,7,8,10,13,14,15,17,20]
for i in range(1,20):
    if lista[i-1] != i:
        lista.insert(i-1,i)
print(lista)

'''
7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
  n<sub>0</sub> = 0<br>
  n<sub>1</sub> = 1<br>
  n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
  Crear una lista con los primeros treinta números de la sucesión.<br>'''
print("(#07)")


n1=0
n2=1
list_finob =  [n1]
for i in range (1,30):
    n=n1 + n2
    list_finob.append(n)
    n2=n1
    n1=n
print(list_finob)
# mas comprimido
fibo = [0,1]
n = 2
while(n < 30):
    fibo.append(fibo[n-1]+fibo[n-2])
    n += 1
print(fibo)

#8) Realizar la suma de todos elementos de la lista del punto anterior
print("(#08)")

print(sum(list_finob))

'''
9) La proporción aurea se expresa con una proporción matemática que nace el número 
irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar 
con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente 
de los últimos 5 pares de dos números contiguos:<br>
Donde i es la cantidad total de elementos<br>
n<sub>i-1</sub> / n<sub>i</sub><br>
n<sub>i-2</sub> / n<sub>i-1</sub><br>
n<sub>i-3</sub> / n<sub>i-2</sub><br>
n<sub>i-4</sub> / n<sub>i-3</sub><br>
n<sub>i-5</sub> / n<sub>i-4</sub><br>'''
print("(#09)")
for i in range(0,5):
    prop = list_finob[len(list_finob)-i-2]/list_finob[len(list_finob)-i-1]
    print (prop)


#10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
print("(#10)")
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
list_cadena=list(cadena)
for i in range(len(list_cadena)):
    if list_cadena[i] == 'n':
        print(i)
#comprimido
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i, c in enumerate(cadena):
    if c == 'n':
        print(i)

#11) Crear un diccionario e imprimir sus claves utilizando un iterador
print("(#11)")
mi_dicc = {'padres':['Maria','Marcelo'],'hermanas':['Betssy','Jany','Leynis'],'abuelos':['Ignacia','Rosa','Ydencio']}
for i in mi_dicc:
    print(i)
#12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 
print("(#12)")
list_cadena2 =list(cadena)
for i in list_cadena2:
    print(i)
#cmprimido
recorre = iter(cadena)
largo = len(cadena)
for i in range(0, largo):
    print(next(recorre))


#13) Crear dos listas y unirlas en una tupla utilizando la función zip
print("(#13)")
pares = [2,4,6,8,10,]
impares=[1,3,5,7,9]
comb = zip(pares,impares)
print(tuple(comb))

#14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
print("(#14)")
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
nueva_lis = [i for i in lis if i%7 == 0]
print(nueva_lis)

#15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en 
  # cuenta que un elemento de la lista podría ser otra lista:<br>
print("(#15)")
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
a = 0
for i in range(len(lis)):
    if type(lis[i]) == list:
        a += len(lis[i])
    else:
        a += 1
print(a)

 

#16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
print("(#16)")
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

for i in range(len(lis)):
    if type(lis[i]) != list:
        lis[i]=[list(lis[i]) ]
print(lis)

# otra forma
for indice, elemento in enumerate(lis):
    if (type(elemento) != list):
        lis[indice]=[elemento]
print(lis)
