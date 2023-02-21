#!/usr/bin/env python3

import re
import argparse
from phonetics import phonetics

class Phonotactics:
    def __init__(self, phonetics):
        self.phonemes_dict = phonetics['phonemes_dict']
        self.char2phone = phonetics['char2phone']
        self.alphabet = phonetics['alphabet']
        self.oclusivas = phonetics['oclusivas']
        self.liquidas = phonetics['liquidas']
        self.diptongos = phonetics['diptongos']
        self.vowels = phonetics['vowels']
    
    def word2silabas(self, word):
        phonemes = self.word2phonemes(word)
        structure = self.phonemes2structure(phonemes)
        silabas =  self.structure2silabas(structure)
        word_divided = self.divide(word, silabas)
        return word_divided
    
    def word2phonemes(self, word):
        """
        function that takes a word and translates it to phonemes
        following the rules from char2phone dictionary
        """
        # findall retrieves a list of characters only
        phonemes = ''.join(re.findall('[^\W]*', word))
        # TODO: deal with punctuation in the middle of sentence
        for rule in self.char2phone.keys():  # certain rules must be applied first
            for char in self.char2phone[rule]:
                if char in phonemes:
                    # modifying the word on the fly
                    phonemes = re.sub(char, self.char2phone[rule][char], phonemes)
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
        temp = ''.join([self.phonemes_dict[phone]
                        if phone in self.alphabet else phone 
                        for phone in temp])  # e.x. 'a' --> 'F'
        structure = self.merge_diptongo(temp)  # e.x. 'FD' --> 'W'
        print('structure:', structure)
        return structure
    
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
    
    def merge_diptongo(self, sequence):
        rdiptongos = '|'.join(self.diptongos)
        pat = re.compile(rf'{rdiptongos}')
        return re.sub(pat, 'W', sequence)
    
    def structure2silabas(self, structure):
        nvowels = self.number_vowels(structure)
        silabas = self.split_silabas(structure, nvowels)
        print('silabas:', silabas)
        return silabas
    
    def number_vowels(self, structure):
        pat = re.compile(r'[FWAD]')
        nvowels = len(re.findall(pat, structure))
        print('number of vowels:', nvowels)
        return nvowels

    def split_silabas(self, structure, nvowels):
        if nvowels == 1:
            return structure
        else:
            match = list(re.finditer(r'([CT]?[FWAD][CT]?(?![FWAD]))', structure))
            silabas = [silaba.group() for silaba in match]
            return silabas
        
    def divide(self, word, silabas):
        temp = ''
        index = 0
        for silaba in silabas:
            for char in silaba:
                if re.match(r'[^TW]', char):
                    temp += word[index]
                    index += 1
                else:
                    temp += word[index:index+2]
                    index += 2
            temp += '-'
        word_divided = temp[:-1]  # cleaning last '-' that was added
        print(word_divided)
        return word_divided  


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', help='text to be read aloud', nargs='+')
    args = parser.parse_args()
    print(args.text)
    ph = Phonotactics(phonetics)
    sentence = ''.join(args.text)
    ph.word2silabas(sentence)
