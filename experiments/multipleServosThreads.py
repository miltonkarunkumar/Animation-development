import object_sketch
import threading
import time
import selectEasing
from servo import Servo, servo2040
import easingfunctions as easing

# Function to control a single servo
def control_single_servo(servo):
    while True:
        angle = float(input("Enter the target angle for servo {} (-90 to 90 degrees): ".format(servo.name)))
        duration = float(input("Enter the duration in milliseconds for servo {}: ".format(servo.name)))
 
        easing_function_name = selectEasing.selectEasingFunction()
        if hasattr(easing, easing_function_name):
            easing_function = getattr(easing, easing_function_name)
            servo.ease_to(angle, duration, easing_function)

            while servo._isMoving:
                servo.update()
                time.sleep(0.01)
        else:
            print("Invalid function, try again.")
            break

# Taking input from user for the number of servos
num_servos = int(input("Enter the number of servos: "))
servos = []

# Creating objects for EasedServo and controlling them in separate threads
for i in range(num_servos):
    servo_pin_number = input("Enter servo pin number for servo {}: ".format(i + 1))
    servo_pin = "SERVO_" + str(servo_pin_number)
    my_servo = object_sketch.EasedServo(getattr(servo2040, servo_pin))
    my_servo.name = "Servo {}".format(i + 1)
    servos.append(my_servo)

threads = []

for servo in servos:
    thread = threading.Thread(target=control_single_servo, args=(servo,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
