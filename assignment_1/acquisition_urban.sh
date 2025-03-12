#!/bin/bash

# 循环设置卫星编号 n=1 到 32
for n in {3..32}; do
    # 1. 修改配置文件中的卫星编号
    echo "new instance."
    sed -i "s/^Channel0\.satellite=.*/Channel0.satellite=${n}/" assignment_1_gnss_sdr_urban.conf

    # 2. 运行 GNSS-SDR 实验
    gnss-sdr --config_file=./assignment_1_gnss_sdr_urban.conf --log_dir=./log/urban

    wait

    # 3. 清理 urban 目录中除 result_1_${n}.mat 外的其他结果文件
    cd results/urban || exit  # 进入 urban 目录，失败则退出
    # 删除所有符合 result_*_${n}.mat 但不等于 result_1_${n}.mat 的文件
    find . -type f -name "acquisition_urban_G_1C_ch_0_*_sat_${n}.mat" ! -name "acquisition_urban_G_1C_ch_0_1_sat_${n}.mat" -delete
    cd ..  # 返回上级目录
    cd ..
done

echo "All experiments completed and redundant files cleaned."