import object_sketch
import time
import selectEasing
from servo import Servo, servo2040
import easingfunctions as easing

def create_servo_instance(pin_number):
    servo_pin = "SERVO_" + str(pin_number)
    return object_sketch.EasedServo(getattr(servo2040, servo_pin))

def main():
    # Taking input from the user for the number of servos
    num_servos = int(input("Enter the number of servos: "))
    servos = [create_servo_instance(i) for i in range(1, num_servos + 1)]

    while True:
        for servo in servos:
            # Taking input from the user for target angle and duration in milliseconds
            angle = float(input("Enter the target angle (-90 to 90 degrees) for servo {}: ".format(servos.index(servo) + 1)))
            duration = float(input("Enter the duration in milliseconds for servo {}: ".format(servos.index(servo) + 1)))

            # Select easing function from selectEasing module
            easing_function_name = selectEasing.selectEasingFunction()
            if hasattr(easing, easing_function_name):
                easing_function = getattr(easing, easing_function_name)
                servo.ease_to(angle, duration, easing_function)

        # Check if any of the servos are still moving
        while any(servo._isMoving for servo in servos):
            for servo in servos:
                if servo._isMoving:
                    servo.update()
            time.sleep(0.01)

        continue_execution = input("Do you want to control more servos? (yes/no): ")
        if continue_execution.lower() != "yes":
            break

if __name__ == "__main__":
    main()
