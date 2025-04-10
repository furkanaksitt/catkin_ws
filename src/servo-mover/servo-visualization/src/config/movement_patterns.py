def circular_movement(steps=100, radius=50):
    import math
    return [(radius * math.cos(2 * math.pi * i / steps), radius * math.sin(2 * math.pi * i / steps)) for i in range(steps)]

def linear_movement(steps=100, distance=100):
    return [(i * distance / steps, 0) for i in range(steps)]

def zigzag_movement(steps=100, amplitude=20, frequency=5):
    return [(i, amplitude * math.sin(frequency * i * (2 * math.pi / steps))) for i in range(steps)]

def get_movement_pattern(pattern_name):
    patterns = {
        'circular': circular_movement,
        'linear': linear_movement,
        'zigzag': zigzag_movement,
    }
    return patterns.get(pattern_name, None)