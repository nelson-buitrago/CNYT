import math

def suma(c1,c2):
    "La funcion suma recibe dos numeros complejos con su parte real y su respectiva parte imaginaria, y retorna la suma de ambos numeros"
    return (c1[0]+c2[0],c1[1]+c2[1])

def producto(c1,c2):
    "La funcion producto recibe dos numeros complejos con su parte real e imaginaria y retorna la multiplicación entre ellos"
    "A continuación se hacen las operaciones de la multiplicación de numeros complejos que dan como resultado su parte real e imaginaria"
    x = c1[0]*c2[0] - c1[1]*c2[1]
    y = c1[0]* c2[1] + c1[1]*c2[0]
    return (x,y)

def resta(c1,c2):
    "En esta funcion vamos a hacer la resta de dos numeros complejos, recibe dos numeros complejos con su parte real y su respectiva parte imaginaria y retorna un numero complejo con sus respectivas partes"
    return (c1[0]-c2[0],c1[1]-c2[1])

def division(c1,c2):
    "En esta funcion vamos a hacer la multiplicación de dos numeros complejos, recibe dos numeros complejos con su parte real y su respectiva parte imaginaria y retorna un numero complejo con sus respectivas partes"
    "A continuación se hacen las operaciones de la multiplicación de numeros complejos que dan como resultado su parte real e imaginaria"
    conju = conjugado(c2)
    numerador = producto(c1,conju)
    denominador = producto(c2,conju)
    return [numerador[0]/denominador[0],numerador[1]/denominador[0]]
    
def conjugado(c1):
    "La función conjugado recibe un numero complejo c1 y retorna un complejo correspondiente a la operación de hallar el conjugado del numero complejo c1"
    return [c1[0],c1[1]*(-1)]

def modulo(c1):
    "La funcion modulo recibe un numero complejo c1 y retorna un numero complejo que corresponde a la operacion de hallar el modulo del numero complejo c1"
    return (c1[0]**2+c1[1]**2)**(1/2)

def conversionComplejoPolar(c1):
    "La funcion conversionComplejoPolar recibe un numero complejo c1 con su fase en radianes, y retorna una lista que contiene las coordenadas polares del numero complejo"
    mod = modulo(c1)
    fase = faseNumeroComplejo(c1)
    return [mod,fase]

def conversionPolarComplejo(c1):
    "La funcion conversionPolarComplejo recibe una lista  que contiene las coordenadas polares de un numero complejo, y retorna un numero complejo"    
    x = c1[0]*math.cos(c1[1])
    y= c1[0]*math.sin(c1[1])
    return [x,y]

def faseNumeroComplejo(c1):
    "La funcion faseNumeroComplejo recibe un numero complejo y retorna la fase del numero complejo en radianes"
    return math.atan2(c1[1],c1[0])
    
