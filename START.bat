@echo off
chcp 65001 >nul
title PLAY.py Launcher

:: 后台启动自动同步
start "GitHub Auto Sync" /min cmd /c "cd /d C:\Users\Administrator\Desktop\pythonPLAY && auto_sync.bat"

echo ✅ GitHub 自动同步已在后台启动
echo 📄 正在打开 PLAY.py...

:: 用 Python 运行 PLAY.py
"C:\Users\Administrator\AppData\Local\Programs\Python\Python314\python.exe" "C:\Users\Administrator\Desktop\pythonPLAY\PLAY.py"

:: PLAY.py 关闭后，结束同步进程
taskkill /fi "WINDOWTITLE eq GitHub Auto Sync*" /f >nul 2>&1

echo 🔴 PLAY.py 已关闭，同步已停止。
timeout /t 2 >nul
