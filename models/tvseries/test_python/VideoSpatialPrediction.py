'''
A sample function for classification using spatial network
Customize as needed:
e.g. num_categories, layer for feature extraction, batch_size
'''

import glob
import os, sys
import numpy as np
import math
import cv2
from scipy.misc import imread, imresize
import scipy.io as sio

caffelib = '/home/zhenyang/local/softs/caffe'
if caffelib:
    caffepath = caffelib + '/python'
    sys.path.append(caffepath)
import caffe

def VideoSpatialPrediction(
        vid_name,
        net,
        num_categories,
        feature_layer,
        start_frame=0,
        num_frames=0,
        num_samples=25
        ):

    if num_frames == 0:
        imglist = glob.glob(os.path.join(vid_name, '*image_*.jpg'))
        duration = len(imglist)
    else:
        duration = num_frames

    print 'Video: ', vid_name, 'Duration: ', duration, 'Sample: ', num_samples
    # selection
    step = int(math.floor((duration-1)/(num_samples-1)))
    #dims = (num_samples,3,224,224)
    dims = (num_samples,3,256,340)
    rgb = np.zeros(shape=dims, dtype=np.float32)
    rgb_flip = np.zeros(shape=dims, dtype=np.float32)

    for i in range(num_samples):
        img_file = os.path.join(vid_name, 'image_{0:04d}.jpg'.format(i*step+1))

        #img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED)
        #img = imread(img_file)
        #img = img[:,:,(2,1,0)]  #convert RGB-> BGR
        img = caffe.io.load_image(img_file)*255.0
        img = img[:,:,(2,1,0)]   #convert RGB-> BGR

        #img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_LINEAR)
        img = cv2.resize(img, (340, 256), interpolation=cv2.INTER_LINEAR)
        img = img - np.array([104., 117., 123.])
        img = np.transpose(img, (2,0,1))
        rgb[i,:,:,:] = img
        rgb_flip[i,:,:,:] = img[:,:,::-1]

        #img = cv2.resize(img, dims[1::-1], interpolation=cv2.INTER_LINEAR)
        #rgb[:,:,:,i] = img
        #rgb_flip[:,:,:,i] = img[:,::-1,:]

    # crop
    rgb_1 = rgb[:, :, :224, :224]
    rgb_2 = rgb[:, :, :224, -224:]
    rgb_3 = rgb[:, :, 16:240, 60:284]
    rgb_4 = rgb[:, :, -224:, :224]
    rgb_5 = rgb[:, :, -224:, -224:]
    rgb_f_1 = rgb_flip[:, :, :224, :224]
    rgb_f_2 = rgb_flip[:, :, :224, -224:]
    rgb_f_3 = rgb_flip[:, :, 16:240, 60:284]
    rgb_f_4 = rgb_flip[:, :, -224:, :224]
    rgb_f_5 = rgb_flip[:, :, -224:, -224:]

    #rgbs = rgb
    rgbs = np.concatenate((rgb_1,rgb_2,rgb_3,rgb_4,rgb_5,rgb_f_1,rgb_f_2,rgb_f_3,rgb_f_4,rgb_f_5), axis=0)

    # substract mean
    #d = sio.loadmat(mean_file)
    #image_mean = d['image_mean']
    #rgbs = rgbs[:,:,::-1,:] - np.tile(image_mean[...,np.newaxis], (1, 1, 1, rgbs.shape[3]))
    #rgbs = rgbs[:,:,:,:] - np.tile(image_mean[...,np.newaxis], (1, 1, 1, rgbs.shape[3]))
    #rgbs = np.transpose(rgbs, (1,0,2,3))

    # test
    batch_size = 50
    prediction = np.zeros((num_categories,rgbs.shape[0]))
    num_batches = int(math.ceil(float(rgbs.shape[0])/batch_size))
    in_data = np.zeros((batch_size,3,224,224), dtype=np.float32)

    #print num_batches
    for bb in range(num_batches):
        span = range(batch_size*bb, min(rgbs.shape[0], batch_size*(bb+1)))
        #net.blobs['data'].data[...] = np.transpose(rgbs[:,:,:,span], (3,2,1,0))
        #output = net.forward()
        #prediction[:, span] = np.transpose(output[feature_layer])

        #print span
        in_data[0:len(span),:,:,:] = rgbs[span,:,:,:]
        out = net.forward(**{net.inputs[0]: in_data})
        output = out[net.outputs[0]]
        prediction[:, span] = np.transpose(output[0:len(span), :])
    return prediction
