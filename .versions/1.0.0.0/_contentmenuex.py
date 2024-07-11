import datetime
import os
import PySimpleGUI as sg
import _contentmenuex_config as _config

menu = list[tuple]()


@_config.add_workspace
def add_workspace(path: str, config):
    projectname = sg.popup_get_text("输入项目名称")
    if projectname == None:
        return
    now = datetime.datetime.now()
    if projectname == "":
        name = "%s%s" % (config['prefix'], now.strftime(r"%Y-%m-%d"))
    else:
        name = "%s%s（%s）" % (
            config['prefix'], now.strftime(r"%Y-%m-%d"), projectname)
    if os.path.exists(name):
        sg.popup_error("创建失败", "文件夹已存在")
        return
    os.mkdir(name)

menu = [
    ("添加Workspace", add_workspace),
]
