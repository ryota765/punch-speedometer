from mpu6050 import mpu6050
from time import sleep

import numpy as np
import matplotlib.pyplot as plt

sensor = mpu6050(0x68)

TIME_STEP = 0.1


def initialize_plot(ax, title, sec, x0=0, y0=0, z0=0):
    x_list = np.zeros(63)
    x_list[0] = x0
    (x_lines,) = ax.plot(sec, x_list, color="red", label="x")

    y_list = np.zeros(63)
    y_list[0] = y0
    (y_lines,) = ax.plot(sec, y_list, color="blue", label="y")

    z_list = np.zeros(63)
    z_list[0] = z0
    (z_lines,) = ax.plot(sec, z_list, color="green", label="z")

    ax.legend()  # ラベル描画
    ax.set_title(title)
    ax.set_ylim(-300, 300)
    ax.set_xticks([])  # X軸のメモリ非表示

    return ax, x_list, x_lines, y_list, y_lines, z_list, z_lines


def plot_loop():
    # センサーデータ取得
    # temp = "%4.1f" % sensor.get_temp()
    gyro_data = sensor.get_gyro_data()
    accel_data = sensor.get_accel_data()

    # for test
    # gyro_data = {'x': 0.1, 'y': 0.2, 'z': 0.3}
    # accel_data = {'x': 0.1, 'y': 0.2, 'z': 0.3}

    fig, (ax_gyro, ax_accel, ax_vel) = plt.subplots(ncols=3, figsize=(10, 7))

    # X座標
    sec = np.arange(-np.pi, np.pi, TIME_STEP)

    # 角速度
    # x: roll, y: pitch, z: yaw
    (
        ax_gyro,
        gyro_list_x,
        gyro_x_lines,
        gyro_list_y,
        gyro_y_lines,
        gyro_list_z,
        gyro_z_lines,
    ) = initialize_plot(
        ax_gyro, "gyro", sec, gyro_data["x"], gyro_data["y"], gyro_data["z"]
    )

    # 加速度
    (
        ax_accel,
        accel_list_x,
        accel_x_lines,
        accel_list_y,
        accel_y_lines,
        accel_list_z,
        accel_z_lines,
    ) = initialize_plot(
        ax_accel, "acceleration", sec, accel_data["x"], accel_data["y"], accel_data["z"]
    )

    # 速度(Initialize velocity is 0)
    (
        ax_vel,
        vel_list_x,
        vel_x_lines,
        vel_list_y,
        vel_y_lines,
        vel_list_z,
        vel_z_lines,
    ) = initialize_plot(ax_vel, "velocity", sec)

    # plotし続ける
    while True:
        # センサーデータ取得
        gyro_data = sensor.get_gyro_data()
        accel_data = sensor.get_accel_data()

        # For test
        # gyro_data = {'x': 0.1, 'y': 0.2, 'z': 0.3}
        # accel_data = {'x': 0.1, 'y': 0.2, 'z': 0.3}

        # データの更新
        sec += TIME_STEP

        gyro_list_x = np.roll(gyro_list_x, 1)
        gyro_list_x[0] = gyro_data["x"]
        gyro_list_y = np.roll(gyro_list_y, 1)
        gyro_list_y[0] = gyro_data["y"]
        gyro_list_z = np.roll(gyro_list_z, 1)
        gyro_list_z[0] = gyro_data["z"]

        accel_list_x = np.roll(accel_list_x, 1)
        accel_list_x[0] = accel_data["x"]
        accel_list_y = np.roll(accel_list_y, 1)
        accel_list_y[0] = accel_data["y"]
        accel_list_z = np.roll(accel_list_z, 1)
        accel_list_z[0] = accel_data["z"]

        vx = vel_list_x[0] + accel_data["x"] * TIME_STEP
        vel_list_x = np.roll(vel_list_x, 1)
        vel_list_x[0] = vx
        vy = vel_list_y[0] + accel_data["y"] * TIME_STEP
        vel_list_y = np.roll(vel_list_y, 1)
        vel_list_y[0] = vy
        vz = vel_list_z[0] + accel_data["z"] * TIME_STEP
        vel_list_z = np.roll(vel_list_z, 1)
        vel_list_z[0] = vz

        # グラフへデータの再セット
        gyro_x_lines.set_data(sec, gyro_list_x)
        gyro_y_lines.set_data(sec, gyro_list_y)
        gyro_z_lines.set_data(sec, gyro_list_z)

        accel_x_lines.set_data(sec, accel_list_x)
        accel_y_lines.set_data(sec, accel_list_y)
        accel_z_lines.set_data(sec, accel_list_z)

        vel_x_lines.set_data(sec, vel_list_x)
        vel_y_lines.set_data(sec, vel_list_y)
        vel_z_lines.set_data(sec, vel_list_z)

        # X軸の更新
        ax_gyro.set_xlim((sec.min(), sec.max()))
        ax_accel.set_xlim((sec.min(), sec.max()))
        ax_vel.set_xlim((sec.min(), sec.max()))

        print(
            "【角速度】 x:"
            + "%6.3f" % gyro_data["x"]
            + " y:"
            + "%6.3f" % gyro_data["y"]
            + " z:"
            + "%6.3f" % gyro_data["z"]
        )
        print(
            "【加速度】 x:"
            + "%6.3f" % accel_data["x"]
            + " y:"
            + "%6.3f" % accel_data["y"]
            + " z:"
            + "%6.3f" % accel_data["z"]
        )
        print("【速度】 x:" + "%6.3f" % vx + " y:" + "%6.3f" % vy + " z:" + "%6.3f" % vz)

        plt.pause(TIME_STEP)  # sleep時間（秒）


if __name__ == "__main__":
    plot_loop()
