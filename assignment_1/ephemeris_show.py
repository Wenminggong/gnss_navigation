# -*- encoding: utf-8 -*-
'''
@File    :   ephemeris_show.py
@Time    :   2025/03/10 22:05:02
@Author  :   wenminggong, AIMS, PolyU
@Version :   1.0
@Desc    :   extract the ephemeris data.
'''


import xml.etree.ElementTree as ET
import pandas as pd
import argparse
import os


def ephemeris_extract(result_path: str):

    # 解析XML文件
    tree = ET.parse(os.path.join(result_path, 'gps_ephemeris.xml'))
    root = tree.getroot()

    # 创建字典来存储所有卫星的数据
    data = {}

    # 遍历每个<item>元素
    for item in root.findall('.//item'):
        # 获取卫星的PRN号，从<second>下的<PRN>标签中获取
        second = item.find('second')
        prn = second.find('PRN').text
        
        # 提取该卫星的所有星历参数到字典中
        satellite_params = {}
        for elem in second:
            param_name = elem.tag
            param_value = elem.text.strip() if elem.text else ''
            satellite_params[param_name] = param_value
        
        # 将当前卫星的数据存入总数据字典中，键为PRN
        data[prn] = satellite_params

    # 转换为DataFrame，并转置使行是参数，列是PRN
    df = pd.DataFrame.from_dict(data, orient='index').transpose()

    # 保存到CSV文件
    df.to_csv(os.path.join(result_path, 'satellite_ephemeris.csv'), index_label='Parameter')
    df.to_html(os.path.join(result_path, 'satellite_ephemeris.html'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--result_path", type=str, default="results/decode/opensky", help="ephemeris path.")
    args = parser.parse_args()

    ephemeris_extract(args.result_path)