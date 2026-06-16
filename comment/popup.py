"""
弹窗组件 —— 构建、绘制、命中
"""
import pygame
import asset_manager
from asset_manager import load_image
from comment.button import make_hover

# 弹窗缓存：{(key): data}，窗口尺寸不变时复用缩放结果
_popup_cache = {}


def build_popup(bg_file, btns_cfg, win_w, win_h):
    """加载弹窗图片，缩放居中，生成按钮列表"""
    key = (bg_file, tuple((f, a) for f, a in btns_cfg), win_w, win_h)
    if key in _popup_cache:
        return _popup_cache[key]

    bg_img = load_image("images/home/" + bg_file)
    pw, ph = bg_img.get_width(), bg_img.get_height()
    ps = min(win_w / pw, win_h / ph)
    pw2, ph2 = int(pw * ps), int(ph * ps)
    popup_bg = pygame.transform.smoothscale(bg_img, (pw2, ph2))
    popup_rect = pygame.Rect((win_w - pw2) // 2, (win_h - ph2) // 2, pw2, ph2)

    popup_btns = []
    for fname, action in btns_cfg:
        bimg = load_image("images/home/" + fname)
        bw, bh = bimg.get_width(), bimg.get_height()
        bw2, bh2 = int(bw * ps), int(bh * ps)
        srf = pygame.transform.smoothscale(bimg, (bw2, bh2))
        popup_btns.append({
            "action": action,
            "surf": srf,
            "hover": make_hover(srf),
            "mask": pygame.mask.from_surface(srf),
            "rect": pygame.Rect(popup_rect.x, popup_rect.y, bw2, bh2),
        })

    # 释放弹窗原始图缓存（已缩放完毕）
    asset_manager._cache.pop("images/home/" + bg_file, None)
    for fname, _ in btns_cfg:
        asset_manager._cache.pop("images/home/" + fname, None)

    data = {"bg": popup_bg, "rect": popup_rect, "btns": popup_btns}
    _popup_cache[key] = data
    return data


def draw_popup(screen, data, win_w, win_h):
    """绘制弹窗：半透明遮罩 + 背景 + 按钮（含悬停变亮）
    参数:
        screen:  pygame display surface
        data:    build_popup 的返回结果
        win_w, win_h: 窗口尺寸
    """
    overlay = pygame.Surface((win_w, win_h), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))
    screen.blit(data["bg"], data["rect"])

    mx, my = pygame.mouse.get_pos()
    for pb in data["btns"]:
        r = pb["rect"]
        hit = False
        if r.collidepoint(mx, my):
            hit = bool(pb["mask"].get_at((mx - r.x, my - r.y)))
        screen.blit(pb["hover"] if hit else pb["surf"], r)


def hit_popup_btn(pos, data):
    """检测鼠标点击命中了弹窗的哪个按钮
    参数:
        pos:  (mx, my) 鼠标屏幕坐标
        data: build_popup 的返回结果
    返回:
        命中的按钮 dict (含 action), 未命中返回 None
    """
    for pb in data["btns"]:
        r = pb["rect"]
        if r.collidepoint(pos):
            lx, ly = pos[0] - r.x, pos[1] - r.y
            if pb["mask"].get_at((lx, ly)):
                return pb
    return None
