# Punch speedometer with Raspberry Pi

## Operation

```
# Setup RaspberryPI and install tightvncserver
# https://qiita.com/murs313/items/81757bf8bc74b6b76cdf

# Enable i2c (Interface setting)
$ sudo raspi-config

# Setup vnc server in pi user environment
$ tightvncserver

# Install python libraries
$ pip3 install mpu6050-raspberrypi
$ pip3 install matplotlib
$ pip3 install numpy --upgrade

$ sudo apt-get install libatlas-base-dev

# scp and run scripts
$ scp plot-sensor.py pi@raspberrypi.local:/home/pi
```

## References
- https://www.blog.danishi.net/2020/04/23/post-3454/
- https://hellobreak.net/raspberry-pi-mpu6050-csv/
