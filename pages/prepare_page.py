import pygame, random, sys
import config
import asset_manager
from asset_manager import load_image, load_map
import store.save as sv
from comment import make_hover, crop_visible, build_popup, draw_popup, hit_popup_btn

# 模块级缓存：准备页按钮预缩放裁剪
_prep_cache = {}


def precompute_prepare(w, h):
    """预计算准备页按钮（缩放 + 裁剪），存入缓存"""
    key = (w, h)
    if key in _prep_cache:
        return

    btns = []
    for fname, ox, oy, bh_pct in [
        ("prepare_1.png", 0.2569, 0.9112, 0.0700),
        ("prepare_2.png", 1.4050, 0.0000, 0.0494),
        ("arrow.png", 0, 0, 0.10),
    ]:
        img = load_image("images/home/" + fname)
        iw, ih = img.get_width(), img.get_height()
        sh = int(h * bh_pct)
        s = sh / ih
        sw = int(iw * s)
        surf = pygame.transform.smoothscale(img, (sw, sh))
        cropped, cx, cy = crop_visible(surf)
        mask = pygame.mask.from_surface(cropped)
        hover = make_hover(cropped)
        if fname == "prepare_2.png":
            x = w - sw + cx
            y = cy
        elif fname == "arrow.png":
            x = w - sw + cx
            y = h - sh + cy
            # 预生成翻转版（← →），box_open 决定显示哪个
            rev = pygame.transform.flip(cropped, True, False)
            rev_hover = make_hover(rev)
            btns.append({
                "surf": cropped, "hover": hover,
                "surf_rev": rev, "hover_rev": rev_hover,
                "mask": mask,
                "rect": pygame.Rect(x, y, cropped.get_width(), cropped.get_height()),
                "tag": fname,
            })
            continue
        else:
            x = int(h * ox) + cx
            y = int(h * oy) + cy
        btns.append({
            "surf": cropped, "hover": hover, "mask": mask,
            "rect": pygame.Rect(x, y, cropped.get_width(), cropped.get_height()),
            "tag": fname,
        })

    _prep_cache[key] = btns
    # 释放原始按钮图
    for fname in ["prepare_1.png", "prepare_2.png", "arrow.png"]:
        asset_manager._cache.pop("images/home/" + fname, None)


