
#*  LLAMADA A LAS LIBRERÍAS NECESARIAS
from time import sleep, sleep_ms
from machine import Pin as pin

#*  PUERTAS
puerta1 = pin(5, pin.IN, pin.PULL_UP)
puerta2 = pin(18, pin.IN, pin.PULL_UP)
puerta3 = pin(19, pin.IN, pin.PULL_UP)
puerta4 = pin(21, pin.IN, pin.PULL_UP)
#*  LED/S
led = pin(22, pin.OUT)


#?  CICLO PRINCIPAL
while True:
    #*   VARIABLE ENCARGADA DE ALMACENAR EL VALOR DE CADA PUERTA, Y DONDE EL "or" SUMA TODOS LOS VALORES
    encendido = puerta1.value() or  puerta2.value() or  puerta3.value() or puerta4.value()

    #*   IMPRESIÓN DE LOS VALORES CORRESPONDIENTES A LOS PULSADORES DE LAS PUERTAS (OPCIONAL)
    print(puerta1.value(),  puerta2.value(),  puerta3.value(), puerta4.value())
    sleep_ms(50)

    #*   SE ASIGNA LA SUMA DE LOS VALORES QUE TIENEN LAS PUERTAS A LOS LEDS
    led.value(encendido)