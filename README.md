<p align="center">
  <img src="assets/archive-print-lab-cover.png" alt="Archive Print Lab / 旧档博物志：植物档案编辑封面" />
</p>

<h1 align="center">Archive Print Lab / 旧档博物志</h1>

<p align="center">
  <strong>把一个主题，编成一张有标题、有标本、有纸张气息的编辑印刷物。</strong><br />
  <em>A visual system for turning a subject into an authored editorial cover.</em>
</p>

<p align="center">
  <a href="releases/archive-print-lab-v5.1.0-generator-agnostic.tar.gz">下载 v5.1.0</a>
  · <a href="SKILL.md">阅读 Skill</a>
  · <a href="README.en.md">English</a>
</p>

<p align="center">
  <a href="releases/archive-print-lab-v5.1.0-generator-agnostic.tar.gz"><img src="https://img.shields.io/badge/version-5.1.0-4a4a4a" alt="Version 5.1.0" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-5b7553" alt="MIT License" /></a>
</p>

---

## 一张图，应该像一份被认真编过的档案

这不是把花、树或器物摆进一个好看的背景里。

旧档博物志让**巨型标题、完整主体、印刷载体、材料细节和被控制的留白**在同一张页面上彼此接触：标题不只是标题，主体不只是插图，留白也不是没画完的地方。

换主题时，花、器物、色板和纸面气质都会重新编写；不换的是这套页面关系。

> 一张好的结果，像一本尚未出版的专题图册里被抽出的一页：有主张，有材料，有秩序，也留下一点没有说尽的地方。

## 从一个词，到一张印刷物

| 你给出 | 旧档博物志在内部编排 | 你得到 |
|---|---|---|
| 向日葵、油灯、玫瑰、一种材料或一句主题 | 主体形态 · 标题尺度 · 接触场 · 新色板 · 纸面完成感 · 留白 | 一条可直接用于生成的视觉指令，以及清晰的构图与色板方向 |

例如，`油灯` 不会只变成一盏被摆着的灯。它会被理解为黄铜、琥珀燃油、玻璃灯罩、火焰和使用痕迹共同组成的中央事件；标题、印刷平面与安静的落款随后才有各自该待的位置。

## 30 秒开始

1. 下载 [v5.1.0 Skill 包](releases/archive-print-lab-v5.1.0-generator-agnostic.tar.gz)，或克隆本仓库。
2. 将整个 `archive-print-lab/` 放进你的 Skill 环境，或让 Agent 读取 [`SKILL.md`](SKILL.md)。
3. 直接说出主题：

```text
/archive-print-lab 用 Image2 生成一张向日葵
/archive-print-lab 为一盏油灯写一张海报提示词
/archive-print-lab 制作一份关于玫瑰的材质档案
```

没有明确指定气质时，系统会根据主题的材料、光线、时间感与观看目的决定画面完成感；你明确提出风格时，它会以你的要求为准。

## 固定的页面语法

```text
巨型标题
     ↕
印刷载体场 ←→ 完整、紧凑的中央主体
     ↕
材料体积 · 小型索引 · 安静的右下释放
```

| 页面角色 | 它负责什么 |
|---|---|
| **巨型标题** | 第一眼的阅读事件。它有分量，但不顶到边缘。 |
| **完整主体** | 花是一株花，器物是一件器物；先成为完整形态，再谈细部。 |
| **接触场** | 半透明平面、纸页、轮廓或印刷痕迹穿过主体，制造前后关系。 |
| **软 / 硬分离** | 花瓣、玻璃、树皮、金属保留材料体积；字、线、刻度保持印刷的清晰。 |
| **主题色板** | 每个主题重新取色，不挪用上一张图的情绪。 |
| **出版式释放** | 右下或侧下留出安静的延续，放下小型 `archive-print-lab` 署名，而不是堆装饰。 |

## 主题决定气质，不是预设模板

页面语法稳定，纸面气质随主题变化。通常由主题内部决定，也可以被你的明确要求覆盖。

