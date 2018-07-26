#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-

__author__ = "YaqiangCao"
__date__ = ""
__email__ = "caoyaqiang0410@gmail.com"

"""
"""
#sys
import os
from collections import Counter

#3rd
import h5py
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout,Flatten,Conv2D,MaxPooling2D
from keras.utils import plot_model,to_categorical,multi_gpu_model
from keras.models import load_model


#global settings
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
#only using CPU, set 1,2,3 to it to use GPU, if remove this, using all GPUs
os.environ["CUDA_VISIBLE_DEVICES"] = "3"
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'


def preWords(words,minFreq=1,dropProb=1e-5,dropCutoff=0.95):
    """
    Prepare words.
    """
    wordFreq = Counter(words)
    #total original words count
    tt = sum(wordFreq.values())
    #filtering words
    #1. too fewer
    wordFreq2 = {w:c for w,c in wordFreq.items() if c > minFreq}
    poorWords = set(wordFreq.keys()).difference(wordFreq2.keys())
    wordFreq = wordFreq2
    #2. too many such as stop words
    wordFreq2 = {w: 1 - np.sqrt(dropProb/c*tt) for w,c in wordFreq.items()}
    wordFreq2 = {w: c for w,c in wordFreq2.items() if c < dropCutoff}
    richWords = set(wordFreq.keys()).difference(wordFreq2.keys())
    wordFreq = wordFreq2
    #word2idx and idx2word
    word2idx = {w:i for i,w in enumerate(wordFreq.keys())}
    idx2word = {i:w for i,w in enumerate(wordFreq.keys())}
    #converting all words to number vectors
    indexedWords = [word2idx[w] for w in words if w in wordFreq]
    vocabSize = len(idx2word)
    return word2idx,idx2word,indexedWords,vocabSize


def getXy(indexedWords,windows=5):
    x,y = [],[]
    for i in range(len(indexedWords)):
        input_w = indexedWords[i]
        left = max(0,i-windows)
        right = min(i+windows+1,len(indexedWords))
        labels = list(set(indexedWords[left:i]+indexedWords[i+1:right]))
        x.extend([input_w]*len(labels))
        y.extend(labels)
    x = np.array(x)
    y = np.expand_dims(y,-1)
    return x,y


def test():
    ss = open("../data/test_tokens.txt").read().split("\n")
    ns = []
    for s in ss:
        ns.extend(s.split(","))
    word2idx,idx2word,indexedWords,vocabSize = preWords(ns[:20000])
    x,y = getXy(indexedWords)



if __name__ == "__main__":
    test()
