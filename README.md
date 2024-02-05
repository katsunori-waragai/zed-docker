# zed-docker
docker example for zed sdk (stereolabs) on Jetson

## install

### 以下のdocker hub から該当するtagを見つけること
https://hub.docker.com/r/stereolabs/zed/

### JetPack5.1
sudo docker pull stereolabs/zed:4.0-py-devel-jetson-jp5.1.0

sudo docker run -it --privileged  stereolabs/zed:4.0-py-devel-jetson-jp5.1.0


docker pull stereolabs/zed:3.7-gl-devel-cuda11.4-ubuntu20.04  # pull ZED SDK v3.7.x devel release with OpenGL support under Ubuntu 20.04
xhost +si:localuser:root  # allow containers to communicate with X server
  docker run -it --runtime nvidia --privileged -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix stereolabs/zed:3.7-gl-devel-cuda11.4-ubuntu20.04
