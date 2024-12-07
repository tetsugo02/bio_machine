import tkinter as tk
from tkinter import scrolledtext, ttk
from MorseDecoder import MorseDecoder
import os


class Moji:
  def __init__(self, interval: int = 3000) -> None:
    # モールス信号デコーダーの初期化
    self.root = tk.Tk()
    self.decoder = MorseDecoder()
    self.decoded_text = ""  # 今までデコードした文字列を保存
    self.current_timer = None  # タイマー
    self.interval = interval
    self.setup_root_window()
    self.create_widgets()
    self.change_mode_button()

  def setup_root_window(self) -> None:
    """ウィンドウの基本設定"""
    self.root.title("静電文字入力")
    self.root.geometry("600x600")
    self.root_frame = ttk.Frame(self.root, padding=(10, 10))
    self.root_frame.pack(expand=True, fill=tk.BOTH)

    # レイアウト用の行列設定
    for i in range(4):  # 4行分のレイアウト
      self.root_frame.grid_rowconfigure(
          i, weight=1 if i in range(2) else 0)
    self.root_frame.grid_columnconfigure(0, weight=1)

  def create_widgets(self) -> None:
    """ウィジェットを作成"""
    self.create_input_area()
    self.create_current_char_label()
    self.create_decoded_textbox()

  def create_input_area(self) -> None:
    """入力エリア（モールス信号入力用）を作成"""
    self.input_area = scrolledtext.ScrolledText(
        self.root_frame, wrap=tk.WORD, width=50, height=3
    )
    self.input_area.grid(
        row=0, column=0, sticky="nsew", padx=5, pady=(5, 10))
    self.input_area.insert(tk.END, "ここにモールス信号を入力してください")

    self.input_area.bind(
        "<FocusIn>", lambda e: self.input_area.delete("1.0", tk.END))
    # キーイベントをバインドしてタイマーをリセット
    self.input_area.bind("<Key>", self.reset_timer)
    self.input_area.bind("<<Modified>>", self.on_text_change)

  def create_current_char_label(self) -> None:
    """現在のデコード結果とモードを表示するラベルを作成"""
    # フレームを作成してラベルを配置
    self.status_frame = ttk.Frame(self.root_frame)
    self.status_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=(10, 10))

    # 現在の文字ラベル
    self.current_char_label = ttk.Label(
        self.status_frame, text="現在の文字: ", font=("Helvetica", 20), anchor="w"
    )
    self.current_char_label.grid(row=0, column=0, sticky="w", padx=10)

    # 現在のモードラベル
    self.current_mode_label = ttk.Label(
        self.status_frame, text=f"現在のモード: {self.decoder.mode}", font=("Helvetica", 20), anchor="e"
    )
    self.current_mode_label.grid(row=0, column=1, sticky="e", padx=10)

    # 列の幅を調整
    self.status_frame.grid_columnconfigure(0, weight=1)
    self.status_frame.grid_columnconfigure(1, weight=1)

  def create_decoded_textbox(self) -> None:
    """今までのデコード文字列を表示するテキストボックスを作成"""
    self.decoded_textbox = scrolledtext.ScrolledText(
        self.root_frame, wrap=tk.WORD, width=50, height=10, font=("Helvetica", 20)
    )
    self.decoded_textbox.grid(
        row=3, column=0, sticky="nsew", padx=5, pady=(5, 10)
    )

  def change_mode_button(self) -> None:
    """モード変更ボタンを作成"""
    self.change_mode_button = ttk.Button(
        self.root_frame, text="モード変更", command=self.change_mode
    )
    self.change_mode_button.grid(
        row=4, column=0, sticky="ew", padx=5, pady=5)

  def reset_timer(self, event=None) -> None:
    """キー入力時にデコードタイマーをリセット"""
    if self.current_timer is not None:
      self.root.after_cancel(self.current_timer)  # 現在のタイマーをキャンセル
    self.current_timer = self.root.after(self.interval, self.decode_input_and_update)  # 新たにタイマーをセット

  def decode_input_and_update(self) -> None:
    """入力エリアの内容をデコード"""
    # 入力エリアからモールス信号を取得
    morse_code = self.input_area.get("1.0", tk.END).strip()
    decoded_char = None

    if morse_code:  # 入力がある場合
      # デコード
      decoded_char = self.decoder.decode_morse_to_str(morse_code)
      if decoded_char is not None:
        decoded_char = decoded_char.lower()
      else:
        pass

    match decoded_char:
      # デコード結果に応じて処理を分岐
      # 　特殊な文字列の場合
      case "delete":
        self.decoded_text = self.decoded_text[:-1]
        self.decoded_textbox.delete("end-2c", tk.END)
        os.system(f'say {decoded_char}')
      case "change_mode":
        self.change_mode()
        os.system(f'say {decoded_char}')
      case "read_all":
        os.system(f'say {self.decoded_text}')
      case None:
        pass
      case _:
        # 今までの文字列に追加
        self.append_decoded_text(decoded_char)
        os.system(f'say {decoded_char}')  # 読み上げ用のキューに追加

    # 現在の文字を更新
    self.update_current_char(decoded_char)

    self.input_area.delete("1.0", tk.END)
    self.current_timer = None  # タイマーをリセット

  def update_current_char(self, char: str) -> None:
    """現在のデコード結果をラベルに表示"""
    self.current_char_label.config(text=f"現在の文字: {char}")

  def change_mode(self):
    """モードを変更"""
    self.decoder.change_mode()
    self.current_mode_label.config(text=f"現在のモード: {self.decoder.mode}")

  def append_morse_code(self, morse_code: str) -> None:
    """モールス信号を入力エリアに追加"""
    self.input_area.insert(tk.END, morse_code)
    print(f"insert: {morse_code}")

  def append_decoded_text(self, char: str) -> None:
    """デコード文字列をテキストボックスに追加"""
    self.decoded_text += char
    self.decoded_textbox.insert(tk.END, char)
    self.decoded_textbox.see(tk.END)  # 自動スクロール

  def on_text_change(self, event: any) -> None:
    """テキストが変更されたときの処理"""
    self.input_area.edit_modified(False)  # 変更フラグをリセット
    self.reset_timer()  # タイマーをリセット

  def run(self):
    """GUIアプリケーションを実行"""
    self.root.mainloop()


if __name__ == "__main__":
  converter = Moji()
  converter.run()
