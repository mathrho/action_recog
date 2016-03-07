#!/usr/bin/env sh

GOOGLE_LOG_DIR=models/hmdb51/log \
    mpirun -np 2 \
    build/install/bin/caffe train \
    --solver=models/hmdb51/vgg_16_rgb_solver2.prototxt \
    --weights=models/hmdb51/snapshot_rgb_5K/hmdb51_action_recognition_vgg_16_split2_rgb_iter_5000.caffemodel

