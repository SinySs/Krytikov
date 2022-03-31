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
    for i in range(2**8):
        GPIO.output(dac, decimal2binary(i))
        time.sleep((0.005))

        if GPIO.input(comp) == GPIO.LOW:
            return i
    
    return -1


try:
    while True:
        val = abc()


        if val == -1:
            print("Error, max voltge 3.3v")

        else:
            print("voltage: ", "{:.2f}, digit: ".format(3.3 * val / 256), val)
        
finally:
    GPIO.setup(dac, 0)
    GPIO.cleanup()