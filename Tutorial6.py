#operaciones de logica

temp = int(input('Que temperatura hace?: '))

if temp >= 0 and temp <= 15:
    print('Hace fresquito no?')
elif temp >= 16 and temp <= 33:
    print('Que bien se esta eh ')
elif temp >= 34 and temp <= 40:
    print('Quieres agua bro?')
elif temp >= 41 and temp <= 1000:
    print('Bro, por que no respiras?')
elif temp <= 0:
    print('Quieres una sopita?')