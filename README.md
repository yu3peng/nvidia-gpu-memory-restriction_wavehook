# nvidia gpu using memory restriction (wavehook)
wavehook functions restrict and isolate nVidia GPU memory.

step0

1. https://www.katacoda.com/courses/ubuntu/playground
2. git clone https://github.com/waveware4ai/nvidia-gpu-memory-restriction_wavehook.git
3. cd nvidia-gpu-memory-restriction_wavehook/src
4. rm -rf wavehook.so
5. docker run -v /root/nvidia-gpu-memory-restriction_wavehook:/nvidia-gpu-memory-restriction_wavehook -it nvidia/cuda:11.2.2-devel-ubuntu20.04 bash
6. cd /nvidia-gpu-memory-restriction_wavehook/src
7. chmod 755 wavehook.make.sh
8. export CPATH=$CPATH:/usr/local/cuda-11.2/targets/x86_64-linux/include
9. export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/cuda-11.2/targets/x86_64-linux/include
10. ./wavehook.make.sh

get wavehook.so

step1. export LD_PRELOAD=/path/wavehook.so

step2. export GPU_FRACTION=0.01 ~ 1.0

step3. run tensorflow_program

This Program intercept function cuMemGetInfo, cuMemGetInfo_v2, cuDeviceGetName, and another mainly methods in nVidia Driver.
Please refer to source program ...

