import pyttsx3
import time
class TextReader:
  def __init__(self):
    self.read_engine = pyttsx3.init(driverName="nsss")
    self.read_engine.setProperty("rate", 150)
    self.read_engine.setProperty("volume", 0.9)
    
  def run_pyttx3(self, read_queue):
    """読み上げ処理"""
    while True:
      if not read_queue.empty():
        text = read_queue.get()  # データを取得
        read_queue.task_done()  # タスクを完了
        self.read_engine.say(text)
        self.read_engine.runAndWait()