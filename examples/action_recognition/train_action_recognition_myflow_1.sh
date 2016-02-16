#!/usr/bin/env sh

GOOGLE_LOG_DIR=models/action_recognition/log \
    mpirun -np 4 \
    build/install/bin/caffe train \
    --solver=models/action_recognition/vgg_16_myflow_solver_1.prototxt \
    --weights=models/action_recognition/snapshot_myflow_lr0.005/lzy_action_recognition_vgg_16_split1_singleflow_iter_39000.caffemodel
