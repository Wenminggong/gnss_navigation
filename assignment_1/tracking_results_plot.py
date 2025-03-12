# -*- encoding: utf-8 -*-
'''
@File    :   results_process.py
@Time    :   2025/03/10 10:20:26
@Author  :   wenminggong, AIMS, PolyU
@Version :   1.0
@Desc    :   plot tracking results from GNSS-SDR.
'''

import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
import argparse
import pandas as pd
from scipy.interpolate import interp1d


def plot_tracking_results(result_path:str, data_type:str, channel:int, sample_num:int):
    assert os.path.exists(result_path), "file path not existing!"


    with h5py.File(os.path.join(result_path, "track_{}{}.mat".format(data_type, channel)), 'r') as f:          
        prn_sample_starts = np.array(f["PRN_start_sample_count"])
        prns = np.array(f["PRN"])
        abs_Es = np.array(f["abs_E"])
        abs_Ps = np.array(f["abs_P"])
        abs_Ls = np.array(f["abs_L"])

    # 创建子图
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 4))

    ax1.plot(prn_sample_starts, abs_Es, label='Early (E)', marker='o', linestyle='-', color='blue')
    ax1.plot(prn_sample_starts, abs_Ps, label='Prompt (P)', marker='s', linestyle='-', color='green')
    ax1.plot(prn_sample_starts, abs_Ls, label='Late (L)', marker='^', linestyle='-', color='red')

    # 添加标题和标签
    ax1.set_title('DLL Correlation Results of Tracking PRN {}'.format(prns[-1]))
    ax1.set_xlabel('Sample Index')
    ax1.set_ylabel('Correlation Magnitude')
    ax1.legend()
    ax1.grid(True)


    E_L_diff = abs_Es - abs_Ls
    # 绘制 E 和 L 的差值图
    ax2.plot(prn_sample_starts, E_L_diff, label='E-L Difference', marker='x', linestyle='-', color='purple')

    # 添加标题和标签
    ax2.set_title('DLL Tracking Performance: E-L Difference of Tracking PRN {}'.format(prns[-1]))
    ax2.set_xlabel('Sample Index')
    ax2.set_ylabel('E-L Difference')
    ax2.legend()
    ax2.grid(True)

    sample_indexs = range(0, len(prn_sample_starts), len(prn_sample_starts)//(sample_num+10)) 
    chip_offsets = np.array([-0.5, 0, 0.5])  # 单位：chip

    for sample_index in sample_indexs[5:-5]:
        correlation_values = np.array([
            abs_Es[sample_index, 0],
            abs_Ps[sample_index, 0],
            abs_Ls[sample_index, 0],
        ])

        # 插值生成完整的相关函数
        interp_func = interp1d(chip_offsets, correlation_values, kind='linear', fill_value='extrapolate')
        chip_offsets_interp = np.linspace(-0.5, 0.5, 20)  # 插值范围：-1 chip 到 +1 chip
        correlation_values_interp = interp_func(chip_offsets_interp)
        
        # 绘制相关函数
        ax3.plot(chip_offsets_interp, correlation_values_interp)
        ax3.scatter(chip_offsets, correlation_values, color='red')

    ax3.axvline(x=-0.5, color='green', linestyle='--', label='Early (E)')
    ax3.axvline(x=0, color='orange', linestyle='--', label='Prompt (P)')
    ax3.axvline(x=0.5, color='purple', linestyle='--', label='Late (L)')

    # 添加标题和标签
    ax3.set_title('Correlation Function of Tracking PRN {}'.format(prns[-1]))
    ax3.set_xlabel('Code Phase Offset (chips)')
    ax3.set_ylabel('Correlation Magnitude')
    ax3.legend()
    ax3.grid(True)

    # 显示图形
    plt.tight_layout(pad=3.0)
    plt.savefig(os.path.join(result_path, "correlation_results.png"))
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--result_path", type=str, default="results/tracking/opensky", help="tracking results path.")
    parser.add_argument("--data_type", type=str, default="opensky", help="data type.")
    parser.add_argument("--channel", type=int, default=0, help="determine tracking channel to plot.")
    parser.add_argument("--sample_num", type=int, default=10, help="sample number for ploting correction function.")
    args = parser.parse_args()


    plot_tracking_results(args.result_path, args.data_type, args.channel, args.sample_num)