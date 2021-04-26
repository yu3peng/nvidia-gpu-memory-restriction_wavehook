# nvidia gpu using memory restriction (wavehook)
wavehook functions restrict and isolate nVidia GPU memory.

step0

1. https://www.katacoda.com/courses/ubuntu/playground
2. git clone https://github.com/yu3peng/nvidia-gpu-memory-restriction_wavehook.git
3. docker run -v /root/nvidia-gpu-memory-restriction_wavehook:/nvidia-gpu-memory-restriction_wavehook -it nvidia/cuda:11.3.0-devel-ubuntu18.04 bash
4. cd /nvidia-gpu-memory-restriction_wavehook/src
5. chmod 755 wavehook.make.sh
6. export CPATH=$CPATH:/usr/local/cuda-11.3/targets/x86_64-linux/include
7. export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/cuda-11.3/targets/x86_64-linux/include
8. ./wavehook.make.sh

get wavehook.so

step1

1. docker run -v /root/nvidia-gpu-memory-restriction_wavehook:/nvidia-gpu-memory-restriction_wavehook -it tensorflow/tensorflow:2.2.2-gpu-py3 bash
2. export LD_PRELOAD=/nvidia-gpu-memory-restriction_wavehook/src/wavehook.so
3. export GPU_MEMORY=200

step2
1. cd /nvidia-gpu-memory-restriction_wavehook/CNN
2. python TensorFlow_example.py

This Program intercept function cuMemGetInfo, cuMemGetInfo_v2, cuDeviceGetName, and another mainly methods in nVidia Driver.
Please refer to source program ...

