"""
植物大战僵尸 - 主入口
"""
import pygame
import sys
import os
import config
import ctypes

# Windows 高 DPI 感知（必须在 pygame.init() 之前）
ctypes.windll.shcore.SetProcessDpiAwareness(1)

os.environ['SDL_VIDEO_CENTERED'] = '1'
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

# ---- 修复 pygame 2.5 在 Windows 枚举注册表字体时，
#      遇到非字符串（int）字体值会 splitext() 崩溃的 bug ----
import winreg as _winreg
from os.path import splitext as _splitext, dirname as _dirname, join as _join
import pygame.sysfont as _sysfont

def _safe_initsysfonts_win32():
    fontdir = _join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")
    fonts = {}
    for domain in (_winreg.HKEY_LOCAL_MACHINE, _winreg.HKEY_CURRENT_USER):
        for sub in (r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts",
                    r"SOFTWARE\Microsoft\Windows\CurrentVersion\Fonts"):
            try:
                key = _winreg.OpenKey(domain, sub)
            except OSError:
                continue
            for i in range(_winreg.QueryInfoKey(key)[1]):
                try:
                    name, font, _ = _winreg.EnumValue(key, i)
                except OSError:
                    break
                if not isinstance(font, str):      # 关键：跳过 int 等非字符串条目
                    continue
                if _splitext(font)[1].lower() not in _sysfont.OpenType_extensions:
                    continue
                if not _dirname(font):
                    font = _join(fontdir, font)
                for n in name.split("&"):
                    _sysfont._parse_font_entry_win(n, font, fonts)
    return fonts

_sysfont.initsysfonts_win32 = _safe_initsysfonts_win32

# 窗口图标
pygame.display.set_icon(pygame.image.load("images/home/game_icon.png"))

info = pygame.display.Info()
WIN_W, WIN_H = info.current_w, info.current_h
screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.NOFRAME)
pygame.display.set_caption(config.WINDOW_TITLE)
print(f"屏幕: {info.current_w}x{info.current_h}  窗口: {WIN_W}x{WIN_H}")

from pages.home_page import HomePage
from pages.prepare_page import PreparePage
from pages.battle_page import BattlePage
from pages.loading_page import LoadingPage
import store.save as sv

# 根据当前关卡设置地图：1=白天, 2=夜晚, 3=泳池, 4=屋顶
_MAP = {1: "day", 2: "night", 3: "pool", 4: "roof"}
config.ACTIVE_MAP = _MAP.get(sv.load()["chapter"], "day")

current = LoadingPage(screen)
clock = pygame.time.Clock()
running = True

while running:
    dt = min(clock.tick(60), 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        current.handle_event(event)

    current.update(dt)

    if current.next_scene:
        next_name = current.next_scene
        if next_name == "home":
            config.SELECTED_PLANTS.clear()
            current = HomePage(screen)
        elif next_name == "select":
            current = PreparePage(screen)
        elif next_name == "battle":
            current = BattlePage(screen)

    current.draw()
    pygame.display.flip()

pygame.quit()
sys.exit()
