# Archive Print Lab / 旧档博物志

[![English](https://img.shields.io/badge/English-EN-lightgreen)](README.md)
[![中文](https://img.shields.io/badge/中文-CN-blue)](README.zh.md)

> **AI 生图 Skill** — 把任意主题编译成可直接出图的编辑海报提示词。
> **AI image-generation skill** — compile any subject into a generator-ready editorial poster prompt.

一个与生成器无关的提示词编译系统，基于稳定的 **9010 衍生编辑封面家族**。输入一个主题（植物、物体、器物、材质、编辑主题），即可输出结构化的生成提示词，让 Image2 / gpt-image-2、Midjourney、Flux、SDXL、Stable Diffusion、ComfyUI、Gemini 及消费级图像工具产出同家族的编辑海报。

## 核心视觉契约

```text
超大高对比度衬线标题
+ 紧凑完整的中央主体事件
+ 不等距接触印刷场
+ 稀疏的学科专属索引标记
+ 安静的右下角作者释放区
+ 小写 `archive-print-lab` 编辑出版署名
```

该家族在保持页面语法稳定的同时，为每个新主题重新编排主体、色板、材质证明、结构载体和释放区。

## 功能

- **生图提示词编译器**：将物体、植物、器物、材质和编辑主题编译为可直接使用的图像提示词。
- **生成器无关**：无需指定具体图像模型即可工作；默认交付物为可直接使用的提示词。
- 仅在指定生成器时适配提示词语法，支持 Image2 / gpt-image-2、Midjourney、Flux、SDXL、Stable Diffusion、ComfyUI、Gemini 及消费级图像工具。
- 使用可选的 Image2 编辑适配器，在原生图像输出中保留强烈的标题、中央事件和接触场压力。

## 规范路径

```yaml
series: 9010-derived-editorial-family
mode: concentrated_cover
recipe: concentrated_editorial_cover
chassis: structural
ratio: 16:9
```

普通请求下，家族保留：

1. 占主导地位的上方标题平面；
2. 宽大、紧凑、深色锚定的中央事件；
3. 主/辅/回返接触场；
4. 柔软材质体量与清晰印刷结构的对比；
5. 连通的右下角释放区，带有小字 `archive-print-lab` 出版署名。

## 画廊 —— 生成效果示例 / Gallery

| 图片 | 主题 | 描述 |
|------|------|------|
| ![向日葵](examples/sunflower.png) | 向日葵 Sunflower | 暖调模拟印刷——金黄花瓣、深色种盘、夏至光线。 |
| ![满天星](examples/babys-breath.png) | 满天星 Gypsophila | 当代冷灰弥散——轻盈枝条上的白色小花，矿物冷光。 |
| ![百合](examples/lily-pink.png) | 百合 Lily | 柔和粉彩编辑——粉色花瓣、斑点花喉、温柔渐变。 |
| ![百合](examples/lily-stargazer.png) | 百合 Lily | 梦幻弥散——暖粉色调、光感氛围。 |
| ![油灯](examples/oil-lamp.png) | 油灯 Oil Lamp | 暖调模拟印刷——黄铜底座、琥珀燃油、燃烧灯芯。 |
| ![树](examples/tree.png) | 树 Tree | 泥土模拟——扭曲树干、苔藓树冠、年轮与分叉标注。 |
| ![雏菊](examples/daisy.png) | 雏菊 Daisy | 当代冷灰弥散——白色花瓣、金色花心，结构平衡。 |
| ![梅花](examples/plum-blossom.png) | 梅花 Plum Blossom | 精致编辑——淡粉花瓣、霜色背景、分叉与花苞。 |
| ![玫瑰](examples/rose.png) | 玫瑰 Rose | 材质档案——绒面花瓣、带刺茎干、植物学精确。 |

## 使用

以 `SKILL.md` 为入口。它路由任务、编译主题与色板、规划构图，然后产出一条生成器就绪的提示词。

```text
/archive-print-lab 用 Image2 生成一张向日葵
/archive-print-lab 为油灯写一张海报提示词
/archive-print-lab 制作一份关于满天星的磨砂编辑封面
```

在原生图像生成中，精确的文字排版本质上是近似的；提示词会保持显示文字简短，并如实报告这一局限。

## 校验

```sh
python3 scripts/validate_skill.py
```

## 发布

打包的 v5.1.0 归档位于 [`releases/`](releases/)。

## 许可

尚未选择许可证。在接受外部贡献或复用之前请添加一个。
