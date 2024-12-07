import serial
import serial.tools.list_ports
import queue

arduino_port = "/dev/cu.usbmodem1101"
virtual_port = "/dev/ttys018"


class SerialComu:
  def __init__(self, port=virtual_port, baudrate=9600):
    self.port = port
    self.baudrate = baudrate
    self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
    self.running = True
    self.data_Queue = queue.Queue()  # データ共有用のキュー
    print(f"Connected to {self.port}")

  def read_line_serial(self):
    while self.running:
      if self.ser.in_waiting > 0:
        data = self.ser.readline()  # データを1行読み込む
        values = data.decode("utf-8").strip()  # decode
        self.data_Queue.put(values)
        print(f"Received: {values}")

  def stop(self):
    self.running = False
    self.ser.close()


if __name__ == "__main__":
  serialcomu = SerialComu()
  serialcomu.read_line_serial()
