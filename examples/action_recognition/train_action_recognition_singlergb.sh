#!/usr/bin/env sh

GOOGLE_LOG_DIR=models/action_recognition/log \
    mpirun -np 4 \
    build/install/bin/caffe train \
    --solver=models/action_recognition/vgg_16_singlergb_solver.prototxt \
    --weights=models/action_recognition/vgg_16_action_rgb_pretrain.caffemodel

