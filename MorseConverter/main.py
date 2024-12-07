import threading
import Moji
import SerialComu

# インスタンスを作成
moji = Moji.Moji()
serialcomu = SerialComu.SerialComu()


def run_moji_with_serialcomu(serialcomu=serialcomu, gui=moji):
  while serialcomu.running:
    try:
      while not serialcomu.data_Queue.empty():
        single_morse_code = serialcomu.data_Queue.get(timeout=1)
        serialcomu.data_Queue.task_done()

        if single_morse_code:
          gui.append_morse_code(single_morse_code)

    except Exception as e:
      print(e)


if __name__ == "__main__":
  # スレッドで実行
  serialcomu_thread = threading.Thread(target=serialcomu.read_line_serial, daemon=True)  # シリアル通信でMorse Code受け取って、Queueに貯蓄するスレッド
  # 　QueueからMorse Codeを取り出して、GUIに追加するスレッド
  run_moji_thread = threading.Thread(target=run_moji_with_serialcomu, daemon=True)
  serialcomu_thread.start()
  run_moji_thread.start()

  try:
    moji.run()
  except KeyboardInterrupt:
    print("Stopping...")
    serialcomu.stop()
    serialcomu_thread.join(timeout=5)
    run_moji_thread.join(timeout=5)
    print("Stopped.")
