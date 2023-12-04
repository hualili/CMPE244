import Jetson.GPIO as GPIO
import time

STEP_PIN = 33
DIR_PIN = 31
STEPS_PER_REV = 200

GPIO.setmode(GPIO.BOARD)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

print("Sharan Raghu Venkatachalam, 016698682\n");
def rotate_motor(degrees, steps_per_rev):
    steps = int(steps_per_rev * abs(degrees) / 360)
    frequency = 800
    period = 1.0 / frequency
    on_time = (period / 4)
    off_time = period - on_time
    
    # Set direction to counter-clockwise
    GPIO.output(DIR_PIN, GPIO.LOW)
    
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(off_time)

try:
    degrees = float(input("Enter degrees to rotate: "))
    rotate_motor(degrees, STEPS_PER_REV)
    print("Rotating counter clockwise")
    print(f"Rotated {degrees} degrees!")
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nScript terminated.")
