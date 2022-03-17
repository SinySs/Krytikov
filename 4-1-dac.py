import RPi.GPIO as GPIO

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


dacs   = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dacs, GPIO.OUT)

try:
    while True:
        num = input("Enter number [0, 255]: ")

        if num.isdigit():
            num = int(num)

            if (num >= 0 and num <= 255):
                GPIO.output(dacs, decimal2binary(num))
                print("Expected CAP: ", "{:.4f}".format(3.3 * num / 255), "V")
            else:
                print("Sorry the number is out of range [0, 255]")
        
        elif num == 'q':
            print('The work is over')
            break
        
        else:
            print("Please enter number [0, 255] or \'q\' to stop")

finally:
    GPIO.setup(dacs, 0)
    GPIO.cleanup()

