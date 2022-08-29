import random
bandera = True

def juego():
    x = 0
    elige_usuario = 0
    elige_pc = 0
    aleatorio = random.randrange(0, 3)
    elige_pc = '' 
    
    print('')
    print('1)Piedra')
    print('2)Papel')
    print('3)Tijera')
    print('4)Salir')

    opcion = int(input('Elige una opción: '))

    elige_usuario = usuario(opcion)
    elige_pc = pc(aleatorio)

    if elige_usuario == 'Error':
        print ('Numero Invalido')
    elif elige_usuario == elige_pc:
            print('')
            print('Elegiste: ', elige_usuario)
            print('PC eligió: ', elige_pc)
            print('Empate')
    elif elige_usuario == 'Tijera':
            if elige_pc == 'Piedra':
                print('')
                print('Elegiste: ', elige_usuario)
                print('PC eligió: ', elige_pc)
                print('Perdiste')   
            else:
                print('')
                print('Elegiste: ', elige_usuario)
                print('PC eligió: ', elige_pc)
                print('Ganaste')
    elif elige_usuario == 'Piedra':
            if elige_pc == 'Tijera':
                print('')
                print('Elegiste: ', elige_usuario)
                print('PC eligió: ', elige_pc)
                print('Ganaste')
            else:
                print('')
                print('Elegiste: ', elige_usuario)
                print('PC eligió: ', elige_pc)
                print('Perdiste')
    elif elige_usuario == 'Papel':
            if elige_pc == 'Tijera':
                print('')
                print('Elegiste: ', elige_usuario)
                print('PC eligió: ', elige_pc)
                print('Perdiste')
            else:
                print('')
                print('Elegiste: ', elige_usuario)
                print('PC eligió: ', elige_pc)
                print('Ganaste')
    

def usuario(x: str):
    if x == 1:
        return 'Piedra'
    elif x == 2:
        return 'Papel'
    elif x == 3:
        return 'Tijera'
    elif x == 4:
        bandera = False
        return ''
    else:
        return 'Error'

def pc (x: str):
    if x == 0:
            return  'Piedra'
    elif x == 1:
            return 'Papel'
    elif x == 2:
            return 'Tijera'

print ('Bienvenido, vamos a jugar a Piedra, papel o tijera.')
while bandera:
    juego()