#Romario Guadalupe Limón Hernández
#API OpenWeather

#_________________________________________________________________________________________________#
#Este script realiza la busqueda de el clima de tres ciudades mediante un menu que permite elejir #
#la ciudad a mostrar el clima, una vez seleccionada la ciudad se abre otro menu el cual nos mues- #
#tra las opciones de ver toda la informacion o ver solo alguna infromacion ya seleccionada.       #
#_________________________________________________________________________________________________#

import requests
import os
from pprint import pprint


#Menu que muestra las ciudades para consultar su clima
def menu_opc1 ():
    #os.system('cls')
    print ("-"*15,"MENU DE CIUDADES","-"*15)
    print ("   Name                ID")
    print ("1- San Pedro:          3985129")
    print ("2- SN de los Garza:    3985241")
    print ("3- Monterrey:          3995465")
    print ("4- Salir.")
    print ("-"*46)



#Funcion del segundo menu, (toda la informacion o solo la temperatura )
def menu_opc2 ():
    print ("-"*15,"MENU DE OPCIONES","-"*15)
    print ("1- Ver toda la informacion formato json")
    print ("2- Ver Nombre de ciudad, descripcion ,temperatura, humedad y velocidad del viento")
    print ("3- Salir.")
    print ("-"*46)



#Ciclo para menu repetitivo
while True:

    menu_opc1()

    opcm1 = input(str("Introduce la opcion: "))

    if opcm1 == "1":
        print (" ")
        print ("--San Pedro--")

        idciudad = "3985129"
        
        url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid=b91dc72959f5d13a98bde8470b52ef61&units=metric'.format(idciudad)

        menu_opc2()

        opcm2 = input(str("Introduce la opcion: "))

        if opcm2 == "1":
            info = requests.get(url)

            tipodato = info.json()

            pprint (tipodato)
        
        elif opcm2 == "2":
            info = requests.get(url)
            tipodato = info.json()
            
            nom = tipodato['name']
            descrip = tipodato['weather'][0]['description']
            temp = tipodato['main']['temp']
            humed = tipodato['main']['humidity']
            vviento = tipodato['wind']['speed']
            print (" ")
            print ("-"*46)
            print ('Nombre: {}'.format(nom))
            print ('Descripcion: {}'.format(descrip))
            print ('Temperatura: {} C°'.format(temp))
            print ('Humedad: {} %'.format(humed))
            print ('Velocidad del viento {} m/s'.format(vviento))
            print ("-"*46)
        
        elif opcm2 == "3":
            continue

    elif opcm1 == "2":
        print (" ")
        print ("--SN de los Garza--")

        idciudad = "3985241"
        
        url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid=b91dc72959f5d13a98bde8470b52ef61&units=metric'.format(idciudad)

        menu_opc2()

        opcm2 = input(str("Introduce la opcion: "))

        if opcm2 == "1":
            info = requests.get(url)

            tipodato = info.json()

            pprint (tipodato)
        
        elif opcm2 == "2":
            info = requests.get(url)
            tipodato = info.json()
            
            nom = tipodato['name']
            descrip = tipodato['weather'][0]['description']
            temp = tipodato['main']['temp']
            humed = tipodato['main']['humidity']
            vviento = tipodato['wind']['speed']
            print (" ")
            print ("-"*46)
            print ('Nombre: {}'.format(nom))
            print ('Descripcion: {}'.format(descrip))
            print ('Temperatura: {} C°'.format(temp))
            print ('Humedad: {} %'.format(humed))
            print ('Velocidad del viento {} m/s'.format(vviento))
            print ("-"*46)
        
        elif opcm2 == "3":
            continue

    elif opcm1 == "3":
        print (" ")
        print ("--Monterrey--")

        idciudad = "3995465"
        
        url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid=b91dc72959f5d13a98bde8470b52ef61&units=metric'.format(idciudad)

        menu_opc2()

        opcm2 = input(str("Introduce la opcion: "))

        if opcm2 == "1":
            info = requests.get(url)

            tipodato = info.json()

            pprint (tipodato)
        
        elif opcm2 == "2":
            info = requests.get(url)
            tipodato = info.json()
            
            nom = tipodato['name']
            descrip = tipodato['weather'][0]['description']
            temp = tipodato['main']['temp']
            humed = tipodato['main']['humidity']
            vviento = tipodato['wind']['speed']
            print (" ")
            print ("-"*46)
            print ('Nombre: {}'.format(nom))
            print ('Descripcion: {}'.format(descrip))
            print ('Temperatura: {} C°'.format(temp))
            print ('Humedad: {} %'.format(humed))
            print ('Velocidad del viento {} m/s'.format(vviento))
            print ("-"*46)
        
        elif opcm2 == "3":
            continue   

    elif opcm1 == "4":
        break

    else:
        print (" ")
        input ("No tecleaste ninguna opcion, Preciona la tecla Enter para volver al menu: ")

