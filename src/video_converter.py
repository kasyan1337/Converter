from moviepy.editor import VideoFileClip, ImageSequenceClip


def mov_to_mp4(input_path: str, output_path: str):
    clip = VideoFileClip(input_path)
    clip.write_videofile(
        output_path, codec="libx264", preset="slow", ffmpeg_params=["-crf", "18"]
    )  # CRF 18 for near-lossless


def mp4_to_mov(input_path: str, output_path: str):
    clip = VideoFileClip(input_path)
    clip.write_videofile(
        output_path, codec="prores", ffmpeg_params=["-qscale", "0"]
    )  # Best quality


def video_to_gif(input_path: str, output_path: str):
    clip = VideoFileClip(input_path)
    clip.write_gif(output_path, fps=10)


def gif_to_video(input_path: str, output_path: str):
    clip = VideoFileClip(input_path)
    clip.write_videofile(
        output_path, codec="libx264", preset="slow", ffmpeg_params=["-crf", "18"]
    )


def live_photo_to_gif(input_path: str, output_path: str):
    clip = VideoFileClip(input_path)
    clip.write_gif(output_path, fps=10)  # Save as GIF


def live_photo_to_video(input_path: str, output_path: str):
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, codec="libx264")
