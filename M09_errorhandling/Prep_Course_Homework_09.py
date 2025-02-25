#!/usr/bin/env python
# coding: utf-8

# ## Manejo de errores

# 1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

# In[1]:




# 2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

# In[5]:





# 3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
# Creacion del objeto incorrecta<br>
# Creacion correcta del objeto<br>
# Metodo valor_modal()<br>
# 
# Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.

# In[9]:




# 4) Probar una creación incorrecta y visualizar la salida del "raise"

# In[13]:




# 6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo
import unittest

class ProbarPrimos(unittest.TestCase):
    def probar_primos():
        h_prim = Herramientas([1,2,3])
        primos = h_prim.primo()
        resultado = ["1 es primo","2 es primo","3 es primo"]
        self.assertEqual(primos,resultado)


unittest.main(argv=[""], verbosity=2, exit=False)
# In[14]:




# 7) Agregar casos de pruebas para el método conversion_grados()

# In[17]:




# 8) Agregar casos de pruebas para el método factorial()

# In[20]:




