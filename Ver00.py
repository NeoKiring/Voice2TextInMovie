
import os
from pydub import AudioSegment

def load_audio_file(file_path):
    # ファイルの存在確認
    if not os.path.exists(file_path):
        raise FileNotFoundError("指定されたファイルが見つかりません。")

    # ファイルの拡張子によって処理を分ける
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == '.mp3':
        audio = AudioSegment.from_mp3(file_path)
    elif ext == '.wav':
        audio = AudioSegment.from_wav(file_path)
    else:
        raise ValueError("サポートされていないファイル形式です。.mp3または.wavファイルを指定してください。")

    # ファイルサイズの表示（オプション）
    file_size = os.path.getsize(file_path)
    print(f"ファイルサイズ: {file_size} バイト")

    return audio

# 例としてファイルパスを指定して関数をテスト
audio_data = load_audio_file('path/to/your/audiofile.mp3')