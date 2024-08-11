def perimetro(*lados):
    '''
    Calcula el area de un polígono.

    Args:
        [lados] (float): La longitude de cada lado separados por coma.
    '''
    p = 0
    for lado in lados:
        p += lado

    return p
