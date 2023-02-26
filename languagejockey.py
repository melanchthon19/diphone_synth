#!/usr/bin/env python3
import argparse
from audioplayer import AudioPlayer

class DiskJockey:
    def __init__(self):
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', help='text to be read aloud', nargs='+')
    args = parser.parse_args()

    ap = AudioPlayer()
    for arg in args.text:
        ap.play_file(arg)
    ap.release_portaudio()