| 完成面 | 感受 | 更容易契合的主题 |
|---|---|---|
| `contemporary_frosted` | 高亮矿物感、克制的雾面与冷光 | 白花、矿物、清冷空气 |
| `warm_analog_print` | 温暖纸张、节制的套印与网点痕迹 | 黄铜、琥珀、夏日植物 |
| `crisp_modern_graphic` | 明亮、清晰、边界更锐利 | 器械、几何、利落线条 |
| `material_archive` | 材料证据优先，强调绒面、纤维、蜡质或磨损 | 植物学、织物、手工艺、器物表面 |
| `custom` | 为一句明确的视觉要求让路 | 特定年代、情绪或媒介感 |

## 作品选辑

<table>
  <tr>
    <td width="33.33%" align="center" valign="top">
      <a href="examples/sunflower.png"><img src="assets/gallery/sunflower.jpg" alt="向日葵编辑海报" width="100%" /></a><br />
      <strong>向日葵</strong><br /><sub>金黄花瓣、深色种盘与夏至纸面。</sub>
    </td>
    <td width="33.33%" align="center" valign="top">
      <a href="examples/babys-breath.png"><img src="assets/gallery/babys-breath.jpg" alt="满天星编辑海报" width="100%" /></a><br />
      <strong>满天星</strong><br /><sub>白色小花、细枝网络与矿物冷光。</sub>
    </td>
    <td width="33.33%" align="center" valign="top">
      <a href="examples/oil-lamp.png"><img src="assets/gallery/oil-lamp.jpg" alt="油灯编辑海报" width="100%" /></a><br />
      <strong>油灯</strong><br /><sub>黄铜、琥珀燃油与被使用过的光。</sub>
    </td>
  </tr>
  <tr>
    <td width="33.33%" align="center" valign="top">
      <a href="examples/rose.png"><img src="assets/gallery/rose.jpg" alt="玫瑰编辑海报" width="100%" /></a><br />
      <strong>玫瑰</strong><br /><sub>绒面花瓣、刺与植物学式的近看。</sub>
    </td>
    <td width="33.33%" align="center" valign="top">
      <a href="examples/tree.png"><img src="assets/gallery/tree.jpg" alt="树编辑海报" width="100%" /></a><br />
      <strong>树</strong><br /><sub>树干、冠层、分叉与年轮的压力。</sub>
    </td>
    <td width="33.33%" align="center" valign="top">
      <a href="examples/plum-blossom.png"><img src="assets/gallery/plum-blossom.jpg" alt="梅花编辑海报" width="100%" /></a><br />
      <strong>梅花</strong><br /><sub>花苞、枝桠与近乎霜色的空气。</sub>
    </td>
  </tr>
</table>

> 这些是不同主题的生成样张，不是可以照搬的模板。每次新主题都会重新组织主体、色板、载体与留白。

## 它适合做什么

| 适合 | 不适合 |
|---|---|
| 植物、器物、材料、手工艺与单一主题 | 信息密集型图表或数据大屏 |
| 能压缩成一个中央视觉事件的内容 | 多人物、多地点的叙事场景 |
| 系列封面、专题海报、展览或出版主视觉 | 电商白底图、常规产品详情页 |
| 需要统一页面语言、但不想每张图长得一样的项目 | 要求图像模型一次写对长段文字的排版成品 |

## 关于文字与生成

原生图像生成中的文字通常是近似呈现：旧档博物志会把标题控制得短而有层级，但不承诺像素级准确的字形或排版。它优先保证的是页面关系、材料感与整体阅读顺序。

生成工具只是执行媒介，不是这套视觉方法的主角；在不同工具中使用时，保持短标题、明确画幅，并按工具要求调整参数即可。

<details>
<summary><strong>包结构与自校验</strong></summary>

```text
archive-print-lab/
├── SKILL.md                 # 主入口：视觉契约与工作流
├── manifest.json            # 包元数据
├── references/              # 主题、构图、完成面与审查规范
├── schemas/                 # 结构化记录
├── scripts/validate_skill.py
├── workflows/               # 操作检查清单
└── releases/                # 打包归档与校验和
```

```sh
python3 scripts/validate_skill.py
```

</details>

## 许可证

本项目采用 [MIT License](LICENSE)：你可以使用、修改和分发；请保留版权与许可声明。作者不承担使用后果。

---

<p align="center">
  <em>旧档博物志 · Archive Print Lab</em><br />
  Compiled with care. Pressed with intent.
</p>
