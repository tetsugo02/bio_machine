import serial
import serial.tools.list_ports
import queue
import time

arduino_port = "/dev/cu.usbmodem1101"
virtual_port = "/dev/ttys015"


class SerialComu:
  def __init__(self, port=virtual_port, baudrate=9600, threshold=50, morseSignal="."):
    self.port = port
    self.baudrate = baudrate
    self.threshold = threshold  # 電圧の閾値
    self.morseSignal = morseSignal  # モールス信号として使う文字
    self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
    self.running = True
    self.data_Queue = queue.Queue()  # データ共有用のキュー
    print(f"Connected to {self.port}")

  def read_line_serial(self):
    last_time = time.time()

    while self.running:
      now = time.time()
      if self.ser.in_waiting > 0:
        data = self.ser.readline()  # データを1行読み込む
        value_str = data.decode("utf-8").strip()  # decode
        # value = float(value_str)
        # if value > self.threshold and now - last_time > 1.4:
        #  self.data_Queue.put(self.morseSignal)
        #  last_time = now
        #  print("over threshold")
        #  print(f"Received: {value},type: {type(value)}, morseSignal: {self.morseSignal}")
        ############################
        # Debug
        value = value_str
        self.data_Queue.put(value)
        print(f"Received: {value},type: {type(value)}, morseSignal: {value}")
        ############################

  def stop(self):
    self.running = False
    self.ser.close()


if __name__ == "__main__":
  serialcomu = SerialComu()
  serialcomu.read_line_serial()
