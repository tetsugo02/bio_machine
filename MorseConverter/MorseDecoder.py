import load_morse
from enum import Enum


class Mode(Enum):
    English = 1
    Japanese = 2


class MorseDecoder:
    def __init__(self):
        self.eng_morse = load_morse.load_morse("./morse_data/morse_eng.json")
        self.jpn_morse = load_morse.load_morse("./morse_data/morse_jpn.json")
        self.mode = Mode.English  # デフォルトは英語モード
        self.morse = self.eng_morse
        self.morseSignal_of_delete = "......"
        self.morseSignal_of_change_mode = "------"

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
        # 特殊な文字列の場合
        match morse_code:
            case self.morseSignal_of_delete:
                decoded_str = "delete"
            case self.morseSignal_of_change_mode:
                decoded_str = "change_mode"

        return decoded_str

    def change_mode(self):
        if self.mode == Mode.English:
            self.mode = Mode.Japanese
        else:
            self.mode = Mode.English
