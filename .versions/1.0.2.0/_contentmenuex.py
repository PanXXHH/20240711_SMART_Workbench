import datetime
import os
import PySimpleGUI as sg
import _contentmenuex_config as _config
import glob
import shutil
from mysupport.Pather.Pather3 import Pather


menu = list[tuple]()

import subprocess

def explore(dir):
    subprocess.run('explorer %s' % dir)


@_config.添加Workspace
def 添加Workspace(path: str, config):
    projectname = sg.popup_get_text("输入项目名称")
    if projectname == None:
        return
    now = datetime.datetime.now()
    if projectname == "":
        projectname = "%s%s" % (config['prefix'], now.strftime(r"%Y-%m-%d"))
    else:
        projectname = "%s%s（%s）" % (
            config['prefix'], now.strftime(r"%Y-%m-%d"), projectname)
    filename = Pather(path)(projectname)
    if filename.exists():
        sg.popup_error("创建失败", "文件夹已存在")
        explore(filename.str())
        return
    
    os.mkdir(filename.str())


# 使用装饰器将函数指定为整理文件夹的功能
@_config.整理文件夹
def 整理文件夹(path: str, config: dict):
    # 指定存档路径，如果不存在则创建
    archive_path = config["archive_path"]
    os.makedirs(archive_path, exist_ok=True)

    # 使用glob.glob获取路径下所有以"Workspace"开头的文件夹
    workspace_folders = [folder for folder in glob.glob(
        os.path.join(path, 'Workspace*')) if os.path.isdir(folder)]

    # 按照文件夹的最后修改时间进行排序
    workspace_folders.sort(
        key=lambda folder: os.path.getmtime(folder), reverse=True)

    print(workspace_folders)

    # 如果文件夹数量小于或等于配置中指定的上限，则不进行操作
    if len(workspace_folders) <= config["limit"]:
        sg.popup("当前文件夹不需要整理", font="微软雅黑")
        return

    # 从已排序的文件夹列表中，取出超过限制数量的文件夹，进行整理
    folders_to_move = workspace_folders[config["limit"]:]

    # 遍历要移动的文件夹，获取每个文件夹的基本名称，并将其移动到存档路径
    for folder in folders_to_move:
        folder_name = os.path.basename(folder)
        shutil.move(folder, os.path.join(archive_path, folder_name))

    # 弹出提示框，显示移动文件夹的数量和目标路径
    sg.popup(f"成功移动{len(folders_to_move)}个文件至{archive_path}", font="微软雅黑")


menu = [
    ("添加Workspace", 添加Workspace),
    ("整理文件夹", 整理文件夹),
    ("添加工作文件并整理文件夹", lambda path:(添加Workspace(path), 整理文件夹(path))),
]

添加Workspace(f"E:\工作台")
