#!/usr/bin/env sh

GOOGLE_LOG_DIR=models/hmdb51/log \
    mpirun -np 2 \
    build/install/bin/caffe train \
    --solver=models/hmdb51/vgg_16_flow_solver.prototxt \
    --weights=models/hmdb51/lzy_action_recognition_vgg_16_split1_myflow_iter_56K.caffemodel

