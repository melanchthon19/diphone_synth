#!/usr/bin/env python3

import re
import argparse
from phonetics import phonetics

class Phonotactics:
    def __init__(self, phonetics, debug=False):
        self.debug = debug
        self.phonemes_dict = phonetics['phonemes_dict']
        self.char2phoneme = phonetics['char2phoneme']
        self.alphabet = phonetics['alphabet']
        self.oclusivas = phonetics['oclusivas']
        self.liquidas = phonetics['liquidas']
        self.diptongos = phonetics['diptongos']
        self.triptongos = phonetics['triptongos']
        self.vowels = phonetics['vowels']
        self.edge = phonetics['edge']
    
    def word2silabas(self, word):
        phonemes = self.word2phonemes(word.lower())
        structure = self.phonemes2structure(phonemes)
        silabas =  self.structure2silabas(structure)
        phonemes_divided = self.divide(phonemes, silabas)
        
        if self.debug:
            return (phonemes, structure, silabas, phonemes_divided)
        return phonemes_divided
    
    def word2phonemes(self, word):
        """
        function that takes a word and translates it to phonemes
        following the rules from char2phoneme dictionary
        """
        # findall retrieves a list of characters only
        phonemes = ''.join(re.findall('[^\W]*', word))
        # TODO: deal with punctuation in the middle of sentence
        for rule in self.char2phoneme.keys():  # certain rules must be applied first
            # TODO: use regex to account for edge cases 
            # (e.x. R at the beginning of word, foreign words (zinc), 'del lodo', etc.)
            for char in self.char2phoneme[rule]:
                if char in phonemes:
                    # modifying the word on the fly
                    phonemes = re.sub(char, self.char2phoneme[rule][char], phonemes)
        print('phonemes:', phonemes)
        return phonemes

    def phonemes2structure(self, phonemes):
        """
        function that takes a sequence of phonemes and translates it to its structure
        in the following order:
        1) oclusive + liquid sounds are merged
        2) direct mapping from phonemes_dict
        3) diphtongs are merged
        """
        temp = self.merge_oclusiva_liquida(phonemes)  # e.x. 'br' --> 'T'
        temp = self.merge_edge_cases(temp)  # 'bs' --> 'T'
        temp = ''.join([self.phonemes_dict[phone]
                        if phone in self.alphabet else phone 
                        for phone in temp])  # e.x. 'a' --> 'F'
        temp = self.merge_triptongo(temp)  # e.x. 'DFD' --> 'Q'
        structure = self.merge_diptongo(temp)  # e.x. 'FD' --> 'W'
        print('structure:', structure)
        return structure
    
    def merge_edge_cases(self, sequence):
        redge = re.compile(rf'{self.edge[0]}(?=[tk])')
        sequence = re.sub(redge, 'T', sequence)
        #redge = re.compile(rf'{self.edge[1]}(?=[tk])')
        #sequence = re.sub(redge, 'T', sequence)
        return sequence

    def merge_oclusiva_liquida(self, sequence):
        """
        function that merges two consonants together: 
        oclusive (p, b, t, d, k , g) + liquid (l, r)
        given that they are phonetically indivisible.
        """
        roclusivas = ''.join(self.oclusivas)
        rliquidas = ''.join(self.liquidas)
        pat = re.compile(rf'[{roclusivas}][{rliquidas}]')  
        return re.sub(pat, 'T', sequence)
    
    def merge_triptongo(self, sequence):
        rtriptongos = '|'.join(self.triptongos)
        pat = re.compile(rf'{rtriptongos}')
        return re.sub(pat, 'Q', sequence)
    
    def merge_diptongo(self, sequence):
        """
        takes first DF, then FD and DD
        """
        for dip in [[self.diptongos[0]], self.diptongos[1:]]:
            rdiptongos = '|'.join(dip)
            pat = re.compile(rf'{rdiptongos}')
            sequence = re.sub(pat, 'W', sequence)
        return sequence
    
    def structure2silabas(self, structure):
        nvowels = self.number_vowels(structure)
        silabas = self.split_silabas(structure, nvowels)
        print('silabas:', silabas)
        return silabas
    
    def number_vowels(self, structure):
        pat = re.compile(r'[FWADQ]')
        nvowels = len(re.findall(pat, structure))
        print('number of vowels:', nvowels)
        return nvowels

    def split_silabas(self, structure, nvowels):
        if nvowels == 1:
            return [structure]
        else:
            # TODO: there are edge cases (e.x. 'dlo')
            match = list(re.finditer(r'([CT]?[FWADQ][CT]{0,2}(?![FWADQ])|[CT]?[FWADQ])', structure))
            silabas = [silaba.group() for silaba in match]
            return silabas
        
    def divide(self, phonemes, silabas):
        if len(silabas) == 1:
            print(phonemes)
            return phonemes
        temp = ''
        index = 0
        for silaba in silabas:
            for char in silaba:
                if re.match(r'[Q]', char):
                    temp += phonemes[index:index+3]
                    index += 3
                elif re.match(r'[TW]', char):
                    temp += phonemes[index:index+2]
                    index += 2
                else:
                    temp += phonemes[index]
                    index += 1
                    
            temp += '-'
        phonemes_divided = temp[:-1]  # cleaning last '-' that was added
        print(phonemes_divided)
        return phonemes_divided


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', help='text to be read aloud', nargs='+')
    args = parser.parse_args()
    print(args.text)
    ph = Phonotactics(phonetics)
    phoneme_sentence = ''.join(args.text)
    ph.word2silabas(phoneme_sentence)
