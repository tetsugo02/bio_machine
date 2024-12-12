import os
import subprocess


def remove_silence(input_file, output_file, silence_threshold=-50, min_silence_duration=1):
  if not os.path.exists(input_file):
    print(f"入力ファイルが見つかりません: {input_file}")
    return

  command = [
      "ffmpeg",
      "-i", input_file,
      "-af",
      f"silenceremove=start_periods=1:start_duration={min_silence_duration}:start_threshold={
          silence_threshold}dB:stop_periods=-1:stop_duration={min_silence_duration}:stop_threshold={silence_threshold}dB",
      output_file
  ]

  try:
    subprocess.run(command, check=True)
    print(f"無音部分を削除したファイルを出力しました: {output_file}")
  except subprocess.CalledProcessError as e:
    print(f"FFmpegコマンドの実行中にエラーが発生しました: {e}")
  except FileNotFoundError:
    print("FFmpegがインストールされていない可能性があります。")


# 使用例
input_path = "./ata_a26.mp3"  # 入力ファイル名
output_path = "output.mp3"  # 出力ファイル名

remove_silence(input_path, output_path, silence_threshold=-40, min_silence_duration=1)
