import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up GPIO 17 as an output
GPIO.setup(17, GPIO.OUT)

def play():
    # Turn the buzzer on and off 5 times
    for i in range(5):
        # Turn the buzzer on
        GPIO.output(17, GPIO.HIGH)

        # Wait for 0.5 seconds
        time.sleep(0.5)

        # Turn the buzzer off
        GPIO.output(17, GPIO.LOW)

        # Wait for 0.5 seconds
        time.sleep(0.5)

    # Clean up the GPIO pins
    GPIO.cleanup()