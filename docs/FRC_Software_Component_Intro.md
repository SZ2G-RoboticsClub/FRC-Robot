- WPILib - 官方所提供的机器人主板 (RoboRIO) api接口程序，仅支持C++/Java

  > The WPI Robotics Library (WPILib) is the standard software library provided for teams to write code for their FRC robots. A [software library](https://en.wikipedia.org/wiki/Library_(computing)) is a collection of code that can be imported into and used by other software. WPILib contains a set of useful classes and subroutines for interfacing with various parts of the FRC control system (such as sensors, motor controllers, and the driver station), as well as an assortment of other utility functions.



- robotpy-wpilib - WPILib的Python包装，使Python程序能够调用机器人主板 (RoboRIO) api

  > This repository contain a python implementation of wrappers for WPILib, the library used to interface with hardware for the FIRST Robotics Competition. Teams can use this library to write their robot code in Python, a powerful dynamic programming language.



- Command / MagicBot Framework - 基于robotpy-wpilib的高度封装的机器人控制框架

  > After creating code for a few robots, you’ll notice that there are a lot of similarities between the code. Robot code frameworks are a collection of patterns and ideas that are generally useful for creating robot code.
  >
  > While frameworks sometimes have a learning curve associated with them, once you learn how they work you will find that they can save you a lot of effort and prevent you from making certain kinds of mistakes.
  >
  > 
  >
  > MagicBot Framework (暂定使用MagicBot框架，不用Command)
  >
  > MagicBot is an opinionated framework for creating Python robot programs for the FIRST Robotics Competition. It is envisioned to be an easier to use pythonic alternative to the Command framework, and has been used by championship caliber teams to power their robots.
  >
  > While MagicBot will tend to be more useful for complex multi-module programs, it does remove some of the boilerplate associated with simple programs as well.



- robotpy-installer (a.k.a. RoboRIO Package Installer) - 用于向机器人中刷入Python程序/第三方库

  (需pyfrc前置支持)

  robotpy-wpilib / MagicBot Framework等库都需通过其刷入

  > Most FRC robots are not placed on networks that have access to the internet, particularly at competition arenas. The RobotPy installer is designed for this type of ‘two-phase’ operation – with individual steps for downloading and installing packages separately.
  >
  > The RobotPy installer supports downloading external packages from the python package repository (pypi) via pip, and installing those packages onto the robot. We cannot make any guarantees about the quality of external packages, so use them at your own risk.

  

- pyfrc - 用于向机器人刷入程序并进行调试的底层工具，一般通过robotpy-installer调用

  > pyfrc is a python 3 library designed to make developing python code using WPILib for FIRST Robotics Competition easier.
  >
  > This library contains a few primary parts:
  >
  > - A built-in uploader that will upload your robot code to the robot
  > - Integration with the py.test testing tool to allow you to easily write unit tests for your robot code.
  > - Various support for robot simulation



- cscore & robotpy-cscore - 用于多进程图像处理的模块

  > The RobotPy project provides [robotpy-cscore](https://github.com/robotpy/robotpy-cscore/), which are python bindings for [cscore](https://github.com/wpilibsuite/cscore), a high performance camera access and streaming library introduced by FIRST in 2017. It can be used to:
  >
  > - Stream a USB/HTTP camera to SmartDashboard or the LabVIEW dashboard via HTTP
  > - Capture images from USB or HTTP camera, modify them using OpenCV/Numpy, and send them via HTTP to SmartDashboard, the LabVIEW dashboard, or a web browser.
  >
  > `robotpy-cscore` is intended to be usable on any platform supported by OpenCV and Numpy, and is a more flexible and powerful alternative to solutions such as mjpg-streamer.



- NetworkTables - 一种FRC比赛中在多程序/线程/进程中通讯的协议，常用于夸线/进程传输变量/视频流等

  在 WPILib (robotpy-wpilib) 中提供了使用此协议进行通讯的接口

  PS: 机器人主板 (RoboRIO) 与 FRC Driver Station / Dashboard也使用此协议通讯

  > NetworkTables is a communications protocol used in FIRST Robotics. It provides a simple to use mechanism for communicating information between several computers. There is a single server (typically your robot) and zero or more clients. These clients can be on the driver station, a coprocessor, or anything else on the robot’s local control network.



更多模块请见：

​	https://docs.wpilib.org/en/stable/docs/getting-started/getting-started-frc-control-system/control-system-software.html

