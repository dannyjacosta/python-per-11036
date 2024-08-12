'''
Contiene funciones para realizar cálculos con circunferencias y esferas.
'''
import math


def perimetro(radio):
    '''
    Calcula el perímetro de un círculo.

    Args:
        radio (float): El radio de círculo.
    '''
    return 2 * math.pi * radio


def area(radio):
    '''
    Calcula el area de un círculo.

    Args:
        radio (float): El radio de círculo.
    '''
    return math.pi * radio ** 2
