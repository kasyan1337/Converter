# File Converter

This project provides a robust file converter supporting various file formats, including documents, images, audio, and video. It leverages Python libraries and command-line tools to ensure high-quality conversions across different formats.

## Features

- **Document Conversion**: Convert between PDF and DOCX formats.
- **Image Conversion**: Convert between HEIC, JPG, PNG with options for transparency.
- **Video Conversion**: Convert between MOV and MP4, and create GIFs from videos.
- **Audio Conversion**: Convert between WAV, MP3, and M4A.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/converter.git
    cd converter
    ```

2. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install external tools**:
    - [LibreOffice](https://www.libreoffice.org/download/download/) for DOCX and PDF conversions.
    - [FFmpeg](https://ffmpeg.org/download.html) for video and audio processing.

## Usage

### Running Conversions

Use the main `convert_file` function from `main.py` to convert files by specifying the input file, output directory, and conversion type.

Example:
```python
from main import convert_file
convert_file("test.docx", "output", "docx_to_pdf")
```

## Running Tests

Tests are located in the tests folder and can be run with the unittest module:
```bash
python -m unittest discover -s tests
```

## Supported Conversions

| Input Type | Output Type | Conversion Type | Example |
|------------|-------------|-----------------|---------|
| PDF        | DOCX        | pdf_to_docx     | convert_file("test.pdf", "output", "pdf_to_docx") |
| DOCX       | PDF         | docx_to_pdf     | convert_file("test.docx", "output", "docx_to_pdf") |
| HEIC       | JPG         | heic_to_jpg     | convert_file("image.HEIC", "output", "heic_to_jpg") |
| JPG        | PNG         | jpg_to_png      | convert_file("image.jpg", "output", "jpg_to_png", transparent_color=(255, 255, 255)) |
| PNG        | JPG         | png_to_jpg      | convert_file("image.png", "output", "png_to_jpg") |
| MOV        | MP4         | mov_to_mp4      | convert_file("video.mov", "output", "mov_to_mp4") |
| MP4        | MOV         | mp4_to_mov      | convert_file("video.mp4", "output", "mp4_to_mov") |
| WAV        | MP3         | wav_to_mp3      | convert_file("audio.wav", "output", "wav_to_mp3") |
| MP3        | WAV         | mp3_to_wav      | convert_file("audio.mp3", "output", "mp3_to_wav") |



### Summary

- **Tests**: `test_conversions.py` covers each file type conversion.
- **README**: Provides setup, usage, and contribution instructions.

