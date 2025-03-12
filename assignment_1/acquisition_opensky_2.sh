#!/bin/bash

# 循环设置卫星编号 n=1 到 32
for n in {1..32}; do
    # 1. 修改配置文件中的卫星编号
    echo "new instance."
    sed -i "s/^Channel0\.satellite=.*/Channel0.satellite=${n}/" assignment_1_gnss_sdr_opensky.conf

    # 2. 运行 GNSS-SDR 实验
    gnss-sdr --config_file=./assignment_1_gnss_sdr_acq_opensky.conf --log_dir=./log/opensky

    wait

    # 3. 清理 urban 目录中除 result_1_${n}.mat 外的其他结果文件
    cd results/acquisition/opensky || exit  # 进入 urban 目录，失败则退出
    
    # 获取所有匹配的文件
    files=(acquisition_opensky_G_1C_ch_0_*_sat_${n}.mat)

    # 如果没有匹配的文件，退出脚本
    if [ ${#files[@]} -eq 0 ]; then
    echo "no find matching files."
    fi

    # 找到*值最大的文件
    max_file=""
    max_num=0

    for file in "${files[@]}"; do
        # 提取*的值
        num=$(echo "$file" | grep -oP "(?<=acquisition_opensky_G_1C_ch_0_)\d+(?=_sat_${n}\.mat)")
        
        # 比较并更新最大值
        if [ "$num" -gt "$max_num" ]; then
            max_num=$num
            max_file=$file
        fi
    done

    # 删除除了最大值文件之外的其他文件
    for file in "${files[@]}"; do
        if [ "$file" != "$max_file" ]; then
            rm "$file"
            echo "removed file: $file"
        fi
    done

    cd ..  # 返回上级目录
    cd ..
    cd ..
done

echo "All experiments completed and redundant files cleaned."