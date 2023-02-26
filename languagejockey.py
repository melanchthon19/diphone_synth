#!/usr/bin/env python3

import argparse
from audioplayer import AudioPlayer
from audiorecorder import AudioRecorder
from lexicon import LexiconGenerator


class LanguageJockey:
    def __init__(self):
        self.ap = AudioPlayer()
        self.ar = AudioRecorder()
        wg = LexiconGenerator('syllables.txt')
        self.lexicon = wg.generate_sentence()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', help='text to be read aloud', nargs='+')
    args = parser.parse_args()

    
    