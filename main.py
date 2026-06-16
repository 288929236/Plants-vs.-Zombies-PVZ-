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
