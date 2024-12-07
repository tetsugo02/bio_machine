import tkinter as tk
from pynput import keyboard
from MorseDecoder import MorseDecoder
import time

# モールス信号デコーダを初期化
morse_decoder = MorseDecoder()

# 入力のタイムアウト時間
INACTIVITY_TIMEOUT = 3

current_symbol = ""
morse_input = ""
last_input_time = time.time()


# GUIの更新関数
def update_gui(decoded_message):
  result_label.config(text=f"デコード結果: {decoded_message}")


# キーが押されたときの処理
def on_press(key):
  global current_symbol, morse_input, last_input_time

  try:
    last_input_time = time.time()  # 最後の入力時間を更新

    if key.char == ".":
      current_symbol += "."
    elif key.char == "-":
      current_symbol += "-"
    elif key == keyboard.Key.space:  # スペースで文字区切り
      if current_symbol:
        morse_input += current_symbol + " "
        current_symbol = ""
  except AttributeError:
    pass


# タイムアウトの監視
def check_timeout():
  global current_symbol, morse_input, last_input_time

  # 現在時刻と最後の入力時刻を比較
  if time.time() - last_input_time > INACTIVITY_TIMEOUT:
    if current_symbol or morse_input:
      # 未処理の入力を追加
      if current_symbol:
        morse_input += current_symbol
        current_symbol = ""

      # 判定を実行
      decoded_message = morse_decoder.decode_morse_to_str(morse_input.strip())
      update_gui(decoded_message)
      morse_input = ""  # 入力リセット
    last_input_time = time.time()  # タイマーリセット

  # 再帰的にタイムアウトを監視
  root.after(100, check_timeout)


# GUIのセットアップ
root = tk.Tk()
root.title("モールス信号デコーダ")

# ラベルウィジェット
instruction_label = tk.Label(
    root,
    text="モールス信号を入力してください",
    font=("Arial", 12),
    wraplength=400
)
instruction_label.pack(pady=10)

result_label = tk.Label(root, text="デコード結果: ", font=("Arial", 16))
result_label.pack(pady=20)

# キーボードリスナーを開始
listener = keyboard.Listener(on_press=on_press)
listener.start()

# タイムアウト監視を開始
check_timeout()

# GUIのメインループ
try:
  root.mainloop()
except KeyboardInterrupt:
  print("\nプログラムを終了します。")
  listener.stop()
