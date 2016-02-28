#!/usr/bin/env sh

GOOGLE_LOG_DIR=models/tvseries/log \
    mpirun -np 1 \
    build/install/bin/caffe train \
    --solver=models/tvseries/VGG_M_2048_rgb_solver.prototxt \
    --weights=models/tvseries/cuhk_ucf101_spatial_v2.caffemodel

