                         #NESTED LOOPS

filas = int(input('Cuantas filas quieres que haya?: '))
columnas = int(input('Cuantas columnas quieres que haya?: '))
simbolo = input('Dime el simbolo que quieres utilizar: ')

for y in range (filas):
    for z in range(columnas):
        print(simbolo, end='')
    print()