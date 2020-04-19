# Servo-con-Python
 En este capítulo, aprenderemos un tipo de motor que puede girar a un ángulo específico, SERVO

Primero, vamos a aprender cómo hacer que el servo gire

Servo:

Servo es un sistema de autocontrol, que consta de motor de CC, engranaje de reducción, sensor y circuito de control. Generalmente
puede girar en el rango de 180 grados. Servo puede emitir un par más grande y es ampliamente utilizado en el modelo de avión,
robot y así sucesivamente. Tiene tres líneas, incluyendo dos para línea de energía eléctrica positiva (2-VCC, rojo), negativa (3-
GND, marrón), y la línea de señal (1-Señal, naranja).
Utilizamos una señal PWM de 50 Hz con un ciclo de trabajo en un cierto rango para conducir el servo. El tiempo de duración 0,5 ms-2,5 ms
de PWM de ciclo único de alto nivel corresponde al ángulo servo 0 grados - 180 grados linealmente. Parte de 
los valores correspondientes segun imagen 1
Al cambiar la señal del servo, el servo girará a la posición designada.

Preste atención a la fuente de alimentación para el motor escalonado es 5v, y no confunda la secuencia de línea.

En este proyecto, hacemos que el servo gire de 0 grados a 180 grados, y luego de 180 grados a 0
Grados.

Después de ejecutar el programa, el servo girará de 0 grados a 180 grados, y luego de 180 grados
a 0 grados, circularmente.

codigo:

Se requiere un pulso de 50 Hz, a saber, un ciclo de 20 ms, para controlar Servo. En la función softPwmCreate (int pin, int
initialValue, int pwmRange), la unidad del tercer parámetro pwmRange es 100US, a saber, 0,1 ms. Con el fin de obtener
el PWM con el ciclo de 20ms, el pwmRange debe establecerse en 200. Así que en la subfunción de servoInit (), creamos
un pin PWM con pwmRange 200.

Como 0-180 grados de servo corresponde a la anchura de pulso PWM 0.5-2.5ms, con PwmRange 200 y unidad 0.1ms.
Por lo tanto, en la función softPwmWrite (int pin, int value), el ámbito 5-25 del valor del parámetro corresponde a 0-180
grados de servo. Además, el número escrito en servoWriteMS () subfunción debe estar dentro del rango
de 5-25. Sin embargo, en la práctica, debido al error de fabricación de cada servo, el ancho del pulso también tendrá desviación.
Así que definimos un ancho de pulso mínimo y un máximo y un desplazamiento de error.

En servoWrite subfunción (), ángulo directo de entrada (0-180 grados), y mapear el ángulo a la anchura del pulso y
a continuación, la salida.

Por último, en el ciclo de la función principal "WHILE" , utilice dos ciclos de "for" para hacer que el servo gire de 0 grados a 180
grados, y luego de 180 grados a 0 grados.
