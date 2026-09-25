"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import show as router_show
from app.routers import repertoire as router_repertoire
from app.routers import rehearsal as router_rehearsal
from app.routers import actor as router_actor
from app.routers import band as router_band
from app.routers import stage as router_stage
from app.routers import lighting as router_lighting
from app.routers import sound as router_sound
from app.routers import costume as router_costume
from app.routers import makeup as router_makeup
from app.routers import tour as router_tour
from app.routers import freight as router_freight
from app.routers import loadin as router_loadin
from app.routers import safety as router_safety
from app.routers import showlog as router_showlog
from app.routers import settle as router_settle
from app.routers import permit as router_permit
from app.routers import media as router_media

ROUTERS = [router_show, router_repertoire, router_rehearsal, router_actor, router_band, router_stage, router_lighting, router_sound, router_costume, router_makeup, router_tour, router_freight, router_loadin, router_safety, router_showlog, router_settle, router_permit, router_media]
