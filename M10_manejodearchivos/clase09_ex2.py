import sys

print("Ingrese True si llovio o False si no llovió:")
print("Ingrese temperatura en °C:")
print("Ingrese porcentaje de humedad:")



if len(sys.argv) == 4:
    temperatura = sys.argv[2]
    humedad = sys.argv[3]
    lluvia = sys.argv[1]
    import datetime
    import os
    marca_de_tiempo = datetime.datetime.now()
    marca_de_tiempo = int(datetime.datetime.timestamp(marca_de_tiempo))
    línea = str(marca_de_tiempo) + ',' + temperatura + ',' + humedad + ',' + lluvia
    print(línea)

    logs_lluvia = open('clase09_ex2.csv', 'a')
    logs_lluvia.write(línea+'\n')
    logs_lluvia.close()

else:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print('Ejemplo: clase09_ej1.py <temperatura> <humedad> <True o False>')
    print("El número de argumentos dados fue de ",len(sys.argv))
    for argumento in sys.argv:
        print(argumento)
