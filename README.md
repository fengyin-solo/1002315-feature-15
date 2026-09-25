# 舞台演出巡演制作平台

面向剧目创排、演员档期、舞台装置、灯光音响与巡演运输装卸的一体化演出制作后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 演出项目 | `show` | 演出项目 | 项目编号、剧目名称、演出类型 |
| 剧目 | `repertoire` | 剧目 | 剧目编号、剧目名称、剧种 |
| 排练计划 | `rehearsal` | 排练计划 | 排练编号、关联剧目、排练类型 |
| 演员档期 | `actor` | 演员档期 | 档期编号、演员姓名、所属院团 |
| 乐队伴奏 | `band` | 乐队 | 乐队编号、乐队名称、编制人数 |
| 舞台装置 | `stage` | 舞台装置 | 装置编号、装置名称、所属剧目 |
| 灯光设备 | `lighting` | 灯光设备 | 设备编号、设备类型、设备型号 |
| 音响设备 | `sound` | 音响设备 | 设备编号、设备类型、额定功率 |
| 服装道具 | `costume` | 服装道具 | 服装编号、服装名称、所属剧目 |
| 化妆造型 | `makeup` | 化妆造型 | 造型编号、饰演角色、造型类型 |
| 巡演路线 | `tour` | 巡演路线 | 路线编号、巡演项目、途经城市 |
| 舞美运输 | `freight` | 舞美运输单 | 运输编号、关联巡演、运输内容 |
| 装台卸台 | `loadin` | 装台作业 | 作业编号、演出场馆、作业类型 |
| 安全预案 | `safety` | 安全预案 | 预案编号、关联演出、预案类型 |
| 演出日志 | `showlog` | 演出日志 | 日志编号、演出场次、演出日期 |
| 演出结算 | `settle` | 演出结算单 | 结算编号、关联场次、演出收入 |
| 报批备案 | `permit` | 报批备案单 | 报批编号、关联演出、报批类型 |
| 宣传推广 | `media` | 宣传推广单 | 推广编号、关联演出、推广渠道 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
