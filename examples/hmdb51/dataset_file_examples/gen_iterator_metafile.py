#!/usr/bin/python

import sys, os
from os import listdir
from os.path import isfile, join
import numpy as np
import glob


if __name__ == "__main__":

    trainset = './train_flow_split3.txt'
    fp_train_filenames = open('/home/zhenyang/Workspace/data/HMDB51/train_filenames_split3.txt', 'w')
    fp_train_framenum = open('/home/zhenyang/Workspace/data/HMDB51/train_framenum_split3.txt', 'w')
    fp_train_labels = open('/home/zhenyang/Workspace/data/HMDB51/train_labels_split3.txt', 'w')
    with open(trainset) as fp:
        for line in fp:
            splits = line.rstrip().split(' ')
            filename = os.path.splitext(os.path.basename(splits[0]))[0]
            numframe = int(splits[1])
            label = int(splits[2])
            
            fp_train_filenames.write(filename+'\n')
            fp_train_framenum.write(str(numframe)+'\n')
            fp_train_labels.write(str(label)+'\n')


    testset = './val_flow_split3.txt'
    fp_test_filenames = open('/home/zhenyang/Workspace/data/HMDB51/test_filenames_split3.txt', 'w')
    fp_test_framenum = open('/home/zhenyang/Workspace/data/HMDB51/test_framenum_split3.txt', 'w')
    fp_test_labels = open('/home/zhenyang/Workspace/data/HMDB51/test_labels_split3.txt', 'w')
    with open(testset) as fp:
        for line in fp:
            splits = line.rstrip().split(' ')
            filename = os.path.splitext(os.path.basename(splits[0]))[0]
            numframe = int(splits[1])
            label = int(splits[2])
            
            fp_test_filenames.write(filename+'\n')
            fp_test_framenum.write(str(numframe)+'\n')
            fp_test_labels.write(str(label)+'\n')


    print '*********** PROCESSED ALL *************'

