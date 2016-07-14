#!/usr/bin/python

import sys, os
import errno
import subprocess
from os import listdir
import glob
from os.path import isfile, join
import cv2

def cp_rn_imagefile(from_dir, filename, to_dir):

    frames = sorted(glob.glob(join(from_dir, filename, 'frame_*.jpg')))
    duration = len(frames)
    print 'Duration: ', duration

    outputdir = join(to_dir, filename)
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    # copy and rename images
    for i, frame in enumerate(frames):
        #copy_to = join(to_dir, filename, 'image_{0:04d}.jpg'.format(i+1))
        #cmd_line = 'cp %s %s' % (frame,copy_to,)
        #proc = subprocess.Popen(cmd_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
        #while proc.poll() is None:
        #    line = proc.stdout.readline()
        #    #print(line)
        save_to = join(to_dir, filename, 'image_{0:04d}.jpg'.format(i+1))
        img = cv2.imread(frame, cv2.CV_LOAD_IMAGE_COLOR)
        img = cv2.resize(img, (340, 256), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(save_to, img)

if __name__ == "__main__":

    src_dir = '/home/egavves/Datasets/tvseries_dissected/frames/'
    dst_dir = '/home/zhenyang/Workspace/data/tvseries/frame_dissected/'

    dataset = './annot_caffe_train.txt'
    #dataset = './annot_caffe_test.txt'
    #dataset = './annot_caffe_val.txt'

    ###
    with open(dataset) as fp:
        for line in fp:
            splits = line.rstrip().split(' ')
            filename = os.path.splitext(os.path.basename(splits[0]))[0]
            cp_rn_imagefile(src_dir, filename, dst_dir)

    print '*********** PROCESSED ALL *************'

