import RPi.GPIO as GPIO
import time

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


dac   = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


try:
    while True:
        period= input("Enter period: ")

        if period == 'q':
            break

        try:
            period = float(period) / (2 * 256)

            while True:
                for i in range(255):
                    GPIO.output(dac, decimal2binary(i))
                    time.sleep(period)

                for i in range (255):
                    GPIO.output(dac, decimal2binary(255 - i))
                    time.sleep(period)

        except ValueError:
            print("You can enter numbers >= 0 or \'q\' to stop programmmmm")

finally:
    GPIO.setup(dac, 0)
    GPIO.cleanup()

