
from pydub import AudioSegment

def wav_to_mp3(input_path: str, output_path: str):
    sound = AudioSegment.from_wav(input_path)
    sound.export(output_path, format="mp3")

def mp3_to_wav(input_path: str, output_path: str):
    sound = AudioSegment.from_mp3(input_path)
    sound.export(output_path, format="wav")