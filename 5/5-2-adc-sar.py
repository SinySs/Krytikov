import RPi.GPIO as GPIO
import time

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac   = [26, 19, 13, 6, 5, 11, 9, 10]
troyka = 17
comp = 4


GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def abc():
    
    val = 0

    for i in range(7, -1, -1):

        heigh = 2 ** i
        val += heigh

        GPIO.output(dac, decimal2binary(val))
        time.sleep(0.1)

        if GPIO.input(comp) == GPIO.LOW:
            val -= heigh

        
    
    return val


try:
    while True:
        val = abc()


        print("voltage: ", "{:.2f}, digit: ".format(3.3 * val / 256), val)
        
finally:
    GPIO.setup(dac, 0)
    GPIO.cleanup()