# ============================================
#  僵尸配置 —— 封面 / 行走 / 攻击 / 属性
# ============================================
#
#  字段:
#    cover:   封面图路径  (images/zombies_cover/)
#    walk:    行走动画路径 (images/zombies_move/)
#    attack:  攻击动画路径 (images/zombies_attack/)
#    name:       中文名
#    attribute:  {hp:生命, atk:攻击, cd:冷却秒, sun:掉落阳光}
#    walk_cfg:  {cols, rows, fps, scale}  行走动画
#    attack_cfg:{cols, rows, fps, scale}  攻击动画
# ============================================================

ALL = {

    "zombie": {
        "cover":      "images/zombies_cover/zombie.png",
        "walk":       "images/zombies_move/zombie_walk.png",
        "attack":     "images/zombies_attack/zombie_attack.png",
        "attribute":  {"hp": 200, "atk": 100, "cd": 0, "sun": 0},
        "name":       "普通僵尸",
        "walk_cfg":   {"cols": 8, "rows": 3, "fps": 12, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 10, "scale": 2},
    },

    "conehead": {
        "cover":      "images/zombies_cover/conehead.png",
        "walk":       "images/zombies_move/conehead_walk.png",
        "attack":     "images/zombies_attack/conehead_attack.png",
        "attribute":  {"hp": 560, "atk": 100, "cd": 0, "sun": 0},
        "name":       "路障僵尸",
        "walk_cfg":   {"cols": 8, "rows": 3, "fps": 12, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 10, "scale": 2},
    },

    "buckethead": {
        "cover":      "images/zombies_cover/buckethead.png",
        "walk":       "images/zombies_move/buckethead_walk.png",
        "attack":     "images/zombies_attack/buckethead_attack.png",
        "attribute":  {"hp": 1300, "atk": 100, "cd": 0, "sun": 0},
        "name":       "铁桶僵尸",
        "walk_cfg":   {"cols": 8, "rows": 3, "fps": 12, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 10, "scale": 2},
    },

}
