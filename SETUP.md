# Git & GitHub SSH 绑定配置记录

> 日期：2026-06-27
> 系统：Windows 11 Pro
> 用户：Administrator

## 一、环境检查

```bash
git --version
# 输出：git version 2.47.1.windows.2
```

Git 已预装，无需额外下载。

## 二、全局用户信息配置

```bash
git config --global user.name "Patato-1"
git config --global user.email "y7kyfbvvtd@privaterelay.appleid.com"
```

## 三、SSH 密钥生成

为 GitHub 单独生成专用密钥，便于将来区分多个账号。

```bash
mkdir -p ~/.ssh
ssh-keygen -t ed25519 -C "y7kyfbvvtd@privaterelay.appleid.com" \
  -f ~/.ssh/github_ed25519 -N ""
```

生成的密钥对：

| 文件 | 用途 |
|------|------|
| `~/.ssh/github_ed25519` | 私钥（不要泄露，不要提交） |
| `~/.ssh/github_ed25519.pub` | 公钥（需上传到 GitHub） |

## 四、公钥添加到 GitHub

1. 打开 https://github.com/settings/keys
2. 点击 **New SSH key**
3. 填写 Title（如 `Administrator-PC`）
4. 粘贴 `github_ed25519.pub` 的完整内容
5. 点击 **Add SSH key** 完成添加

## 五、SSH Config 配置

为了让 `git@github.com` 自动使用专用密钥，创建 `~/.ssh/config`：

```
# GitHub
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/github_ed25519
    IdentitiesOnly yes
```

## 六、连接验证

```bash
ssh -T git@github.com
```

成功输出：

```
Hi Patato-1! You've successfully authenticated, but GitHub does not provide shell access.
```

## 七、常用命令

```bash
# 克隆仓库
git clone git@github.com:Patato-1/PatatoPLAY.git

# 添加远程
git remote add origin git@github.com:Patato-1/PatatoPLAY.git

# 首次推送
git push -u origin master

# 后续推送
git push
```