"""
首页场景 —— 背景 + 开始游戏按钮
"""
import pygame, sys
import config
import asset_manager
from asset_manager import load_image, fit_background
from comment import make_hover, crop_visible, build_popup, draw_popup, hit_popup_btn

# 模块级缓存：避免每次切回首页重新 smoothscale + mask
_home_cache = {}


def precompute_home(w, h):
    """预计算首页所有资源（缩放 + mask），存入缓存"""
    key = (w, h)
    if key in _home_cache:
        return

    raw_bg = load_image(config.HOME_BG)
    bg, bg_ox, bg_oy, bg_scale = fit_background(raw_bg, w, h)

    btns = []
    for cfg in config.HOME_BTNS:
        img = load_image(cfg["file"])
        bw, bh = img.get_width(), img.get_height()
        bw2, bh2 = int(bw * bg_scale), int(bh * bg_scale)
        surf = pygame.transform.smoothscale(img, (bw2, bh2))
        cropped, cx, cy = crop_visible(surf)
        mask = pygame.mask.from_surface(cropped)
        hover = make_hover(cropped)
        dx = int(cfg["ox"] * bg_scale)
        dy = int(cfg["oy"] * bg_scale)
        btns.append({
            "surf":  cropped,
            "hover": hover,
            "mask":  mask,
            "rect":  pygame.Rect(bg_ox + dx + cx, bg_oy + dy + cy,
                                 cropped.get_width(), cropped.get_height()),
            "click": cfg.get("click", False),
        })

    popups = {}
    for idx, bg_file, btns_cfg in [
        (11, "button12_1.png", [("button12_2.png", None), ("button12_3.png", "close")]),
        (12, "button13_1.png", [("button13_2.png", "close")]),
        (13, "button14_1.png", [("button14_2.png", "close"), ("button14_3.png", "quit")]),
    ]:
        popups[idx] = build_popup(bg_file, btns_cfg, w, h)
    quit_popup = build_popup(
        "button14_1.png", [("button14_2.png", "close"), ("button14_3.png", "quit")], w, h)

    _home_cache[key] = {
        "bg_info": (bg, bg_ox, bg_oy, bg_scale),
        "btns": btns, "popups": popups, "quit_popup": quit_popup,
    }

    # 释放首页专属的原始图缓存（弹窗图共用，不能删）
    asset_manager._cache.pop(config.HOME_BG, None)
    for cfg in config.HOME_BTNS:
        asset_manager._cache.pop(cfg["file"], None)


class HomePage:
    def __init__(self, screen):
        self.screen = screen
        self.w, self.h = screen.get_size()

        c = _home_cache[(self.w, self.h)]
        self.bg, self.bg_ox, self.bg_oy, self.bg_scale = c["bg_info"]
        self.btns = c["btns"]
        self._popups = c["popups"]
        self._quit_popup = c["quit_popup"]

        self._show_popup = False
        self._popup_data = None
        self._show_esc = False
        self.next_scene = None

    def _hit_btn(self, x, y):
        """返回像素命中的按钮，无命中返回 None"""
        for b in self.btns:
            if b["rect"].collidepoint(x, y):
                lx, ly = x - b["rect"].x, y - b["rect"].y
                if b["mask"].get_at((lx, ly)):
                    return b
        return None

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self._show_esc = not self._show_esc
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._show_esc:
                self._handle_popup(event.pos, self._quit_popup, is_esc=True)
                return
            if self._show_popup:
                self._handle_popup(event.pos, self._popup_data)
                return
            b = self._hit_btn(*event.pos)
            if b:
                idx = self.btns.index(b)
                if b["click"]:
                    self.next_scene = "select"
                if idx in self._popups:
                    self._show_popup = True
                    self._popup_data = self._quit_popup if idx == 13 else self._popups[idx]

    def _handle_popup(self, pos, data, is_esc=False):
        pb = hit_popup_btn(pos, data)
        if pb:
            if pb["action"] == "close":
                if is_esc:
                    self._show_esc = False
                else:
                    self._show_popup = False
            elif pb["action"] == "quit":
                pygame.quit()
                sys.exit()

    def update(self, dt):
        pass

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        mx, my = pygame.mouse.get_pos()
        hit = None if (self._show_popup or self._show_esc) else self._hit_btn(mx, my)
        for b in self.btns:
            s = b["hover"] if b is hit else b["surf"]
            self.screen.blit(s, b["rect"])

        if self._show_popup and not self._show_esc:
            draw_popup(self.screen, self._popup_data, self.w, self.h)
        if self._show_esc:
            draw_popup(self.screen, self._quit_popup, self.w, self.h)
