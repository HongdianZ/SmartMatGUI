import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import serial
from PIL import ImageTk, Image, ImageDraw, ImageFont
import numpy as np
import time
from scipy.ndimage import gaussian_filter, zoom
from matplotlib.figure import Figure
import threading


class PressureMonitorSystem:
    def __init__(self, master):
        self.master = master
        master.title("Pressure Monitoring System")

        # Flags for setting
        self.stop_plotting = False
        self.start_pressed = False
        self.half_sensor = False
        self.row = 64
        self.column = 128
        # Create left frame with labels and buttons
        left_frame = tk.Frame(master, bg='gray', width=400, height=320)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        left_frame.pack_propagate(False)

        title_label = tk.Label(left_frame, text="Pressure Injury Monitoring", font=("Helvetica", 20), bg='gray')
        title_label.pack(pady=15)

        button1 = tk.Button(left_frame, text="Start", font=("Helvetica", 14), bg='white', width=20, height=1,
                            relief=tk.RAISED, command=self.start_recording)
        button1.pack(pady=5)

        button2 = tk.Button(left_frame, text="Decrease Resolution", font=("Helvetica", 14), bg='white', width=20,
                            height=1, relief=tk.RAISED, command=self.decrease_resolution)
        button2.pack(pady=5)

        button3 = tk.Button(left_frame, text="Full Resolution", font=("Helvetica", 14), bg='white', width=20, height=1,
                            relief=tk.RAISED, command=self.full_resolution)
        button3.pack(pady=5)

        button4 = tk.Button(left_frame, text="Stop", bg='white', font=("Helvetica", 14), width=20, height=1,
                            relief=tk.RAISED, command=self.stop_recording)
        button4.pack(pady=5)

        # Create text box to display messages
        self.text_box = tk.Text(left_frame, bg='red', width=30, height=2)
        self.text_box.pack(pady=10)

        # Create right frame for displaying updated image
        right_frame = tk.Frame(master)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create a placeholder image for initial display
        self.img_array = np.zeros((320, 640), dtype=np.uint8)
        self.img = Image.fromarray(self.img_array)
        self.photo = ImageTk.PhotoImage(self.img)

        # Add image to label in right frame
        self.image_label = tk.Label(right_frame, image=self.photo)
        self.image_label.pack(fill=tk.BOTH, expand=True)

        # Call function to update image
        self.welcome_image()

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
        ser = serial.Serial('COM3', 2500000)
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
        ser = serial.Serial('COM5', 2000000)
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        time.sleep(1)
        ser.write(b'upper')
        print(ser.readline())

    def stop_recording(self):
        self.stop_plotting = False
        self.text_box.delete('1.0', 'end')
        self.text_box.insert(tk.END, "Recording stopped.")
        self.text_box.update()
        self.update_image()
        self.thread.join()

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
        ser = serial.Serial('COM3', 2500000)
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
                for row in range(num_rows):  # read the value one by one
                    for col in range(num_cols):  # read the value one by one
                        string = ser.readline()  # read from serial port and store the value from one line
                        value = int(string)  # transfer to interger
                        output[row, col] = value
                        # print("row:{}, col:{}, value:{}".format(row, col, value))
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

        self.thread = threading.Thread(target=monitor_pressure)
        self.thread.start()


window = tk.Tk()
platform = PressureMonitorSystem(window)
window.mainloop()
