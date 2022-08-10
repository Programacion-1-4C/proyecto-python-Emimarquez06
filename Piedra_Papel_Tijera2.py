import random
from time import sleep

print ('Bienvenido, vamos a jugar a Piedra, papel o tijera.')
print ('')
sleep(2)
print ('Jugamos al mejor de tres, o prefieres cambiar?')
sleep(1)
print ('')

#Funcion que realiza la lógica del juego
def juego(intentos):
 x = 0
 tu = 0
 pc = 0
 while str(x) != intentos:
  aleatorio = random.randrange(0, 3)
    elige_pc = ''

    print ('')
    print('1)Piedra')
    print('2)Papel')
    print('3)Tijera')
    print('4)Salir')

    opcion = int(input('Elige una opción: '))

    if opcion == 1:
        elige_usuario = 'Piedra'
    elif opcion == 2:
        elige_usuario = 'Papel'
    elif opcion == 3:
        elige_usuario = 'Tijera'
    else:
        break

    print('Elegiste: ', elige_usuario)

    if aleatorio == 0:
        elige_pc = 'Piedra'
    elif aleatorio == 1:
        elige_pc = 'Papel'
    elif aleatorio == 2:
        elige_pc = 'Tijera'

    print('PC eligió: ', elige_pc)
    print('...')

    if elige_pc == 'Piedra' and elige_usuario == 'Papel':
        print('Ganaste, Papel envuelve a Piedra')

    elif elige_pc == 'Papel' and elige_usuario == 'Tijera':
        print("Ganaste, Tijera corta Papel")

    elif elige_pc == 'Tijera' and elige_usuario == 'Piedra':
        print('Ganaste, Piedra aplasta Tijera')

    if elige_pc == 'Papel' and elige_usuario == 'Piedra':
        print('Perdiste, Papel envuelve Piedra')

    elif elige_pc == 'Tijera' and elige_usuario == 'Papel':
        print('Perdiste, Tijera corta Papel')

    elif elige_pc == 'Piedra' and elige_usuario == 'Tijera':
        print('Perdiste, Piedra aplasta Tijera')

    elif elige_pc == elige_usuario:
        print('Empate')