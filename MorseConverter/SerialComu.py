import serial
import serial.tools.list_ports
import queue


class SerialComu:
  def __init__(self, port="/dev/cu.usbmodem1101", baudrate=9600):
    self.port = port
    self.baudrate = baudrate
    self.ser = serial.Serial(port, baudrate, timeout=1)
    self.running = True
    self.data_Queue = queue.Queue()  # データ共有用のキュー

  def read_line_serial(self):
    while self.running:
      if self.ser.in_waiting > 0:
        data = self.ser.readline()  # データを1行読み込む
        values = data.decode("utf-8").strip()  # decode
        self.data_Queue.put(values)

  def stop(self):
    self.running = False
    self.ser.close()
