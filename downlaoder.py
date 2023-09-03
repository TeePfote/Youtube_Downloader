import os
from pytube import YouTube


def download_video_as_mp3(url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Choose the stream with audio only (the highest quality)
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio stream as MP3
        audio_stream.download(output_path)
        print(f"Audio from '{yt.title}' downloaded successfully as MP3.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    output_directory = input("Enter the output directory: ")

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    while True:
        video_url = input("Enter a YouTube video URL (or 'q' to quit): ")

        if video_url.lower() == 'q':
            break

        mp3_output_filename = os.path.join(output_directory, "music-mp3")
        download_video_as_mp3(video_url, mp3_output_filename)
