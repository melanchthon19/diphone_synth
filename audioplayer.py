#!/usr/bin/env python3

import wave
import pyaudio
import argparse


class AudioPlayer:
    def __init__(self):
        self.chunk = 1024
        
    def play_file(self, file):
        # PyAudio Docs
        # https://people.csail.mit.edu/hubert/pyaudio/#docs
        print(f"playing: {file}")
        with wave.open(file, 'rb') as wf:
            # Instantiate PyAudio and initialize PortAudio system resources (1)
            self.p = pyaudio.PyAudio()
            # Open stream (2)
            stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            # Play samples from the wave file (3)
            while len(data := wf.readframes(self.chunk)):  # Requires Python 3.8+ for :=
                stream.write(data)

            # Close stream (4)
            stream.close()
            # Release PortAudio system resources (5)
            self.p.terminate()
        
        return
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input files to be played', nargs='+')
    args = parser.parse_args()
    
    ap = AudioPlayer()
    for arg in args.input:
        ap.play_file(arg)
