#name = input('Como te llamas?: ')
#surname = input('Y tu apellido?: ')
#print(' ')
#print('Hola ' + name + surname + ' Como estas?')
#print(' ')
#edad = int(input('Cuantas primaveras has vivido?: '))

#if edad <=9:
   # print(' ')
   # print('Bro, eres menor que mi hermana. Deja el ordenador')
#elif edad <=12:
   ## print('Sigues siendo muy enano...')
#elif edad <=17:
   # print('Eres un adolescente...')
#elif edad >= 18:
 #   print('Eres mayor de edad')
#elif edad ==50:
 #   print('Has vivido medio siglo!!!!')
#elif edad >=51:
 #   print('Ya te vas haciendo mayor')
#elif edad ==100:
#    print('Has vivido un siglo')
#elif edad >=130:
  #  print('Bro eres una momia')







print('NOS VAS A DECIR TU NOMBRE, TIENES 3 INTENTOS, SI NO LO HACES LA MAQUINA SE CERRARA.')
print(' ')

name = input('Dime tu nombre: ')
print(' ')

if len(name) <=2:
    print('Intentalo de nuevo')
    print(' ')
elif len(name) >=3:
    print('Muchas gracias ' + name)
    print(' ')

name_1 = input('Dime tu nombre: ')
print(' ')

if len(name_1) >=3:
    print('Hola ' + name_1)
    print(' ')
elif len(name_1) <=2:
    print('Intentalo de nuevo, solo tienes una oportunidad mas.')
    print(' ')

name_2 = input('Dime tu nombre de una vez: ')
print(' ')

if len(name_2) >=3:
    print('Gracias ' + name_2)
    print(' ')
elif len(name_2) <=2:
    print('Te has quedado sin intentos retrasado')
    print(' ')
    exit(0)





