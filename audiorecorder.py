#!/usr/bin/env python3

import sys
import wave
import pyaudio
import argparse


class AudioRecorder():
    def __init__(self):
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1 if sys.platform == 'darwin' else 2
        self.rate = 44100
        self.record_seconds = 5
        self.p = None

    def record(self, output):
        # https://people.csail.mit.edu/hubert/pyaudio/#docs
        with wave.open(output + '.wav', 'wb') as wf:
            self.p = pyaudio.PyAudio()
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.format))
            wf.setframerate(self.rate)

            stream = self.p.open(format=self.format, channels=self.channels, rate=self.rate, input=True)

            print('Recording...')
            for _ in range(0, self.rate // self.chunk * self.record_seconds):
                wf.writeframes(stream.read(self.chunk))
            print('Done')

            stream.close()
            self.p.terminate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='name of output file')
    args = parser.parse_args()

    recorder = AudioRecorder()
    recorder.record(args.output)