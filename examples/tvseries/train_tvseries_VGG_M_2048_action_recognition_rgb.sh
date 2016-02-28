#!/usr/bin/env sh

GOOGLE_LOG_DIR=models/tvseries/log \
    mpirun -np 1 \
    build/install/bin/caffe train \
    --solver=models/tvseries/VGG_M_2048_rgb_solver.prototxt \
    --weights=models/tvseries/VGG_CNN_M_2048.caffemodel

