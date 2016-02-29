#!/usr/bin/python

import sys, os
from os import listdir
from os.path import isfile, join
import numpy as np
import glob


if __name__ == "__main__":

    dataset = '/home/zhenyang/Workspace/data/HMDB51'

    allclasses = sorted(glob.glob(join(dataset, 'test_train_splits', '*_test_split1.txt')))

    fp_train = open(join(dataset, 'train1.txt'), 'w')
    fp_test = open(join(dataset, 'test1.txt'), 'w')
    for c, class_file in enumerate(allclasses):
        with open(class_file) as fp:
            for line in fp:
                splits = line.rstrip().split(' ')
                filename = splits[0]
                label = int(splits[1])
                # check train or test
                if label > 0:
                    if label == 1:
                        fp_train.write(filename + ' ' + str(c) + '\n')
                    elif label == 2:
                        fp_test.write(filename + ' ' + str(c) + '\n')
                    else:
                        print 'error!'
                        exit()

    fp_train.close()
    fp_test.close()


    print '*********** PROCESSED ALL *************'

