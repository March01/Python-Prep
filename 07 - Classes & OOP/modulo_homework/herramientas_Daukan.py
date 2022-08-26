
class herramientasx:
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