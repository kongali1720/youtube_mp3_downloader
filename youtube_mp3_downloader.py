import os
from pytube import YouTube
from tqdm import tqdm

def download_mp3(url):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"\n🎬 Judul Video: {yt.title}")
        print("📥 Mulai download audio...")

        audio_stream = yt.streams.filter(only_audio=True).first()
        out_file = audio_stream.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(f"✅ Berhasil didownload dan disimpan sebagai: {new_file}")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = int((bytes_downloaded / total_size) * 100)
    tqdm.write(f"⏳ Downloading... {progress}%")

if __name__ == '__main__':
    print("🎵 YouTube MP3 Downloader 🎵")
    link = input("Masukkan URL YouTube: ")
    download_mp3(link)
