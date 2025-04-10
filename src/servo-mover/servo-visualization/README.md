# Servo Visualization Project

This project is designed to control and visualize the movement of servo motors using a graphical user interface. It integrates with ROS (Robot Operating System) to receive commands and publish servo positions.

## Project Structure

```
servo-visualization
├── src
│   ├── main.py                  # Entry point of the application
│   ├── servo_controller          # Package for servo control logic
│   │   ├── __init__.py
│   │   ├── controller.py         # Manages servo movements
│   │   └── ros_interface.py      # Handles ROS communication
│   ├── visualization             # Package for GUI components
│   │   ├── __init__.py
│   │   ├── gui.py                # Creates the GUI for visualization
│   │   └── renderer.py           # Renders the 3D model of the arm
│   └── config                   # Package for configuration settings
│       ├── __init__.py
│       ├── servo_config.py       # Configuration constants for servos
│       └── movement_patterns.py   # Defines movement patterns for servos
├── resources
│   └── models
│       └── arm_model.obj         # 3D model of the arm
├── tests
│   ├── __init__.py
│   ├── test_controller.py        # Unit tests for ServoController
│   └── test_visualization.py     # Unit tests for GUI and Renderer
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd servo-visualization
   ```

2. **Install dependencies**:
   Ensure you have Python and pip installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Execute the main script:
   ```
   python src/main.py
   ```

## Usage Guidelines

- The application will initialize the servo motors and start the GUI.
- You can interact with the GUI to visualize the servo movements.
- The system communicates with ROS to receive commands and update servo positions accordingly.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.