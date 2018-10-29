#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : savecsv.py
# @Author: Lyn
# @Date  : 2018/10/27
# @Desc  :
import csv
import pandas as pd

def save_csv(list):
    fileHeader = ["高管姓名","性别","年龄","股票代码","职位"]

    # info = pd.DataFrame(columns=title, data=list)
    # info.to_csv('executive_prep.csv', 'a')

    csvFile = open("executive_prep.csv", "w",encoding='utf8')
    writer = csv.writer(csvFile)
    writer.writerow(fileHeader)
    writer.writerow(list)


