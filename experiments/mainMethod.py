import object_sketch
import time
from servo import Servo, servo2040
import easingfunctions as easing


# my_servo = EasedServo(1)
my_servo = object_sketch.EasedServo(servo2040.SERVO_1)
print(servo2040.SERVO_1)
my_servo.ease_to(-90, 1000, easing.easeInQuint)

while my_servo._isMoving:
    my_servo.update()
    print(my_servo.proportion_complete)
    time.sleep(0.01)

time.sleep_ms(200)
my_servo.ease_to(90, 1000, easing.easeOutQuint)

while my_servo._isMoving:
    my_servo.update()
    time.sleep(0.01)

print("Done!")

