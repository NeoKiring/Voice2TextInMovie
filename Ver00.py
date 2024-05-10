import os
from pydub import AudioSegment
import whisper
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# 音声ファイルの読み込み (ソース①)
def load_audio_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("指定されたファイルが見つかりません。")
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == '.mp3':
        audio = AudioSegment.from_mp3(file_path)
    elif ext == '.wav':
        audio = AudioSegment.from_wav(file_path)
    else:
        raise ValueError("サポートされていないファイル形式です。.mp3または.wavファイルを指定してください。")
    file_size = os.path.getsize(file_path)
    print(f"ファイルサイズ: {file_size} バイト")
    return audio

# Whisperを使用して音声からテキストへの変換 (ソース②)
def transcribe_audio(audio_data):
    model = whisper.load_model("base")
    result = model.transcribe(audio_data.get_array_of_samples(), language="ja")
    transcription = result["text"]
    return transcription

# 字幕付きのカラオケ動画を作成 (ソース③)
def create_karaoke_video(audio_path, transcribed_text, output_path):
    video_clip = VideoFileClip(audio_path).subclip(0, 10)
    txt_clip = TextClip(transcribed_text, fontsize=24, color='white', font='Arial')
    txt_clip = txt_clip.set_position('bottom').set_duration(video_clip.duration)
    result = CompositeVideoClip([video_clip, txt_clip])
    result.write_videofile(output_path, codec='libx264', fps=24)

# メインプログラムの実行 (ソース④)
def main(audio_file_path):
    try:
        audio_data = load_audio_file(audio_file_path)
        transcribed_text = transcribe_audio(audio_data)
        print(f"変換されたテキスト: {transcribed_text}")
        output_video_path = "output_karaoke_video.mp4"
        create_karaoke_video(audio_file_path, transcribed_text, output_video_path)
        print(f"動画が作成されました: {output_video_path}")
    except FileNotFoundError as e:
        print(f"エラー: {e}")
    except ValueError as e:
        print(f"エラー: {e}")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")

# メイン関数の実行例
main("path/to/your/audiofile.mp3")