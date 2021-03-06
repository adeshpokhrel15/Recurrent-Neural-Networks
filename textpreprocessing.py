# -*- coding: utf-8 -*-
"""TextPreprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VoZCWUSCy2rYnG-Tpa1oy-bmjFmOuumT
"""

#Importing the library
import tensorflow as tf
from d2l import tensorflow as d2l
import collections
import re

#!pip install d2l==0.16.6 #==> if d2l is not working then setup the environment '''

#Reading the Dataset
#we load text from > The Time Machine <. This is a fairly small corpus of just over 30000 words
d2l.DATA_HUB['time_machine'] = (d2l.DATA_URL + 'timemachine.txt',
                                '090b5e7e70c295757f55df93cb0a180b9691891a')

def read_time_machine():  #function made 
# Load the time machine dataset into a list of text lines 
    with open(d2l.download('time_machine'), 'r') as f: 
        lines = f.readlines()
    return [re.sub('[^A-Za-z]+', ' ', line).strip().lower() for line in lines]  #split the words into lower form

lines = read_time_machine()

print(f'# text lines: {len(lines)}')  #length of lines
print(lines[0]) #first line
print(lines[10])  #tenth line

#Tokenization
def tokenize(lines, token='word'):  
#Split text lines into word or character tokens
    if token == 'word':
        return [line.split() for line in lines]
    elif token == 'char':
        return [list(line) for line in lines]
    else:
        print('ERROR: unknown token type: ' + token)

tokens = tokenize(lines)
for i in range(11):
    print(tokens[i])

#Vocabulary
#build a dictionary, often called vocabulary 
class Vocab: 
#Vocabulary for text."""
    def __init__(self, tokens=None, min_freq=0, reserved_tokens=None):
        if tokens is None:
            tokens = []
        if reserved_tokens is None:
            reserved_tokens = []
# Sort according to frequencies
        counter = count_corpus(tokens)  # count the unique tokens in all the documents from the training set named as corpus
        self.token_freqs = sorted(counter.items(), key=lambda x: x[1],
                                  reverse=True)
# The index for the unknown token is 0
        self.unk, uniq_tokens = 0, ['<unk>'] + reserved_tokens
        uniq_tokens += [
            token for token, freq in self.token_freqs
            if freq >= min_freq and token not in uniq_tokens]
        self.idx_to_token, self.token_to_idx = [], dict()
        for token in uniq_tokens:
            self.idx_to_token.append(token)
            self.token_to_idx[token] = len(self.idx_to_token) - 1

    def __len__(self):
        return len(self.idx_to_token)

    def __getitem__(self, tokens):
        if not isinstance(tokens, (list, tuple)):
            return self.token_to_idx.get(tokens, self.unk)
        return [self.__getitem__(token) for token in tokens]

    def to_tokens(self, indices):
        if not isinstance(indices, (list, tuple)):
            return self.idx_to_token[indices]
        return [self.idx_to_token[index] for index in indices]

def count_corpus(tokens):  #save
#Count token frequencies."""
    # Here `tokens` is a 1D list or 2D list
    if len(tokens) == 0 or isinstance(tokens[0], list):
        # Flatten a list of token lists into a list of tokens
        tokens = [token for line in tokens for token in line]
    return collections.Counter(tokens)

#We construct a vocabulary using the time machine dataset as the corpus. Then we print the first few frequent tokens with their indices
vocab = Vocab(tokens)
print(list(vocab.token_to_idx.items())[:10])

# convert each text line into a list of numerical indices
for i in [0, 10]:
    print('words:', tokens[i])
    print('indices:', vocab[tokens[i]])

#Putting All Things Together
def load_corpus_time_machine(max_tokens=-1):  
#Return token indices and the vocabulary of the time machine dataset
    lines = read_time_machine()
    tokens = tokenize(lines, 'char')
    vocab = Vocab(tokens)
    # Since each text line in the time machine dataset is not necessarily a
    # sentence or a paragraph, flatten all the text lines into a single list
    corpus = [vocab[token] for line in tokens for token in line]
    if max_tokens > 0:
        corpus = corpus[:max_tokens]
    return corpus, vocab

corpus, vocab = load_corpus_time_machine()
len(corpus), len(vocab)

''' 
1) we tokenize text into characters, not words, to simplify the training in later sections 
2) corpus is a single list, not a list of token lists, since each text line in the time machine dataset is not necessarily a sentence or a paragraph '''

