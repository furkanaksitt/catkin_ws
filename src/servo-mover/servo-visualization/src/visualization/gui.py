from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
import sys

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Servo Visualization")
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel("Servo Positions: ", self)
        self.label.setStyleSheet("font-size: 20px;")

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.servo_positions = [0, 0, 0]
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)
        self.timer.start(100)  # Update every 100 ms

    def update_display(self):
        # Here you would normally get the servo positions from the controller
        # For demonstration, we will simulate movement
        self.servo_positions = [(pos + 5) % 180 for pos in self.servo_positions]
        self.label.setText(f"Servo Positions: {self.servo_positions}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())