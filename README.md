# FRC-robot

2020/2021 [FIRST Robotics Competition](https://www.firstinspires.org/robotics/frc) (5307 ?) 组机器人项目程序仓库

开发使用 Python3 (优先使用Python3.6)

依赖接口 [RobotPy WPILib](https://github.com/robotpy/robotpy-wpilib) , 框架 [MagicBot](https://robotpy.readthedocs.io/en/stable/frameworks/magicbot.html#magicbot-framework-docs)



## 开发环境配置

1. 安装 Python3 [(3.7 for Windows)](https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe)  **安装时勾选安装pip**

2. 安装 [Visual Studio 2019 redistributable](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)

3. 编译安装 pyfrc (若下载失败请**换源**)

   (cmd中输入下面的命令)

   ```bash
   py -3 -m pip install pyfrc
   ```

   

Referance: https://robotpy.readthedocs.io/en/stable/install/index.html



## 项目约定

仓库文件结构

- 机器人代码 src/

- 机器人主程序入口 src/robot.py

- 文档 docs/



commit时如果**无法保证正常运行**时 (新功能未完成/没进行模拟器测试) ，添加 **[Unfinished]**

若**未进行实机测试**，添加 **[Untested]**，并添加到 Project 中的 In progress / Untested 中

