#if                  Segundo programa mas facil

age = int(input('Cuantas primaveras has vivido?: '))

if age == 100:
    print('Felicidades has vivido un siglo')
elif age >= 101:
    print('Eres una de las personas mas sabias del planeta')
elif age >= 18:
    print('Eres mayor de edad')
elif age <0:
    print('Todavia no has nacido bru')
else:
    print('Eres un bebe')