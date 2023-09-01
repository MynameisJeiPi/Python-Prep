

#3) Crear un archivo a partir de los datos presentes en el diccionario provisto. 
# Debe contener en la primera fila el nombre de las claves y luego cada línea los elementos i-ésimos  de las listas de valores contiguos y separados por coma ','.
# Este archivo debe llamarse clase09_ej3.csv

#__________________________________________________________________________________________________
# En esta versión se escribe una nueva línea después del ciclo for que escribe las claves.
# Además, en el ciclo while se utiliza como condición <while i < len(montañas['orden']):>, ...
# ... para que no sea necesario conocer la extensión del diccionario.


montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

import os

archivo_ex = open("clase09_ex3.csv","w")


for clave in montañas.keys():
    archivo_ex.write(clave+",")
archivo_ex.write("\n")

nombre = montañas["nombre"]
orden = (montañas["orden"])
cordillera = montañas["cordillera"]
pais = montañas["pais"]
altura = (montañas["altura"])

i = 0
while i < len(montañas['orden']):
    archivo_ex.write(nombre[i] + ",")
    archivo_ex.write(str(orden[i]) + ",")
    archivo_ex.write(cordillera[i] + ",")
    archivo_ex.write(pais[i] + ",")
    archivo_ex.write(str(altura[i]) + "\n")
    i += 1

archivo_ex.close()

print('El archivo tiene un tamaño de', str(os.path.getsize('clase09_ej3.csv')/1048576),'MB')

# 3) Crear una carpeta nueva "Clase09_Montañasaltas"
import os
os.makedirs("Clase09_Montañasaltas")

# 6) Copiar el archivo clase09_ej3.scv en la carpeta clase09_montañas_altas usando la sentencia **os.system**

directorio_actual = os.getcwd()
print(f"El directorio actual es {directorio_actual}")

nombre_carpeta = 'Clase09_Montañasaltas'
ruta_carpeta = os.path.join(directorio_actual, nombre_carpeta)
print(f"La ruta completa de '{nombre_carpeta}' es: {ruta_carpeta}")

try:
    archivo_copia = "clase09_ex3.csv"
    comando = f"copy {archivo_copia} {ruta_carpeta}"
    resultado = os.system(comando)

    if resultado == 0:
        print(f"El archivo {archivo_copia} ha sido copiado en {ruta_carpeta}")
    else:
        print(f"Error al copiar el archivo {archivo_copia}")
except Exception as e:
    print(f"Se produjo un error: {str(e)}")

# 7) Lista el contenido de la carpeta.

os.listdir("./Clase09_Montañasaltas")

# O bien: 

os.listdir(ruta_carpeta)
______________________________________________________________________________________________
# En esta versión no se crean nuevas listas para cada clave. Utiliza una sintaxis para llamar 
# elementos a partir de una clase y un índice: diccionario["clave"][índice]

import os
archivo = open('clase09_ej3.csv', 'w')

for clave in montañas.keys():
    if (clave == 'altura'):
        archivo.write(clave+'\n')
    else:
        archivo.write(clave+',')

ind = 0
while (ind < 10):
    archivo.write(montañas['nombre'][ind]+',')
    archivo.write(str(montañas['orden'][ind])+',')
    archivo.write(montañas['cordillera'][ind]+',')
    archivo.write(montañas['pais'][ind]+',')
    archivo.write(str(montañas['altura'][ind])+'\n')
    ind += 1

archivo.close()


