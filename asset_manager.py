"""
资源管理器 —— 按需加载 + LRU 缓存
"""
import pygame
import os


_cache = {}       # {"path": Surface}


def load_image(path):
    """加载图片，自动缓存。路径为空/不存在返回 None"""
    if not path:
        return None
    if path in _cache:
        return _cache[path]
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        _cache[path] = img
        return img
    return None


def fit_background(image, target_w, target_h):
    """等比缩放居中，黑边填充。
    Returns: (surface, ox, oy, scale) 或 (None, 0, 0, 0)
    """
    if not image:
        return None, 0, 0, 0
    iw, ih = image.get_width(), image.get_height()
    scale = min(target_w / iw, target_h / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    scaled = pygame.transform.smoothscale(image, (nw, nh))
    bg = pygame.Surface((target_w, target_h))
    bg.fill((0, 0, 0))
    ox = (target_w - nw) // 2
    oy = (target_h - nh) // 2
    bg.blit(scaled, (ox, oy))
    return bg, ox, oy, scale


def load_map(map_cfg, target_h):
    """加载地图：裁切左侧 → 等比缩放到目标高度，裁后释放原图"""
    path = map_cfg["file"]
    img = load_image(path)
    if not img:
        return None, 0
    iw, ih = img.get_width(), img.get_height()
    crop = map_cfg.get("crop_left", 0)
    if crop > 0:
        cx = int(iw * crop)
        img = img.subsurface(pygame.Rect(cx, 0, iw - cx, ih)).copy()  # copy释放原图引用
        _cache.pop(path, None)
    scale = target_h / ih
    nw = int((iw - int(iw * crop)) * scale) if crop > 0 else int(iw * scale)
    return pygame.transform.smoothscale(img, (nw, target_h)), nw


def clear_cache():
    """清空缓存（切场景时调用）"""
    _cache.clear()
