import os

from src.audio_converter import wav_to_mp3, mp3_to_wav
from src.image_converter import heic_to_jpg, jpg_to_png, png_to_jpg
from src.pdf_converter import pdf_to_docx, docx_to_pdf
from src.video_converter import mov_to_mp4, mp4_to_mov


def convert_file(input_file: str, output_folder: str, conversion_type: str):
    input_path = os.path.join("input", input_file)
    output_path = os.path.join(output_folder, f"{os.path.splitext(input_file)[0]}_converted")

    conversions = {
        "pdf_to_docx": lambda: pdf_to_docx(input_path, f"{output_path}.docx"),
        "docx_to_pdf": lambda: docx_to_pdf(input_path, f"{output_path}.pdf"),
        "heic_to_jpg": lambda: heic_to_jpg(input_path, f"{output_path}.jpg"),
        "jpg_to_png": lambda: jpg_to_png(input_path, f"{output_path}.png"),
        "png_to_jpg": lambda: png_to_jpg(input_path, f"{output_path}.jpg"),
        "mov_to_mp4": lambda: mov_to_mp4(input_path, f"{output_path}.mp4"),
        "mp4_to_mov": lambda: mp4_to_mov(input_path, f"{output_path}.mov"),
        "wav_to_mp3": lambda: wav_to_mp3(input_path, f"{output_path}.mp3"),
        "mp3_to_wav": lambda: mp3_to_wav(input_path, f"{output_path}.wav")
    }

    if conversion_type in conversions:
        conversions[conversion_type]()
        print(f"Conversion {conversion_type} completed.")
    else:
        print(f"Conversion type {conversion_type} not supported.")


if __name__ == "__main__":
    # Example usage
    convert_file("example.pdf", "output", "pdf_to_docx")
