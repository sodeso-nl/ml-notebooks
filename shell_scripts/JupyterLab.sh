#!/bin/sh
eval "$(conda shell.bash hook)"
conda activate ml

# So Tensorflow can find the Cuda nvvm folder.
# Install through conda install -c nvidia cuda-nvcc:
export XLA_FLAGS=--xla_gpu_cuda_data_dir=/home/sodeso/anaconda3/envs/ml

jupyter lab --notebook-dir=/home/sodeso/Development/ml-notebooks --NotebookApp.iopub_data_rate_limit=10000000 
