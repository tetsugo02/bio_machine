import serial
import serial.tools.list_ports
import queue
import time

arduino_port = "/dev/cu.usbmodem1101"
virtual_port = "/dev/ttys015"


class SerialComu:
  def __init__(self, port=arduino_port, baudrate=9600):
    self.port = port
    self.baudrate = baudrate
    self.threshold_A0 = 60  # 電圧の閾値
    self.threshold_A1 = 50  # 電圧の閾値
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
        value_str_A0: str = value_str.split(",")[0]
        value_str_A1: str = value_str.split(",")[1]
        value_A0: float = float(value_str_A0)
        value_A1: float = float(value_str_A1)
        if value_A0 > self.threshold_A0 and now - last_time > 1.5:
          self.data_Queue.put(".")
          last_time = now
          print("A0 over threshold")
        if value_A1 > self.threshold_A1 and now - last_time > 1.5:
          self.data_Queue.put("-")
          last_time = now
          print("A1 over threshold")

        print(f"Received: {value_str}")
        ############################
        # Debug
        # value = value_str
        # self.data_Queue.put(value)
        # print(f"Received: {value},type: {type(value)}, morseSignal: {value}")
        ############################

  def stop(self):
    self.running = False
    self.ser.close()


if __name__ == "__main__":
  serialcomu = SerialComu()
  serialcomu.read_line_serial()
