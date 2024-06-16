##IMPORTS
import serial
import sys
import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import queue
import numpy as np
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Slot
from PySide2.QtMultimedia import QAudioDeviceInfo, QAudio, QCameraInfo
from qt_material import *
##Import GUI
from UI_interface import *
port_number = 'COM10'
buad_rate = 2000000

##Main window
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow() #Create UI
        self.ui.setupUi(self) #Setup UI
        ## load stylesheet
        #apply_stylesheet(app, theme='dark_teal.xml')
        ##Window settings
        self.resize(1280, 960)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 92, 157, 550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        self.setWindowIcon(QtGui.QIcon("Icon/icons8-pressure-40.png"))
        self.setWindowTitle("Pressure Monitor System")
        QSizeGrip(self.ui.SizeGrip)
        #minimalize and close buttons
        self.ui.ShrinkWindowButton.clicked.connect(lambda: self.showMinimized())
        self.ui.ResizeWindowButton.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.CloseWindowButton.clicked.connect(lambda: self.close())
        self.ui.Start.clicked.connect(lambda: self.start_recording())
        self.ui.Stop.clicked.connect(lambda: self.stop_recording())
        ##Clock
        self.update_clock()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)
        self.show()

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

    def start_recording(self):
        self.start_pressed = True
        self.text_box.delete('1.0', 'end')
        self.text_box.insert(tk.END, "Recording started.")
        self.text_box.update()
        threading.Thread(target=self.plotpressure_image).start()

    def decrease_resolution(self):
        self.half_sensor = True
        self.text_box.delete('1.0', 'end')
        self.text_box.insert(tk.END, "Now using 2048 sensing points.")
        self.text_box.update()
        ser = serial.Serial(port_number, buad_rate)
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        time.sleep(1)
        ser.write(b'lower')
        print(ser.readline())

    def full_resolution(self):
        self.half_sensor = False
        self.row = 64
        self.column = 128
        self.text_box.delete('1.0', 'end')
        self.text_box.insert(tk.END, "Now using 8192 sensing points.")
        self.text_box.update()
        ser = serial.Serial(port_number, buad_rate)
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        time.sleep(1)
        ser.write(b'upper')
        print(ser.readline())


    def stop_recording(self):
        self.stop_plotting = False
        scene = QGraphicsScene()
        scene.addText("Hello, world!")
        view = self.ui.PressureDisplay(scene)
        view.show()


    def update_image(self):
        # Generate random image data for demo purposes
        self.img_array = np.random.randint(0, 255, size=(320, 640), dtype=np.uint8)
        self.img = Image.fromarray(self.img_array)
        self.photo = ImageTk.PhotoImage(self.img)

        # Update image label
        self.image_label.configure(image=self.photo)
        self.image_label.image = self.photo

        # Schedule next update after 1 second
        self.master.after(500, self.update_image)

    def welcome_image(self):
        self.img = Image.new('RGB', (640, 320), color=(255, 255, 255))
        draw = ImageDraw.Draw(self.img)
        message = "Welcome to Pressure Monitoring System!\n\n                 Press button to start."
        font = ImageFont.truetype("arial.ttf", 30)
        w, h = draw.textsize(message, font=font)
        draw.text(((640 - w) / 2, (320 - h) / 2), message, font=font, fill=(0, 0, 0))

        # Update image label with the welcome image
        self.img_array = np.array(self.img)
        self.img = Image.fromarray(self.img_array)
        self.photo = ImageTk.PhotoImage(self.img)
        self.image_label.configure(image=self.photo)
        self.image_label.image = self.photo

    def plotpressure_image(self):
        self.stop_plotting = True  # Initialize the flag variable
        ser = serial.Serial(port_number, buad_rate)
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        time.sleep(1)
        if self.half_sensor:
            num_rows = 32
            num_cols = 64
        else:
            num_rows = 64
            num_cols = 128
        output = np.ones((num_rows, num_cols), dtype=int)
        output = output
        def monitor_pressure():
            # Start pressure monitoring loop
            while self.stop_plotting:
                ser.write(b'start')
                # Read the output values from the device
                for row in range(num_rows):     # read the value one by one
                    for col in range(num_cols): # read the value one by one
                        string = ser.readline() #read from serial port and store the value from one line
                        value = int(string) #transfer to interger
                        output[row, col] = value
                        #print("row:{}, col:{}, value:{}".format(row, col, value))
                print("finished!\r\n")
                # Update pressure data
                smoothed_pressure = gaussian_filter(output, sigma=0.8)
                if self.half_sensor:
                    resized_pressure = zoom(smoothed_pressure, 10, order=1)
                else:
                    resized_pressure = zoom(smoothed_pressure, 5, order=1)
                # Update heatmap image
                self.img_array = np.uint8(resized_pressure)
                heatmap_img = Image.fromarray(self.img_array, mode='RGB')
                heatmap_img = heatmap_img.resize((640, 320), Image.NEAREST)
                self.img = ImageTk.PhotoImage(heatmap_img)

                # Update image label
                self.image_label.configure(image=self.img)
                self.image_label.image = self.img
                # Update text box
                self.text_box.delete('1.0', 'end')
                self.text_box.insert(tk.END, "Recording...\n\nPress button to stop.")
                self.text_box.update()
                time.sleep(0.1)

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        fig.tight_layout()

class Worker(QtCore.QRunnable):

    def __init__(self, function, *args, **kwargs):
        super(Worker, self).__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        self.function(*self.args, **self.kwargs)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
