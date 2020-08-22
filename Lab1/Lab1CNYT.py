import math

def suma(c1, c2):
    """
    La función suma recibe dos números complejos (listas de longitud 2) y retorna
    un único número complejo (lista de longitud 2) que corresponde a la suma de la parte real y
    la suma de la parte imaginaria de cada número respectivamente
    """
    return [c1[0] + c2[0], c1[1] + c2[1]]


def resta(c1, c2):
    """
    La función resta recibe dos números complejos (listas de longitud 2) y retorna
    un único número complejo (lista de longitud 2) que corresponde a la resta de la parte real y
    la resta de la parte imaginaria de cada número respectivamente
    """
    return [c1[0] - c2[0], c1[1] - c2[1]]


def producto(c1, c2):
    """
    La función producto recibe dos números complejos [a,b] y [c,d] (listas de longitud 2) y retorna
    un único número complejo (lista de longitud 2) que su parte real corresponde a la operación (a*c - b*d) y
    su parte imaginaria corresponde a la operación (a*d + b*c)
    """
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginario = c1[0] * c2[1] + c1[1] * c2[0]
    return [real, imaginario]


def division(c1, c2):
    """
    La función división recibe dos números complejos (listas de longitud 2) y retorna
    un único número complejo (lista de longitud 2) que corresponde a la operación a/b
    """
    num = producto(c1, conjugado(c2))
    denomi = producto(c2, conjugado(c2))
    real = num[0] / denomi[0]
    imaginario = num[1] / denomi[0]
    return [real, imaginario]


def conjugado(c1):
    """
    La función conjugado recibe un número complejo (lista de longitud 2) y retorna
    un número complejo (lista de longitud 2) que corresponde a hallar el conjugado de un número complejo,
    es decir, multiplicar la parte imaginaria por -1
    """
    return [c1[0], c1[1]*-1]


def modulo(c1):
    """
    La función modulo recibe un número complejo (lista de longitud 2) y retorna la
    operación de hallar el modulo de un número complejo, es decir, un número real
    """
    return math.sqrt(c1[0]**2 + c1[1]**2)



def cart_pol(c1):
    """
    La función cart_pol recibe un número complejo (lista de longitud 2) y retorna la
    operación de pasar de cartesianas a polares, con el lado y ángulo respectivamente
    """
    r = math.sqrt(c1[0]**2 + c1[1]**2)
    angle = math.degrees(math.atan2(c1[1], c1[0]))
    return [r, angle]


def pol_cart(c1):
    """
    La función pol_cart recibe un número complejo (lista de longitud 2) y retorna la
    operación de pasar de polares a cartesianas, con las coordenadas X y Y respectivamente
    """
    r, angle = c1[0], math.radians(c1[1])
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    return [x, y]


def fase(c1):
    """
    La función fase recibe un número complejo (lista de longitud 2) y retorna la
    operación de hallar la fase de un número complejo
    """
    return math.degrees(math.atan2(c1[1], c1[0]))


