import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
from MorseDecoder import MorseDecoder

class MorseConverter:
  
  def __init__(self):
    self.decoder = MorseDecoder()
    self.root = tk.Tk()
    self.root.title = "モールス信号変換器"
    self.root.geometry("800x600")
    

  def creat_widgets(self):
    self.root_frame = ttk.Frame(self.root, padding=(5, 5))
  
  def run(self):
    self.root.mainloop()

if __name__ == "__main__":
  converter = MorseConverter()
  converter.run()