class ServoController:
    def __init__(self, ros_interface):
        self.ros_interface = ros_interface
        self.servo_angles = [0, 0, 0]  # Initial angles for the servos

    def move_servos(self):
        for angle in range(0, 181, 10):  # Move from 0 to 180 degrees
            self.servo_angles = [angle, angle, angle]  # Update angles for all servos
            self.ros_interface.publish_servo_positions(self.servo_angles)
            time.sleep(0.1)  # Delay to simulate movement time

        for angle in range(180, -1, -10):  # Move back from 180 to 0 degrees
            self.servo_angles = [angle, angle, angle]  # Update angles for all servos
            self.ros_interface.publish_servo_positions(self.servo_angles)
            time.sleep(0.1)  # Delay to simulate movement time

    def get_servo_angles(self):
        return self.servo_angles