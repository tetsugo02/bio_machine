import serial
import serial.tools.list_ports


class SerialComu:
  def __init__(self,port="/dev/cu.usbmodem1101",baudrate=9600):
    self.port = port
    self.baudrate = baudrate
    self.ser = serial.Serial(port, baudrate, timeout=1)
    
  def read_line_serial(self):
    while True:
      if self.ser.in_waiting > 0:
        data = self.ser.readline()  # データを1行読み込む
        values = data.decode("utf-8") # decode
        print("Received:", values)
