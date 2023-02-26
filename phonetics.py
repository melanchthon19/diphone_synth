#!/usr/bin/env python3

# this file contains information about spanish phonetics
# that is needed for the Phonotactics class.

# phonemes_dict is used in Phonotactics.phonemes2structure():
vowels_strong = {'a':'F', 'e':'F', 'o':'F',}
vowels_weak = {'i':'D', 'u':'D', 'ü':'D'}
vowels_accented = {'á':'F', 'é':'F', 'í':'A', 'ó':'F', 'ú':'A'}
consonants = {'m':'C', 'n':'C', 'ñ':'C',
              'p':'C', 't':'C', 'k':'C', 'b':'C', 'd':'C', 'g':'C',
              'X':'C',  # ts
              'K': 'C',  # ks
              'B': 'C',  # bs followed by plosive (obstinada)
              'f':'C', 's':'C', 'L':'C', 'x':'C',
              'l':'C', 'r':'C', 'R':'C'}
phonemes_dict = {**vowels_strong, **vowels_weak, **vowels_accented, **consonants}
diptongos = ['DF', 'FD', 'DD']
triptongos = ['DFD', 'DAD']
oclusivas = ['p', 'b', 't', 'd', 'k', 'g']
liquidas = ['l', 'r']  # leaving out 'R' on purpose
edge = ['bs', 'nk']  #

# char2phoneme dict is used in Phonotactics.word2phonemes()
char2phoneme = {
       1:{
       'ci': 'si',
       'cí': 'sí',
       'ce': 'se',
       'cé': 'sé',
       'ch': 'X',
       'qu': 'k',
       'gui': 'gi',
       'gue': 'ge',
       },
       2:{
       'c': 'k',
       'x': 'K',
       'll': 'L',
       'rr': 'R',
       'j': 'x',
       'gi': 'xi',
       'gí': 'xí',
       'gé': 'xé',
       'ge': 'xe',
       'h': '',
       'z': 's',
       'v': 'b',
       'y': 'i',}
       }

#double_consonants = ['tr', 'dr', 'ns', 'pr', 'fr', 'br', 'gr']
#punctuation = ['.', ',', ';', '?']
vowels = list(vowels_strong.keys()) + list(vowels_weak.keys()) + list(vowels_accented.keys())
alphabet = vowels + list(consonants.keys())

phonetics = {'alphabet': alphabet,
             'vowels': vowels,
             'consonants': consonants,
             'char2phone': char2phoneme,
             'phonemes_dict': phonemes_dict,
             #'punctuation': punctuation,
             #'double_consonants': double_consonants,
             'oclusivas': oclusivas,
             'liquidas': liquidas,
             'diptongos': diptongos,
             'triptongos': triptongos,
             'edge': edge,
             }