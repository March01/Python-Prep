#1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos 
    # e imprimir por pantalla
print("(#01)")
list_ciudades=['Lima','Montevideo','Buenos Aires','Sao Paulo','Bogota','Caracas','Monterrey']
print(list_ciudades)
#2) Imprimir por pantalla el segundo elemento de la lista
print("(#02)")
print(list_ciudades[1])
#3) Imprimir por pantalla del segundo al cuarto elemento
print("(#03)")
print(list_ciudades[1:4])
#4) Visualizar el tipo de dato de la lista
print("(#04)")
print(type(list_ciudades))
#5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir,
    #  sin explicitar la posición del último elemento
print("(#05)")
print(list_ciudades[2:])
#6) Visualizar los primeros 4 elementos de la lista
print("(#06)")
print(list_ciudades[:4])
#7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
print("(#07)")
list_ciudades.append('Lima')  
list_ciudades.append('Tokio')  
print(list_ciudades)
#8) Agregar otra ciudad, pero en la cuarta posición
print("(#08)") 
list_ciudades.insert(3,'Quito')  
print(list_ciudades)
#9) Concatenar otra lista a la ya creada
print("(#09)") 
list_ciudades.extend(['Peru','Chile'])  
print(list_ciudades)
#10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. 
   # ¿Se nota alguna particularidad?
print("(#010)") 
print(list_ciudades.index('Lima'))# si busca primero desde la posicion 0 en adelante
#11) ¿Qué pasa si se busca un elemento que no existe?
print("(#011") 
#print(list_ciudades.index('jupiter'))# sale error que el elemento no se encuentra en la lista
#12) Eliminar un elemento de la lista
print("(#012)")
#list_ciudades.remove('Lima') 
list_ciudades.remove('Tokio')
print(list_ciudades)
#13) ¿Qué pasa si el elemento a eliminar no existe?
print("(#013)") 
#list_ciudades.remove('xxx')#sale error no esta en lista
#14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
print("(#014)") 
var1 = list_ciudades.pop()
print(var1)
#15) Mostrar la lista multiplicada por 4
print("(#015)") 
print(list_ciudades*4)
#16) Crear una tupla que contenga los números enteros del 1 al 20
print("(#016)") 
list_num =[]
for i in range (1,21):
    list_num.insert(i,i)
tupla_num=tuple(list_num)
print(list_num)
print(tupla_num)

#17) Imprimir desde el índice 10 al 15 de la tupla
print("(#017)") 

print(tupla_num[10:16])

for i in range (10,16):
    pass
    #print(tupla_num[i])

#18) Evaluar si los números 20 y 30 están dentro de la tupla
print("(#018)") 

print(20 in tupla_num)
print(30 in tupla_num)

for i in range (len(tupla_num)):
    if (tupla_num[i] == 20):
        print("si esta el 20")

    if (tupla_num[i] == 30):
        print("si esta el 30")
   
#19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y 
   # si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
print("(#019)") 

if ('Paris' in list_ciudades):
    info="Paris, si esta en la lista"
else:
    info="Paris,no nestaba en lista ya se agrego"
    list_ciudades.append('Paris')
print(info)

'''
print(list_ciudades)
for i in range(len(list_ciudades)):
    var3 = list_ciudades[i]
    if(var3 == 'Paris'):
        print("si existe : Paris")
    if (i == len(list_ciudades)-1):
        list_ciudades.append('Paris')
print(list_ciudades)
'''
#20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla 
    # y de la lista
print("(#020)") 
print(tupla_num.count(1))
print(list_ciudades.count('Lima'))
#21) Convertir la tupla en una lista
print("(#021)") 
print(list(tupla_num))
#22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
print("(#022)") 

a,b,c=list(tupla_num)[0:3]
print("a: ",a," b: ",b," c: ",c)

#23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". 
   # Agregar tambien otras claves, como puede ser "Pais" y "Continente".
print("(#023)") 
mi_diccionario = {'ciudad':list_ciudades,'Pais':'P','Continente':'C'}
#24) Imprimir las claves del diccionario
print(mi_diccionario)
print("(#024)") 
print(mi_diccionario.keys())
#25) Imprimir las ciudades a través de su clave
print("(#025)") 
print(mi_diccionario['ciudad'])
