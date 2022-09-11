
#*  LLAMADA A LAS LIBRERÍAS NECESARIAS
from time import sleep, sleep_ms
from machine import Pin as pin

#*  PUERTAS
capó = pin(5, pin.IN, pin.PULL_UP)
puerta_derecha = pin(18, pin.IN, pin.PULL_UP)
puerta_izquierda = pin(19, pin.IN, pin.PULL_UP)
baúl = pin(21, pin.IN, pin.PULL_UP)
#*  LED/S
led = pin(22, pin.OUT)


#?  CICLO PRINCIPAL
while True:
    #*   VARIABLE ENCARGADA DE ALMACENAR EL VALOR DE CADA PUERTA, Y DONDE EL "or" SUMA TODOS LOS VALORES
    encendido = capó.value() or  puerta_derecha.value() or  puerta_izquierda.value() or baúl.value()

    #*   IMPRESIÓN DE LOS VALORES CORRESPONDIENTES A LOS PULSADORES DE LAS PUERTAS (OPCIONAL)
    print(capó.value(),  puerta_derecha.value(),  puerta_izquierda.value(), baúl.value())
    sleep_ms(50)

    #*   SE ASIGNA LA SUMA DE LOS VALORES QUE TIENEN LAS PUERTAS A LOS LEDS
    led.value(encendido)