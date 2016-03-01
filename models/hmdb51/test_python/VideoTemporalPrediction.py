'''
A sample function for classification using temporal network
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

def VideoTemporalPrediction(
        vid_name,
        net,
        num_categories,
        feature_layer,
        start_frame=0,
        num_frames=0,
        num_samples=25,
        optical_flow_frames=1
        ):

    if num_frames == 0:
        vid_name_ = vid_name.replace('[', '[[]')
        imglist = glob.glob(os.path.join(vid_name_, '*flow_x*.jpg'))
        duration = len(imglist)
    else:
        duration = num_frames

    print 'Video: ', vid_name, 'Duration: ', duration, 'Sample: ', num_samples
    # selection
    step = int(math.floor((duration-optical_flow_frames+1)/num_samples))
    dims = (num_samples,optical_flow_frames*2,256,340)
    #dims = (num_samples,optical_flow_frames*2,224,224)
    flow = np.zeros(shape=dims, dtype=np.float32)
    flow_flip = np.zeros(shape=dims, dtype=np.float32)

    for i in range(num_samples):
        for j in range(optical_flow_frames):
            flow_x_file = os.path.join(vid_name, 'flow_x_{0:04d}.jpg'.format(i*step+j+1 + start_frame))
            flow_y_file = os.path.join(vid_name, 'flow_y_{0:04d}.jpg'.format(i*step+j+1 + start_frame))
            img_x = cv2.imread(flow_x_file, cv2.IMREAD_GRAYSCALE)
            img_y = cv2.imread(flow_y_file, cv2.IMREAD_GRAYSCALE)
            #img_x = caffe.io.load_image(flow_x_file)*255.0
            #img_y = caffe.io.load_image(flow_y_file)*255.0

            img_x = cv2.resize(img_x, (340, 256), interpolation=cv2.INTER_LINEAR)
            img_y = cv2.resize(img_y, (340, 256), interpolation=cv2.INTER_LINEAR)
            #img_x = cv2.resize(img_x, (224, 224), interpolation=cv2.INTER_LINEAR)
            #img_y = cv2.resize(img_y, (224, 224), interpolation=cv2.INTER_LINEAR)

            flow[i,j*2,:,:] = img_x - 128.0
            flow[i,j*2+1,:,:] = img_y - 128.0

            flow_flip[i,j*2,:,:] = 255 - img_x[:, ::-1] - 128.0
            flow_flip[i,j*2+1,:,:] = img_y[:, ::-1] - 128.0

    # crop
    flow_1 = flow[:, :, :224, :224]
    flow_2 = flow[:, :, :224, -224:]
    flow_3 = flow[:, :, 16:240, 60:284]
    flow_4 = flow[:, :, -224:, :224]
    flow_5 = flow[:, :, -224:, -224:]
    flow_f_1 = flow_flip[:, :, :224, :224]
    flow_f_2 = flow_flip[:, :, :224, -224:]
    flow_f_3 = flow_flip[:, :, 16:240, 60:284]
    flow_f_4 = flow_flip[:, :, -224:, :224]
    flow_f_5 = flow_flip[:, :, -224:, -224:]

    #flows = flow
    flows = np.concatenate((flow_1,flow_2,flow_3,flow_4,flow_5,flow_f_1,flow_f_2,flow_f_3,flow_f_4,flow_f_5), axis=0)

    # substract mean
    #d = sio.loadmat(mean_file)
    #flow_mean = d['image_mean']
    #flows = flows - np.tile(flow_mean[...,np.newaxis], (1, 1, 1, flows.shape[3]))
    #flows = np.transpose(flows, (1,0,2,3))

    # test
    batch_size = 50
    prediction = np.zeros((num_categories,flows.shape[0]))
    num_batches = int(math.ceil(float(flows.shape[0])/batch_size))
    in_data = np.zeros((batch_size,optical_flow_frames*2,224,224), dtype=np.float32)

    #print num_batches
    for bb in range(num_batches):
        span = range(batch_size*bb, min(flows.shape[0],batch_size*(bb+1)))
        #net.blobs['data'].data[...] = np.transpose(flows[:,:,:,span], (3,2,1,0))
        #output = net.forward()
        #prediction[:, span] = np.transpose(output[feature_layer])

        #print span
        in_data[0:len(span),:,:,:] = flows[span,:,:,:]
        out = net.forward(**{net.inputs[0]: in_data})
        output = out[net.outputs[0]]
        prediction[:, span] = np.transpose(output[0:len(span), :])
    return prediction
