import unittest
from src.servo_controller.controller import ServoController

class TestServoController(unittest.TestCase):

    def setUp(self):
        self.controller = ServoController()

    def test_initial_positions(self):
        self.assertEqual(self.controller.get_servo_positions(), [0, 0, 0])

    def test_move_servos(self):
        self.controller.move_servos([90, 45, 180])
        self.assertEqual(self.controller.get_servo_positions(), [90, 45, 180])

    def test_move_servos_out_of_bounds(self):
        self.controller.move_servos([200, -10, 360])
        self.assertEqual(self.controller.get_servo_positions(), [180, 0, 360])

if __name__ == '__main__':
    unittest.main()