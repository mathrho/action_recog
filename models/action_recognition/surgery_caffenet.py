#!/usr/bin/python

import argparse
import sys, os
import errno
from os.path import isfile, join

caffelib = '/home/zhenyang/local/softs/caffe'

if caffelib:
    caffepath = caffelib + '/python'
    sys.path.append(caffepath)

import caffe

def caffe_init(use_gpu, model_def_file, model_file, gpu_id):
    """
    Initilize pycaffe wrapper
    """

    if use_gpu:
        print 'Using GPU Mode'
        caffe.set_mode_gpu()
        caffe.set_device(gpu_id)
    else:
        print 'Using CPU Mode'
        caffe.set_mode_cpu()

    # By default use imagenet_deploy
    # model_def_file = 'models/UCF_CNN_M_2048_deploy.prototxt'
    # By default use caffe reference model
    # model_file = 'models/1_vgg_m_fine_tuning_rgb_iter_20000.caffemodel'
    if os.path.isfile(model_file):
        # NOTE: you'll have to get the pre-trained ILSVRC network
        print 'You need a network model file'

    if os.path.isfile(model_def_file):
        # NOTE: you'll have to get network definition
        print 'You need the network prototxt definition'

    # run with phase test (so that dropout isn't applied)
    net = caffe.Net(model_def_file, model_file, caffe.TEST)
    #caffe.set_phase_test()
    print 'Done with init, Done with set_phase_test'

    return net

if __name__ == "__main__":

    # initialize original caffe network
    net_origin = caffe_init(0, 'cuhk_action_temporal_vgg_16_flow_deploy.prototxt', 'vgg_16_action_flow_pretrain.caffemodel', None)
    net_surgery = caffe_init(0, 'cuhk_action_singleflow_vgg_16_deploy.prototxt', 'vgg_16_action_flow_pretrain.caffemodel', None)

    print("net_origin: blobs {}\nparams {}".format(net_origin.blobs.keys(), net_origin.params.keys()))
    print("net_surgery: blobs {}\nparams {}".format(net_surgery.blobs.keys(), net_surgery.params.keys()))

    params_origin = ['conv1_1']
    params_surgery = ['conv1_1_flow']

    conv_params_origin = {pr: (net_origin.params[pr][0].data, net_origin.params[pr][1].data) for pr in params_origin}
    for conv in params_origin:
        print '{} weights are {} dimensional and biases are {} dimensional'.format(conv, conv_params_origin[conv][0].shape, conv_params_origin[conv][1].shape)

    conv_params_surgery = {pr: (net_surgery.params[pr][0].data, net_surgery.params[pr][1].data) for pr in params_surgery}
    for conv in params_surgery:
        print '{} weights are {} dimensional and biases are {} dimensional'.format(conv, conv_params_surgery[conv][0].shape, conv_params_surgery[conv][1].shape)

    for pr, pr_conv in zip(params_origin, params_surgery):
        conv_params_surgery[pr_conv][0].flat = conv_params_origin[pr][0][:,:3,:,:].flat  # select 3 channels and flat unrolls the arrays
        conv_params_surgery[pr_conv][1][...] = conv_params_origin[pr][1]

    net_surgery.save('cuhk_action_singleflow_vgg_16_split1.caffemodel')

    print '*********** PROCESSED ALL *************'

