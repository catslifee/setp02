def ganador_cachipun():
    x = 0
    while x == 0:
        A[0] =  [input("Primer jugador ")]
        A2[0] = [input("jugada ")]
        B[0] = [input("Segundo jugador ")]
        B2[0] = [input('jugada ')]
        if A2[0] != 'T' and A2[0] != 'R' and A2[0] != 'P':
	        print (" Primer jugador vuelva a intentarlo")
        if B2[0] != 'T' and B2[0] != 'R' and B2[0] != 'P':
	        print (" Segundo jugador vuelva a intentarlo")
        if (A2[0] == 'T' or A2[0] == 'R' or A2[0] == 'P') and (B2[0] == 'T' or B2[0] == 'R' or B2[0] == 'P'):
                permiso=1
    if A2[0] == 'R' and B2[0] == 'T':
        print("Gana ",A[0], "con ",A2[0])
    if A2[0] == 'R' and B2[0] == 'P':
        print("Gana ",'B', "con ",B2[0])
    if A2[0] == 'T' and B2[0] == 'P':
    	print("Gana ",A[0], "con ",A2[0])
    if A2[0] == B2[0]:
        print("Gana ", A[0] ,'por ser el primero en escoger la jugada')



ganador_cachipun()
