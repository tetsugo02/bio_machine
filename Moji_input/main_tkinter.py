import threading
import queue
from MorseConverter import Moji
from SerialComu import SerialComu

# インスタンスを作成
moji = Moji.Moji()
serialcomu = SerialComu.SerialComu()
morse_queue = queue.Queue()


def run_serialcomu(serialcomu=serialcomu):
  while serialcomu.running:
    try:
      while not serialcomu.data_Queue.empty():
        single_morse_code = serialcomu.data_Queue.get()
        serialcomu.data_Queue.task_done()

        if single_morse_code:
          morse_queue.put(single_morse_code)

    except Exception as e:
      print(e)


def process_morse_queue():
  while not morse_queue.empty():
    single_morse_code = morse_queue.get()
    moji.append_morse_code(single_morse_code)
  moji.root.after(1, process_morse_queue)


if __name__ == "__main__":
  # スレッドで実行
  serialcomu_thread = threading.Thread(target=serialcomu.read_line_serial, daemon=True)
  run_serialcomu_thread = threading.Thread(target=run_serialcomu, daemon=True)
  serialcomu_thread.start()
  run_serialcomu_thread.start()

  # キューを処理するための関数を呼び出す
  moji.root.after(100, process_morse_queue)

  try:
    moji.run()
  except KeyboardInterrupt:
    print("Stopping...")
    serialcomu.stop()
    serialcomu_thread.join(timeout=5)
    run_serialcomu_thread.join(timeout=5)
    print("Stopped.")
