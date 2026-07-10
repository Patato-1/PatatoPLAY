@echo off
chcp 65001 >nul
title GitHub Auto Sync - pythonPLAY
color 0A

echo ========================================
echo    GitHub 自动同步脚本
echo    监控目录: pythonPLAY
echo    目标仓库: Patato-1/PatatoPLAY
echo ========================================
echo.

cd /d "C:\Users\Administrator\Desktop\pythonPLAY"

:loop
:: 检查是否有文件变化
git status --porcelain > "%TEMP%\gitstatus.tmp" 2>&1
set /p CHANGES=<"%TEMP%\gitstatus.tmp"
del "%TEMP%\gitstatus.tmp" >nul 2>&1

if defined CHANGES (
    echo [%date% %time%] 检测到文件变化，正在同步...
    git add -A
    git commit -m "Auto sync: %date% %time%"
    git push origin main
    if %errorlevel% equ 0 (
        echo [%date% %time%] ✅ 同步成功！
    ) else (
        echo [%date% %time%] ❌ 同步失败，请检查网络
    )
    echo.
    set "CHANGES="
) else (
    echo [%date% %time%] 暂无变化，等待中...
)

timeout /t 5 /nobreak >nul
goto loop
