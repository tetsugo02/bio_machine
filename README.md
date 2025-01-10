# プロジェクト名

## TODOLIST
- [x] モールス信号のデコード処理を実装する
- [x] GUIの作成
- [x] 文字呼び上げの実装
- [x] Arduino側のAD変換及び送信処理の実装
- [x] Arduinoを用いたテスト

## 環境構築
まずは次のように、`MorseConverter`ディレクトリに移動したことを確認する。
```bash
$ pwd
/home/user/**/bio_machine/MorseConverter
```
仮想環境を作成し、必要なパッケージをインストールする。
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements_Mac.txt  #Macの場合
```

## 各ファイルの機能とAPIリスト

### `SerialComu.py`
シリアル通信を扱うクラスを提供する。
- **クラス**
  - `SerialComu`
    - **メソッド**
      - `__init__(self, port="/dev/cu.usbmodem1101", baudrate=9600)`
      - `read_line_serial(self)`
      - `stop(self)`

### `MorseDecoder.py`
モールス信号をデコードするクラスを提供する。
- **クラス**
  - `Mode`
    - **列挙型**
      - `English`
      - `Japanese`
  - `MorseDecoder`
    - **メソッド**
      - `__init__(self)`
      - `decode_morse_to_str(self, morse_code: str) -> str`
      - `change_mode(self)`

### `Moji.py`
GUIを使用してモールス信号をデコードし、テキストを表示および読み上げるクラスを提供する。
- **クラス**
  - `Moji`
    - **メソッド**
      - `__init__(self)`
      - `setup_root_window(self)`
      - `create_widgets(self)`
      - `create_input_area(self)`
      - `create_current_char_label(self)`
      - `create_decoded_textbox(self)`
      - `change_mode_button(self)`
      - `reset_timer(self, event=None)`
      - `decode_input_and_update(self)`
      - `update_current_char(self, str)`
      - `append_morse_code(self, morse_code)`
      - `append_decoded_text(self, str)`
      - `special_char_action(self, str)`
      - `on_text_change(self, event)`
      - `run(self)`

### `load_morse.py`
モールス信号のデータをJSONファイルから読み込む関数を提供する。
- **関数**
  - `load_morse(path: str) -> dict`

### `Process_morse.py`
シリアル通信から受け取ったモールス信号をデコードする処理を提供する。
- **関数**
  - `process_morse_data(serialcomu, morsedecoder)`

### `main_tkinter.py`
GUIを使用して、エミュレートされたシリアル通信から受け取ったモールス信号をデコードし、テキストを表示および読み上げるスクリプト。
- **関数**
  - `run_serialcomu(serialcomu)`
  - `process_morse_queue()`

### `virtual_serial.py`
Arduinoからのシリアル通信をエミュレートするスクリプト。
- **関数**
  - `text_to_morse(text)`

### `virtual_serial_port.sh`
仮想シリアルポートを作成するshellスクリプト。

### `morse_data/morse_eng.json`
英語のモールス信号データを提供する。

### `morse_data/morse_jpn.json`
日本語のモールス信号データを提供する。

### `sequence.pu`
シーケンス図を提供する。

### `Arduino/process_data_and_generate_morse/process_data_and_generate_morse.ino`
Arduinoでアナログデータを読み取り、シリアル通信で送信するスケッチ。

### `Arduino/test/test.ino`
Arduinoでアナログデータを読み取り、シリアル通信で送信するテストスケッチ。