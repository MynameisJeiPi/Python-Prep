# MÓDULO DE HERRAMIENTAS 

class Herramientas:
    def __init__(self,lista_números):
        if not isinstance(lista_números,list):
            raise ValueError("Solo se admiten listas.")
        for núm in lista_números:
            if not isinstance(núm,int):
                raise ValueError("La lista solo debe contener números enteros.")
        self.lista = lista_números


    # Función que nos dice qué hay en la lista

    def longitud_de_lista(self):
        print(len(self.lista))

    # Función para verificar primos.

    def primo(self):
        lista_primos = []
        for x in self.lista:
            assert type(x) == int, "Solo se admiten números enteros." # Assert para contemplar elementos no int.
            num_prim=True
            for divisor in range(2,x):
                if x%divisor==0:
                    num_prim=False
            if num_prim==True:
                lista_primos.append(True)
            else:
                lista_primos.append(False)
        return lista_primos

    # Función para calcular el valor modal.

    def valor_moda(self): 
        números_contados = [] 
        ya_evaluados = [] 
        count = 0 
        try:
            for elemento in self.lista:
                int(elemento)
            for núm in self.lista:
                if núm in ya_evaluados:
                    continue
                ya_evaluados.append(núm) 
                for i in self.lista: 
                    if núm == i:
                        count +=1
                        s = i 
                números_contados.append((s,count))
                count=0 
            cuenta_max=(0)
            número_max=(0)
            for número, cuenta in números_contados: 
                    if cuenta > cuenta_max: 
                        cuenta_max=cuenta
                        número_max=número 
            return ("Se repite " + str(cuenta_max) + " veces el número " + str(número_max))
        except: 
            print("Solo se admiten números enteros.")

    # Función para convertir los grados.
    
    def conversión_grados(self,origen,destino):
        assert origen in ["Celsius","Kelvin","Fahrenheit"], "Parámetro inválido. Los parámetros válidos son Celsius, Kelvin y Fahrenheit."
        assert destino in ["Celsius","Kelvin","Fahrenheit"], "Parámetro inválido. Los parámetros válidos son Celsius, Kelvin y Fahrenheit."
        for valor in self.lista:
            if origen == "Celsius":
                if destino == "Kelvin":
                    resultado = (valor+273.15)
                elif destino == "Fahrenheit":
                    resultado = ((valor*9/5)+32)
                elif destino == "Celsius":
                    resultado = valor
            elif origen == "Kelvin":
                if destino == "Celsius":
                    resultado = (valor-273.15)
                elif destino == "Fahrenheit":
                    resultado =  (((valor-273.15)*1.8)+32)    
                elif destino == "Kelvin":
                    resultado = valor       
            elif origen == "Fahrenheit":
                if destino == "Kelvin":
                    resultado = ((valor-32)*(5/9)+273.15)
                elif destino == "Celsius":
                    resultado = ((valor-32)*5/9)
                elif destino == "Fahrenheit":
                    resultado = valor
            print(valor,origen,"es igual a",resultado,str(destino)+".")
        
    def conversión_grados_prueba(self,origen,destino):
        lista_resultados = []
        assert origen in ["Celsius","Kelvin","Fahrenheit"], "Parámetro inválido. Los parámetros válidos son Celsius, Kelvin y Fahrenheit."
        assert destino in ["Celsius","Kelvin","Fahrenheit"], "Parámetro inválido. Los parámetros válidos son Celsius, Kelvin y Fahrenheit."
        for valor in self.lista:
            if origen == "Celsius":
                if destino == "Kelvin":
                    resultado = (valor+273.15)
                elif destino == "Fahrenheit":
                    resultado = ((valor*9/5)+32)
                elif destino == "Celsius":
                    resultado = valor
            elif origen == "Kelvin":
                if destino == "Celsius":
                    resultado = (valor-273.15)
                elif destino == "Fahrenheit":
                    resultado =  (((valor-273.15)*1.8)+32)    
                elif destino == "Kelvin":
                    resultado = valor       
            elif origen == "Fahrenheit":
                if destino == "Kelvin":
                    resultado = ((valor-32)*(5/9)+273.15)
                elif destino == "Celsius":
                    resultado = ((valor-32)*5/9)
                elif destino == "Fahrenheit":
                    resultado = valor
            lista_resultados.append(resultado)
        return lista_resultados
        
    # Función para calcular el factorial de un número.

    def factorial(self):
        número = 0
        for x in self.lista:
            if type(x) == int and x > 0:
                fact = x
                while x > 1:
                    número = (fact)*(x-1)
                    fact = número
                    x-=1
                print(número)
            else:
                print("Parámetro inválido.")

    # Función factorial de prueba
    def factorial(self):
        número = 0
        factoriales = []
        for x in self.lista:
            if type(x) == int and x > 0:
                fact = x
                while x > 1:
                    número = (fact)*(x-1)
                    fact = número
                    x-=1
                factoriales.append(número)
            else:
                print("Parámetro inválido.")
        return factoriales