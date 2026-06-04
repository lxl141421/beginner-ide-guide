# 🚀 编程入门开发环境指南

> 为编程初学者整理的开发环境选择指南。  
> 只收录**活跃维护**的项目，已停更/冻结/存档的不在本列表中。

---

## 快速选择

| 你的情况 | 推荐类别 |
|---------|---------|
| 零基础，不想折腾环境 | [解压即用型 IDE](#一解压即用型-ide) |
| 有一定基础，想更专业的工具 | [需要配置环境的 IDE](#二需要配置环境的-ide) |
| 想深度学习底层原理 | [编辑器 + 手动配置环境](#三编辑器--手动配置环境) |

---

## 一、解压即用型 IDE

> 下载解压就能用，不需要额外安装编译器/解释器。

| IDE | 语言 | 最新版本 | 更新时间 | 平台 | 亮点 |
|-----|------|---------|---------|------|------|
| [Thonny](https://thonny.org) | Python | v4.1 | 2024-09 | Win/Mac/Linux | Python 官方推荐教学 IDE，内置解释器，调试器可视化变量 |
| [Processing](https://processing.org) | Processing/Java | v4.3 | 2024-06 | Win/Mac/Linux | 创意编程入门，可视化反馈即时，内置图形库 |
| [Arduino IDE](https://www.arduino.cc/en/software) | C/C++ | v2.3 | 2024-08 | Win/Mac/Linux | 硬件编程入门，一键烧录，海量示例代码 |
| [Mu Editor](https://codewith.mu) | Python | v1.2 | 2023-12 | Win/Mac/Linux | 面向初学者的 Python 编辑器，支持 MicroPython/CircuitPython |
| [BlueJ](https://bluej.org) | Java | v5.4 | 2024-02 | Win/Mac/Linux | Java 教学专用，可视化类图，交互式对象创建 |
| [Greenfoot](https://greenfoot.org) | Java | v3.8 | 2024-01 | Win/Mac/Linux | Java 游戏开发教学，可视化场景编辑器 |
| [Racket](https://racket-lang.org) | Racket/Scheme | v8.14 | 2024-09 | Win/Mac/Linux | 函数式编程教学，自带 DrRacket IDE，SL 教学语言 |
| [IDLE](https://docs.python.org/3/library/idle.html) | Python | (随 Python 发布) | 2024-10 | Win/Mac/Linux | Python 自带，零安装，交互式解释器 |
| [Code::Blocks](https://www.codeblocks.org) | C/C++ | v20.03 | 2024-07 | Win/Mac/Linux | 开箱即用的 C/C++ IDE，自带 MinGW（Windows 版） |
| [Emacspeak](https://emacspeak.sourceforge.net) | 多语言 | 持续更新 | 2024-08 | Linux/Mac | 无障碍编程环境，视障人士专用 |

**适用场景：**
- Thonny → Python 零基础入门首选
- Processing → 想通过画画/动画学编程
- Arduino → 想玩硬件/机器人
- BlueJ/Greenfoot → 计算机专业 Java 课程
- Racket → SICP/函数式编程入门

---

## 二、需要配置环境的 IDE

> 功能更强大，但需要先安装语言运行时（JDK、Python、Node.js 等）。

| IDE | 语言 | 最新版本 | 更新时间 | 平台 | 亮点 |
|-----|------|---------|---------|------|------|
| [IntelliJ IDEA CE](https://www.jetbrains.com/idea/) | Java/Kotlin | 2024.2 | 2024-09 | Win/Mac/Linux | 最强 Java IDE，智能补全，社区版免费 |
| [PyCharm CE](https://www.jetbrains.com/pycharm/) | Python | 2024.2 | 2024-09 | Win/Mac/Linux | 最强 Python IDE，科学计算支持，社区版免费 |
| [Visual Studio Community](https://visualstudio.microsoft.com) | C++/C#/.NET | v17.11 | 2024-09 | Windows | 微软官方，C#/.NET 开发首选，社区版免费 |
| [Eclipse](https://eclipse.org) | Java/C++/PHP | 2024-09 | 2024-09 | Win/Mac/Linux | 经典 Java IDE，插件生态丰富 |
| [NetBeans](https://netbeans.apache.org) | Java/PHP/JS | 22 | 2024-09 | Win/Mac/Linux | Apache 出品，Java 教学常用 |
| [Android Studio](https://developer.android.com/studio) | Kotlin/Java | Ladybug 2024.2 | 2024-09 | Win/Mac/Linux | Android 开发唯一官方 IDE |
| [CLion](https://www.jetbrains.com/clion/) | C/C++ | 2024.2 | 2024-09 | Win/Mac/Linux | 最强 C/C++ IDE，CMake 支持，学生免费 |
| [WebStorm](https://www.jetbrains.com/webstorm/) | JS/TS | 2024.2 | 2024-09 | Win/Mac/Linux | 最强前端 IDE，开箱即用 |
| [Spyder](https://www.spyder-ide.org) | Python | v6.0 | 2024-09 | Win/Mac/Linux | 科学计算/数据分析专用，变量浏览器 |

**适用场景：**
- IntelliJ → Java 开发标配
- PyCharm → Python Web 开发/数据分析
- VS Community → Windows 桌面开发、C# 学习
- Android Studio → 想做手机 App
- Spyder → 数据科学/AI 入门

> 💡 JetBrains 全家桶对学生和开源项目免费：[申请地址](https://www.jetbrains.com/community/education/)

---

## 三、编辑器 + 手动配置环境

> 需要自己安装语言运行时 + 配置编译/运行命令。灵活性最高，但上手门槛也最高。

| 编辑器 | 类型 | 最新版本 | 更新时间 | 平台 | 亮点 |
|--------|------|---------|---------|------|------|
| [VS Code](https://code.visualstudio.com) | 代码编辑器 | v1.94 | 2024-10 | Win/Mac/Linux | 最流行，插件生态最强，远程开发 |
| [Vim/Neovim](https://neovim.io) | 终端编辑器 | v0.10 | 2024-09 | Win/Mac/Linux | 终端效率之王，学习曲线陡峭 |
| [Sublime Text](https://www.sublimetext.com) | 代码编辑器 | v4 | 2024-08 | Win/Mac/Linux | 极速启动，轻量，买断制 |
| [Helix](https://helix-editor.com) | 终端编辑器 | v24.07 | 2024-07 | Win/Mac/Linux | 后现代终端编辑器，内置 LSP |
| [Zed](https://zed.dev) | 代码编辑器 | 持续更新 | 2024-10 | Mac/Linux | 最快的现代编辑器，Rust 编写 |
| [Lapce](https://lapce.dev) | 代码编辑器 | v0.4 | 2024-06 | Win/Mac/Linux | Rust 编写，原生 GUI，内置终端 |
| [Kate](https://kate-editor.org) | 代码编辑器 | v24.08 | 2024-08 | Win/Mac/Linux | KDE 出品，轻量但功能全 |

**需要手动安装的环境（按语言）：**

| 语言 | 安装方式 | 验证命令 |
|------|---------|---------|
| Python | [python.org](https://python.org) 下载 或 `pyenv` | `python3 --version` |
| Java | [Adoptium](https://adoptium.net) | `java -version` |
| Node.js | [nodejs.org](https://nodejs.org) 或 `nvm` | `node -v` |
| C/C++ | Windows: MinGW-w64; Mac: Xcode CLI; Linux: `build-essential` | `gcc --version` |
| Go | [go.dev](https://go.dev) | `go version` |
| Rust | [rustup.rs](https://rustup.rs) | `rustc --version` |

---

## 选型决策树

```
开始
 ├─ 完全零基础？
 │   ├─ 想学 Python → Thonny
 │   ├─ 想学 Java → BlueJ
 │   ├─ 想学创意编程 → Processing
 │   └─ 想玩硬件 → Arduino IDE
 │
 ├─ 有少量编程经验？
 │   ├─ Python → PyCharm CE
 │   ├─ Java → IntelliJ CE
 │   ├─ C#/.NET → VS Community
 │   ├─ 前端 → WebStorm 或 VS Code
 │   └─ 数据科学 → Spyder
 │
 └─ 想要最大灵活性？
     └─ VS Code + 手动配置语言环境
```

---

## 更新状态

> 🤖 最后自动检查: 2026-06-04 17:34 UTC

> 以下状态由自动化脚本每日更新。  
> ⚠️ = 超过 12 个月未更新；✅ = 活跃维护中

| 项目 | 最后活跃 | 状态 |
|------|---------|------|
| Thonny | - | ❓ |
| Processing | - | ❓ |
| Arduino IDE | - | ❓ |
| Mu Editor | - | ❓ |
| Greenfoot | - | ❓ |
| Racket | - | ❓ |
| IntelliJ IDEA CE | - | ❓ |
| PyCharm CE | - | ❓ |
| Eclipse | - | ❓ |
| NetBeans | - | ❓ |
| Spyder | - | ❓ |
| VS Code | - | ❓ |
| Neovim | - | ❓ |
| Helix | - | ❓ |
| Zed | - | ❓ |
| Lapce | - | ❓ |
| Kate | - | ❓ |

---

## 如何贡献

1. Fork 本项目
2. 添加/修改 IDE 信息
3. 确保项目**仍在活跃维护**
4. 提交 PR

### 添加标准
- ✅ 最近 12 个月内有版本发布或代码提交
- ✅ 适合编程入门或教学使用
- ❌ 已停止维护超过 1 年
- ❌ 已标记为 archived / frozen
- ❌ 需要付费才能使用核心功能

---

## 许可

MIT License - 欢迎自由使用和分享。
