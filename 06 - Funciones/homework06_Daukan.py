#1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False
   #si no lo es

print("(#01)")
def comprobar_primo(x):
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
        #return "error"
print(comprobar_primo("a"))
print(comprobar_primo(0))
print(comprobar_primo(1))
print(comprobar_primo(2))
print(comprobar_primo(3))
print(comprobar_primo(4))
print(comprobar_primo(5))

#2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de
   #números y devuelva sólo aquellos que son primos en otra lista
print("(#02)")
def primos_lista(lista):
    listx = []
    for i in range(0,len(lista)):
        if(comprobar_primo(lista[i]) == True):
            listx.append(lista[i])
    return listx

list1 = [0,1,2,3,4,5,6,7,8,10]
list2 = primos_lista(list1)
print(list1)
print(list2)

#3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas 
  #veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera
print("(#03)")
def repetido1(lista):
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

        
list1 = [1,1,9,9,2,2,2,3,1,1,1,4,1,2,5,5,8,8,1,9,9,9,9,9]
print(list1)
num,rep=repetido1(list1)
print("numero: ",num,"  repeticiones: ",rep)



#4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor 
  #o el mayor de los mas repetidos.
print("(#04)")
def repetido(lista,elegir):
    cuenta2 = 0
    cuenta1 =0
    dato = 0
    dato_list=[]
    for i in lista:#primero creamos lista con numeros sin repeticiones
        if i not in dato_list:
            dato_list.append(i)
    print(dato_list)
    cuenta1= lista.count(dato_list[0])
    for i in range (0,len(dato_list)):#luego buscamos dichos numeros las veces q se repiten
        cuenta2=lista.count(dato_list[i])
        if (cuenta1 > cuenta2 and elegir == "mayor"):#mayor)
            continue
        #print("cuenta1: ",cuenta1 , "cuenta2: ",cuenta2)
        if (cuenta1< cuenta2 and elegir == "menor"):#menor
            #print(cuenta1)
            continue
        else:
            cuenta1 = cuenta2
            dato = dato_list[i]
    return dato,cuenta1



print("(#04)")
def repetido1(lista,elegir):
    cuenta2 = 0
    cuenta1 =0
    dato_list=[]
    
    for i in lista:#primero creamos lista con numeros sin repeticiones
        if i not in dato_list:
            dato_list.append(i)
    cuenta1= lista.count(dato_list[0])
    
    for i in range (0,len(dato_list)):#luego buscamos dichos numeros las veces q se repiten
        cuenta2=lista.count(dato_list[i])
        if (cuenta1 > cuenta2 ):#mayor)
            continue
        else:
            cuenta1 = cuenta2
            maximo = dato_list[i]
    if(elegir == "mayor"):
        return maximo,cuenta1
    if(elegir == "menor"):
        dato_list.remove(maximo)
        for i in range (0,len(dato_list)):
            cuenta2=lista.count(dato_list[i])
            if (cuenta1 > cuenta2 ):#menor
                continue
            else:
                cuenta1 = cuenta2
                maximo = dato_list[i]
    return maximo,cuenta1
       

list1 = [0,0,1,8,2,9,99,9,2,2,2,1,1,1,1,2,8,8,1,9,9,5,9,7,7,9,9,8,8,8,8,1,2,28,8,8,8,8,2,2,2]
#list1 = [10,1,5,6,8,10,22,5,6,4,11,10,9,5]
print(list1)
num,rep=repetido1(list1,"mayor")
print("numero: ",num,"  repeticiones mayor: ",rep)
num,rep=repetido1(list1,"menor")
print("numero: ",num,"  repeticiones menor: ",rep)#notar que buscara toda la lista asi esten repetidos al inicio


#5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
#   Fórmula 1	: (°C × 9/5) + 32 = °F<br>
#   Fórmula 2	: °C + 273.15 = °K<br>
#   Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
print("(#05)")

def temp(t,m1,m2):
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

print(temp(22.5,"C","K"))
print(temp(22,"C","F"))
print(temp(22,"F","C"))
print(temp(22,"F","K"))
print(temp(22,"K","C"))
print(temp(22,"K","F"))
#6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del 
 #  punto 5, hacer un print para cada combinación de los mismos:
print("(#06)")
temps_list =[20]
convs_list= ["CF","CK","FC","FK","KF","KC"]
for d in temps_list:
    for i in convs_list:
        l1 =list(i)#convierto en una lista cada elemento de la lista convs_list
        marcador=iter(l1)
        print(i,temp(d,str(next(marcador)),str(next(marcador))))



#7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario
 # puede equivocarse y enviar de parámetro un número no entero o negativo
print("(#07)")
def fact(n):
    if type(n) != int:
        return "error_no es entero"
    if n < 0:
        return "error_valor negativo"
    
    if n==0:
        return 1
    else:
        return n*fact(n-1)
  
print(fact("s"))
print(fact(2.5))
print(fact(-5))
print(fact(-5.4))
print(fact(0))
print(fact(1))
print(fact(6))