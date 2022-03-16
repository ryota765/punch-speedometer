# https://hellobreak.net/raspberry-pi-mpu6050-csv/

import smbus
import math
from time import sleep
import time

DEV_ADDR = 0x68

ACCEL_XOUT = 0x3B
ACCEL_YOUT = 0x3D
ACCEL_ZOUT = 0x3F
TEMP_OUT = 0x41
GYRO_XOUT = 0x43
GYRO_YOUT = 0x45
GYRO_ZOUT = 0x47

PWR_MGMT_1 = 0x6B
PWR_MGMT_2 = 0x6C   

bus = smbus.SMBus(1)
time.sleep(0.2)

# Initialize
bus.write_byte_data(DEV_ADDR, 0x6B, 0x80) # RESET
time.sleep(0.25)
bus.write_byte_data(DEV_ADDR, 0x6B, 0x00) # RESET
time.sleep(0.25)
bus.write_byte_data(DEV_ADDR, 0x6A, 0x07) # RESET
time.sleep(0.25)
bus.write_byte_data(DEV_ADDR, 0x6A, 0x00) # RESET
time.sleep(0.25)
bus.write_byte_data(DEV_ADDR, 0x1A, 0x00) # CONFIG
bus.write_byte_data(DEV_ADDR, 0x1B, 0x18) # +-2000°/s
bus.write_byte_data(DEV_ADDR, 0x1C, 0x08) # +-4g
time.sleep(0.1)


def read_word(adr):
    high = bus.read_byte_data(DEV_ADDR, adr)
    low = bus.read_byte_data(DEV_ADDR, adr+1)
    val = (high << 8) + low
    return val

def read_word_sensor(adr):
    val = read_word(adr)
    if (val >= 0x8000):  return -((65535 - val) + 1)
    else:  return val

# def get_temp():
#     temp = read_word_sensor(TEMP_OUT)
#     x = temp / 340 + 36.53      # data sheet(register map)記載の計算式.
#     return x

# def getGyro():
#     x = read_word_sensor(GYRO_XOUT)/ 16.4
#     y = read_word_sensor(GYRO_YOUT)/ 16.4
#     z = read_word_sensor(GYRO_ZOUT)/ 16.4
#     return [x, y, z]


def getAccel():
    x = read_word_sensor(ACCEL_XOUT)/ 8192
    y = read_word_sensor(ACCEL_YOUT)/ 8192
    z = read_word_sensor(ACCEL_ZOUT)/ 8192
    return [x, y, z]

while(True):
    for i in range(1000):
        ax, ay, az = getAccel()
        # gx, gy, gz = getGyro()
        print('ax: {0:4.3f}, ay: {0:4.3f}, az: {0:4.3f}' .format(ax, ay, az))
        time.sleep(0.05)
    break