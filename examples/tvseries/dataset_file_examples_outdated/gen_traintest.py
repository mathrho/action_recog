#!/usr/bin/python

import sys, os
from os import listdir
from os.path import isfile, join
import numpy as np


if __name__ == "__main__":

    ###
    filename = './annot_caffe_train_origin.txt'
    fp_ = open('./annot_caffe_train.txt', 'w')
    with open(filename) as fp:
        for line in fp:
            splits = line.rstrip().split(' ')
            label = int(splits[2]) - 1
            fp_.write(splits[0]+' '+splits[1]+' '+str(label)+'\n')
    fp_.close()

    ###
    filename = './annot_caffe_test_origin.txt'
    fp_ = open('./annot_caffe_test.txt', 'w')
    with open(filename) as fp:
        for line in fp:
            splits = line.rstrip().split(' ')
            label = int(splits[2]) - 1
            fp_.write(splits[0]+' '+splits[1]+' '+str(label)+'\n')
    fp_.close()

    ###
    filename = './annot_caffe_val_origin.txt'
    fp_ = open('./annot_caffe_val.txt', 'w')
    with open(filename) as fp:
        for line in fp:
            splits = line.rstrip().split(' ')
            label = int(splits[2]) - 1
            fp_.write(splits[0]+' '+splits[1]+' '+str(label)+'\n')
    fp_.close()

    print '*********** PROCESSED ALL *************'

