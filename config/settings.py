# ============================================
#  全局设置 —— 窗口 / 字体 / 首页 / 当前状态
# ============================================

# ---- 首页 (images/home/) ----
HOME_BG = "images/home/home_bg.jpg"

# 首页按钮（从背景扣下来的png，悬停变亮）
# 格式: { "file":路径, "ox":背景原图X, "oy":背景原图Y, "click":是否有点击事件 }
HOME_BTNS = [
    {"file": "images/home/start_button1.png", "ox": 0, "oy": 0, "click": True},
    {"file": "images/home/start_button2.png", "ox": 0, "oy": 0, "click": False},
    {"file": "images/home/start_button3.png", "ox": 0, "oy": 0, "click": False},
    {"file": "images/home/start_button4.png", "ox": 0, "oy": 0, "click": False},
    {"file": "images/home/start_button5.png", "ox": 0, "oy": 0, "click": False},
    {"file": "images/home/start_button6.png", "ox": 0, "oy": 0, "click": False},
    {"file": "images/home/start_button7.png", "ox": 0, "oy": 0, "click": False},
    {"file": "images/home/start_button8.png", "ox": 0, "oy": 0, "click": False},
    {"file": "images/home/start_button9.png", "ox": 0, "oy": 0, "click": False},
    {"file": "images/home/start_button10.png", "ox": 0, "oy": 0, "click": False},
    {"file": "images/home/start_button11.png", "ox": 0, "oy": 0, "click": False},
    {"file": "images/home/start_button12.png", "ox": 0, "oy": 0, "click": False},
    {"file": "images/home/start_button13.png", "ox": 0, "oy": 0, "click": False},
    {"file": "images/home/start_button14.png", "ox": 0, "oy": 0, "click": False},
]

# ---- 窗口 ----
WINDOW_TITLE      = "植物大战僵尸"

# ---- 字体 ----
FONT_NAME     = "microsoftyahei"

# ---- 默认值 ----
DEFAULT_FPS   = 12
DEFAULT_SCALE = 2

# ---- 当前状态 ----
ACTIVE_MAP        = "day"          # 当前场景
SELECTED_PLANTS   = []             # 玩家选的植物
