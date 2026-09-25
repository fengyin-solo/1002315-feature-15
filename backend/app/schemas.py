"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class ShowEntry(BaseModel):
    """演出项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 剧目名称
    field_2: str | None = None  # 演出类型
    field_3: str | None = None  # 演出场次
    field_4: str | None = None  # 巡演城市
    field_5: str | None = None  # 制作单位
    field_6: str | None = None  # 首演日期
    field_7: str | None = None  # 项目状态

class RepertoireEntry(BaseModel):
    """剧目明细结构。"""

    field_0: str | None = None  # 剧目编号
    field_1: str | None = None  # 剧目名称
    field_2: str | None = None  # 剧种
    field_3: str | None = None  # 演出时长
    field_4: str | None = None  # 幕次结构
    field_5: str | None = None  # 首演年份
    field_6: str | None = None  # 主创团队
    field_7: str | None = None  # 剧目状态

class RehearsalEntry(BaseModel):
    """排练计划明细结构。"""

    field_0: str | None = None  # 排练编号
    field_1: str | None = None  # 关联剧目
    field_2: str | None = None  # 排练类型
    field_3: str | None = None  # 排练场地
    field_4: str | None = None  # 计划时段
    field_5: str | None = None  # 参与人数
    field_6: str | None = None  # 排练次数
    field_7: str | None = None  # 排练状态

class ActorEntry(BaseModel):
    """演员档期明细结构。"""

    field_0: str | None = None  # 档期编号
    field_1: str | None = None  # 演员姓名
    field_2: str | None = None  # 所属院团
    field_3: str | None = None  # 饰演角色
    field_4: str | None = None  # 档期起止
    field_5: str | None = None  # 排练场次
    field_6: str | None = None  # 联系电话
    field_7: str | None = None  # 档期状态

class BandEntry(BaseModel):
    """乐队明细结构。"""

    field_0: str | None = None  # 乐队编号
    field_1: str | None = None  # 乐队名称
    field_2: str | None = None  # 编制人数
    field_3: str | None = None  # 乐器配置
    field_4: str | None = None  # 指挥姓名
    field_5: str | None = None  # 排练次数
    field_6: str | None = None  # 演出场次
    field_7: str | None = None  # 乐队状态

class StageEntry(BaseModel):
    """舞台装置明细结构。"""

    field_0: str | None = None  # 装置编号
    field_1: str | None = None  # 装置名称
    field_2: str | None = None  # 所属剧目
    field_3: str | None = None  # 结构形式
    field_4: str | None = None  # 尺寸规格
    field_5: str | None = None  # 搭建人员
    field_6: str | None = None  # 搭建日期
    field_7: str | None = None  # 装置状态

class LightingEntry(BaseModel):
    """灯光设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备类型
    field_2: str | None = None  # 设备型号
    field_3: str | None = None  # 通道数量
    field_4: str | None = None  # 所属剧目
    field_5: str | None = None  # 上次检修日
    field_6: str | None = None  # 责任人
    field_7: str | None = None  # 设备状态

