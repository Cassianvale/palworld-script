#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import configparser
import shutil
import time
import datetime
import os
import codecs

# 读取配置文件
config = configparser.ConfigParser()
with codecs.open('config.ini', 'r', encoding='utf-8-sig') as f:
    config.read_file(f)
backup_source = config.get('Settings', 'backup_source')
backup_interval_hours = config.get('Settings', 'backup_interval_hours')


# 备份任务
def backup_task():

    # 在当前目录下创建名为Backup的文件夹
    backup_dir = './Backup'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # 如果备份间隔不为空，则执行备份
    if backup_interval_hours:
        backup_interval = float(backup_interval_hours) * 3600  # 将备份间隔转换为秒
        print("\n自动备份已开启，正在进行备份......")
        
        while True:
            datetime_now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

            # 备份文件
            shutil.copytree(backup_source, os.path.join(backup_dir, f"Saved_{datetime_now}"))
            time.sleep(1)
            print("备份成功，文件名为：Saved_" + datetime_now)

            # 显示倒计时并等待指定的备份间隔
            for i in range(int(backup_interval), 0, -1):
                print(f'\r下一次备份将在 {i} 秒后开始...', end='')
                time.sleep(1)
    else:
        print("自动备份未开启，需要自动备份请需改config.ini配置")


if __name__ == '__main__':
    backup_task()
