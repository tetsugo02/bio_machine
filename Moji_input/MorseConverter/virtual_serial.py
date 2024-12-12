import time
import serial

# 仮想シリアルポートの設定
# !NOTE: socatで生成した仮想ポートは、入力と出力2つ存在する。
PORT = "/dev/ttys014"  # 仮想ポートを指定（Windowsなら 'COM3'）
BAUDRATE = 9600

# モールス信号表
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    'change_mode': '------', 'delete': '......', 'read_all': '...---',
}


def text_to_morse(text):
  """文字列をモールス信号に変換"""
  return ' '.join(MORSE_CODE_DICT.get(char, '') for char in text.upper())


if __name__ == "__main__":
  with serial.Serial(PORT, BAUDRATE, timeout=1) as ser:
    print(f"Connected to {PORT}")
    while True:
      message = input("Enter text to send as Morse Code: ")
      match message:
        case "change_mode":
          morse = "------"
        case "delete":
          morse = "......"
        case "read_all":
          morse = "...---"
        case _:
          morse = text_to_morse(message) + "\n"

      for char in morse:
        ser.write(char.encode())
        print(f"Sent: {char}")
        time.sleep(1.6)

      print(f"Sent: {morse}")
      time.sleep(1)  # 次の送信まで待機
