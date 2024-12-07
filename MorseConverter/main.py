import threading
import time
import Moji
import SerialComu
import queue

# インスタンスを作成
moji = Moji.Moji()
serialcomu = SerialComu.SerialComu()


def run_moji_with_serialcomu(serialcomu=serialcomu, gui=moji):
  while serialcomu.running:
    try:
      while not serialcomu.data_Queue.empty():
        single_morse_code = serialcomu.data_Queue.get()
        serialcomu.data_Queue.task_done()

        if single_morse_code:
          gui.append_morse_code(single_morse_code)

    except queue.Empty:
      pass
    time.sleep(0.5)


if __name__ == "__main__":
  # スレッドで実行
  serialcomu_thread = threading.Thread(target=serialcomu.read_line_serial)
  run_moji_thread = threading.Thread(target=run_moji_with_serialcomu)
  serialcomu_thread.start()
  run_moji_thread.start()

  try:
    moji.run()
  except KeyboardInterrupt:
    print("Stopping...")
    serialcomu.stop()
    serialcomu_thread.join()
    run_moji_thread.join()
    print("Stopped.")
