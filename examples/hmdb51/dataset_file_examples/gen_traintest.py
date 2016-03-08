#!/usr/bin/python

import sys, os
from os import listdir
from os.path import isfile, join
import numpy as np
import glob


if __name__ == "__main__":

    dataset = '/home/zhenyang/Workspace/data/HMDB51'
    #allclasses = sorted(glob.glob(join(dataset, 'test_train_splits', '*_test_split1.txt')))
    #allclasses = sorted(glob.glob(join(dataset, 'test_train_splits', '*_test_split2.txt')))
    allclasses = sorted(glob.glob(join(dataset, 'test_train_splits', '*_test_split3.txt')))

    fp_train = open(join(dataset, 'train3.txt'), 'w')
    fp_test = open(join(dataset, 'test3.txt'), 'w')
    for c, class_file in enumerate(allclasses):
        with open(class_file) as fp:
            for line in fp:
                splits = line.rstrip().split(' ')
                filename = splits[0]
                label = int(splits[1])
                # check train or test
                if label > 0:
                    if label == 1:
                        fp_train.write(filename+ ' '+str(c)+'\n')
                    elif label == 2:
                        fp_test.write(filename+ ' '+str(c)+'\n')
                    else:
                        print 'error!'
                        exit()

    fp_train.close()
    fp_test.close()

    max_duration = 0
    ##
    #fp_train = open('./train_rgb_split3.txt', 'w')
    fp_train = open('./train_flow_split3.txt', 'w')
    with open(join(dataset, 'train3.txt')) as fp:
        for line in fp:
            splits = line.rstrip().split(' ')
            filename = splits[0]
            label = int(splits[1])
            filename_ = os.path.splitext(os.path.basename(filename))[0]
            _filename = filename_.replace('[', '[[]')

            #frames = glob.glob(join(dataset, 'features', 'flow_tvl1_gpu', _filename, 'image_*.jpg'))
            frames = glob.glob(join(dataset, 'features', 'flow_tvl1_gpu', _filename, 'flow_x_*.jpg'))
            duration = len(frames)
            if duration == 0:
                print 'video: ', filename
            #print 'Duration: ', duration

            fp_train.write(join(dataset, 'features', 'flow_tvl1_gpu', filename_)+' '+str(duration)+' '+str(label)+'\n')

            if duration > max_duration:
                max_duration = duration
    fp_train.close()

    ##
    #fp_test = open('./val_rgb_split3.txt', 'w')
    fp_test = open('./val_flow_split3.txt', 'w')
    with open(join(dataset, 'test3.txt')) as fp:
        for line in fp:
            splits = line.rstrip().split(' ')
            filename = splits[0]
            label = int(splits[1])
            filename_ = os.path.splitext(os.path.basename(filename))[0]
            _filename = filename_.replace('[', '[[]')

            #frames = glob.glob(join(dataset, 'features', 'flow_tvl1_gpu', _filename, 'image_*.jpg'))
            frames = glob.glob(join(dataset, 'features', 'flow_tvl1_gpu', _filename, 'flow_x_*.jpg'))
            duration = len(frames)
            if duration == 0:
                print 'video: ', filename
            #print 'Duration: ', duration

            fp_test.write(join(dataset, 'features', 'flow_tvl1_gpu', filename_)+' '+str(duration)+' '+str(label)+'\n')

            if duration > max_duration:
                max_duration = duration
    fp_test.close()

   
    print 'Video Max Duration: ', max_duration

    print '*********** PROCESSED ALL *************'

