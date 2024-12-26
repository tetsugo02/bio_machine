import os
from . import load_morse
from enum import Enum


class Mode(Enum):
  English = 1
  Japanese = 2


class MorseDecoder:
  def __init__(self):
    # 現在のファイルの場所を基準にしたパスを構築
    current_dir = os.path.dirname(os.path.abspath(__file__))
    eng_morse_path = os.path.join(current_dir, "morse_data", "morse_eng.json")
    jpn_morse_path = os.path.join(current_dir, "morse_data", "morse_jpn.json")

    self.eng_morse = load_morse.load_morse(eng_morse_path)
    self.jpn_morse = load_morse.load_morse(jpn_morse_path)
    self.mode = Mode.Japanese  # デフォルトは英語モード
    self.morse = self.eng_morse

  def decode_morse_to_str(self, morse_code: str) -> str:
    if self.mode == Mode.English:
      self.morse = self.eng_morse
    else:
      self.morse = self.jpn_morse
    decoded_str = None

    # モールス信号を文字に変換
    for character, morse in self.morse.items():
      if morse_code == morse:
        decoded_str = character
        break

    return decoded_str

  def change_mode(self) -> None:
    if self.mode == Mode.English:
      self.mode = Mode.Japanese
      os.system("osascript -e 'tell application \"System Events\" to key code 104'")
    else:
      self.mode = Mode.English
      os.system("osascript -e 'tell application \"System Events\" to key code 102'")
