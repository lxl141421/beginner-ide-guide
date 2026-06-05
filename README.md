# 🚀 编程入门开发环境指南

> 为编程教育整理的开发环境选择指南——适合学校教学、培训机构、自学入门。  
> 只收录**活跃维护**的项目，已停更/冻结/存档的不在本列表中。

---

## 快速选择

| 你的情况 | 推荐类别 |
|---------|---------|
| 零基础 / 课堂教学 / 不想折腾环境 | [解压即用型 IDE](#一解压即用型-ide) |
| 有一定基础 / 项目开发 / 培训课程 | [需要配置环境的 IDE](#二需要配置环境的-ide) |
| 深度学习底层原理 / 计算机专业 | [编辑器 + 手动配置环境](#三编辑器--手动配置环境) |

---

## 一、解压即用型 IDE

> 下载解压就能用，不需要额外安装编译器/解释器。

**Python：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Python | [WinPython](https://winpython.github.io) | 17.4 | 2026-05-17 | Windows | 便携免安装，自带 NumPy/Pandas/Matplotlib，选 **CPython 3.12** 版本 |
| Python | [Thonny](https://thonny.org) | v5.0.0 | 2026-04-25 | Win/Mac/Linux | Python 官方推荐，逐行执行可视化变量，零配置 |
| Python | [PyScripter](https://github.com/lmbelo/pyscripter) | v5.3.0 | 2025-11-11 | Windows | Windows 专属轻量 IDE，启动秒开，内置调试器 |

**C / C++：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| C/C++ | [Arduino IDE](https://www.arduino.cc/en/software) | v2.3.9 | 2026-05-26 | Win/Mac/Linux | 硬件编程首选，一键烧录到开发板，海量库支持 |
| C/C++ | [小龙 Dev-C++](https://gitee.com/devcpp/devcpp) | v6.4.1 | 2026-01 | Windows | 国产增强版 Dev-C++，自带 GCC 11.4，OJ 刷题/竞赛常用 |
| C/C++ | [Red Panda C++](https://github.com/royqh1979/RedPanda-CPP) | v3.4 | 2025-11-30 | Windows/Linux | 信奥/竞赛首选，内置 OJ 题库，智能补全，中文界面 |

**Java：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Java | [BlueJ](https://bluej.org) | v5.5.0 | 2025-06-03 | Win/Mac/Linux | 大学 Java 课程标配，可视化类图交互式创建对象 |

**Go：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Go | [LiteIDE](https://github.com/visualfc/liteide) | x38.4 | 2025-05-19 | Win/Mac/Linux | 唯一专注 Go 的轻量 IDE，解压即用，中文界面 |

**其他：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Racket | [Racket](https://racket-lang.org) | v9.2 | 2026-05-28 | Win/Mac/Linux | SICP/函数式编程首选，自带 DrRacket，教学语言分级 |
| Processing | [Processing](https://processing.org) | v4.5.2 | 2026-01-29 | Win/Mac/Linux | 创意编程/可视化艺术首选，5 行代码画动画，即时反馈 |

**适用场景：**
- Python 零基础 → Thonny（跨平台）/ WinPython（Windows 便携）/ PyScripter（Windows 轻量）
- Go 入门 → LiteIDE
- 创意编程 → Processing
- 硬件/机器人 → Arduino IDE
- 函数式编程/SICP → Racket

---

## 二、需要配置环境的 IDE

> 功能更强大，但需要先安装语言运行时（JDK、Python、Node.js 等）。

**Java / Kotlin：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Java/Kotlin | [IntelliJ IDEA CE](https://www.jetbrains.com/idea/) · [下载](https://www.jetbrains.com/idea/download/) | 2026.1.3 | 2026-06-04 | Win/Mac/Linux | Java 开发行业标准，重构/补全/调试一体，社区版免费 |
| Java | [NetBeans](https://netbeans.apache.org) | 30 | 2026-05-11 | Win/Mac/Linux | Apache 出品，Maven/Gradle 原生支持，GUI 拖拽设计器 |
| Java | [Eclipse](https://eclipse.org) | 2026-03 | 2026-03 | Win/Mac/Linux | 老牌 Java IDE，插件生态最全，企业项目常用 |
| Kotlin/Java | [Android Studio](https://developer.android.com/studio) | Narwhal 2025.1.1 | 2025-05 | Win/Mac/Linux | Android 开发唯一官方 IDE，内置模拟器，布局可视化 |

**Python：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Python | [PyCharm CE](https://www.jetbrains.com/pycharm/) · [下载](https://www.jetbrains.com/pycharm/download/) | 2026.1.3 | 2026-06-04 | Win/Mac/Linux | Python 开发首选，Django/Flask 支持，社区版免费 |
| Python | [Spyder](https://www.spyder-ide.org) | v6.1.4 | 2026-04-07 | Win/Mac/Linux | 数据科学专用，变量浏览器实时查看 DataFrame，类 MATLAB |

**C / C++ / C#：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| C++/C#/.NET | [Visual Studio Community](https://visualstudio.microsoft.com/vs/) · [社区版](https://visualstudio.microsoft.com/vs/community/) | v17.14 | 2026-06 | Windows | C++/C# 开发最强，IntelliSense 智能补全，社区版免费 |
| C/C++ | [CLion](https://www.jetbrains.com/clion/) · [下载](https://www.jetbrains.com/clion/download/) | 2025.1.1 | 2025-05 | Win/Mac/Linux | C/C++ 开发首选，CMake 原生支持，学生免费 |

**JS / TS：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| JS/TS | [WebStorm](https://www.jetbrains.com/webstorm/) · [下载](https://www.jetbrains.com/webstorm/download/) | 2026.1 | 2026-06 | Win/Mac/Linux | 前端开发首选，Vue/React/Angular 全支持，学生免费 |

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
| 全语言 | [VS Code](https://code.visualstudio.com) | v1.123 | 2026-06-03 | Win/Mac/Linux | 市占率第一，插件 3 万+，远程开发/Dev Containers |
| 全语言 | [Zed](https://zed.dev) | v1.5.3 | 2026-06-03 | Mac/Linux | GPU 加速渲染，多光标协作，Rust 编写极速启动 |
| 全语言 | [Vim/Neovim](https://neovim.io) | v0.12.2 | 2026-04-22 | Win/Mac/Linux | 终端编辑器之王，纯键盘操作，服务器必装 |
| C#/.NET | [RoslynPad](https://github.com/roslynpad/roslynpad) | v21 | 2026-05-21 | Windows | C# 即时执行 REPL，无需创建项目即可测试代码片段 |
| 全语言 | [Kate](https://kate-editor.org) | v26.04.2 | 2026-04 | Win/Mac/Linux | KDE 出品，内置终端/LSP/文件树，比 VS Code 轻 3 倍 |
| 全语言 | [Sublime Text](https://www.sublimetext.com) | Build 4200 | 2026-03 | Win/Mac/Linux | 启动 <1 秒，多光标编辑，买断制 ¥70 |
| 全语言 | [Lapce](https://lapce.dev) | v0.4.6 | 2026-01-21 | Win/Mac/Linux | Rust 原生 GUI，内置 LSP 和远程开发，比 Electron 快 |
| 全语言 | [Helix](https://helix-editor.com) | 25.07.1 | 2025-07-18 | Win/Mac/Linux | 类 Vim 但开箱即用，内置 LSP/树形选择，无需插件 |

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
| 小龙 Dev-C++ | 2026-05-22 | ✅ |
| Arduino IDE | 2026-06-01 | ✅ |
| Racket | 2026-06-02 | ✅ |
| Red Panda C++ | 2026-06-04 | ✅ |
| LiteIDE | 2026-05-19 | ✅ |
| WinPython | 2026-05-25 | ✅ |
| Thonny | 2026-05-28 | ✅ |
| Processing | 2026-05-26 | ✅ |
| PyScripter | 2025-11-24 | ✅ |
| BlueJ | 2025-06-03 | ✅ |
| IntelliJ IDEA CE | 2026-06-04 | ✅ |
| PyCharm CE | 2026-06-04 | ✅ |
| VS Community | 2026-06 | ✅ |
| WebStorm | 2026-06 | ✅ |
| NetBeans | 2026-06-04 | ✅ |
| Spyder | 2026-06-02 | ✅ |
| Eclipse | 2026-06-04 | ✅ |
| CLion | 2025-05 | ✅ |
| Android Studio | 2025-05 | ✅ |
| VS Code | 2026-06-05 | ✅ |
| Zed | 2026-06-04 | ✅ |
| Vim/Neovim | 2026-06-04 | ✅ |
| Kate | 2026-06-04 | ✅ |
| Sublime Text | 2026-03 | ✅ |
| Lapce | 2026-06-04 | ✅ |
| Helix | 2026-06-04 | ✅ |
| RoslynPad | 2026-05-21 | ✅ |

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
