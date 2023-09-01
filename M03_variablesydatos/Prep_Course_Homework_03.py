#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:


var1 = 7
type(var1)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:


print(type(8.5))


# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:


print(type(var1))


# 4) Crear una variable que contenga tu nombre

# In[2]:


nombre="Juan Pablo"


# 5) Crear una variable que contenga un número complejo

# In[3]:


num_complejo=8j


# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:


print(type(num_complejo))


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:


cadena="True"
booleano=True


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:


print(type(cadena))
print(type(booleano))


# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:


var2 = 5 + 5.5
print(var2)


# 11) Realizar una operación de suma de números complejos

# In[2]:


sum_numcomplejos = 8j + 8j
print(sum_numcomplejos)


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:


sum_nums = 8j + 8
print(sum_nums)


# 13) Realizar una operación de multiplicación

# In[5]:


3*15


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:


2**8


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:


var3 = 27/4
print(var3)


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

var4=(int(var3))
print(var4) #Retomando la variable
27//4 #Realizando la operación de nuevo


# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:


var5 = 27%4
print(var5)


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:


(var4*4)+var5


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:


nom = "Juan"
apell = "Silva"
nom_ap = nom+" "+apell
print(nom_ap)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

numdos="2"
num2=2
2=="2"


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:


int(numdos)
numdos==num2


# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:


a = float(3,8)


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:


tres = 3
tres-=1
print(tres)


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:


1<<2 #Se recorre el 1 dos posiciones a la izquierda (0100)


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:


2 + "2"


# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

var6 = "bueno, "
var6*10
print(var6)

# %%
