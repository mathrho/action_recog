#!/usr/bin/env sh

GOOGLE_LOG_DIR=models/tvseries/log \
    mpirun -np 1 \
    build/install/bin/caffe train \
    --solver=models/tvseries/vgg_16_rgb_solver.prototxt \
    --weights=models/tvseries/vgg_16_action_rgb_pretrain.caffemodel

