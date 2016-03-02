#!/usr/bin/python

import sys, os
from os import listdir
from os.path import isfile, join
import numpy as np
import glob


if __name__ == "__main__":

    ###
    testset = '/home/egavves/Datasets/tvseries/videolist_test.txt'
    fp_test = open('./list_test.txt', 'w')
    with open(testset) as fp:
        for line in fp:
            filename = line.rstrip().split(' ')[0]
            filename_ = os.path.splitext(os.path.basename(filename))[0]
            vid_name = join('/home/egavves/Datasets/tvseries/frames', filename_)

            imglist = glob.glob(join(vid_name, 'frame_*.jpg'))
            duration = len(imglist)
            assert duration>0
            fp_test.write(vid_name+' '+str(duration)+'\n')
    fp_test.close()

    ###
    valset = '/home/egavves/Datasets/tvseries/videolist_val.txt'
    fp_val = open('./list_val.txt', 'w')
    with open(valset) as fp:
        for line in fp:
            filename = line.rstrip().split(' ')[0]
            filename_ = os.path.splitext(os.path.basename(filename))[0]
            vid_name = join('/home/egavves/Datasets/tvseries/frames', filename_)

            imglist = glob.glob(join(vid_name, 'frame_*.jpg'))
            duration = len(imglist)
            assert duration>0
            fp_val.write(vid_name+' '+str(duration)+'\n')
    fp_val.close()

    ###
    trainset = '/home/egavves/Datasets/tvseries/videolist_train.txt'
    fp_train = open('./list_train.txt', 'w')
    with open(trainset) as fp:
        for line in fp:
            filename = line.rstrip().split(' ')[0]
            filename_ = os.path.splitext(os.path.basename(filename))[0]
            vid_name = join('/home/egavves/Datasets/tvseries/frames', filename_)

            imglist = glob.glob(join(vid_name, 'frame_*.jpg'))
            duration = len(imglist)
            assert duration>0
            fp_train.write(vid_name+' '+str(duration)+'\n')
    fp_train.close()

    print '*********** PROCESSED ALL *************'

