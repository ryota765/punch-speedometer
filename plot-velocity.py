from mpu6050 import mpu6050

import numpy as np
import matplotlib.pyplot as plt

sensor = mpu6050(0x68)

TIME_STEP = 0.1

def initialize_plot(ax, title, sec, x0=0, y0=0, z0=0):
    x_list = np.zeros(sec.size)
    x_list[0] = x0
    (x_lines,) = ax.plot(sec, x_list, color="red", label="x")

    y_list = np.zeros(sec.size)
    y_list[0] = y0
    (y_lines,) = ax.plot(sec, y_list, color="blue", label="y")

    z_list = np.zeros(sec.size)
    z_list[0] = z0
    (z_lines,) = ax.plot(sec, z_list, color="green", label="z")

    ax.legend()
    ax.set_title(title)
    ax.set_ylim(-30, 30)
    ax.set_xticks([])

    return ax, x_list, x_lines, y_list, y_lines, z_list, z_lines


def main():
    # Fetch sensor data
    # temp = "%4.1f" % sensor.get_temp()
    # gyro_data = sensor.get_gyro_data()
    accel_data = sensor.get_accel_data()

    fig, (ax_accel, ax_vel) = plt.subplots(ncols=2, figsize=(10, 7))

    # x-axis
    sec = np.arange(0, 1, TIME_STEP)

    # Acceleration [m/s^2]
    (
        ax_accel,
        accel_list_x,
        accel_x_lines,
        accel_list_y,
        accel_y_lines,
        accel_list_z,
        accel_z_lines,
    ) = initialize_plot(
        ax_accel, "acceleration [m/s^2]", sec, accel_data["x"], accel_data["y"], accel_data["z"]
    )

    # Velocity [m/s] (Initialize velocity is 0)
    (
        ax_vel,
        vel_list_x,
        vel_x_lines,
        vel_list_y,
        vel_y_lines,
        vel_list_z,
        vel_z_lines,
    ) = initialize_plot(ax_vel, "velocity [m/s]", sec)

    while True:
        # Fetch sensor data
        accel_data = sensor.get_accel_data()

        # Update data
        sec += TIME_STEP

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

        # Update plot
        accel_x_lines.set_data(sec, accel_list_x)
        accel_y_lines.set_data(sec, accel_list_y)
        accel_z_lines.set_data(sec, accel_list_z)

        vel_x_lines.set_data(sec, vel_list_x)
        vel_y_lines.set_data(sec, vel_list_y)
        vel_z_lines.set_data(sec, vel_list_z)

        # Update x-axis
        ax_accel.set_xlim((sec.min(), sec.max()))
        ax_vel.set_xlim((sec.min(), sec.max()))

        print(
            "acceleration x:"
            + "%6.3f" % accel_data["x"]
            + " y:"
            + "%6.3f" % accel_data["y"]
            + " z:"
            + "%6.3f" % accel_data["z"]
        )
        print("velocity x:" + "%6.3f" % vx + " y:" + "%6.3f" % vy + " z:" + "%6.3f" % vz)

        plt.pause(TIME_STEP)  # sleep time (seconds)


if __name__ == "__main__":
    main()
