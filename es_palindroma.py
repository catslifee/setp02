def es_palindroma(pal):
    L_pal=list(pal)
    L_pal_alreves=L_pal[-1::-1]
    if L_pal==L_pal_alreves:
        return True
    else:
        return False
