#!/usr/bin/env python3
########################################################################
# Filename    : Sweep.py
# Description : Servo sweep
# Author      : antonio2709
# modification: 19/04/2020
########################################################################
import RPi.GPIO as GPIO
import time
OFFSE_DUTY = 0.5        #definir el desplazamiento del pulso del servo
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY     #definir el pulso de trabajo para un minimo de servo
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY    #definir el pulso de trabajo para un maximo de servo
servoPin = 12

def map( value, fromLow, fromHigh, toLow, toHigh):  # mapear un valor de un rango a otro
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)         # usar GPIIO fisico
    GPIO.setup(servoPin, GPIO.OUT)   # poner servopin como salida
    GPIO.output(servoPin, GPIO.LOW)  # hacer que servopin este en bajo nivel

    p = GPIO.PWM(servoPin, 50)     # poner como frecuencia 50Hz
    p.start(0)                     # empezar ciclo de trabajo en 0
    
def servoWrite(angle):      # definir que el servo rote el angulo especifico 0-180 
    if(angle<0):
        angle = 0
    elif(angle > 180):
        angle = 180
    p.ChangeDutyCycle(map(angle,0,180,SERVO_MIN_DUTY,SERVO_MAX_DUTY)) # mapear el angulode trabajo y poner salida
    
def loop():
    while True:
        for dc in range(0, 181, 1):   # hacer que el servo rote desde 0 a 180 grados
            servoWrite(dc)     # escribir el valor del servo en dc
            time.sleep(0.001)
        time.sleep(0.5)
        for dc in range(180, -1, -1): #  hacer que el servo rote desde 180 a 0 grados
            servoWrite(dc)
            time.sleep(0.001)
        time.sleep(0.5)

def destroy():
    p.stop()
    GPIO.cleanup()

if __name__ == '__main__':     # Arrancando programa
    print ('Programa arrancado...')
    print('presionar control+C para finalizar')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # 
        destroy()
