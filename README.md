<div align="center">

# 店小秘 · TEMU 全托 / 半托 自动上品

**把「引用模板 → 切片图 → 变种 → 属性 → 描述 → 主题 → 自检 → 发布」整条流水线交给程序跑**

![最近提交](https://img.shields.io/github/last-commit/hund111/dianxiaomi-temu-uploader?style=flat-square&label=%E6%9C%80%E8%BF%91%E6%8F%90%E4%BA%A4)
![提交活跃度](https://img.shields.io/github/commit-activity/m/hund111/dianxiaomi-temu-uploader?style=flat-square&label=%E6%AF%8F%E6%9C%88%E6%8F%90%E4%BA%A4)
![Issues](https://img.shields.io/github/issues/hund111/dianxiaomi-temu-uploader?style=flat-square)
![Stars](https://img.shields.io/github/stars/hund111/dianxiaomi-temu-uploader?style=flat-square)
![状态](https://img.shields.io/badge/%E7%8A%B6%E6%80%81-%E5%8F%AF%E7%94%A8-brightgreen?style=flat-square)

</div>

> 仅用于自有店铺的日常上新，请遵守店小秘与 TEMU 的平台规则；本项目不包含任何绕过平台风控的手段。

---

## 项目动态

<!-- ACTIVITY:START -->

> 下面的表格由 GitHub Actions 自动维护 · 仓库累计提交 **17** 次

| 日期 | 提交信息 | 作者 | 提交 |
|---|---|---|---|
| 2026-11-27 | chore(deps): 补齐 Pillow 与 pywinstyles（仅 Windows… | hund111 | [`9952f8b`](https://github.com/hund111/dianxiaomi-temu-uploader/commit/9952f8b7554e48545b42592372c6cb3f77d5d045) |
| 2026-11-27 | docs: 更新到 v1.4（描述切片 / 主题 / 记忆 / 动态界面） | hund111 | [`cbf1717`](https://github.com/hund111/dianxiaomi-temu-uploader/commit/cbf1717e2999a757ab5b534500e251087c59c52a) |
| 2026-11-27 | fix(activity): 恢复完整脚本（上一步误覆盖）并修正说明行空格 | hund111 | [`ae9d25e`](https://github.com/hund111/dianxiaomi-temu-uploader/commit/ae9d25eb7984f9b31c19adadf4e50836281b19d3) |
| 2026-11-27 | style(activity): 修正说明行空格 | hund111 | [`1047284`](https://github.com/hund111/dianxiaomi-temu-uploader/commit/1047284defabf0978674be3698ee9c97d67f12e7) |
| 2026-11-27 | fix(activity): 过滤机器人提交、去掉每次变化的时间戳，避免无意义提交 | hund111 | [`aa89dc3`](https://github.com/hund111/dianxiaomi-temu-uploader/commit/aa89dc3182df445405ba63a3d4d39faf0196b07b) |

<sub>自动机器人的提交不计入本表；工作流文件：`.github/workflows/update-activity.yml`。</sub>
<!-- ACTIVITY:END -->

---

## 它解决什么问题

店小秘上架 TEMU 全托/半托产品时，一款商品要重复点十几步：引用模板、删旧图、传 7 张切片、填 4~5 行变种与变种图、补产品属性、插商品描述图、选主题、传外包装、传视频、自检、发布。手工一款 5 分钟起步，几十款就是一整天。

这个工具把这些步骤编排成一条可无人值守的流水线，并且**每一步都会核对页面真实状态**再往下走，失败会留截图与日志，而不是静默跳过。

## 功能

- **浏览器内核自适应**：本机有 Chrome 就用 Chrome；只有 Microsoft Edge 时自动切换 Edge（同为 Chromium 内核，点击逻辑完全复用）
- **轮播图**：启动时拦截系统文件选择框，直接把本地路径交给页面（多张一次进）；上传前逐张清掉模板旧图，传完自动全选
- **变种表**：行数 / 尺码 / 申报价格全部跟随引用模板，脚本只写两样——SKU 货号与每行变种图（引用轮播图第 N 张）
- **产品属性**：是否画布类 / 画布材质 / 框架类型 缺项自动补齐
- **商品描述套用切片图**：自动走「编辑描述 → 批量操作 → 批量传图 → 本地上传」，把整套详情切片一次排进描述区；只挑宽高 ≥480、比例 0.5~2、≤10M 的图，失败只记日志不影响发布
- **按表格换主题**：读取标题表格的「主题」列（自动识别 主题 / 产品主题 / Theme），发布前在商品属性里把主题下拉改成对应值；下拉藏在「其他属性」折叠区时会先自动展开，选完再回读校验
- **上次匹配记忆**：自动保存上一次的款号、切片目录与张数、外包装/视频、描述插图数、主题与结果，下次启动在运行日志里直接提示
- **动态界面**：自绘底栏与圆角按钮、流光进度条、呼吸灯状态点，浅色/深色一键切换，Win11 下带云母玻璃底
- **发布结果识别**：认「产品已提交发布」弹窗，成功后把表格 A 列写回 OK，下次自动跳过
- **图片空间自管**：用量达到阈值（默认 280M）自动清空，清空前会确认采集箱/待发布为空
- **多店铺轮转**：店铺栏留空取下拉第一个；填多个用逗号分隔，按商品序号轮流用，各自用自己收藏里的模板
- **试跑 / 真发**：界面上琥珀色 = 只填不发布，红色 = 会真的提交，避免误点
- **一键启动**：封装成单文件 exe，双击即可用，不用装 Python；另附 `启动软件.bat` 做环境自检兜底
- **命令行**：`--run` 后台跑、`--check` 只做素材自检、`--only` 指定款、`--limit` 限量、`--visible` 开窗看着跑

## 快速开始

1. 环境：Windows 10/11，Chrome 或 Microsoft Edge 任一；产品页需要已登录店小秘
2. 直接双击 `店小秘上品.exe` 即可（单文件封装，自带 Python 运行时）
   源码方式：Python 3.12+，先 `pip install -r requirements.txt`，再 `python 店小秘上品.py`
3. 首次打开后按自己机器改四个路径：`image_path`（切片图目录，一款一个文件夹）、`xlsx_path`（标题表格）、`package_path`（外包装图）、`video_path`（视频）
4. 登录态：把店小秘的 Cookie 粘进「Cookie 登录态」保存，或点「浏览器里新抓」
5. **第一次一定先试跑**：勾上「试跑（只填不发布）」，「本次只跑前 N 个」填 1，点开始；到店小秘页面核对轮播图、变种、属性、描述、主题都在，再取消勾选批量跑。

## 目录结构

```text
.
├─ 店小秘上品.py          # 主程序（GUI + 引擎 + 命令行）
├─ ui_dynamics.py         # 动态界面组件（自绘按钮 / 流光条 / 呼吸灯 / 深浅色）
├─ 店小秘上品.exe         # 单文件封装版（双击即用，不用装 Python）
├─ 启动软件.bat           # 源码启动：找 Python + 依赖自检
├─ 后台运行.bat           # 无窗口后台跑
├─ 排错启动.bat           # 窗口一闪就退时用它看报错
├─ 清理缓存.bat           # 清浏览器缓存与临时目录
├─ 打包exe.bat            # 重新打单文件 exe
├─ config.json            # 运行配置（路径、开关、试跑/真发）——不要提交
├─ cookies.json           # 店小秘登录态——不要提交
├─ requirements.txt
├─ logs/                  # 后台运行.log / error.log / 失败截图
└─ scripts/
   └─ update_activity.py  # 自动生成 README 的「项目动态」
```

## 常见问题

| 现象 | 原因 | 处理 |
|---|---|---|
| `cannot find Chrome binary` | 本机没装 Chrome | 装 Chrome，或让脚本自动切 Edge（v1.2 起内置兜底） |
| 轮播图「已选 0 张」 | 系统文件框没被拦截 | 看 `logs/error.log`，确认浏览器是以脚本方式启动的 |
| 发布被拦「请选择分类 / 外包装类型」 | 引用模板缺必填 | 在店小秘里把模板补全，脚本不改模板 |
| 描述区没出现切片 | 图太小或比例不对 | 宽高 ≥480、宽÷高在 0.5~2、单张 ≤10M；日志会列出被跳过的文件 |
| 主题没改成功 | 该值不在下拉可选项里 | 日志会打出「主题」可选项清单；表格里换成清单里的原词即可 |
| 双击 exe 没反应 | 被杀软/权限拦了 | 用 `排错启动.bat` 看报错，或右键 exe「以管理员身份运行」 |
| 列表一直「发布中」 | 平台侧排队 | 正常，2 小时内出结果，别急着判失败 |

## 版本记录

| 日期 | 版本 | 说明 |
|---|---|---|
| 2026-11-27 | v1.4 | 商品描述一键插切片图；按表格「主题」列换主题；上次匹配记忆；动态界面与体积精简（1.2 GB → 约 45 MB，浏览器配置移到 AppData） |
| 2026-11-27 | v1.3 | 界面重做：卡片式三栏布局、状态药丸、真发/试跑醒目标识 |
| 2026-11-26 | v1.2 | 无 Chrome 时自动改用 Microsoft Edge 运行 |
| 2026-11-17 | v1.1 | 补齐图片空间自动清理、产品属性补填、模板跟随 |

## 许可

All rights reserved. 未授权请勿二次分发或商用；需要源码授权请联系作者。
