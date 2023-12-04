#For CMPE244 Class PWM Demo Code

import Jetson.GPIO as GPIO
import time


STEPPER_MOTOR_PIN = 33
DIRECTION_PIN = 31

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(STEPPER_MOTOR_PIN, GPIO.OUT)
GPIO.setup(DIRECTION_PIN, GPIO.OUT)

def rotate_motor(direction, duration, frequency=200, duty_cycle=50):
    GPIO.output(DIRECTION_PIN, direction)

    cycle_length = 1.0 / frequency
    on_time = cycle_length * (duty_cycle / 100.0)
    off_time = cycle_length - on_time

    end_time = time.time() + duration
    while time.time() < end_time:
        GPIO.output(STEPPER_MOTOR_PIN, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(STEPPER_MOTOR_PIN, GPIO.LOW)
        time.sleep(off_time)

if __name__ == "__main__":
    try:
        frequency = float(input("Enter the desired user step frequency (in Hz): "))
        duty_cycle = float(input("Enter desired user duty cycle (0-100): "))

        print("Clockwise rotation in progress.")
        rotate_motor(GPIO.HIGH, 5,frequency, duty_cycle)

        time.sleep(0.5) #giving a sleep timer for 5 seconds

        print("Counter-clockwise rotation in progress. Performed by Priyam Hajisheth. Student ID: 016659357.")
        rotate_motor(GPIO.LOW, 5, frequency, duty_cycle)
        
    except Exception as e:
        print("Error",e)

    finally:
        GPIO.cleanup()

