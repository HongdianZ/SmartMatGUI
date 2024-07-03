from UI_interface import *
##IMPORTS
import sys
import numpy as np
from PIL import Image, ImageQt
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QTime, QTimer
from PySide6.QtWidgets import QMainWindow, QLabel

# Import the generated UI file from PySide6
from UI_interface import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## Window settings
        self.resize(1280, 960)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowIcon(QtGui.QIcon("Icon/icons8-pressure-40.png"))
        self.setWindowTitle("Pressure Monitor System")

        # Minimalize and close buttons
        self.ui.ShrinkWindowButton.clicked.connect(self.showMinimized)
        self.ui.ResizeWindowButton.clicked.connect(self.restore_or_maximize_window)
        self.ui.CloseWindowButton.clicked.connect(self.close)

        # Buttons
        self.ui.Start.clicked.connect(self.start_recording)
        self.ui.Stop.clicked.connect(self.stop_recording)

        # Clock
        self.update_clock()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        # Add a QLabel dynamically for image display
        self.image_label = QLabel(self.ui.PressureDisplay)
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)

        # Layout to ensure QLabel resizes properly
        layout = QtWidgets.QVBoxLayout(self.ui.PressureDisplay)
        layout.addWidget(self.image_label)
        layout.setContentsMargins(0, 0, 0, 0)
        self.ui.PressureDisplay.setLayout(layout)

        # Print initial setup complete
        print("UI Setup Complete. Window initialized.")

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.ResizeWindowButton.setIcon(QtGui.QIcon(u"Icon/icons8-resize-96.png"))
        else:
            self.showMaximized()
            self.ui.ResizeWindowButton.setIcon(QtGui.QIcon(u"Icon/icons8-shrink-96.png"))

    def update_clock(self):
        current_time = QTime.currentTime()
        formatted_time = current_time.toString("hh:mm:ss")
        self.ui.Time.display(formatted_time)
        print("Clock updated:", formatted_time)

    def start_recording(self):
        print("Start recording clicked.")
        self.display_static_image()

    def stop_recording(self):
        print("Stop recording clicked.")
        if hasattr(self.ui, 'AIResult'):
            self.ui.AIResult.setText("Operation stopped.")
        else:
            print("Error: AIResult widget not found.")

    def display_static_image(self):
        img_array = np.random.randint(0, 255, size=(320, 640), dtype=np.uint8)
        heatmap_img = Image.fromarray(img_array, mode='L')
        heatmap_img = heatmap_img.convert('RGB').resize((640, 320), Image.NEAREST)
        img = ImageQt.ImageQt(heatmap_img)
        self.image_label.setPixmap(QtGui.QPixmap.fromImage(img))
        print("Static image displayed.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
