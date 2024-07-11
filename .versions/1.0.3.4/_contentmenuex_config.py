from mysupport.WindowContentMenuEx.configer import asconfig

@asconfig
def 添加Workspace():
    prefix = "Workspace"
    
    return dict(locals())

@asconfig
def 整理文件夹():
    limit = 10
    archive_path = r"E:\工作文件\Workspaces"

    return dict(locals())
