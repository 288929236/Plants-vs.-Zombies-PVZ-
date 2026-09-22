# ============================================
#  地图配置  (images/maps/)
# ============================================

# 格式: { "file":路径, "width":宽, "height":高, "rows":行数, "note":说明, "bg":背景色, "crop_left":左侧裁切比例 }
ALL = {
    "day": {
        "file":      "images/maps/day.png",
        "width":     800, "height": 600,
        "rows":      5,
        "note":      "白天草地",
        "bg":        (135, 200, 120),
        "crop_left": 0,
    },
    "night": {
        "file":      "images/maps/night.jpg",
        "width":     800, "height": 600,
        "rows":      5,
        "note":      "夜晚草地",
        "bg":        (20, 20, 60),
        "crop_left": 0.15,
    },
    "pool": {
        "file":      "images/maps/pool.jpg",
        "width":     800, "height": 600,
        "rows":      6,
        "note":      "泳池",
        "bg":        (80, 160, 200),
        "crop_left": 0.1,
    },
    "roof": {
        "file":      "images/maps/roof.jpg",
        "width":     800, "height": 600,
        "rows":      5,
        "note":      "屋顶",
        "bg":        (100, 80, 60),
        "crop_left": 0.1,
    },
}
