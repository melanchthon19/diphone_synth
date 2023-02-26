#!/usr/bin/env python3

from operator import itemgetter
from phonotactics import Phonotactics
from phonetics import phonetics


def read_data():
    with open('textdata.txt', 'r') as file:
        text = file.read()
        print(text)
    return text

def unique_syllables(syllables):
    all = syllables.split('-')
    stats = set([(syl, all.count(syl)) for syl in all])
    stats = sorted(stats, key=itemgetter(1), reverse=True)
    return stats


if __name__ == "__main__":
    text = read_data()
    ph = Phonotactics(phonetics)
    syllables = ph.word2silabas(text)
    stats = unique_syllables(syllables)
    print(stats)
    with open('syllables.txt', 'w') as file:
        for syl, freq in stats:
            file.write(syl + '\t' + str(freq) + '\n')
