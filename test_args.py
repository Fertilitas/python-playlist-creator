#!/usr/bin/env python3
import tarfile
import argparse
from pathlib import Path
import os

from pydub import AudioSegment

def func_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p","--path",
        type=str,
        help="masukkan nama anda"
    )
    args = parser.parse_args()
    return args.path

def playlist_creator(file_path):
    # Inisialisasi audio kosong untuk memulai playlist
    playlist = AudioSegment.empty()

    # Loop melalui setiap file lagu dan tambahkan ke playlist
    file_path = sorted(f for f in file_path.iterdir())
    for file in file_path:
        
        lagu = AudioSegment.from_file(file)
        playlist += lagu
        if file.is_file():
            file.unlink()

    # Simpan playlist ke file output
    playlist.export("output.mp3", format="mp3")
    print(f"Playlist berhasil dibuat dan disimpan sebagai output.mp3")

def extract_(file_path,extract_path,remove_=False):
    try:
        with tarfile.open(file_path,'r:xz') as tar:
            tar.extractall(extract_path)
        if remove_:
            os.remove(file_path)
        print("file berhasil di ekstrak")
    except Exception as e:
        raise FileExistsError(e)


if __name__ == "__main__":
    # path = func_parser()
    path = "music.tar.xz"
    input_dir = Path(path)
    temp = Path("temp")

    extract_(input_dir,temp)
    playlist_creator(temp)





