import SerialComu
import MorseDecoder
import threading
import time
import queue

# インスタンスを作成
serialcomu = SerialComu.SerialComu()
morsedecoder = MorseDecoder.MorseDecoder()

def process_morse_data(serialcomu, morsedecoder):
    """モールス信号をデコードする処理"""
    while serialcomu.running:
      whole_morse_code = ""
      try:
        # キューからデータを取り出して結合
        while not serialcomu.data_Queue.empty():
          single_morse_code = serialcomu.data_Queue.get()  # データを取得
          serialcomu.data_Queue.task_done()  # タスクを完了
          whole_morse_code += single_morse_code

          # モールス信号をデコード
        if whole_morse_code:
              print(whole_morse_code)
              print(morsedecoder.decode_morse_to_str(whole_morse_code))

      except queue.Empty:
          # キューが空の場合は何もしない
          pass
      time.sleep(1)
        # 1秒間遅延して次のループを実行


# スレッドで実行
process_thread = threading.Thread(target=process_morse_data, args=(serialcomu, morsedecoder))
serialcomu_thread = threading.Thread(target=serialcomu.read_line_serial)
process_thread.start()
serialcomu_thread.start()

try:
    while True:
        time.sleep(1)  # メインスレッドで何か他の処理を入れる場合はここに記述
except KeyboardInterrupt:
    print("Stopping...")
    serialcomu.stop()
    process_thread.join()
    serialcomu_thread.join()
    print("Stopped.")
