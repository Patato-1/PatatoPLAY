@echo off
chcp 65001 >nul
echo ========================================
echo    AI 学习专栏 - 一键更新到 GitHub
echo ========================================
echo.

cd /d "C:\Users\Administrator\Desktop\Ailearning\AI学习"

set /p msg=请输入本次更新说明（例如：W1周一练习完成）：

echo.
echo 正在添加文件...
git add .

echo 正在提交...
git commit -m "%msg%"

echo 正在推送到 GitHub...
git push

echo.
echo ========================================
echo    ✅ 更新完成！
echo ========================================
echo.
echo 仓库地址：https://github.com/Patato-1/PatatoPLAY
echo.
pause