class SoundEntry(BaseModel):
    """音响设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备类型
    field_2: str | None = None  # 额定功率
    field_3: str | None = None  # 通道数量
    field_4: str | None = None  # 所属剧目
    field_5: str | None = None  # 上次调试日
    field_6: str | None = None  # 调试人员
    field_7: str | None = None  # 设备状态

class CostumeEntry(BaseModel):
    """服装道具明细结构。"""

    field_0: str | None = None  # 服装编号
    field_1: str | None = None  # 服装名称
    field_2: str | None = None  # 所属剧目
    field_3: str | None = None  # 饰演角色
    field_4: str | None = None  # 尺码
    field_5: str | None = None  # 制作日期
    field_6: str | None = None  # 清洗次数
    field_7: str | None = None  # 服装状态

class MakeupEntry(BaseModel):
    """化妆造型明细结构。"""

    field_0: str | None = None  # 造型编号
    field_1: str | None = None  # 饰演角色
    field_2: str | None = None  # 造型类型
    field_3: str | None = None  # 化妆品清单
    field_4: str | None = None  # 造型师
    field_5: str | None = None  # 试妆日期
    field_6: str | None = None  # 定妆日期
    field_7: str | None = None  # 造型状态

class TourEntry(BaseModel):
    """巡演路线明细结构。"""

    field_0: str | None = None  # 路线编号
    field_1: str | None = None  # 巡演项目
    field_2: str | None = None  # 途经城市
    field_3: str | None = None  # 演出场馆
    field_4: str | None = None  # 演出场次
    field_5: str | None = None  # 首站日期
    field_6: str | None = None  # 末站日期
    field_7: str | None = None  # 路线状态

class FreightEntry(BaseModel):
    """舞美运输单明细结构。"""

    field_0: str | None = None  # 运输编号
    field_1: str | None = None  # 关联巡演
    field_2: str | None = None  # 运输内容
    field_3: str | None = None  # 车辆数量
    field_4: str | None = None  # 运输方式
    field_5: str | None = None  # 启运日期
    field_6: str | None = None  # 到达日期
    field_7: str | None = None  # 运输状态

class LoadinEntry(BaseModel):
    """装台作业明细结构。"""

    field_0: str | None = None  # 作业编号
    field_1: str | None = None  # 演出场馆
    field_2: str | None = None  # 作业类型
    field_3: str | None = None  # 计划时段
    field_4: str | None = None  # 作业班组
    field_5: str | None = None  # 参与人数
    field_6: str | None = None  # 完成时间
    field_7: str | None = None  # 作业状态

class SafetyEntry(BaseModel):
    """安全预案明细结构。"""

    field_0: str | None = None  # 预案编号
    field_1: str | None = None  # 关联演出
    field_2: str | None = None  # 预案类型
    field_3: str | None = None  # 风险等级
    field_4: str | None = None  # 应急措施
    field_5: str | None = None  # 责任人
    field_6: str | None = None  # 演练日期
    field_7: str | None = None  # 预案状态

class ShowlogEntry(BaseModel):
    """演出日志明细结构。"""

    field_0: str | None = None  # 日志编号
    field_1: str | None = None  # 演出场次
    field_2: str | None = None  # 演出日期
    field_3: str | None = None  # 观众人数
    field_4: str | None = None  # 演出时长
    field_5: str | None = None  # 异常情况
    field_6: str | None = None  # 记录人员
    field_7: str | None = None  # 日志状态

class SettleEntry(BaseModel):
    """演出结算单明细结构。"""

    field_0: str | None = None  # 结算编号
    field_1: str | None = None  # 关联场次
    field_2: str | None = None  # 演出收入
    field_3: str | None = None  # 场租费用
    field_4: str | None = None  # 人员费用
    field_5: str | None = None  # 运输费用
    field_6: str | None = None  # 结算金额
    field_7: str | None = None  # 结算状态

class PermitEntry(BaseModel):
    """报批备案单明细结构。"""

    field_0: str | None = None  # 报批编号
    field_1: str | None = None  # 关联演出
    field_2: str | None = None  # 报批类型
    field_3: str | None = None  # 受理单位
    field_4: str | None = None  # 提交日期
    field_5: str | None = None  # 批复日期
    field_6: str | None = None  # 批复文号
    field_7: str | None = None  # 报批状态

class MediaEntry(BaseModel):
    """宣传推广单明细结构。"""

    field_0: str | None = None  # 推广编号
    field_1: str | None = None  # 关联演出
    field_2: str | None = None  # 推广渠道
    field_3: str | None = None  # 物料类型
    field_4: str | None = None  # 投放日期
    field_5: str | None = None  # 触达人次
    field_6: str | None = None  # 负责人
    field_7: str | None = None  # 推广状态
