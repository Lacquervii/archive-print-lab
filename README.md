# Archive Print Lab / 旧档博物志

[![English](https://img.shields.io/badge/English-EN-lightgreen)](README.en.md)
[![中文](https://img.shields.io/badge/中文-CN-blue)](README.md)

> **AI 生图 Skill** — 把任意主题编译成可直接出图的编辑海报提示词。
> **AI image-generation skill** — compile any subject into a generator-ready editorial poster prompt.

## 这是什么风格？

一句话：**复古博物档案风的杂志封面海报** —— 像老式植物图鉴、博物馆档案卡，遇上现代杂志的排版。

每张图都保持同一套骨架：

```text
巨型衬线大标题压住上方（约占画面 1/3 到 1/2）
+ 主题物完整、紧凑地居中（花、树、器物……）
+ 纸张/印刷质感做底，带一点旧档案的味道
+ 散布小标注、刻度、十字标记，像图鉴里的索引
+ 右下角一块安静的留白释放区
```

就像博物馆里一张精工细作的专题档案卡：大标题、居中标本、印刷细部、安静落款。换主题时只换「标本」和颜色气质，骨架不变。

## 输入与输出

输入一个主题（向日葵、油灯、满天星、红玫瑰……），输出一条可直接丢给生图模型的提示词：

```text
/archive-print-lab 用 Image2 生成一张向日葵
/archive-print-lab 为油灯写一张海报提示词
/archive-print-lab 制作一份关于满天星的磨砂编辑封面
```

支持 Image2 / gpt-image-2、Midjourney、Flux、SDXL、Stable Diffusion、ComfyUI、Gemini 及消费级图像工具。

## 功能

- **生图提示词编译器**：将物体、植物、器物、材质和编辑主题编译为可直接使用的图像提示词。
- **生成器无关**：无需指定具体图像模型即可工作；默认交付物为可直接使用的提示词。
- 仅在指定生成器时适配提示词语法，保留强烈的标题、中央事件和接触场压力。
- 在原生图像生成中，精确文字排版本质上是近似的；提示词会保持显示文字简短，并如实报告这一局限。

## 画廊 —— 生成效果示例

| 图片 | 主题 | 描述 |
|------|------|------|
| ![向日葵](examples/sunflower.png) | 向日葵 | 暖调模拟印刷——金黄花瓣、深色种盘、夏至光线。 |
| ![满天星](examples/babys-breath.png) | 满天星 | 当代冷灰弥散——轻盈枝条上的白色小花，矿物冷光。 |
| ![百合](examples/lily-pink.png) | 百合 | 柔和粉彩编辑——粉色花瓣、斑点花喉、温柔渐变。 |
| ![百合](examples/lily-stargazer.png) | 百合 | 梦幻弥散——暖粉色调、光感氛围。 |
| ![油灯](examples/oil-lamp.png) | 油灯 | 暖调模拟印刷——黄铜底座、琥珀燃油、燃烧灯芯。 |
| ![树](examples/tree.png) | 树 | 泥土模拟——扭曲树干、苔藓树冠、年轮与分叉标注。 |
| ![雏菊](examples/daisy.png) | 雏菊 | 当代冷灰弥散——白色花瓣、金色花心，结构平衡。 |
| ![梅花](examples/plum-blossom.png) | 梅花 | 精致编辑——淡粉花瓣、霜色背景、分叉与花苞。 |
| ![玫瑰](examples/rose.png) | 玫瑰 | 材质档案——绒面花瓣、带刺茎干、植物学精确。 |

## 使用

以 `SKILL.md` 为入口。它路由任务、编译主题与色板、规划构图，然后产出一条生成器就绪的提示词。

## 校验

```sh
python3 scripts/validate_skill.py
```

## 发布

打包的 v5.1.0 归档位于 [`releases/`](releases/)。

## 许可

尚未选择许可证。在接受外部贡献或复用之前请添加一个。