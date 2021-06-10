#string slicing      Indexing[]

#Esquema     [start:stop:step]

#nombre = 'berto'

#first_name = nombre[0:3]
#last_name = nombre[3:]
#nombre_raro = nombre[0:6:1]

#en este ejemplo solo hacemos que se ejecuten las cifras en espacios pares(contando al primero)
#otro_nombre_raro = nombre[0:6:2]

#en este ejemplo solo hacemos que se ejecuten las cifras cada 3 espacios(contando al primero)
#otro_nombre_raro2 = nombre[0:6:3]

#Para poner el nombre al reves
#nombre_al_reves = nombre[::-1]

#print(first_name)
#print(last_name)
#print(nombre_raro)
#print(otro_nombre_raro)
#print(otro_nombre_raro2)
#print(nombre_al_reves)

                            #string slicing         slice()

#Esquema   (start,stop,step)

#EJ 1

#website = 'http://google.com'

#slice = slice(7, -4)

#print(website[slice])

#website = 'http://google.es'

#slice = slice(7,-3)

#print(website[slice])
