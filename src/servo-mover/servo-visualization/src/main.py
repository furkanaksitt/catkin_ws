import sys
import time
from servo_controller.controller import ServoController
from visualization.gui import GUI

def main():
    servo_controller = ServoController()
    gui = GUI()

    while True:
        servo_controller.move_servos()
        gui.update_display(servo_controller.get_servo_angles())
        time.sleep(0.1)

if __name__ == "__main__":
    main()