#!/usr/bin/env python3

import re
import random
import numpy as np


class LexiconGenerator():
    def __init__(self, syllables_file):
        self.sylfreq = self.read_data(syllables_file)
        self.syllables = list(self.sylfreq.keys())
        self.freqs = list(self.sylfreq.values())
        self.total = sum(self.freqs)
        self.probs = [self.sylfreq[syl]/self.total for syl in self.syllables]

    def read_data(self, syllables_file):
        with open(syllables_file, 'r') as file:
            data = file.readlines()
            sylfreq = {line.strip().split('\t')[0]:
                            int(line.strip().split('\t')[1]) 
                            for line in data}
            #print(sylfreq)
            return sylfreq
    
    def generate_sentence(self, N=12):
        syllables_to_use = list(np.random.choice(self.syllables, N, replace=False, p=self.probs))
        print('syllables:', syllables_to_use)
        sentence = []
        for index in range(len(syllables_to_use)-2):
            sentence.append(''.join(syllables_to_use[index:index+3]))
            index += 3
        print('generated:', sentence)
        sentence = self.phonemes2char(' '.join(sentence))
        print('sentence:', sentence)
        return sentence
    
    def phonemes2char(self, sentence):
        ph2char = {'X': 'ch', 'R': 'rr', 'L': 'll', 'x': 'j'}
        for ph, char in ph2char.items():
            if ph in sentence:
                sentence = re.sub(rf'{ph}', char, sentence)
        return sentence
    
if __name__ == '__main__':
    wg = LexiconGenerator('syllables.txt')
    wg.generate_sentence()
    # 12 syllables --> 10 words --> 1 sentences
