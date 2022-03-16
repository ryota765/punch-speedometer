from mpu6050 import mpu6050
from time import sleep

sensor = mpu6050(0x68)

while True:
    gyro_data = sensor.get_gyro_data()
    accel_data = sensor.get_accel_data()
    temp = sensor.get_temp()

    # 小数点以下第3位まで表示
    print("【角速度】 x:" + "%6.3f" % gyro_data['x'] + " y:" + "%6.3f" % gyro_data['y'] + " z:" + "%6.3f" % gyro_data['z'])

    # 小数点以下第3位まで表示
    print("【加速度】 x:" + "%6.3f" % accel_data['x'] + " y:" + "%6.3f" % accel_data['y'] + " z:" + "%6.3f" % accel_data['z'])

    # 小数点以下第1位まで表示
    print("【温度】" + "%4.1f" % temp + "℃")

    sleep(0.5)