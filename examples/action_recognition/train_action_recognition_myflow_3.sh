#!/usr/bin/env sh

GOOGLE_LOG_DIR=models/action_recognition/log \
    mpirun -np 4 \
    build/install/bin/caffe train \
    --solver=models/action_recognition/vgg_16_myflow_solver_3.prototxt \
    --weights=models/action_recognition/snapshot_myflow_lr0.005_2_lr0.0001/lzy_action_recognition_16_split1_myflow_iter_20000.caffemodel
