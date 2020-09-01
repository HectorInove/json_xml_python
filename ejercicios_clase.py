#!/usr/bin/env python
'''
JSON XML [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json
import requests
import xml.etree.ElementTree as ET

import matplotlib.pyplot as plt
import matplotlib.axes

def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    json_data = {
                "nombre": "Marcos",
                "apellido": "Escalzo",
                "DNI": 38999666,
                "Cantidad prendas": [
                    {
                    "Prenda": "pares zapatilla",
                    "cantidad": 3
                    },
                    {
                    "Prenda": "campera",
                    "cantidad": 5
                    }
                    ]
                }

    with open('ej_1.json', 'w') as jsonfile:
        data = [json_data]
        json.dump(data, jsonfile, indent=4)

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado
    pass


def ej2():
    
    with open('ej_1.json', 'r') as jsonfile:
        current_data = json.load(jsonfile)
    json_string = json.dumps(current_data, indent=4)
    print(json_string)
    
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1
    pass


def ej3():
    # Ejercicio de XML
    # Basado en la estructura de datos del ejercicio 1,
    # crear a mano un archivo ".xml" y generar una estructura
    # lo más parecida al ejercicio 1.
    # El objectivo es que armen un archivo XML al menos
    # una vez para que entiendan como funciona.
    pass


def ej4():
    # XML Parser

    tree = ET.parse('datos.xml')
    # Inovetip: Acá en vez de datos.xml, tu archivo es ej3.xml
    root = tree.getroot()

    
    for child in root:
        print(child.tag, ":", child.attrib, child.text)
        for child2 in child:
            print(child2.tag, ":", child2.text)
    # Tomar el archivo realizado en el punto anterior
    # e iterar todas las tags del archivo e imprimirlas
    # en pantalla tal como se realizó en el ejemplo de clase.
    # El objectivo es que comprueben que el archivo se realizó
    # correctamente, si la momento de llamar al ElementTree
    # Python lanza algún error, es porque hay problemas en el archivo.
    # Preseten atención al número de fila y al mensaje de error
    # para entender que puede estar mal en el archivo.
    pass


def ej5():
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de torta.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.
    
    # Inovetip: Tenes que buscar la manera de hacer que el programa
    # admita una cantidad n de usuarios, de esa manera tu programa va a ser escalable
    # Por ejemplo, en vez de declarar 10 usuarios, crea una lista vacía user_id = []
    # y la vas completando con user_id.append(), de esa manera, no importa cuantos usuarios
    # tenga el request, siempre va a haber una lista que se acomoda a tu request.
    
    u1 = 0
    u2 = 0
    u3 = 0
    u4 = 0
    u5 = 0
    u6 = 0
    u7 = 0
    u8 = 0
    u9 = 0
    u10 = 0
    
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    dataset = response.json()

    filter_data1 = [x['userId'] for x in dataset if x.get('completed') is True]

    # Inovetip: En esta parte podes volver a utilizar compresión de listas? 
    for user in filter_data1:
        if user == 1:
            u1 += 1
        elif user == 2:
            u2 += 1
        elif user == 3:
            u3 += 1
        elif user == 4:
            u4 += 1
        elif user == 5:
            u5 += 1
        elif user == 6:
            u6 += 1
        elif user == 7:
            u7 += 1
        elif user == 8:
            u8 += 1
        elif user == 9:
            u9 += 1
        elif user == 10:
            u10 += 1

    users_titles = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]
    users = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    fig = plt.figure()
    fig.suptitle('ej 5', fontsize=16)
    ax = fig.add_subplot()

    

    ax.pie(users_titles, labels=users,
           autopct='%1.1f%%', shadow=True, startangle=90
           )
    
    ax.axis('equal')
    plt.show()





if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
