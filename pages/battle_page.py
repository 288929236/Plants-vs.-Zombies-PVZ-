"""
战斗场景 —— 地图 + 倒计时 + 阳光
"""
import pygame, sys, random
import config
from asset_manager import load_image, load_map, clear_cache
from comment import build_popup, draw_popup, hit_popup_btn

SUN_FALL_TIME = 5000    # 下落持续 5 秒
SUN_LIFE_TIME = 10000   # 总存活 10 秒

class BattlePage:
    def __init__(self, screen):
        self.screen = screen
        self.w, self.h = screen.get_size()

        clear_cache()

        # 地图
        self.map_cfg = config.MAPS[config.ACTIVE_MAP]
        self.map_bg, _ = load_map(self.map_cfg, self.h)

        # 倒计时：每段~1秒
        self._countdown = 0.0
        self._cd_msgs = ["准备！", "3", "2", "1", "开始！"]

        # 阳光（加载 GIF 全部帧）
        from PIL import Image
        gif = Image.open("images/home/move_sum.gif")
        sun_h = int(self.h * 0.10)
        s = sun_h / gif.height
        sun_w = int(gif.width * s)
        self._sun_frames = []
        for i in range(gif.n_frames):
            gif.seek(i)
            frame = gif.convert("RGBA")
            ps = pygame.image.fromstring(frame.tobytes(), frame.size, "RGBA")
            self._sun_frames.append(pygame.transform.smoothscale(ps, (sun_w, sun_h)))
        self._sun_count = 50
        self._suns = []           # 场上阳光列表
        self._spawn_timer = 0.0   # 生成计时器(ms)

        # ESC 弹窗
        self._esc_popup = build_popup(
            "button14_1.png", [("button14_2.png", "close"), ("button14_3.png", "quit")],
            self.w, self.h)
        self._show_esc = False

        self.next_scene = None

    def _spawn_sun(self):
        sw = self._sun_frames[0].get_width()
        sh = self._sun_frames[0].get_height()
        target_y = random.randint(int(self.h * 0.35), int(self.h * 0.70))
        self._suns.append({
            "x": random.randint(sw, self.w - sw * 2),
            "y": -sh,                         # 底部贴屏幕顶
            "target_y": target_y,
            "timer": 0.0,
            "frame_idx": 0,
            "frame_timer": 0,
            "collected": False,
            "collect_timer": 0.0,
            "start_x": 0,
            "start_y": 0,
        })

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self._show_esc = not self._show_esc
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._show_esc:
                pb = hit_popup_btn(event.pos, self._esc_popup)
                if pb:
                    if pb["action"] == "close":
                        self._show_esc = False
                    elif pb["action"] == "quit":
                        pygame.quit()
                        sys.exit()
                return
            # 点击阳光
            mx, my = event.pos
            sw, sh = self._sun_frames[0].get_width(), self._sun_frames[0].get_height()
            for s in self._suns:
                if s["collected"]:
                    continue
                r = pygame.Rect(int(s["x"]), int(s["y"]), sw, sh)
                if r.collidepoint(mx, my):
                    s["collected"] = True
                    s["collect_timer"] = 0.0
                    s["start_x"], s["start_y"] = s["x"], s["y"]
                    return

    def update(self, dt):
        self._countdown += dt / 1000.0

        # 每 3 秒生成一个阳光
        self._spawn_timer += dt
        if self._spawn_timer >= 3000:
            self._spawn_timer -= 3000
            self._spawn_sun()

        # 更新阳光状态
        sh = self._sun_frames[0].get_height()
        for s in self._suns[:]:
            s["timer"] += dt
            # 帧动画
            s["frame_timer"] += dt
            if s["frame_timer"] >= 50:
                s["frame_timer"] -= 50
                s["frame_idx"] = (s["frame_idx"] + 1) % len(self._sun_frames)
            if s["collected"]:
                s["collect_timer"] += dt
                t = min(s["collect_timer"] / 300.0, 1.0)
                et = 1 - (1 - t) ** 2
                tx, ty = 20, 20  # 飞向左上角计数区
                s["x"] = int(s["start_x"] + (tx - s["start_x"]) * et)
                s["y"] = int(s["start_y"] + (ty - s["start_y"]) * et)
                if t >= 1.0:
                    self._sun_count += 25
                    self._suns.remove(s)
            elif s["timer"] >= SUN_LIFE_TIME:
                self._suns.remove(s)
            elif s["timer"] < SUN_FALL_TIME:
                t = s["timer"] / SUN_FALL_TIME
                s["y"] = -sh + (s["target_y"] + sh) * t  # 从顶部开始落下

    def draw(self):
        self.screen.blit(self.map_bg, (0, 0))

        # 倒计时文字（页面中央）
        cd_idx = int(self._countdown)
        if cd_idx < len(self._cd_msgs):
            msg = self._cd_msgs[cd_idx]
            font_cd = pygame.font.SysFont(config.FONT_NAME, 80, bold=True)
            txt = font_cd.render(msg, True, (255, 255, 255))
            self.screen.blit(txt, ((self.w - txt.get_width()) // 2,
                                   (self.h - txt.get_height()) // 2))

        # 阳光
        for s in self._suns:
            self.screen.blit(self._sun_frames[s["frame_idx"]], (int(s["x"]), int(s["y"])))

        # 阳光计数（左上角）
        font_s = pygame.font.SysFont(config.FONT_NAME, 24, bold=True)
        count_txt = font_s.render(f"☀ {self._sun_count}", True, (255, 220, 80))
        self.screen.blit(count_txt, (10, 10))

        if self._show_esc:
            draw_popup(self.screen, self._esc_popup, self.w, self.h)
