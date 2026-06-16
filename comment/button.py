"""
按钮组件 —— 悬停变亮、裁剪可见区、命中检测
"""
import pygame


def make_hover(surf):
    """在 surf 上叠加半透明白色，返回变亮版"""
    h = surf.copy()
    overlay = pygame.Surface(surf.get_size(), pygame.SRCALPHA)
    overlay.fill((80, 80, 80, 0))
    h.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
    return h


def crop_visible(surf):
    """裁剪表面，去掉四周透明区域
    返回: (cropped_surface, offset_x, offset_y)
    offset 是裁剪区在原图内的左上角坐标
    """
    bbox = pygame.mask.from_surface(surf).get_bounding_rects()
    if not bbox:
        return surf, 0, 0
    r = bbox[0]
    return surf.subsurface(r).copy(), r.x, r.y


def pixel_hit(rect, mask, mx, my):
    """判断 (mx, my) 是否命中按钮的不透明区域"""
    if not rect.collidepoint(mx, my):
        return False
    return bool(mask.get_at((mx - rect.x, my - rect.y)))
