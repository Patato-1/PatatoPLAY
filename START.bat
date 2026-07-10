@echo off
chcp 65001 >nul
title GitHub Auto Sync

echo ==========================================
echo    GitHub 自动同步
echo    PyCharm + 实时推送
echo ==========================================
echo.

:: 后台启动自动同步
start "GitHub Auto Sync" /min cmd /c "cd /d C:\Users\Administrator\Desktop\pythonPLAY && auto_sync.bat"

echo ✅ 自动同步已启动（后台运行）
echo 📂 正在用 PyCharm 打开 PLAY.py...
echo.
echo ⚠️  关闭此窗口即可停止同步

:: 用 PyCharm 打开 PLAY.py
start "" "C:\Program Files\JetBrains\PyCharm 2026.1.3\bin\pycharm64.exe" "C:\Users\Administrator\Desktop\pythonPLAY\PLAY.py"

:: 保持窗口，按任意键停止同步
pause >nul

:: 停止同步进程
taskkill /fi "WINDOWTITLE eq GitHub Auto Sync*" /f >nul 2>&1
echo 🔴 同步已停止。
timeout /t 2 >nul
