## TODOLIST
- [x] モールス信号のデコード処理を実装する
- [x] GUIの作成
- [ ] 文字呼び上げの実装
- [ ] Arduino側のAD変換及び送信処理の実装
- [ ] Arduinoを用いたテスト

## 環境構築
まずは次のように、`MoreseConverter`ディレクトリに移動したことを確認する。
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

### `Text_reader.py`
テキストを音声で読み上げるクラスを提供する。
- **クラス**
  - `TextReader`
    - **メソッド**
      - `__init__(self)`
      - `run_pyttx3(self, read_queue)`

### `load_morse.py`
モールス信号のデータをJSONファイルから読み込む関数を提供する。
- **関数**
  - `load_morse(path: str) -> dict`

### `Process_morse.py`
シリアル通信から受け取ったモールス信号をデコードする処理を提供する。
- **関数**
  - `process_morse_data(serialcomu, morsedecoder)`

### `test.py`
シリアル通信から受け取ったモールス信号をデコードする処理をテストするスクリプトである。
- **関数**
  - `process_morse_data(serialcomu, morsedecoder)`

### `test2.py`
GUIを使用してモールス信号をデコードするスクリプトである。
- **関数**
  - `update_gui(decoded_message)`
  - `on_press(key)`
  - `check_timeout()`

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
      - `change_mode(self)`
      - `reset_timer(self, event=None)`
      - `decode_input(self)`
      - `update_current_char(self, char)`
      - `append_decoded_text(self, char)`
      - `run(self)`

### `morse_data/morse_eng.json`
英語のモールス信号データを提供する。

### `morse_data/morse_jpn.json`
日本語のモールス信号データを提供する。