# Punch speedometer with Raspberry Pi

## About

Punch speedometer made in Raspberry Pi.  

![image](/readme-src/punch-speedometer.jpg)

Moves on Raspberry Pi.  
Uses acceleration sensors and integrates to calculate velocity.  

![plot](/readme-src/velocity-acceleration-plot.png)

## Operation

```
# Setup RaspberryPI and install tightvncserver
# https://qiita.com/murs313/items/81757bf8bc74b6b76cdf

# Enable i2c (Interface setting)
$ sudo raspi-config

# check ip address of RaspberryPi
$ ip addr

# Setup vnc server in pi user environment
$ tightvncserver

# Install python libraries
$ pip3 install mpu6050-raspberrypi
$ pip3 install matplotlib
$ pip3 install numpy --upgrade

$ sudo apt-get install libatlas-base-dev

# scp python script
$ scp plot-sensor.py pi@raspberrypi.local:/home/pi

# run script with sensor set stable
# initial velocity is assumed to be 0 on every axis
$ python3 plot-velocity.py
```

# ToDo
- Acceleration from gravity should be cancelled. (use gyro sensor data and initial calibration)
- Plot speed is too slow to capture punch speed. Maybe better to only store data or send them via bluetooth.
- Wiring can affect punch speed. Sensors like [this](https://www.amazon.co.jp/Bluetooth%E5%8A%A0%E9%80%9F%E5%BA%A6%E8%A8%88-BWT901CL-MPU9250%E9%AB%98%E7%B2%BE%E5%BA%A69%E8%BB%B8%E3%82%B8%E3%83%A3%E3%82%A4%E3%83%AD%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97-%E8%A7%92%E5%BA%A6%EF%BC%88XY0-05%C2%B0%E7%B2%BE%E5%BA%A6%EF%BC%89-%E3%82%AB%E3%83%AB%E3%83%9E%E3%83%B3%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%83%BC%E4%BB%98%E3%81%8D%E7%A3%81%E5%8A%9B%E8%A8%88%E3%80%81200Hz%E9%AB%98%E5%AE%89%E5%AE%9A3%E8%BB%B8IMU%E3%82%BB%E3%83%B3%E3%82%B5%E3%83%BC/dp/B07RX6N4B1) can be more effective.

## References
- https://www.blog.danishi.net/2020/04/23/post-3454/
- https://hellobreak.net/raspberry-pi-mpu6050-csv/