class PreparePage:
    def __init__(self, screen):
        self.screen = screen
        self.w, self.h = screen.get_size()
        self.map_cfg = config.MAPS[config.ACTIVE_MAP]
        self.map_bg, self.map_scaled_w = load_map(self.map_cfg, self.h)
        self._map_max = max(0, self.map_scaled_w - self.w)
        self.map_scroll_x = 0
        raw_box = load_image("images/home/plant_box.png")
        iw, ih = raw_box.get_width(), raw_box.get_height()
        s = self.h / ih
        self.box_w = int(iw * s)
        self.box_h = int(ih * s)
        self._box_img = pygame.transform.smoothscale(raw_box, (self.box_w, self.box_h))
        # 植物卡片网格（48张，按config.PLANT_ALL顺序）
        self._card_imgs = []
        for plant in config.PLANT_ALL.values():
            self._card_imgs.append(load_image(plant["cover"]))
        self._cards = []
        cx0, cy0 = 0.0338, 0.2062
        dx, dy, cw, ch = 0.0889, 0.1170, 0.0848, 0.1131
        for row in range(6):
            for col in range(8):
                cx = cx0 + col * dx
                cy = cy0 + row * dy
                r = pygame.Rect(int(self.h * cx), int(self.h * cy),
                                int(self.h * cw), int(self.h * ch))
                self._cards.append({"rect": r})
        # 预缩放卡片至网格尺寸，draw 时直接 blit
        for i, c in enumerate(self._cards):
            cr = c["rect"]
            img = self._card_imgs[i]
            iw, ih = img.get_width(), img.get_height()
            s = min(cr.w / iw, cr.h / ih)
            self._card_imgs[i] = pygame.transform.smoothscale(img, (int(iw * s), int(ih * s)))
        # 列表卡片属性（按键可调）
        self._sel_cw, self._sel_ch = 0.0829, 0.1112
        self._sel_dx = 0.0855
        self._sel_x0, self._sel_y0 = 0.1284, 0.0151
        self.box_target_x = 0
        self.box_y = 0
        self.box_off_x = -self.box_w - 20
        self.box_current_x = self.box_off_x
        self.box_rect = pygame.Rect(self.box_current_x, self.box_y, self.box_w, self.box_h)
        self._anim_t = 0.0
        self._anim_done = False
        self._box_open = False
        self._box_toggling = False
        self._box_toggle_t = 0.0
        self._wait_timer = 0.0
        level = config.load_level(sv.current_level())
        z_types = [t for t, n in level["count"].items() if n > 0]
        self.zombie_actors = []
        for i in range(6):
            zk = random.choice(z_types)
            cfg = config.ZOMBIE_ALL[zk]
            frames = self._zombie_idle_frames(zk)
            y = random.randint(int(self.h * 0.10), int(self.h * 0.70))
            x = random.randint(int(self.w * 0.65), int(self.w * 0.88))
            self.zombie_actors.append({
                "type": zk, "name": cfg["name"],
                "frames": frames, "idx": 0, "timer": 0,
                "x": x, "y": y,
            })
        self.zombie_actors.sort(key=lambda a: a["y"])
        self.next_scene = None
        self._pending_battle = False
        self._show_popup = False
        self._popup_data = build_popup(
            "button14_1.png", [("button14_2.png", "close"), ("button14_3.png", "quit")],
            self.w, self.h)
        # 按钮（预计算缓存）
        self._btns = _prep_cache.get((self.w, self.h), [])
        if not self._btns:
            for fname, ox, oy, bh_pct in [
                ("prepare_1.png", 0.2569, 0.9112, 0.0700),
                ("prepare_2.png", 1.4050, 0.0000, 0.0494),
                ("arrow.png", 0, 0, 0.10),
            ]:
                img = load_image("images/home/" + fname)
                iw, ih = img.get_width(), img.get_height()
                sh = int(self.h * bh_pct)
                s = sh / ih
                sw = int(iw * s)
                surf = pygame.transform.smoothscale(img, (sw, sh))
                mask = pygame.mask.from_surface(surf)
                hover = make_hover(surf)
                if fname == "prepare_2.png":
                    x, y = self.w - sw, 0
                    btn = {"surf": surf, "hover": hover, "mask": mask,
                           "rect": pygame.Rect(x, y, sw, sh), "tag": fname}
                elif fname == "arrow.png":
                    x, y = self.w - sw, self.h - sh
                    rev = pygame.transform.flip(surf, True, False)
                    rev_hover = make_hover(rev)
                    btn = {"surf": surf, "hover": hover,
                           "surf_rev": rev, "hover_rev": rev_hover,
                           "mask": mask,
                           "rect": pygame.Rect(x, y, sw, sh), "tag": fname}
                else:
                    x, y = int(self.h * ox), int(self.h * oy)
                    btn = {"surf": surf, "hover": hover, "mask": mask,
                           "rect": pygame.Rect(x, y, sw, sh), "tag": fname}
                self._btns.append(btn)
        self._selected = []          # 已选卡片索引
        self._sel_max = 10
        self._sel_x0, self._sel_y0 = 0.1281, 0.0131
        self._fly = {}
        self._btn2_popup = build_popup(
            "prepare_2_1.png", [("prepare_2_2.png", "home"), ("prepare_2_3.png", "close")],
            self.w, self.h)
        self._show_btn2 = False

    def _handle_popup(self, pos, data, is_esc=False):
        pb = hit_popup_btn(pos, data)
        if pb:
            if pb["action"] == "close":
                if is_esc:
                    self._show_popup = False
                else:
                    self._show_btn2 = False
            elif pb["action"] == "quit":
                pygame.quit()
                sys.exit()
            elif pb["action"] == "home":
                self._show_btn2 = False
                self.next_scene = "home"


    def _card_pos(self, idx):
        """卡片在网格中的位置（左上角，预缩放已适配网格）"""
        c = self._cards[idx]
        cr = c["rect"]
        card_img = self._card_imgs[idx]
        iw, ih = card_img.get_width(), card_img.get_height()
        return (cr.x + self.box_current_x + (cr.w - iw) // 2,
                cr.y + (cr.h - ih) // 2)

    def _bar_pos(self, pi, idx):
        """选中栏第pi个槽位的位置（左上角）"""
        sx = int(self.h * (self._sel_x0 + pi * self._sel_dx)) + self.box_current_x
        sy = int(self.h * self._sel_y0)
        sw = int(self.h * self._sel_cw)
        sh = int(self.h * self._sel_ch)
        card_img = self._card_imgs[idx]
        iw, ih = card_img.get_width(), card_img.get_height()
        return (sx + (sw - iw) // 2, sy + (sh - ih) // 2)

    def _zombie_idle_frames(self, key):
        cfg = config.ZOMBIE_ALL[key]
        cover = load_image(cfg["cover"])
        size = int(self.h * 0.22)
        s = min(size / cover.get_width(), size / cover.get_height())
        sw, sh = int(cover.get_width() * s), int(cover.get_height() * s)
        return [(pygame.transform.smoothscale(cover, (sw, sh)), 200)]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self._show_popup = not self._show_popup
            return
        if event.type == pygame.KEYDOWN:
            k = event.key
            d = 0.0001; acted = False
            if k == pygame.K_LEFT:   self._sel_x0 -= d; acted = True
            if k == pygame.K_RIGHT:  self._sel_x0 += d; acted = True
            if k == pygame.K_UP:     self._sel_y0 -= d; acted = True
            if k == pygame.K_DOWN:   self._sel_y0 += d; acted = True
            if k == pygame.K_MINUS or k == pygame.K_KP_MINUS:
                self._sel_cw = max(0.0001, self._sel_cw - d); self._sel_ch = max(0.0001, self._sel_ch - d); acted = True
            if k == pygame.K_EQUALS or k == pygame.K_KP_PLUS:
                self._sel_cw += d; self._sel_ch += d; acted = True
            if k == pygame.K_1: self._sel_dx = max(0.0001, self._sel_dx - d); acted = True
            if k == pygame.K_2: self._sel_dx += d; acted = True
            if acted and self._selected:
                print(f"列表: pos=({self._sel_x0:.4f},{self._sel_y0:.4f}) cw={self._sel_cw:.4f} ch={self._sel_ch:.4f} dx={self._sel_dx:.4f}")
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(f"点击: ({x},{y})  {x/self.h*100:.2f}%  {y/self.h*100:.2f}%")
            if self._show_popup:
                self._handle_popup(event.pos, self._popup_data, is_esc=True)
                return
            if self._show_btn2:
                self._handle_popup(event.pos, self._btn2_popup)
                return
            # 按钮点击
            for btn in self._btns:
                r = btn["rect"]
                if r.collidepoint(x, y):
                    lx, ly = x - r.x, y - r.y
                    if btn["mask"].get_at((lx, ly)):
                        if btn["tag"] == "prepare_1.png" and self._box_open:
                            if len(self._selected) == self._sel_max:
                                self._pending_battle = True
                        elif btn["tag"] == "prepare_2.png":
                            self._show_btn2 = True
                        elif btn["tag"] == "arrow.png":
                            if self._anim_done and not self._box_toggling:
                                self._box_open = not self._box_open
                                self._box_toggling = True
                                self._box_toggle_t = 0.0
                        return
            # 点击已选列表 => 取消（克隆从列表滑回卡片）
            for pi, idx in enumerate(self._selected):
                sx = int(self.h * (self._sel_x0 + pi * self._sel_dx)) + self.box_current_x
                sy = int(self.h * self._sel_y0)
                sw = int(self.h * self._sel_cw)
                sh = int(self.h * self._sel_ch)
                if pygame.Rect(sx, sy, sw, sh).collidepoint(x, y):
                    if idx not in self._fly:
                        self._fly[idx] = {"t": 0.0, "dir": "out"}
                    return
            # 点击卡片 => 选中/取消
            for i, c in enumerate(self._cards):
                r = c["rect"]
                if r.collidepoint(x, y):
                    if i in self._selected:
                        if i not in self._fly:
                            self._fly[i] = {"t": 0.0, "dir": "out"}
                    elif len(self._selected) < self._sel_max:
                        self._selected.append(i)
                        self._fly[i] = {"t": 0.0, "dir": "in"}
                    return

    def update(self, dt):
        # 战斗跳转
        if self._pending_battle:
            self._anim_t = max(0, self._anim_t - dt / 400.0)
            self.box_current_x = int(self.box_off_x + (self.box_target_x - self.box_off_x) * min(self._anim_t, 1.0))
            self.box_rect.x = self.box_current_x
            self.map_scroll_x = int(self._map_max * min(self._anim_t, 1.0))
            if self._anim_t <= 0:
                import json
                keys = list(config.PLANT_ALL.keys())
                config.SELECTED_PLANTS[:] = [keys[i] for i in self._selected]
                json.dump(config.SELECTED_PLANTS, open("store/selected_plants.json", "w", encoding="utf-8"),
                          ensure_ascii=False)
                self.next_scene = "battle"
                return
            self._anim_t = min(1.0, self._anim_t)
        if not self._anim_done:
            self._wait_timer += dt / 1000.0
            if self._wait_timer >= 0.5:
                self._anim_t += dt / 800.0
                if self._anim_t >= 1.0:
                    self._anim_t = 1.0
                    self._anim_done = True
                    self._box_open = True
                t = self._anim_t
                et = 2*t*t if t < 0.5 else 1 - (-2*t+2)**2/2
                self.map_scroll_x = int(self._map_max * et)
                self.box_current_x = int(self.box_off_x + (self.box_target_x - self.box_off_x) * et)
                self.box_rect.x = self.box_current_x
        if self._anim_done and self._box_toggling:
            self._box_toggle_t += dt / 400.0
            if self._box_toggle_t >= 1.0:
                self._box_toggle_t = 1.0
                self._box_toggling = False
            t = self._box_toggle_t
            et = 1 - (1 - t) * (1 - t)
            if self._box_open:
                self.box_current_x = int(self.box_off_x + (self.box_target_x - self.box_off_x) * et)
                self.map_scroll_x = int(self._map_max * et)
            else:
                self.box_current_x = int(self.box_target_x + (self.box_off_x - self.box_target_x) * et)
                self.map_scroll_x = int(self._map_max * (1 - et))
            self.box_rect.x = self.box_current_x
        for a in self.zombie_actors:
            a["timer"] += dt
            _, dur = a["frames"][a["idx"]]
            if a["timer"] >= dur:
                a["timer"] -= dur
                a["idx"] = (a["idx"] + 1) % len(a["frames"])
        # 克隆飞行动画
        done, done_dir = [], {}
        for idx, f in list(self._fly.items()):
            f["t"] += dt / 200.0
            if f["t"] >= 1.0:
                f["t"] = 1.0
                done.append(idx)
                done_dir[idx] = f["dir"]
        for idx in done:
            del self._fly[idx]
            if done_dir.get(idx) == "out" and idx in self._selected:
                self._selected.remove(idx)

    def draw(self):
        self.screen.blit(self.map_bg, (-self.map_scroll_x, 0))
        gap = max(0, self.w - (self.map_scaled_w - self.map_scroll_x))
        if gap:
            self.screen.fill((0, 0, 0), (self.w - gap, 0, gap, self.h))
        if self._anim_t > 0:
            self.screen.blit(self._box_img, self.box_rect)
            # 已选列表（顶部，跟随植物框滑动）
            for pi, idx in enumerate(self._selected):
                sx = int(self.h * (self._sel_x0 + pi * self._sel_dx)) + self.box_current_x
                sy = int(self.h * self._sel_y0)
                sw = int(self.h * self._sel_cw)
                sh = int(self.h * self._sel_ch)
                sr = pygame.Rect(sx, sy, sw, sh)
                out_fly = idx in self._fly and self._fly[idx]["dir"] == "out"
                if out_fly:
                    pygame.draw.rect(self.screen, (30, 30, 30), sr, border_radius=6)
                    pygame.draw.rect(self.screen, (80, 80, 80), sr, 2, border_radius=6)
                else:
                    bg_c = (50, 60, 70)
                    bd_c = (100, 160, 180)
                    pygame.draw.rect(self.screen, bg_c, sr, border_radius=6)
                    pygame.draw.rect(self.screen, bd_c, sr, 2, border_radius=6)
                if not out_fly:
                    card_img = self._card_imgs[idx]
                    iw, ih = card_img.get_width(), card_img.get_height()
                    self.screen.blit(card_img, (sx + (sw - iw) // 2, sy + (sh - ih) // 2))
            # 卡片网格（48张，预缩放直绘）
            for i, c in enumerate(self._cards):
                card_img = self._card_imgs[i]
                cr = c["rect"]
                iw, ih = card_img.get_width(), card_img.get_height()
                dx = cr.x + self.box_current_x + (cr.w - iw) // 2
                dy = cr.y + (cr.h - ih) // 2
                self.screen.blit(card_img, (dx, dy))
                if i in self._selected:
                    overlay = pygame.Surface((cr.w, cr.h), pygame.SRCALPHA)
                    overlay.fill((0, 0, 0, 100))
                    self.screen.blit(overlay, (cr.x + self.box_current_x, cr.y))
                    pygame.draw.rect(self.screen, (120, 180, 255),
                                     pygame.Rect(cr.x + self.box_current_x, cr.y, cr.w, cr.h),
                                     3, border_radius=6)
            # 飞行动画（克隆，预缩放直绘，最上层）
            for idx, f in self._fly.items():
                card_img = self._card_imgs[idx]
                t = min(f["t"], 1.0)
                et = 1.0 - (1.0 - t) * (1.0 - t)
                pi = len(self._selected) - 1 if f["dir"] == "in" else self._selected.index(idx)
                src = self._card_pos(idx) if f["dir"] == "in" else self._bar_pos(pi, idx)
                dst = self._bar_pos(pi, idx) if f["dir"] == "in" else self._card_pos(idx)
                ax = int(src[0] + (dst[0] - src[0]) * et)
                ay = int(src[1] + (dst[1] - src[1]) * et)
                self.screen.blit(card_img, (ax, ay))
        if self._anim_done:
            offset = self._map_max - self.map_scroll_x
            for a in self.zombie_actors:
                frame, _ = a["frames"][a["idx"]]
                self.screen.blit(frame, (a["x"] + offset, a["y"]))
        if self._show_btn2 and not self._show_popup:
            draw_popup(self.screen, self._btn2_popup, self.w, self.h)
        if self._show_popup:
            draw_popup(self.screen, self._popup_data, self.w, self.h)
        # 按钮（动画完成后显示）
        mx, my = pygame.mouse.get_pos()
        for btn in self._btns:
            if not self._anim_done:
                continue
            if btn["tag"] == "prepare_1.png" and not self._box_open:
                continue
            r = btn["rect"]
            hit = False
            if not (self._show_popup or self._show_btn2) and r.collidepoint(mx, my):
                lx, ly = mx - r.x, my - r.y
                if btn["mask"].get_at((lx, ly)):
                    hit = True
            if btn["tag"] == "arrow.png" and "surf_rev" in btn:
                s = btn["hover_rev" if hit else "surf_rev"] if not self._box_open else btn["hover" if hit else "surf"]
            else:
                s = btn["hover"] if hit else btn["surf"]
            self.screen.blit(s, r)
