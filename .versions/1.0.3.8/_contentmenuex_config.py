from mysupport.WindowContentMenuEx.configer import asconfig

nametypes = [
    {'nametype':"PrefixYYYY-MM-DD","template":"【Prefix】【YYYY】-【MM】-【DD】"}
    {'nametype':"PrefixYYYY-MM-X","template":"【Prefix】【YYYY】-【MM】-【X】"}
    {'nametype':"PrefixYYYY-X","template":"【Prefix】【YYYY】-【X】"}
]

@asconfig
def 添加Workspace():
    prefix = "Workspace"
    
    return dict(locals())

@asconfig
def 整理文件夹():
    limit = 10
    archive_path = r"E:\工作文件\Workspaces"

    return dict(locals())
