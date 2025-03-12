# -*- encoding: utf-8 -*-
'''
@File    :   results_process.py
@Time    :   2025/03/10 10:20:26
@Author  :   wenminggong, AIMS, PolyU
@Version :   1.0
@Desc    :   plot multi positioning results in a figure.
'''

import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
import argparse


def com_plot_position_results(algo_1:str, algo_2:str, data_type:str):
    result_path_1 = os.path.join("results", algo_1, data_type)
    result_path_2 = os.path.join("results", algo_2, data_type)
    assert os.path.exists(result_path_1) and os.path.exists(result_path_2), "file pathes not existing!"
                
    with h5py.File(os.path.join(result_path_1, "pvt.mat"), 'r') as f:
        latitude_1 = np.array(f["latitude"])
        longitude_1 = np.array(f["longitude"])
    with h5py.File(os.path.join(result_path_2, "pvt.mat"), 'r') as f:
        latitude_2 = np.array(f["latitude"])
        longitude_2 = np.array(f["longitude"])

    # 数据采样间隔
    sampling_step = 10
    n_1 = latitude_1.shape[0]
    indices_1 = np.arange(0, n_1, sampling_step)
    # 采样数据（转换为1D数组）
    latitude_sampled_1 = latitude_1[indices_1, 0]
    longitude_sampled_1 = longitude_1[indices_1, 0]

    n_2 = latitude_2.shape[0]
    indices_2 = np.arange(0, n_2, sampling_step)
    # 采样数据（转换为1D数组）
    latitude_sampled_2 = latitude_2[indices_2, 0]
    longitude_sampled_2 = longitude_2[indices_2, 0]

    if data_type == "opensky":
        longitude_truth = 114.1713630049711
        latitude_truth = 22.328444770087565
    elif data_type == "urban":
        longitude_truth = 114.209101777778
        latitude_truth = 22.3198722

    # 创建子图
    fig, (ax1) = plt.subplots(1, 1, figsize=(8, 6))

    # ------------------
    # 绘制位置散点图
    # ------------------
    scatter = ax1.scatter(longitude_sampled_1, latitude_sampled_1, 
                        c='blue', s=30, alpha=0.8, label='Estimated Positions from {}'.format(algo_1))
    scatter = ax1.scatter(longitude_sampled_2, latitude_sampled_2, 
                        c='orange', s=30, alpha=0.8, label='Estimated Positions from {}'.format(algo_2))
    truth_point = ax1.scatter(longitude_truth, latitude_truth, 
                            c='red', s=300, marker='*', edgecolor='black', 
                            label='True Position', zorder=5)

    ax1.set_xlabel("Longitude (degrees)", fontsize=10)
    ax1.set_ylabel("Latitude (degrees)", fontsize=10)
    ax1.set_title("Position Estimation Distribution between {} and {}".format(algo_1, algo_2), fontsize=12)
    ax1.legend(loc='best', fontsize=8)
    ax1.grid(True, linestyle='--', alpha=0.6)

    # 调整布局
    plt.tight_layout(pad=3.0)
    plt.savefig(os.path.join(result_path_2, "com_{}_results.png".format(data_type)))
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo_1", type=str, default="wls", help="algorithm 1.")
    parser.add_argument("--algo_2", type=str, default="ekf", help="algorithm 2.")
    parser.add_argument("--data_type", type=str, default="opensky", help="data type.")
    args = parser.parse_args()

    com_plot_position_results(args.algo_1, args.algo_2, args.data_type)