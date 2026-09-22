"""
加载画面 —— 渐变背景 + 旋转太阳花纹 + 进度条
"""
import pygame, math, time, config
from asset_manager import load_image


class LoadingPage:
    def __init__(self, screen):
        self.screen = screen
        self.w, self.h = screen.get_size()
        self._angle = 0.0
        self._done = False
        self._start = time.time()
        self.next_scene = None

        # 加载画面背景图（有就用，没有就渐变）
        raw = load_image("images/home/loading.jpg")
        if raw:
            iw, ih = raw.get_width(), raw.get_height()
            s = min(self.w / iw, self.h / ih)
            self._bg = pygame.transform.smoothscale(raw, (int(iw * s), int(ih * s)))
            self._bg_x = (self.w - self._bg.get_width()) // 2
            self._bg_y = (self.h - self._bg.get_height()) // 2
        else:
            self._bg = None

        self._tasks = self._collect_all()
        self._task_idx = 0
        self._font_title = pygame.font.SysFont(config.FONT_NAME, 36, bold=True)
        self._font_sub = pygame.font.SysFont(config.FONT_NAME, 20)

    @staticmethod
    def _collect_all():
        tasks = set()
        tasks.add(config.HOME_BG)
        for btn in config.HOME_BTNS:
            tasks.add(btn["file"])
        for f in ["button12_1.png", "button12_2.png", "button12_3.png",
                  "button13_1.png", "button13_2.png",
                  "button14_1.png", "button14_2.png", "button14_3.png"]:
            tasks.add("images/home/" + f)
        tasks.add(config.MAPS[config.ACTIVE_MAP]["file"])
        tasks.add("images/home/plant_box.png")
        for plant in config.PLANT_ALL.values():
            tasks.add(plant["cover"])
        for z in config.ZOMBIE_ALL.values():
            tasks.add(z["cover"])
        for f in ["prepare_1.png", "prepare_2.png", "arrow.png"]:
            tasks.add("images/home/" + f)
        for f in ["prepare_2_1.png", "prepare_2_2.png", "prepare_2_3.png"]:
            tasks.add("images/home/" + f)
        return list(tasks)

    def update(self, dt):
        self._angle += dt * 0.003

        if not self._done:
            for _ in range(8):
                if self._task_idx >= len(self._tasks):
                    self._done = True
                    from pages.home_page import precompute_home
                    from pages.prepare_page import precompute_prepare
                    precompute_home(self.w, self.h)
                    precompute_prepare(self.w, self.h)
                    elapsed = time.time() - self._start
                    print(f"加载完成，耗时 {elapsed:.2f} 秒")
                    self.next_scene = "home"
                    break
                load_image(self._tasks[self._task_idx])
                self._task_idx += 1

    def handle_event(self, event):
        pass

    def draw(self):
        if self._bg:
            self.screen.blit(self._bg, (self._bg_x, self._bg_y))
        else:
            # 径向渐变暗底
            self._draw_gradient_bg()

        cx, cy = self.w // 2, self.h // 2

        # 旋转太阳花纹：12 条光线，长度+alpha 递减
        for i in range(12):
            a = self._angle + i * math.pi / 6
            r = 36 + 12 * math.sin(self._angle * 3 + i * 0.5)
            alpha = max(20, 180 - i * 14)
            color = (255, 220 + int(30 * math.sin(a)), 60, alpha)
            ex = cx + int(r * math.cos(a))
            ey = cy - 20 + int(r * math.sin(a))
            pygame.draw.line(self.screen, color[:3], (cx, cy - 20), (ex, ey), 3)

        # 中心圆
        pygame.draw.circle(self.screen, (255, 200, 40), (cx, cy - 20), 14)
        pygame.draw.circle(self.screen, (255, 160, 20), (cx, cy - 20), 10)

        # 标题
        title = self._font_title.render("Plants vs. Zombies", True, (255, 255, 220))
        shadow = self._font_title.render("Plants vs. Zombies", True, (0, 0, 0))
        tx = cx - title.get_width() // 2
        ty = cy + 60
        self.screen.blit(shadow, (tx + 2, ty + 2))
        self.screen.blit(title, (tx, ty))

        # 副标题
        sub = self._font_sub.render("加载中...", True, (180, 200, 220))
        self.screen.blit(sub, (cx - sub.get_width() // 2, ty + 42))

        # 进度条
        if self._tasks:
            pct = self._task_idx / len(self._tasks)
            bw, bh = 320, 8
            bx, by = cx - bw // 2, ty + 80
            # 底色
            pygame.draw.rect(self.screen, (30, 35, 50), (bx - 2, by - 2, bw + 4, bh + 4), border_radius=6)
            pygame.draw.rect(self.screen, (60, 65, 80), (bx, by, bw, bh), border_radius=4)
            # 进度填充 + 光晕
            fw = int(bw * pct)
            if fw > 0:
                glow = pygame.Surface((fw + 6, bh + 6), pygame.SRCALPHA)
                glow.fill((255, 200, 60, 30))
                self.screen.blit(glow, (bx - 3, by - 3))
                pygame.draw.rect(self.screen, (255, 180, 40), (bx, by, fw, bh), border_radius=4)
                # 高光
                pygame.draw.rect(self.screen, (255, 220, 100), (bx, by, fw, bh // 2), border_radius=4)

    def _draw_gradient_bg(self):
        """径向渐变深色背景"""
        for i in range(self.h, 0, -2):
            t = i / self.h
            r = int(10 + 25 * t)
            g = int(10 + 30 * t)
            b = int(20 + 50 * t)
            pygame.draw.rect(self.screen, (r, g, b), (0, i - 2, self.w, 2))
