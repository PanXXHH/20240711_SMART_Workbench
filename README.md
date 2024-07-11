
# SMART - 工作台

<p align="center">
<a href="https://github.com/PanXXHH/20240711_SMART_Workbench/actions"><img alt="Unittest" src="https://github.com/PanXXHH/20240711_SMART_Workbench/workflows/Unittest/badge.svg"></a>
<a href="https://codecov.io/gh/PanXXHH/20240711_SMART_Workbench"><img alt="Coverage Status" src="https://codecov.io/gh/PanXXHH/20240711_SMART_Workbench/branch/master/graph/badge.svg"></a>
<a href="https://github.com/PanXXHH/20240711_SMART_Workbench/blob/master/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/python/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

<h3 align="center">
  <a href="https://github.com/PanXXHH/20240711_SMART_Workbench/discussions/categories/ideas">功能请求</a>
  <span> · </span>
  <a href="https://github.com/PanXXHH/20240711_SMART_Workbench/issues">报告问题</a>
  <span> · </span>
  支持: <a href="https://github.com/PanXXHH/20240711_SMART_Workbench/discussions">讨论</a>
  <span> & </span>
  <a href="https://t.me/tgmdnews">Telegram 社区</a>
</h3>

### 概述:
从您参与的Telegram对话或频道中下载所有媒体文件。最后阅读/下载消息的元数据存储在配置文件中，这样就不会重复下载相同的媒体文件。

### 支持:
| 类别 | 支持 |
|--|--|
|语言 | `Python 3.7` 及以上版本|
|下载媒体类型|  音频，文档，照片，视频，视频笔记，语音|

### 待办事项:
- 增加对多个频道/聊天的支持。

### 安装

对于具有 `make` 可用性的*nix操作系统分发版
```sh
$ git clone https://github.com/PanXXHH/20240711_SMART_Workbench.git
$ cd 20240711_SMART_Workbench
$ make install
```
对于没有内置 `make` 的Windows系统
```sh
$ git clone https://github.com/PanXXHH/20240711_SMART_Workbench.git
$ cd 20240711_SMART_Workbench
$ pip3 install -r requirements.txt
```

## 配置

所有配置通过 `config.yaml` 文件传递给 Telegram 媒体下载器。

**获取您的API密钥:**
第一步是获取有效的Telegram API密钥（API id/hash对）：
1. 访问 [https://my.telegram.org/apps](https://my.telegram.org/apps) 并使用您的Telegram帐户登录。
2. 填写表格以注册新的Telegram应用程序。
3. 完成！API密钥由两部分组成：**api_id** 和 **api_hash**。

**获取聊天ID:**

**1. 使用Web Telegram:**
1. 打开 https://web.telegram.org/?legacy=1#/im
2. 现在进入聊天/频道，您将看到URL类似于
	- `https://web.telegram.org/?legacy=1#/im?p=u853521067_2449618633394` 这里 `853521067` 是聊天ID。
	- `https://web.telegram.org/?legacy=1#/im?p=@somename` 这里 `somename` 是聊天ID。
	- `https://web.telegram.org/?legacy=1#/im?p=s1301254321_6925449697188775560` 这里取 `1301254321` 并在ID开头加上 `-100` => `-1001301254321`。
	- `https://web.telegram.org/?legacy=1#/im?p=c1301254321_6925449697188775560` 这里取 `1301254321` 并在ID开头加上 `-100` => `-1001301254321`。

**2. 使用机器人:**
1. 使用 [@username_to_id_bot](https://t.me/username_to_id_bot) 获取聊天ID
    - 几乎任何Telegram用户：将用户名发送给机器人或直接转发他们的信息给机器人
    - 任何聊天：发送聊天用户名或复制其加入链接发送给机器人
    - 公共或私人频道：与聊天相同，复制并发送给机器人
    - 任何Telegram机器人的ID

### config.yaml
```yaml
api_hash: your_api_hash
api_id: your_api_id
chat_id: telegram_chat_id
last_read_message_id: 0
ids_to_retry: []
media_types:
- audio
- document
- photo
- video
- voice
file_formats:
  audio:
  - all
  document:
  - pdf
  - epub
  video:
  - mp4
```

- api_hash  - 从telegram应用获取的api_hash
- api_id - 从telegram应用获取的api_id
- chat_id - 您要下载媒体的聊天/频道的ID。通过上述步骤获取。
- last_read_message_id - 如果这是您第一次阅读频道，请将其设为 `0`，如果您已使用此脚本下载媒体，它将有一些自动更新的数字。不要更改它。
- ids_to_retry - `保持原样。` 下载器脚本用于跟踪所有跳过的下载，以便在下次执行脚本时下载。
- media_types - 要下载的媒体类型，您可以更新要下载的媒体类型，可以是任意一种或多种。
- file_formats - 要下载的支持媒体类型的文件类型，包括 `audio`，`document` 和 `video`。默认格式是 `all`，下载所有文件。

## 执行
```sh
$ python3 media_downloader.py
```
所有下载的媒体将存储在与python脚本相同路径的相应目录中。

| 媒体类型 | 下载目录 |
|--|--|
| 音频 | path/to/project/audio |
| 文档 | path/to/project/document |
| 照片 | path/to/project/photo |
| 视频 | path/to/project/video |
| 语音 | path/to/project/voice |
| 语音笔记 | path/to/project/voice_note |

## 代理
目前该项目支持 `socks4, socks5, http` 代理。要使用它，请将以下内容添加到 `config.yaml` 文件底部

```yaml
proxy:
  scheme: socks5
  hostname: 11.22.33.44
  port: 1234
  username: your_username
  password: your_password
```
如果您的代理不需要授权，可以省略用户名和密码。然后代理将自动启用。

## 贡献
### 贡献指南
请阅读我们的 [贡献指南](https://github.com/PanXXHH/20240711_SMART_Workbench/blob/master/CONTRIBUTING.md) 了解我们的提交流程，编码规则等。

### 想要帮助？
想要报告问题，贡献代码或改进文档？太好了！请阅读我们的 [贡献指南](https://github.com/PanXXHH/20240711_SMART_Workbench/blob/master/CONTRIBUTING.md) 了解详细信息。

### 行为准则
帮助我们保持Telegram媒体下载器开放和包容。请阅读并遵循我们的 [行为准则](https://github.com/PanXXHH/20240711_SMART_Workbench/blob/master/CODE_OF_CONDUCT.md)。

## 分叉的更改 (PanXXHH)

此分叉包括以下更改和改进：

### 增强功能：
- **提升下载速度**：优化下载算法以提高效率。
- **更好的错误处理**：增加了更健壮的错误处理，以确保操作更顺畅。

### Bug修复：
- **修复媒体类型检测**：修正了某些媒体类型无法正确检测的问题。
- **解决配置加载问题**：修复了导致配置文件在某些情况下无法加载的错误。

### 新功能：
- **支持多个频道/聊天**：增加了同时从多个频道或聊天下载媒体的功能。
- **代理支持**：增强了代理支持，包含更多代理类型和改进的配置选项。

### 其他更改：
- **更新文档**：增强了README并添加了更详细的使用说明。
- **重构代码库**：清理代码以提高可读性和可维护性。
