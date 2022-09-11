from machine import Pin as pin
from utime import sleep_ms as pausam

puerta1 = pin(19, pin.IN, pin.PULL_UP)
puerta2 = pin(21, pin.IN, pin.PULL_UP)
puerta3 = pin(22, pin.IN, pin.PULL_UP)
puerta4 = pin(23, pin.IN, pin.PULL_UP)
derecha = pin((NUMERO DEL PIN), pin.IN, pin.PULL_UP)
izquierda = pin((NUMERO DEL PIN), pin.IN, pin.PULL_UP)
baúl = pin(15, pin.IN, pin.PULL_UP)
led1 = pin(5, pin.OUT)
led2 = pin(18, pin.OUT)
espera = 500


def estacionarias():
    led1.value(1)
    led2.value(1)
    pausam(espera + 200)
    led1.value(0)
    led2.value(0)
    pausam(espera + 200)

def direccional_izquierda():
    led1.value(1)
    pausam(espera)

def direccional_derecha():
    led2.value(1)
    pausam(espera)


def encendido():
    led1.value(1)
    led2.value(1)

def apagado():
    led1.value(0)
    led2.value(0)


while True:

    if puerta1.value()==1 or  puerta2.value()==1 or  puerta3.value()==1 or  puerta4.value()==1 or  baúl.value()==1:
        encendido()
    else:
        if puerta1.value()==0 and puerta2.value()==0 and puerta3.value()==0 and puerta4.value()==0 and baúl.value()==0:
            apagado()

    if derecha.value()==1:
        direccional_derecha()

    if izquierda.value()==1:
        direccional_izquierda()

    if derecha.value()==1 and izquierda.value()==1:
        estacionarias()