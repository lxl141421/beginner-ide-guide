# 🚀 编程入门开发环境指南

> 为编程教育整理的开发环境选择指南——适合学校教学、培训机构、自学入门。  
> 涵盖本地 IDE、编辑器、在线编程平台、算法可视化网站。  
> 只收录**活跃维护**的项目，已停更/冻结/存档的不在本列表中。

---

## 快速选择

| 你的情况 | 推荐类别 |
|---------|---------|
| 零基础 / 课堂教学 / 不想折腾环境 | [无需配置环境的 IDE](#一无需配置环境的-ide) |
| 有一定基础 / 项目开发 / 培训课程 | [需要配置环境的 IDE](#二需要配置环境的-ide) |
| 深度学习底层原理 / 计算机专业 | [编辑器 + 手动配置环境](#三编辑器--手动配置环境) |
| 不想装软件 / 随时随地写代码 | [在线网页版 IDE](#四在线网页版-ide) |
| 想理解算法运行过程 | [算法可视化网站](#五算法可视化网站) |

---

## 一、无需配置环境的 IDE

> 下载解压就能用，不需要额外安装编译器/解释器。

**Python：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Python | [WinPython](https://winpython.github.io) | 17.9.20260805/wppm | 2026-08-06 | Windows | 便携免安装，数据科学选 **free** 版，只学基础选 **slim** 版 |
| Python | [Thonny](https://thonny.org) | 5.0.0 | 2026-04-25 | Win/Mac/Linux | Python 官方推荐，逐行执行可视化变量，零配置 |


**C / C++：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| C/C++ | [Arduino IDE](https://www.arduino.cc/en/software) | 2.3.10 | 2026-06-09 | Win/Mac/Linux | 硬件编程首选，一键烧录到开发板，海量库支持 |
| C/C++ | [小龙 Dev-C++](https://gitee.com/devcpp/devcpp) · [GitHub](https://github.com/anbangli/XiaoLoong-DevCpp) | 6.4.1 | 2026-01-24 | Windows | 国产增强版 Dev-C++，自带 TDM-GCC，OJ 刷题/竞赛常用 |
| C/C++ | [Red Panda C++](https://github.com/royqh1979/RedPanda-CPP) | 3.4 | 2025-11-30 | Windows/Linux | 信奥/竞赛首选，内置 OJ 题库，智能补全，中文界面 |

**Java：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Java | [BlueJ](https://bluej.org) | 6.0.0 | 2026-07-01 | Win/Mac/Linux | 专为初学者设计的 Java IDE，可视化类图交互式创建对象，自带 JDK |



**其他：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Processing | [Processing](https://processing.org) | 4.5.6 | 2026-07-20 | Win/Mac/Linux | 创意编程/可视化艺术首选，5 行代码画动画，即时反馈 |
| Pascal | [Lazarus](https://www.lazarus-ide.org) | 4.8 | 2026-06-11 | Win/Mac/Linux | Delphi 开源替代，可视化窗体设计器，自带 Free Pascal 编译器 |
| Racket | [Racket](https://racket-lang.org) | 9.2 | 2026-05-28 | Win/Mac/Linux | SICP/函数式编程首选，自带 DrRacket，教学语言分级 |

**适用场景：**
- Python 零基础 → Thonny（跨平台）/ WinPython（Windows 便携）
- Pascal/OJ 刷题 → Lazarus / 小龙 Dev-C++ / Red Panda C++
- 创意编程 → Processing
- 硬件/机器人 → Arduino IDE
- 函数式编程/SICP → Racket

---

## 二、需要配置环境的 IDE

> 功能更强大，但需要先安装语言运行时（JDK、Python、Node.js 等）。

**Java / Kotlin：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Java/Kotlin | [IntelliJ IDEA CE](https://www.jetbrains.com/idea/) · [下载](https://www.jetbrains.com/idea/download/) | 2025.2.6.3 | 2026-07-28 | Win/Mac/Linux | Java 开发行业标准，重构/补全/调试一体，社区版免费 |
| Kotlin/Java | [Android Studio](https://developer.android.com/studio) | Narwhal 2025.1.4 | 2026-06-04 | Win/Mac/Linux | Android 开发唯一官方 IDE，内置模拟器，布局可视化 |
| Java | [NetBeans](https://netbeans.apache.org) | 30 | 2026-05-11 | Win/Mac/Linux | Apache 出品，Maven/Gradle 原生支持，GUI 拖拽设计器 |
| Java | [Eclipse](https://eclipse.org) | 2026-03 | 2026-03-12 | Win/Mac/Linux | 老牌 Java IDE，插件生态最全，企业项目常用 |

**Python：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| Python | [Spyder](https://www.spyder-ide.org) | 6.1.6 | 2026-07-29 | Win/Mac/Linux | 数据科学专用，变量浏览器实时查看 DataFrame，类 MATLAB |
| Python | [PyCharm CE](https://www.jetbrains.com/pycharm/) · [下载](https://www.jetbrains.com/pycharm/download/) | 2026.1.3 | 2026-06-04 | Win/Mac/Linux | Python 开发首选，Django/Flask 支持，社区版免费 |
| Python | [PyScripter](https://github.com/lmbelo/pyscripter) | 5.3.0 | 2025-11-11 | Windows | 轻量级 Python IDE，启动秒开，内置调试器 |

**C / C++ / C#：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| C++/C#/.NET | [Visual Studio Community](https://visualstudio.microsoft.com/vs/) · [社区版](https://visualstudio.microsoft.com/vs/community/) | 2022 17.14 | 2026-07-22 | Windows | C++/C# 开发最强，IntelliSense 智能补全，社区版免费 |
| C/C++ | [CLion](https://www.jetbrains.com/clion/) · [下载](https://www.jetbrains.com/clion/download/) | 2026.1.2 | 2026-05-18 | Win/Mac/Linux | C/C++ 开发首选，CMake 原生支持，学生免费 |

**JS / TS：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| JS/TS | [WebStorm](https://www.jetbrains.com/webstorm/) · [下载](https://www.jetbrains.com/webstorm/download/) | 2026.1.3 | 2026-06-04 | Win/Mac/Linux | 前端开发首选，Vue/React/Angular 全支持，学生免费 |

**其他 / 多语言：**

| 语言 | IDE | 最新版本 | 更新时间 | 平台 | 亮点 |
|------|-----|---------|---------|------|------|
| 多语言 | [Geany](https://www.geany.org) | 2.1.0 | 2025-07-01 | Win/Mac/Linux | 轻量级 GUI IDE，50+ 语言，内置编译运行集成，需自行安装语言环境 |

**适用场景：**
- Java 开发 → IntelliJ CE（首选）/ Eclipse / NetBeans
- Python 开发 → PyCharm CE（全功能）/ PyScripter（轻量 Windows）
- 数据科学/AI → Spyder
- C#/.NET → VS Community
- C/C++ → CLion / Geany（轻量）
- 前端 → WebStorm
- Android → Android Studio

> 💡 JetBrains 全家桶对学生和开源项目免费：[申请地址](https://www.jetbrains.com/community/education/)

---

## 三、编辑器 + 手动配置环境

> 需要自己安装语言运行时 + 配置编译/运行命令。灵活性最高，但上手门槛也最高。

| 语言支持 | 编辑器 | 最新版本 | 更新时间 | 平台 | 亮点 |
|---------|--------|---------|---------|------|------|
| 全语言 | [Zed](https://zed.dev) | 1.14.2 | 2026-08-05 | Win/Mac/Linux | GPU 加速渲染，多光标协作，Rust 编写极速启动 |
| **全语言** | **[VS Code](https://code.visualstudio.com)** | 1.132.0 | 2026-08-05 | **Win/Mac/Linux** | **市占率第一，插件 3 万+，远程开发/Dev Containers** |
| 全语言 | [nano](https://nano-editor.org) | 9.2 | 2026-07-31 | Linux/Mac | 最简单的终端编辑器，服务器必装，零学习成本 |
| **全语言** | **[Vim/Neovim](https://neovim.io)** | 0.12.4 | 2026-07-05 | **Win/Mac/Linux** | **终端编辑器之王，纯键盘操作，服务器必装** |
| **全语言** | **[Sublime Text](https://www.sublimetext.com)** | **Build 4200** | **2026-05-29** | **Win/Mac/Linux** | **启动 <1 秒，多光标编辑，可无限试用** |
| 全语言 | [gedit](https://gedit-technology.github.io/apps/gedit/) | 50.0 | 2026-03-27 | Linux | GNOME 桌面自带，语法高亮，适合 Linux 课堂 |
| 全语言 | [Emacs](https://www.gnu.org/software/emacs/) | 30.2 | 2025-08-14 | Win/Mac/Linux | 可编程编辑器，Org-mode/Lisp 生态，学习曲线陡峭 |

**需要手动安装的环境（按语言）：**

| 语言 | 推荐版本 | 安装方式 | 验证命令 |
|------|---------|---------|---------|
| Python | 3.12+（最新稳定版） | [python.org](https://python.org) 下载 或 `pyenv` | `python3 --version` |
| Java | 21 LTS（长期支持版） | [Adoptium](https://adoptium.net) | `java -version` |
| Node.js | 22 LTS（长期支持版） | [nodejs.org](https://nodejs.org) 或 `nvm` | `node -v` |
| C/C++ | 12.x~13.x（竞赛）/ 最新稳定版（日常） | Windows: MinGW-w64 或 [MSYS2](https://www.msys2.org); Mac: Xcode CLI; Linux: `build-essential` | `gcc --version` |
| Go | 1.22+（最新稳定版） | [go.dev](https://go.dev) | `go version` |
| Rust | 最新稳定版（rustup 自动管理） | [rustup.rs](https://rustup.rs) | `rustc --version` |
| C#/.NET | 8 LTS（长期支持版） | [dotnet.microsoft.com](https://dotnet.microsoft.com) | `dotnet --version` |

> 💡 选版本原则：**有 LTS（长期支持）选 LTS，没有就选最新稳定版**。LTS 版本维护时间长、社区支持好，适合学习和生产环境。

> 💡 Windows 用户推荐用 [MSYS2](https://www.msys2.org) 管理 C/C++/Go/Rust 工具链，比单独装 MinGW 方便得多。

> ⚠️ **竞赛编译器版本限制：** 参加编程竞赛（ICPC/NOI/蓝桥杯等）时，OJ 平台对编译器版本有严格要求，本地版本过新可能导致编译失败。推荐同时安装一个较旧版本（如 GCC 12.x）备用。竞赛常用限制：C++ 标准 `-std=c++14` 或 `-std=c++17`，不支持 C++20/23 新特性；NOI/NOIP 系列仅允许 C/C++，不接受 Java 和 Python。

---

## 四、在线网页版 IDE

> 打开浏览器就能写代码，不用安装任何软件。适合课堂演示、快速验证想法、随时随地练习。

**综合型（多语言）：**

| 平台 | 支持语言 | 需要登录 | 免费 | 亮点 |
|------|---------|---------|------|------|
| [Replit](https://replit.com) | 50+ 种（Python/Java/C++/JS/Go 等） | 是 | ✅ 基础免费 | 浏览器完整 IDE，多人协作，AI 助手 |
| [GitHub Codespaces](https://github.com/features/codespaces) | 全语言（VS Code） | 是（GitHub） | ✅ 60 小时/月 | 浏览器完整 VS Code，直接打开仓库 |
| [OnlineGDB](https://www.onlinegdb.com) | 15+ 种（C/C++/Java/Python/JS 等） | 否 | ✅ 完全免费 | 内置 GDB 调试器，适合学习调试 |
| [JDoodle](https://www.jdoodle.com) | 110+ 种语言 | 否 | ✅ 有每日限额 | 语言支持最广，快速测试代码 |
| [W3Schools Tryit](https://www.w3schools.com/tryit/) | 15+ 种（HTML/Python/Java/C 等） | 否 | ✅ 完全免费 | 配套 W3Schools 教程，一键试运行 |
| [菜鸟工具](https://www.runoob.com) | 10+ 种（Python/C/Java/JS/PHP 等） | 否 | ✅ 完全免费 | 配套菜鸟教程，中文界面，一键运行 |
| [IDEONE](https://ideone.com) | 60+ 种语言 | 否 | ✅ 完全免费 | 简洁快速，适合多语言对比测试 |
| [Programiz](https://www.programiz.com/python-programming/online-compiler) | 18 种语言 | 否 | ✅ 完全免费 | 界面极简，零基础友好，配套教程 |

**专项型：**

| 平台 | 支持语言 | 需要登录 | 免费 | 亮点 |
|------|---------|---------|------|------|
| [Google Colab](https://colab.research.google.com) | Python | 是（Google） | ✅ 含免费 GPU | 数据科学/ML 首选，预装 NumPy/PyTorch |
| [PythonAnywhere](https://www.pythonanywhere.com) | Python | 是 | ✅ 基础免费 | Python 专属，可部署 Flask/Django 网站 |
| [CodePen](https://codepen.io) | HTML/CSS/JS | 否 | ✅ 基础免费 | 前端开发实验场，实时预览，社区分享 |
| [StackBlitz](https://stackblitz.com) | JS/TS/HTML/CSS | 否 | ✅ 完全免费 | 浏览器内运行 Node.js，秒开 GitHub 项目 |


**国内编程竞赛/刷题平台（在线 IDE）：**

| 平台 | 支持语言 | 需要登录 | 免费 | 亮点 |
|------|---------|---------|------|------|
| [力扣 LeetCode](https://leetcode.cn) | 15+ 种（Python/C++/Java/JS/Go 等） | 是 | ✅ 大部分免费 | 算法刷题首选，内置代码编辑器+测试用例 |
| [AcWing](https://www.acwing.com) | C++/Python/Java | 是 | 部分免费 | 高质量算法课程+在线评测，B站配套视频 |
| [牛客](https://www.nowcoder.com) | 10+ 种（C/C++/Java/Python/JS 等） | 是 | ✅ 大部分免费 | 面试刷题+在线笔试模拟，校招必备 |
| [洛谷](https://www.luogu.com.cn) | C/C++/Java/Python | 是 | ✅ 大部分免费 | 3000+ 题库，难度分级，社区活跃 |
| [蓝桥杯官方练习](https://www.lanqiao.cn) | C/C++/Java/Python/JS/Go | 是 | ✅ 练习免费 | 蓝桥杯竞赛配套，在线模拟考试 |

> 💡 不想登录只想快速跑代码 → Programiz / OnlineGDB / JDoodle（打开即用）
> 💡 想刷算法题 → 力扣（国际通用）/ 洛谷（国内竞赛）

---

## 五、算法可视化网站

> 用动画看算法怎么运行，比读代码直观 100 倍。推荐配合 Hello Algo 和代码随想录学习。

**综合算法可视化：**

| 网站 | 形式 | 需要登录 | 免费 | 支持语言 | 亮点 |
|------|------|---------|------|---------|------|
| [VisuAlgo](https://visualgo.net) | 交互动画 | 否 | ✅ 完全免费 | 伪代码（多语言切换） | 新加坡国立大学出品，覆盖排序/图/字符串/数据结构 |
| [Algorithm Visualizer](https://algorithm-visualizer.org) | 代码+动画同步 | 否 | ✅ 完全免费 | JS/Java/C++/Python | 开源，边写代码边看动画，社区贡献算法 |
| [Python Tutor](https://pythontutor.com) | 逐步执行可视化 | 否 | ✅ 完全免费 | Python/Java/C/C++/JS/TS/Ruby | ⭐ 初学者神器！逐行显示变量值+调用栈+指针关系 |
| [USF 数据结构可视化](https://www.cs.usfca.edu/~galles/visualization/) | 点击交互 | 否 | ✅ 完全免费 | 无需写代码 | 经典教材级，堆/树/哈希表/图算法，纯点击操作 |

**排序算法专题：**

| 网站 | 形式 | 需要登录 | 免费 | 支持语言 | 亮点 |
|------|------|---------|------|---------|------|
| [SortVisualizer](https://sortvisualizer.com) | 并排动画对比 | 否 | ✅ 完全免费 | 无需写代码 | 多种排序算法并排运行，直观对比速度差异 |
| [Toptal 排序演示](https://www.toptal.com/developers/sorting-algorithms) | 动画+声音 | 否 | ✅ 完全免费 | 无需写代码 | 排序过程有声音反馈，不同算法音色不同 |

**路径规划算法：**

| 网站 | 形式 | 需要登录 | 免费 | 支持语言 | 亮点 |
|------|------|---------|------|---------|------|
| [PathFinding.js](https://qiao.github.io/PathFinding.js/visual/) | 网格交互 | 否 | ✅ 完全免费 | JavaScript | 画障碍物→看 A*/Dijkstra/BFS/DFS 找路径过程 |

**中文学习资源（含算法图解）：**

| 网站 | 形式 | 需要登录 | 免费 | 支持语言 | 亮点 |
|------|------|---------|------|---------|------|
| [Hello Algo（动手学数据结构与算法）](https://www.hello-algo.com) | 电子书+动画 | 否 | ✅ 完全免费 | Python/C++/Java/C/Go/JS/TS/C#/Swift/Rust/Zig/Kotlin/Dart/Ruby | ⭐⭐ 中文最佳！全彩图解+动画+14 种语言代码 |
| [代码随想录](https://programmercarl.com) | 图文+代码 | 否 | ✅ 完全免费 | C++/Python/Java/Go/JS | ⭐⭐ LeetCode 题解+动画图解，B 站配套视频 |
| [The Algorithms](https://the-algorithms.com) | 代码实现+说明 | 否 | ✅ 完全免费 | Python/Java/C++/C/JS/Go/Rust 等 15+ 种 | 开源算法大全，按语言+类别分类 |

> 💡 零基础想理解代码执行过程 → **Python Tutor**（粘贴代码，逐步运行，看变量变化）
> 💡 系统学习数据结构与算法 → **Hello Algo**（中文图解+动画+多语言代码）
> 💡 刷 LeetCode 需要思路讲解 → **代码随想录**（视频+图解+题解）
> 💡 纯看动画不想写代码 → **USF 数据结构可视化** / **SortVisualizer**

---

## 选型决策树

```
 开始
 ├─ 完全零基础？
 │   ├─ 想学 Python → Thonny（跨平台）/ WinPython（Win便携）
 │   ├─ 想学 Java → BlueJ
 │   ├─ 想学创意编程 → Processing
 │   ├─ 想玩硬件 → Arduino IDE
 │   └─ 不想装软件？→ Programiz / OnlineGDB / 菜鸟工具（打开即写）
 │
 ├─ 有少量编程经验？
 │   ├─ Python → PyCharm CE
 │   ├─ Java → IntelliJ CE
 │   ├─ C#/.NET → VS Community
 │   ├─ 前端 → WebStorm 或 VS Code
 │   ├─ 数据科学 → Spyder / Google Colab
 │   └─ 随时随地写？→ Replit / GitHub Codespaces
 │
 ├─ 想理解算法怎么运行？
 │   ├─ 看代码逐行执行 → Python Tutor
 │   ├─ 系统学数据结构 → Hello Algo
 │   ├─ 刷 LeetCode → 代码随想录 / 力扣
 │   └─ 纯看动画 → USF 数据结构可视化 / SortVisualizer
 │
 └─ 想要最大灵活性？
     └─ VS Code + 手动配置语言环境
```

---

## 更新状态

> 🤖 最后自动检查: 2026-08-09 09:46 UTC

> 以下状态由自动化脚本每日更新。  
> ⚠️ = 超过 12 个月未更新；✅ = 活跃维护中

| 项目 | 最后活跃 | 状态 |
|------|---------|------|
| WinPython | 2026-08-06 | ✅ |
| VS Code | 2026-08-05 | ✅ |
| Zed | 2026-08-05 | ✅ |
| nano | 2026-07-31 | ✅ |
| Spyder | 2026-07-29 | ✅ |
| IntelliJ IDEA CE | 2026-07-28 | ✅ |
| Visual Studio Community | 2026-07-22 | ✅ |
| Processing | 2026-07-20 | ✅ |
| Vim/Neovim | 2026-07-05 | ✅ |
| BlueJ | 2026-07-01 | ✅ |
| Lazarus | 2026-06-11 | ✅ |
| Arduino IDE | 2026-06-09 | ✅ |
| Android Studio | 2026-06-04 | ✅ |
| PyCharm CE | 2026-06-04 | ✅ |
| WebStorm | 2026-06-04 | ✅ |
| Sublime Text | 2026-05-29 | ✅ |
| Racket | 2026-05-28 | ✅ |
| CLion | 2026-05-18 | ✅ |
| NetBeans | 2026-05-11 | ✅ |
| Thonny | 2026-04-25 | ✅ |
| gedit | 2026-03-27 | ✅ |
| Eclipse | 2026-03-12 | ✅ |
| 小龙 Dev-C++ | 2026-01-24 | ✅ |
| Red Panda C++ | 2025-11-30 | ✅ |
| PyScripter | 2025-11-11 | ✅ |
| Emacs | 2025-08-14 | ✅ |
| Geany | 2025-07-01 | ⚠️ 可能停更 |

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

## 自动更新说明

本项目通过 GitHub Actions 自动维护：
- **每天**：检查所有链接是否失效
- **每周日**：完整更新版本号、发布日期、链接检查、按时间排序
- **手动触发**：随时可运行完整更新

所有 27 个项目均已实现自动版本号获取：
- GitHub/GitLab 项目：通过 Release API 或 Tag 获取
- 非 GitHub 项目（Emacs/Geany/BlueJ/Lazarus/Sublime Text/nano/JetBrains系列/VS Community/Eclipse/Android Studio）：通过网页抓取获取

---

## 许可

MIT License - 欢迎自由使用和分享。

---

## 致谢

感谢 [JetBrains](https://www.jetbrains.com) 对全球开发者社区的无私贡献。

JetBrains 打造了 IntelliJ IDEA、PyCharm、WebStorm、CLion 等一系列伟大的开发工具，深刻影响了现代软件开发的方式。作为一名学生时，我曾受益于 JetBrains 的[免费学生授权](https://www.jetbrains.com/community/education/)，这些工具陪伴我走过了编程学习的关键阶段，对我帮助很大。

尽管目前已不再符合免费授权的条件，但我对 JetBrains 始终心怀感激。一个公司愿意长期为学生和开源社区提供免费的专业工具，这件事本身就值得尊敬。

> *"The best tools are the ones that make you better at what you do."*
