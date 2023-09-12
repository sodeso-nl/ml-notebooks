
## Introduction

### Dependencies

Install the dependencies mentioned in the requirements.txt using the following command

python3 -m pip install -r requirements.txt

Do use the python3 -m ... command and not `pip install ...` command when using a conda environemnt, this will make sure that the dependencies are installed within the environment and not in the global python environment.

Updating so_ml_tools

so_ml_tools can be updated seperatly by issueing the following command:

python3 -m pip install -U so_ml_tools --no-deps


### Setup

#### Kaggle

Some notebooks require Kaggle API keys, you can create these on kaggle.com. To store this information create a file ´kaggle.json´ in your ~/.kaggle folder with the following information:

{"username":"[your username]","key":"[your API key]"}

### Errors & Messages

Certain errors or messages can pop-up when executing the notebooks (assuming Linux & NVidia graphics card):

##### IOPub message rate exceeded. The Jupyter server will temporarily stop sending output

The output explains some solutions, for me the solution of adding the '--NotebookApp.iopub_data_rate_limit=10000000' when executing Jupyter.

##### This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations. To enable the following instructions: AVX2 AVX512F AVX512_VNNI AVX512_BF16 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.

This message is telling the user that TensorFlow is optimized to use these instructions, the following code can be used to suppress this message:

  import os; 

  os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

Another option is to add the following environmental variable:

    export TF_CPP_MIN_LOG_LEVEL=1

##### libdevice not found at ./libdevice.10.bc

This has to do with a missing library which is not part of the installation steps covered by Tensorflow ( https://www.tensorflow.org/install/pip ). To solve this error we can follow these steps:

1) Install the necessary dependencies:
   conda install -c nvidia cuda-nvcc==12.2.240

2) Next we need to create an environmental variable:
   export XLA_FLAGS=--xla_gpu_cuda_data_dir=.../anaconda3/envs/ml

   Where the envs/ml is in this case my conda environment `ml`, within this environment there should be a folder with the name `nvvm`
   
##### successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355

More information about this error can be found here:

https://saturncloud.io/blog/understanding-memoryerror-in-tensorflow-and-successful-numa-node-read-from-sysfs-had-negative-value-1-with-xen/

##### TF-TRT Warning: Could not find TensorRT

Check the documentation on: https://www.tensorflow.org/install/pip#software_requirements

This warning is not really an issue, TensorRT can speed up inference but is not mandatory.