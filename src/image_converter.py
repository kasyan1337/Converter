from PIL import Image
import pyheif
from pathlib import Path

def heic_to_jpg(input_path: str, output_path: str):
    heif_file = pyheif.read(input_path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(output_path, "JPEG")

def jpg_to_png(input_path: str, output_path: str):
    image = Image.open(input_path)
    image.save(output_path, "PNG")

def png_to_jpg(input_path: str, output_path: str):
    image = Image.open(input_path)
    image.convert("RGB").save(output_path, "JPEG")