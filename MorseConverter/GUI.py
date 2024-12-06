import tkinter as tk
from tkinter import scrolledtext, ttk
from MorseDecoder import MorseDecoder


class MorseConverter:
    def __init__(self):
        # モールス信号デコーダーの初期化
        self.decoder = MorseDecoder()
        self.decoded_text = ""  # 今までデコードした文字列を保存
        self.root = tk.Tk()
        self.current_timer = None  # タイマー
        self.setup_root_window()
        self.create_widgets()

    def setup_root_window(self):
        """ウィンドウの基本設定"""
        self.root.title("モールス信号デコーダ")
        self.root.geometry("500x500")
        self.root_frame = ttk.Frame(self.root, padding=(10, 10))
        self.root_frame.pack(expand=True, fill=tk.BOTH)

        # レイアウト用の行列設定
        for i in range(4):  # 4行分のレイアウト
            self.root_frame.grid_rowconfigure(i, weight=1 if i in range(2) else 0)
        self.root_frame.grid_columnconfigure(0, weight=1)

    def create_widgets(self):
        """ウィジェットを作成"""
        self.create_input_area()
        self.create_current_char_label()
        self.create_decoded_textbox()

    def create_input_area(self):
        """入力エリア（モールス信号入力用）を作成"""
        self.input_area = scrolledtext.ScrolledText(
            self.root_frame, wrap=tk.WORD, width=50, height=3
        )
        self.input_area.grid(row=0, column=0, sticky="nsew", padx=5, pady=(5, 10))
        self.input_area.insert(tk.END, "ここにモールス信号を入力してください")
        
        # キーイベントをバインドしてタイマーをリセット
        self.input_area.bind("<Key>", self.reset_timer)

    def create_current_char_label(self):
        """現在のデコード結果を表示するラベルを作成"""
        self.current_char_label = ttk.Label(
            self.root_frame, text="現在の文字: ", font=("Helvetica", 14), anchor="w"
        )
        self.current_char_label.grid(
            row=1, column=0, sticky="ew", padx=5, pady=(10, 5)
        )

    def create_decoded_textbox(self):
        """今までのデコード文字列を表示するテキストボックスを作成"""
        self.decoded_textbox = scrolledtext.ScrolledText(
            self.root_frame, wrap=tk.WORD, width=50, height=10
        )
        self.decoded_textbox.grid(
            row=2, column=0, sticky="nsew", padx=5, pady=(5, 10)
        )

    def reset_timer(self, event=None):
        """キー入力時にデコードタイマーをリセット"""
        if self.current_timer is not None:
            self.root.after_cancel(self.current_timer)  # 現在のタイマーをキャンセル
        self.current_timer = self.root.after(3000, self.decode_input)  # 新たにタイマーをセット

    def decode_input(self):
        """入力エリアの内容をデコード"""
        # 入力エリアからモールス信号を取得
        morse_code = self.input_area.get("1.0", tk.END).strip()

        if morse_code:  # 入力がある場合
            # デコード
            decoded_char = self.decoder.decode_morse_to_str(morse_code)

            # 現在の文字を更新
            self.update_current_char(decoded_char)

            # 今までの文字列に追加
            self.append_decoded_text(decoded_char)

            self.input_area.delete("1.0", tk.END)

        self.current_timer = None  # タイマーをリセット

    def update_current_char(self, char):
        """現在のデコード結果をラベルに表示"""
        self.current_char_label.config(text=f"現在の文字: {char}")

    def append_decoded_text(self, char):
        """デコード文字列をテキストボックスに追加"""
        self.decoded_text += char
        self.decoded_textbox.insert(tk.END, char)
        self.decoded_textbox.see(tk.END)  # 自動スクロール

    def run(self):
        """GUIアプリケーションを実行"""
        self.root.mainloop()


if __name__ == "__main__":
    converter = MorseConverter()
    converter.run()
