<div align="center">

# 店小秘 · TEMU 全托 / 半托 自动上品

**把「引用模板 → 切片图 → 变种 → 属性 → 自检 → 发布」整条流水线交给程序跑**

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

> 下面的表格由 GitHub Actions 自动维护· 仓库累计提交 **9** 次

| 日期 | 提交信息 | 作者 | 提交 |
|---|---|---|---|
| 2026-11-27 | fix(activity): 过滤机器人提交、去掉每次变化的时间戳，避免无意义提交 | hund111 | [`aa89dc3`](https://github.com/hund111/dianxiaomi-temu-uploader/commit/aa89dc3182df445405ba63a3d4d39faf0196b07b) |
| 2026-11-27 | chore: 增加 .gitignore（登录态与素材不入库） | hund111 | [`3f9ddda`](https://github.com/hund111/dianxiaomi-temu-uploader/commit/3f9ddda259987e518b6cc12f1ee74acf236564d0) |
| 2026-11-27 | chore: 增加依赖清单 | hund111 | [`baedd67`](https://github.com/hund111/dianxiaomi-temu-uploader/commit/baedd6782a83b4a765646334ffa9c56977ed6c23) |
| 2026-11-27 | feat: 增加项目动态生成脚本 | hund111 | [`9f4359d`](https://github.com/hund111/dianxiaomi-temu-uploader/commit/9f4359d60461b395c4c837963bef2927b281fcab) |
| 2026-11-27 | ci: 增加项目动态自动更新工作流 | hund111 | [`7ec582e`](https://github.com/hund111/dianxiaomi-temu-uploader/commit/7ec582e8d394eecdefb7e6696f4566cf2cfe0bad) |

<sub>自动机器人的提交不计入本表；工作流文件：`.github/workflows/update-activity.yml`。</sub>
<!-- ACTIVITY:END -->

---

## 它解决什么问题

店小秘上架 TEMU 全托/半托产品时，一款商品要重复点十几步：引用模板、删旧图、传 7 张切片、填 4~5 行变种与变种图、补产品属性、传外包装、传视频、自检、发布。手工一款 5 分钟起步，几十款就是一整天。

这个工具把这些步骤编排成一条可无人值守的流水线，并且**每一步都会核对页面真实状态**再往下走，失败会留截图与日志，而不是静默跳过。

## 功能

- **浏览器内核自适应**：本机有 Chrome 就用 Chrome；只有 Microsoft Edge 时自动切换 Edge（同为 Chromium 内核，点击逻辑完全复用）
- **轮播图**：启动时拦截系统文件选择框，直接把本地路径交给页面（多张一次进）；上传前逐张清掉模板旧图，传完自动全选
- **变种表**：行数 / 尺码 / 申报价格全部跟随引用模板，脚本只写两样——SKU 货号与每行变种图（引用轮播图第 N 张）
- **产品属性**：是否画布类 / 画布材质 / 框架类型 缺项自动补齐
- **发布结果识别**：认「产品已提交发布」弹窗，成功后把表格 A 列写回 OK，下次自动跳过
- **图片空间自管**：用量达到阈值（默认 280M）自动清空，清空前会确认采集箱/待发布为空
- **多店铺轮转**：店铺栏留空取下拉第一个；填多个用逗号分隔，按商品序号轮流用，各自用自己收藏里的模板
- **试跑 / 真发**：界面上琥珀色 = 只填不发布，红色 = 会真的提交，避免误点
- **命令行**：`--run` 后台跑、`--check` 只做素材自检、`--only` 指定款、`--limit` 限量、`--visible` 开窗看着跑

## 快速开始

1. 环境：Windows 10/11 + Python 3.12+，Chrome 或 Microsoft Edge 任一
2. 装依赖：

   ```bash
   pip install -r requirements.txt
   ```

3. 按你的机器改 `config.json` 里四个路径：`image_path`（切片图目录，一款一个文件夹）、`xlsx_path`（标题表格）、`package_path`（外包装图）、`video_path`（视频）
4. 启动界面：

   ```bash
   python 店小秘上品.py
   ```

5. **第一次一定先试跑**：勾上「试跑（只填不发布）」，「本次只跑前 N 个」填 1，点开始；到店小秘页面核对轮播图、变种、属性都在，再取消勾选批量跑。

## 目录结构

```text
.
├─ 店小秘上品.py          # 主程序（GUI + 引擎 + 命令行）
├─ config.json            # 运行配置（路径、开关、试跑/真发）
├─ cookies.json           # 店小秘登录态（不要提交到仓库）
├─ requirements.txt
├─ drivers/               # chromedriver（可选，缺省由 Selenium Manager 配）
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
| 列表一直「发布中」 | 平台侧排队 | 正常，2 小时内出结果，别急着判失败 |

## 版本记录

| 日期 | 版本 | 说明 |
|---|---|---|
| 2026-11-27 | v1.3 | 界面重做：卡片式三栏布局、状态药丸、真发/试跑醒目标识 |
| 2026-11-26 | v1.2 | 无 Chrome 时自动改用 Microsoft Edge 运行 |
| 2026-11-17 | v1.1 | 补齐图片空间自动清理、产品属性补填、模板跟随 |

## 许可

All rights reserved. 未授权请勿二次分发或商用；需要源码授权请联系作者。
