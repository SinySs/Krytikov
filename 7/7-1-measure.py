import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    
    val = 0

    for i in range(7, -1, -1):

        heigh = 2 ** i
        val += heigh

        GPIO.output(dac, decimal2binary(val))
        time.sleep(0.01)

        if GPIO.input(comp) == GPIO.LOW:
            val -= heigh      
    
    return val

dac  = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
troyka = 17
comp = 4

MAX_VOLTAGE = 3.3
HIEGHER_VOLTAGE = 0.8 * 3.3
LOWER_VOLTAGE = 0.1 * 3.3

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

try:
    voltage = list()
    start_time = time.time()
    digit = 0
    troyka_voltage = 0

    GPIO.output(troyka, 1)

    while troyka_voltage < HIEGHER_VOLTAGE:
        digit = adc()
        print("voltage: ", "{:.2f}, digit: ".format(MAX_VOLTAGE * digit / 256), digit)
        GPIO.output(leds, decimal2binary(digit))
        troyka_voltage = MAX_VOLTAGE * digit / 256
        voltage.append(troyka_voltage)

    increase_duration = time.time() - start_time
    GPIO.output(troyka, 0)

    while troyka_voltage > LOWER_VOLTAGE:
        digit = adc()
        print("voltage: ", "{:.2f}, digit: ".format(MAX_VOLTAGE * digit / 256), digit)
        GPIO.output(leds, decimal2binary(digit))
        troyka_voltage = MAX_VOLTAGE * digit / 256
        voltage.append(troyka_voltage)

    exp_duration = time.time() - start_time

    plt.plot(voltage)
    plt.show()

    voltage_str = [str[i] for i in voltage]

    with open("data.txt", "w") as file:
        file.write("\n".join(voltage_str))
    
    with open("settings.txt.txt", "w") as file:
        file.write("discret: {} s\nquant: {:.5f} V\n", format(exp_duration / len(voltage), 3.3 / 256))
        file.write("E[periment time: {:.5} s\n".format(exp_duration))


finally:
    GPIO.setup(dac, 0)
    GPIO.setup(leds, 0)
    GPIO.setup(troyka, 0)
    GPIO.cleanup()