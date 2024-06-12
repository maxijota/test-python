import random

win_user =0
win_pc = 0
same = 0
Round = 0


while True:
    print ('ESTE ES EL JUEGO DE PIEDRA PAPEL Y TIJERA\n')
    user_opcion = input("Escoge una opcion \n PIEDRA - PAPEL - TIJERA -->")
    user_opcion = user_opcion.upper ()



    opciones =('PIEDRA','PAPEL','TIJERA')
    pc_opcion = random.choice(opciones)


    if not user_opcion in opciones:
        print ("Esta opcion no es valida, intende de nuevo\n")
        continue

    if user_opcion == 'PIEDRA' and pc_opcion == 'TIJERA' or user_opcion == 'PAPEL' and pc_opcion == 'PIEDRA' or user_opcion == 'TIJERA' and pc_opcion == 'PAPEL':
        win_user +=1 
        print ('Gano la Usuario Ronda\n')

    elif pc_opcion == 'TIJERA' and pc_opcion == 'PIEDRA' or user_opcion == 'PIEDRA' and pc_opcion == 'PAPEL' or user_opcion == 'PAPEL' and pc_opcion == 'TIJERA':
        win_pc +=1
        print ('Gano la maquina Ronda\n')

    if user_opcion == pc_opcion:
        print('>> EMPATE <<')
        same +=1

    if win_pc == 2:
        print ('Gano la maquina')
        break
    if win_user == 2:
        print ('Gano Usuario')
        break



print ('pc->',pc_opcion,'win->pc',win_pc)
print ('user->',user_opcion,'winU->',win_user,same)
