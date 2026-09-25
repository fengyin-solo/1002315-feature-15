<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">舞台演出巡演制作平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向剧目创排、演员档期、舞台装置、灯光音响与巡演运输装卸的一体化演出制作后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "演出项目", path: "/show" }, { label: "剧目", path: "/repertoire" }, { label: "排练计划", path: "/rehearsal" }, { label: "演员档期", path: "/actor" }, { label: "乐队伴奏", path: "/band" }, { label: "舞台装置", path: "/stage" }, { label: "灯光设备", path: "/lighting" }, { label: "音响设备", path: "/sound" }, { label: "服装道具", path: "/costume" }, { label: "化妆造型", path: "/makeup" }, { label: "巡演路线", path: "/tour" }, { label: "舞美运输", path: "/freight" }, { label: "装台卸台", path: "/loadin" }, { label: "安全预案", path: "/safety" }, { label: "演出日志", path: "/showlog" }, { label: "演出结算", path: "/settle" }, { label: "报批备案", path: "/permit" }, { label: "宣传推广", path: "/media" }]
</script>
