# -*- encoding: utf-8 -*-
'''
@File    :   results_process.py
@Time    :   2025/03/10 10:20:26
@Author  :   wenminggong, AIMS, PolyU
@Version :   1.0
@Desc    :   plot positioning results from GNSS-SDR.
'''

import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
import argparse
import pandas as pd
from geopy.distance import geodesic


def plot_position_results(result_path:str, data_type:str):
    assert os.path.exists(result_path), "file path not existing!"
                
    with h5py.File(os.path.join(result_path, "pvt.mat"), 'r') as f:
        height = np.array(f["height"]) # [n, 1]
        latitude = np.array(f["latitude"])
        longitude = np.array(f["longitude"])
        vel_x = np.array(f["vel_x"])
        vel_y = np.array(f["vel_y"])
        vel_z = np.array(f["vel_z"])

    # print("estimated sample no.100: lat {}, long {}".format(latitude[99], longitude[99]))

    # 数据采样间隔
    sampling_step = 10
    n = latitude.shape[0]
    indices = np.arange(0, n, sampling_step)

    if data_type == "opensky":
        longitude_truth = 114.1713630049711
        latitude_truth = 22.328444770087565
    elif data_type == "urban":
        longitude_truth = 114.209101777778
        latitude_truth = 22.3198722

    # 采样数据（转换为1D数组）
    latitude_sampled = latitude[indices, 0]
    longitude_sampled = longitude[indices, 0]
    vel_x_sampled = vel_x[indices, 0]
    vel_y_sampled = vel_y[indices, 0]
    vel_z_sampled = vel_z[indices, 0]

    # 创建子图
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    # ------------------
    # 绘制位置散点图
    # ------------------
    scatter = ax1.scatter(longitude_sampled, latitude_sampled, 
                        c='blue', s=30, alpha=0.8, label='Estimated Positions')
    truth_point = ax1.scatter(longitude_truth, latitude_truth, 
                            c='red', s=300, marker='*', edgecolor='black', 
                            label='True Position', zorder=5)

    # 智能坐标轴范围调整
    lon_min = min(np.min(longitude_sampled), longitude_truth)
    lon_max = max(np.max(longitude_sampled), longitude_truth)
    lat_min = min(np.min(latitude_sampled), latitude_truth)
    lat_max = max(np.max(latitude_sampled), latitude_truth)

    lon_range = lon_max - lon_min if (lon_max - lon_min) != 0 else 0.0001
    lat_range = lat_max - lat_min if (lat_max - lat_min) != 0 else 0.0001

    ax1.set_xlim(lon_min - 0.1*lon_range, lon_max + 0.1*lon_range)
    ax1.set_ylim(lat_min - 0.1*lat_range, lat_max + 0.1*lat_range)

    ax1.set_xlabel("Longitude (degrees)", fontsize=10)
    ax1.set_ylabel("Latitude (degrees)", fontsize=10)
    ax1.set_title("Position Estimation Distribution", fontsize=12)
    ax1.legend(loc='best', fontsize=8)
    ax1.grid(True, linestyle='--', alpha=0.6)

    # ------------------
    # 绘制速度曲线图
    # ------------------
    line_width = 0.8
    ax2.plot(indices, vel_x_sampled, label='Velocity X', 
            linewidth=line_width, color='tab:blue')
    ax2.plot(indices, vel_y_sampled, label='Velocity Y', 
            linewidth=line_width, color='tab:orange')
    ax2.plot(indices, vel_z_sampled, label='Velocity Z', 
            linewidth=line_width, color='tab:green')

    ax2.set_xlabel("Sampled Data Index", fontsize=10)
    ax2.set_ylabel("Velocity (m/s)", fontsize=10)
    ax2.set_title("Velocity Components Variation", fontsize=12)
    ax2.legend(loc='best', fontsize=8)
    ax2.grid(True, linestyle='--', alpha=0.6)

    # 自动调整刻度密度
    ax2.xaxis.set_major_locator(plt.MaxNLocator(6))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(6))

    # plot error
    truth_pos = (latitude_truth, longitude_truth)
    estimated_poses = list(zip(latitude_sampled, longitude_sampled))
    pos_errors = np.array([geodesic(estimated_pos, truth_pos).meters for estimated_pos in estimated_poses]).reshape(-1, 1)
    ax3.plot(indices, pos_errors, label='Pos Error', color='tab:blue')
    ax3.set_xlabel("Sampled Data Index", fontsize=10)
    ax3.set_ylabel("Pos error (m)", fontsize=10)
    ax3.set_title("Pos Error Variation", fontsize=12)
    ax3.legend(loc='best', fontsize=8)
    ax3.grid(True, linestyle='--', alpha=0.6)

    # 自动调整刻度密度
    ax3.xaxis.set_major_locator(plt.MaxNLocator(6))
    ax3.yaxis.set_major_locator(plt.MaxNLocator(6))

    # 调整布局
    plt.tight_layout(pad=3.0)
    plt.savefig(os.path.join(result_path, "{}_results.png".format(data_type)))
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--result_path", type=str, default="results/wls/opensky", help="wls results path.")
    parser.add_argument("--data_type", type=str, default="opensky", help="data type.")
    args = parser.parse_args()

    # with h5py.File(os.path.join(args.result_path, "pvt.mat"), 'r') as f:
    #     for key in f.keys():
    #         print("{}: {}, shape: {}".format(key, np.array(f[key]), np.array(f[key]).shape))

    plot_position_results(args.result_path, args.data_type)