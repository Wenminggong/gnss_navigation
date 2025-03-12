# -*- encoding: utf-8 -*-
'''
@File    :   results_process.py
@Time    :   2025/03/09 11:29:26
@Author  :   wenminggong, AIMS, PolyU
@Version :   1.0
@Desc    :   plot acquisition results from GNSS-SDR.
'''

import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
import argparse
import pandas as pd


def plot_acquisition_results(result_path:str, data_type:str):
    assert os.path.exists(result_path), "file path not existing!"

    acq_prns = []
    acq_test_statistic = []
    acq_threshold = []
    acq_doppler_hz = []
    acq_positive = []
    acq_delay_samples = []
    for file_name in os.listdir(result_path):
        if file_name.startswith("acquisition_"+data_type):
            with h5py.File(os.path.join(result_path, file_name), 'r') as f:
                acq_prns.append(np.array(f["PRN"])[0])
                acq_test_statistic.append(np.array(f["test_statistic"])[0])
                acq_threshold.append(np.array(f["threshold"])[0])
                acq_doppler_hz.append(np.array(f["acq_doppler_hz"])[0])
                acq_positive.append(np.array(f["d_positive_acq"])[0])
                acq_delay_samples.append(np.array(f["acq_delay_samples"])[0])

    print("[Acquisition Results] Estimated Doppler Frequency (PRN, doppler_hz): {}".format(list(zip(acq_prns, acq_doppler_hz))))
    print("[Acquisition Results] Code Phase (PRN, acq_delay_samples): {}".format(list(zip(acq_prns, acq_delay_samples))))
    print("[Acquisition Results] Threshold (PRN, threshold): {}".format(list(zip(acq_prns, acq_threshold))))

    data = {
        "data": [data_type, data_type],
        "item": ["doppler freq", "code phase"],
        **{f"PRN {i}": [acq_doppler_hz[acq_prns.index(i)], acq_delay_samples[acq_prns.index(i)]] for i in range(1, 33)}
    }

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(result_path, "results.csv"), index=False)
    df.to_html(os.path.join(result_path, "results.html"), index=False)

    # 设置颜色：超过阈值为绿色，低于阈值为红色
    colors = ['red' if test_statistic > acq_threshold[0] else 'green' for test_statistic in acq_test_statistic]

    # 创建柱状图
    plt.figure(figsize=(16, 8))
    bars = plt.bar(acq_prns, acq_test_statistic, color=colors)

    # 绘制阈值线
    plt.axhline(y=acq_threshold[0], color='blue', linestyle='--', label=f'Threshold ({acq_threshold[0]})')

    # 在每个柱子上方标注值
    for bar in bars:
        height = round(bar.get_height(), 2)
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', 
                ha='center', va='bottom', fontsize=6)

    # 添加标题和标签
    plt.title('Acquisition Results.', fontsize=14)
    plt.xlabel('Satellite PRNs', fontsize=12)
    plt.ylabel('Test Statistic', fontsize=12)
    plt.legend()
    plt.savefig(os.path.join(result_path, "acquisition_results.png"))

    # 显示图形
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--result_path", type=str, default="results/acquisition/opensky", help="acquisition results path.")
    parser.add_argument("--data_type", type=str, default="opensky", help="data type.")
    args = parser.parse_args()

    plot_acquisition_results(args.result_path, args.data_type)