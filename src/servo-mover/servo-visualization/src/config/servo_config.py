# servo-visualization/src/config/servo_config.py

SERVO_PINS = {
    'servo1': 9,
    'servo2': 10,
    'servo3': 11
}

ANGLE_LIMITS = {
    'servo1': (0, 180),
    'servo2': (0, 180),
    'servo3': (0, 360)
}

MOVEMENT_SPEED = 0.1  # Speed of servo movement in seconds per degree

DEFAULT_POSITIONS = {
    'servo1': 90,
    'servo2': 90,
    'servo3': 180
}