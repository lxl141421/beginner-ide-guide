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

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Racket | [Racket](https://racket-lang.org) | v9.2 | 2026-05-28 | Win/Mac/Linux | 函数式编程教学，自带 DrRacket IDE，SL 教学语言 |
| C/C++ | [Arduino IDE](https://www.arduino.cc/en/software) | v2.3.9 | 2026-05-26 | Win/Mac/Linux | 硬件编程入门，一键烧录，海量示例代码 |
| Python | [WinPython](https://winpython.github.io) | 17.4 | 2026-05-17 | Windows | 便携式 Python 发行版，自带科学计算全家桶，解压即用 |
| Python | [Thonny](https://thonny.org) | v5.0.0 | 2026-04-25 | Win/Mac/Linux | Python 官方推荐教学 IDE，内置解释器，调试器可视化变量 |
| Processing | [Processing](https://processing.org) | v4.5.2 | 2026-01-29 | Win/Mac/Linux | 创意编程入门，可视化反馈即时，内置图形库 |
| C/C++ | [小龙 Dev-C++](https://gitee.com/devcpp/devcpp) | v6.4.1 | 2026-01 | Windows | 轻量免费 C/C++ IDE，自带 GCC 11.4，经典 Dev-C++ 增强版 |
| C/C++ | [Red Panda C++](https://github.com/royqh1979/RedPanda-CPP) | v3.4 | 2025-11-30 | Windows/Linux | Dev-C++ 精神续作，现代化界面，内置调试器 |
| Python | [PyScripter](https://github.com/lmbelo/pyscripter) | v5.3.0 | 2025-11-11 | Windows | 轻量 Python IDE，语法高亮、调试器、代码补全 |
| Java | [BlueJ](https://bluej.org) | v5.5.0 | 2025-06-03 | Win/Mac/Linux | Java 教学专用，可视化类图，交互式对象创建 |
| Go | [LiteIDE](https://github.com/visualfc/liteide) | x38.4 | 2025-05-19 | Win/Mac/Linux | 轻量 Go IDE，解压即用，启动快，代码补全 |

**适用场景：**
- Python 零基础 → Thonny（跨平台）/ WinPython（Windows 便携）/ PyScripter（Windows 轻量）
- Go 入门 → LiteIDE
- 创意编程 → Processing
- 硬件/机器人 → Arduino IDE
- 函数式编程/SICP → Racket

---

## 二、需要配置环境的 IDE

> 功能更强大，但需要先安装语言运行时（JDK、Python、Node.js 等）。

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
**Java / Kotlin：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Java/Kotlin | [IntelliJ IDEA CE](https://www.jetbrains.com/idea/) · [下载](https://www.jetbrains.com/idea/download/) | 2026.1.3 | 2026-06-04 | Win/Mac/Linux | 最强 Java IDE，智能补全，社区版免费 |
| Java | [NetBeans](https://netbeans.apache.org) | 30 | 2026-05-11 | Win/Mac/Linux | Apache 出品，Java 教学常用 |
| Java | [Eclipse](https://eclipse.org) | 2026-03 | 2026-03 | Win/Mac/Linux | 经典 Java IDE，插件生态丰富 |
| Kotlin/Java | [Android Studio](https://developer.android.com/studio) | Narwhal 2025.1.1 | 2025-05 | Win/Mac/Linux | Android 开发唯一官方 IDE |

**Python：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Python | [PyCharm CE](https://www.jetbrains.com/pycharm/) · [下载](https://www.jetbrains.com/pycharm/download/) | 2026.1.3 | 2026-06-04 | Win/Mac/Linux | 最强 Python IDE，科学计算支持，社区版免费 |
| Python | [Spyder](https://www.spyder-ide.org) | v6.1.4 | 2026-04-07 | Win/Mac/Linux | 科学计算/数据分析专用，变量浏览器 |

**C / C++ / C#：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| C++/C#/.NET | [Visual Studio Community](https://visualstudio.microsoft.com/vs/) · [社区版](https://visualstudio.microsoft.com/vs/community/) | v17.14 | 2026-06 | Windows | 微软官方，C#/.NET 开发首选，社区版免费 |
| C/C++ | [CLion](https://www.jetbrains.com/clion/) · [下载](https://www.jetbrains.com/clion/download/) | 2025.1.1 | 2025-05 | Win/Mac/Linux | 最强 C/C++ IDE，CMake 支持，学生免费 |

**JS / TS：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| JS/TS | [WebStorm](https://www.jetbrains.com/webstorm/) · [下载](https://www.jetbrains.com/webstorm/download/) | 2026.1 | 2026-06 | Win/Mac/Linux | 最强前端 IDE，开箱即用 |

**适用场景：**
- Java 开发 → IntelliJ CE（首选）/ Eclipse / NetBeans
- Python Web/数据分析 → PyCharm CE
- 数据科学/AI → Spyder
- C#/.NET → VS Community
- C/C++ → CLion
- 前端 → WebStorm
- Android → Android Studio

> 💡 JetBrains 全家桶对学生和开源项目免费：[申请地址](https://www.jetbrains.com/community/education/)

---

## 三、编辑器 + 手动配置环境

> 需要自己安装语言运行时 + 配置编译/运行命令。灵活性最高，但上手门槛也最高。

| 语言支持 | 编辑器 | 最新版本 | 更新时间 | 平台 | 亮点 |
|---------|--------|---------|---------|------|------|
| 全语言 | [VS Code](https://code.visualstudio.com) | v1.123 | 2026-06-03 | Win/Mac/Linux | 最流行，插件生态最强，远程开发 |
| 全语言 | [Zed](https://zed.dev) | v1.5.3 | 2026-06-03 | Mac/Linux | 最快的现代编辑器，Rust 编写 |
| 全语言 | [Kate](https://kate-editor.org) | v26.04.2 | 2026-04 | Win/Mac/Linux | KDE 出品，轻量但功能全 |
| 全语言 | [Vim/Neovim](https://neovim.io) | v0.12.2 | 2026-04-22 | Win/Mac/Linux | 终端效率之王，学习曲线陡峭 |
| 全语言 | [Lapce](https://lapce.dev) | v0.4.6 | 2026-01-21 | Win/Mac/Linux | Rust 编写，原生 GUI，内置终端 |
| 全语言 | [Sublime Text](https://www.sublimetext.com) | Build 4200 | 2026-03 | Win/Mac/Linux | 极速启动，轻量，买断制 |
| 全语言 | [Helix](https://helix-editor.com) | 25.07.1 | 2025-07-18 | Win/Mac/Linux | 后现代终端编辑器，内置 LSP |
| C#/.NET | [RoslynPad](https://github.com/aelij/RoslynPad) | - | - | Windows | C# REPL 即时执行，基于 Roslyn 编译器 |

**需要手动安装的环境（按语言）：**

| 语言 | 安装方式 | 验证命令 |
|------|---------|---------|
| Python | [python.org](https://python.org) 下载 或 `pyenv` | `python3 --version` |
| Java | [Adoptium](https://adoptium.net) | `java -version` |
| Node.js | [nodejs.org](https://nodejs.org) 或 `nvm` | `node -v` |
| C/C++ | Windows: MinGW-w64 或 [MSYS2](https://www.msys2.org); Mac: Xcode CLI; Linux: `build-essential` | `gcc --version` |
| Go | [go.dev](https://go.dev) | `go version` |
| Rust | [rustup.rs](https://rustup.rs) | `rustc --version` |
| C#/.NET | [dotnet.microsoft.com](https://dotnet.microsoft.com) | `dotnet --version` |

> 💡 Windows 用户推荐用 [MSYS2](https://www.msys2.org) 管理 C/C++/Go/Rust 工具链，比单独装 MinGW 方便得多。

---

## 选型决策树

```
开始
 ├─ 完全零基础？
 │   ├─ 想学 Python → Thonny（跨平台）/ WinPython（Win便携）
 │   ├─ 想学 Java → BlueJ
 │   ├─ 想学 Go → LiteIDE
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

> 🤖 最后自动检查: 2026-06-05 00:01 UTC

> 以下状态由自动化脚本每日更新。  
> ⚠️ = 超过 12 个月未更新；✅ = 活跃维护中

| 项目 | 最后活跃 | 状态 |
|------|---------|------|
| Thonny | 2026-05-28 | ✅ |
| WinPython | 2026-05-25 | ✅ |
| PyScripter | 2025-11-24 | ✅ |
| Processing | 2026-05-26 | ✅ |
| Arduino IDE | 2026-06-01 | ✅ |
| Greenfoot | - | ❓ |
| Racket | 2026-06-02 | ✅ |
| Embarcadero Dev-C++ | 2024-06-17 | ⚠️ 可能停更 |
| Red Panda C++ | 2026-06-04 | ✅ |
| LiteIDE | 2026-05-19 | ✅ |
| IntelliJ IDEA CE | 2026-06-04 | ✅ |
| PyCharm CE | - | ❓ |
| Eclipse | 2026-06-04 | ✅ |
| NetBeans | 2026-06-04 | ✅ |
| Spyder | 2026-06-02 | ✅ |
| VS Code | 2026-06-05 | ✅ |
| Neovim | 2026-06-04 | ✅ |
| RoslynPad | 2026-06-03 | ✅ |
| Helix | 2026-06-04 | ✅ |
| Zed | 2026-06-04 | ✅ |
| Lapce | 2026-06-04 | ✅ |
| Kate | 2026-06-04 | ✅ |

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
