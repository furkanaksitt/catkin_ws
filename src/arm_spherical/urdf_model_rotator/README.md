# URDF Model Rotator

This project provides a Python script to continuously rotate a URDF model in a ROS environment. It utilizes ROS's `rospy` library to publish rotation commands to the model.

## Project Structure

```
urdf_model_rotator
├── src
│   ├── main.py          # Main script to run the rotation
│   └── utils
│       └── __init__.py  # Utility functions for rotation logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. **Install ROS**: Ensure that you have ROS installed on your system. Follow the instructions on the [ROS installation guide](http://wiki.ros.org/ROS/Installation).

2. **Create a Python Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**: Install the required Python packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Script

To run the rotation script, follow these steps:

1. Open a terminal and source your ROS workspace:
   ```bash
   source /opt/ros/<your_ros_distro>/setup.bash
   ```

2. Launch your ROS core:
   ```bash
   roscore
   ```

3. In a new terminal, navigate to the project directory and run the main script:
   ```bash
   cd path/to/urdf_model_rotator/src
   python main.py
   ```

## Additional Information

- The `main.py` script initializes the ROS node and continuously publishes rotation commands to the specified URDF model.
- You can modify the rotation parameters in the `main.py` file as needed.
- For any utility functions or additional logic, you can add them in the `utils/__init__.py` file.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.